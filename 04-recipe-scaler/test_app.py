from fractions import Fraction
import unittest

from app import scale, show_amount


class RecipeTests(unittest.TestCase):
    def setUp(self):
        self.recipe = {"name": "Soup", "servings": 2,
                       "ingredients": [{"amount": "3/4", "unit": "cup", "name": "stock"}]}

    def test_exact_scaling(self):
        self.assertEqual(scale(self.recipe, 3)[0][0], Fraction(9, 8))
        self.assertEqual(show_amount(Fraction(9, 8)), "1 1/8")

    def test_invalid_amount(self):
        self.recipe["ingredients"][0]["amount"] = "0"
        with self.assertRaises(ValueError):
            scale(self.recipe, 3)

    def test_invalid_servings(self):
        with self.assertRaises(ValueError):
            scale(self.recipe, 0)


if __name__ == "__main__":
    unittest.main()
