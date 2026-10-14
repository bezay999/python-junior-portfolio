# Markdown Link Inspector

Moving notes between folders can quietly break relative links. This tool walks a folder of Markdown files and reports links to local files that no longer exist. Web links and `#anchors` are left alone; checking those would be a different job.

```bash
python3 app.py /path/to/notes
```

It handles ordinary inline links to files such as `docs/guide.md` and URL-encoded spaces. It does not parse every corner of Markdown (reference-style links and nested parentheses are outside this small project). Nothing is edited. Run `python3 -m unittest -v` for the checks.
