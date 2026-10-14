# Recipe Scaler

Recipe quantities get awkward when a dish serves four but only two people are coming over. This tool reads a small JSON recipe and scales its ingredients using exact fractions, so `1/3` does not turn into a long decimal.

```bash
python3 app.py samples/pancakes.json 6
```

The second number is the servings you want. Amounts in the file can be whole numbers, decimals, or fractions like `3/4`. Units are copied as written; the tool does not pretend to convert teaspoons to cups. Run `python3 -m unittest -v` in this folder to check the math and validation.
