# Duplicate File Scout

Before cleaning up a folder, I would rather know which files are truly identical than trust their names. This tool groups files by size, then hashes the possible matches. It only reports duplicates; it never removes or changes a file.

```bash
python3 app.py /path/to/folder
```

Symbolic links are skipped. Files that cannot be read are reported and left alone. The report shows the SHA-256 group and each path. To run the tests, use `python3 -m unittest -v` in this folder.
