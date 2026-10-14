# CSV Tidy

This tool is for the kind of CSV export that is almost useful: extra spaces, empty lines, and repeated rows. It makes a new file with tidy cells while leaving the original alone.

```bash
python3 app.py samples/messy.csv output/clean.csv
```

The first row is the header. Rows with the wrong number of columns are treated as errors instead of guessed into shape. Repeated rows are compared without case or surrounding spaces, and the first version is kept. The output path must not already exist. Run `python3 -m unittest -v` for the checks.
