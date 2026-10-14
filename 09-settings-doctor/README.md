# Settings Doctor

A typo in a settings file can be harder to notice than a typo in code. This tool reads a JSON file and gives specific feedback about the fields a small web app expects. It does not change the file.

```bash
python3 app.py samples/settings.json
```

The expected fields are an app name, a port, a debug flag, a data folder, and a list of allowed hosts. Unknown fields are reported too, since they are often spelling mistakes. This is a small, fixed example schema rather than a general JSON Schema implementation. Run `python3 -m unittest -v` for the checks.
