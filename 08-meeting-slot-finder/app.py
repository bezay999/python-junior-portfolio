import argparse
import json
from pathlib import Path


def to_minutes(value):
    if not isinstance(value, str) or len(value) != 5 or value[2] != ":":
        raise ValueError("Times must use HH:MM")
    try:
        hour, minute = int(value[:2]), int(value[3:])
    except ValueError as error:
        raise ValueError("Times must use HH:MM") from error
    if not 0 <= hour <= 23 or not 0 <= minute <= 59:
        raise ValueError("Time is outside a day")
    return hour * 60 + minute


def clock_time(minutes):
    return f"{minutes // 60:02d}:{minutes % 60:02d}"


def interval(pair):
    if not isinstance(pair, list) or len(pair) != 2:
        raise ValueError("Each interval needs start and end")
    start, end = map(to_minutes, pair)
    if start >= end:
        raise ValueError("An interval must end after it starts")
    return start, end


def find_slot(schedule, duration):
    if not isinstance(duration, int) or duration < 1:
        raise ValueError("Meeting length must be a positive number of minutes")
    if not isinstance(schedule, dict) or not isinstance(schedule.get("people"), dict):
        raise ValueError("Schedule needs a people object")
    start, end = interval(schedule.get("workday"))
    busy = []
    for periods in schedule["people"].values():
        if not isinstance(periods, list):
            raise ValueError("Each person's busy periods must be a list")
        for period in periods:
            first, last = interval(period)
            if first < start or last > end:
                raise ValueError("Busy periods must fit inside the workday")
            busy.append((first, last))
    cursor = start
    for first, last in sorted(busy):
        if first - cursor >= duration:
            return clock_time(cursor), clock_time(cursor + duration)
        cursor = max(cursor, last)
    if end - cursor >= duration:
        return clock_time(cursor), clock_time(cursor + duration)
    return None


def main():
    parser = argparse.ArgumentParser(description="Find the first shared free meeting slot")
    parser.add_argument("schedule", type=Path)
    parser.add_argument("minutes", type=int)
    args = parser.parse_args()
    try:
        schedule = json.loads(args.schedule.read_text(encoding="utf-8"))
        slot = find_slot(schedule, args.minutes)
    except (OSError, json.JSONDecodeError, ValueError) as error:
        parser.error(str(error))
    print(f"Free slot: {slot[0]}–{slot[1]}" if slot else "No shared slot found.")


if __name__ == "__main__":
    main()
