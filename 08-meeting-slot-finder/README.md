# Meeting Slot Finder

Two people can each have a free afternoon and still struggle to find the same half hour. This tool combines busy periods from a small JSON schedule and finds the first shared opening in a workday.

```bash
python3 app.py samples/day.json 30
```

The number is meeting length in minutes. Times are `HH:MM` on one local day; the sample does not deal with time zones or overnight shifts. Busy periods must sit inside the stated workday. Run `python3 -m unittest -v` for the checks.
