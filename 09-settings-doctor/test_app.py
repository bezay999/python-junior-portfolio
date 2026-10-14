import unittest

from app import validate


VALID = {"app_name": "Notebook", "port": 8080, "debug": False,
         "data_dir": "data", "allowed_hosts": ["localhost"]}


class SettingsTests(unittest.TestCase):
    def test_valid_file(self):
        self.assertEqual(validate(VALID), [])

    def test_missing_and_unknown_fields(self):
        settings = dict(VALID)
        del settings["debug"]
        settings["debgu"] = True
        self.assertIn("Missing field: debug", validate(settings))
        self.assertIn("Unknown field: debgu", validate(settings))

    def test_bool_is_not_a_port(self):
        settings = dict(VALID, port=True)
        self.assertTrue(any("port" in problem for problem in validate(settings)))

    def test_repeated_hosts(self):
        settings = dict(VALID, allowed_hosts=["Localhost", "localhost"])
        self.assertTrue(any("repeat" in problem for problem in validate(settings)))


if __name__ == "__main__":
    unittest.main()
