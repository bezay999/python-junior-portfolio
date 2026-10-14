import argparse
import json
from pathlib import Path


FIELDS = {"app_name", "port", "debug", "data_dir", "allowed_hosts"}


def validate(settings):
    if not isinstance(settings, dict):
        return ["The top level must be a JSON object."]
    problems = []
    for field in sorted(FIELDS - settings.keys()):
        problems.append(f"Missing field: {field}")
    for field in sorted(settings.keys() - FIELDS):
        problems.append(f"Unknown field: {field}")

    name = settings.get("app_name")
    if "app_name" in settings and (not isinstance(name, str) or not name.strip() or len(name) > 40):
        problems.append("app_name must be a non-empty string of at most 40 characters")
    port = settings.get("port")
    if "port" in settings and (type(port) is not int or not 1024 <= port <= 65535):
        problems.append("port must be a whole number from 1024 to 65535")
    if "debug" in settings and type(settings["debug"]) is not bool:
        problems.append("debug must be true or false")
    folder = settings.get("data_dir")
    if "data_dir" in settings and (not isinstance(folder, str) or not folder.strip()):
        problems.append("data_dir must be a non-empty path string")
    hosts = settings.get("allowed_hosts")
    if "allowed_hosts" in settings:
        if (not isinstance(hosts, list) or not hosts
                or any(not isinstance(host, str) or not host.strip() or " " in host for host in hosts)):
            problems.append("allowed_hosts must be a non-empty list of host names")
        elif len({host.casefold() for host in hosts}) != len(hosts):
            problems.append("allowed_hosts must not repeat a host")
    return problems


def main():
    parser = argparse.ArgumentParser(description="Check a small JSON settings file")
    parser.add_argument("settings", type=Path)
    args = parser.parse_args()
    try:
        settings = json.loads(args.settings.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        parser.error(str(error))
    problems = validate(settings)
    if problems:
        for problem in problems:
            print(f"- {problem}")
        return 1
    print("Settings look good.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
