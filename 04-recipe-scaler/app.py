import argparse
from fractions import Fraction
import json
from pathlib import Path


def validate(recipe):
    if not isinstance(recipe, dict) or not isinstance(recipe.get("name"), str):
        raise ValueError("Recipe needs a name")
    servings = recipe.get("servings")
    if not isinstance(servings, int) or isinstance(servings, bool) or servings < 1:
        raise ValueError("Servings must be a positive whole number")
    ingredients = recipe.get("ingredients")
    if not isinstance(ingredients, list) or not ingredients:
        raise ValueError("Recipe needs at least one ingredient")
    for item in ingredients:
        if not isinstance(item, dict) or not isinstance(item.get("name"), str) or not item["name"].strip():
            raise ValueError("Every ingredient needs a name")
        if not isinstance(item.get("unit"), str):
            raise ValueError("Every ingredient needs a unit (empty is fine)")
        try:
            amount = Fraction(str(item["amount"]))
        except (KeyError, ValueError, ZeroDivisionError) as error:
            raise ValueError("Ingredient amounts must be numbers or fractions") from error
        if amount <= 0:
            raise ValueError("Ingredient amounts must be positive")


def scale(recipe, wanted):
    validate(recipe)
    if wanted < 1:
        raise ValueError("Wanted servings must be positive")
    factor = Fraction(wanted, recipe["servings"])
    return [(Fraction(str(item["amount"])) * factor, item["unit"], item["name"])
            for item in recipe["ingredients"]]


def show_amount(amount):
    whole, remainder = divmod(amount.numerator, amount.denominator)
    if remainder == 0:
        return str(whole)
    fraction = f"{remainder}/{amount.denominator}"
    return f"{whole} {fraction}" if whole else fraction


def main():
    parser = argparse.ArgumentParser(description="Scale a JSON recipe")
    parser.add_argument("recipe", type=Path)
    parser.add_argument("servings", type=int)
    args = parser.parse_args()
    try:
        recipe = json.loads(args.recipe.read_text(encoding="utf-8"))
        ingredients = scale(recipe, args.servings)
    except (OSError, json.JSONDecodeError, ValueError) as error:
        parser.error(str(error))
    print(f"{recipe['name']} — {args.servings} servings")
    for amount, unit, name in ingredients:
        print("  " + " ".join(part for part in (show_amount(amount), unit, name) if part))


if __name__ == "__main__":
    main()
