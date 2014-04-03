import unittest
from rot13 import Rot13


class Tests(unittest.TestCase):

    def test_add_to_dictionary(self):

        # add the lower case alhpabet
        encryptor = Rot13()

        test_dict = {}

        test_dict.update(encryptor.get_rot_values("a", "z"))

        self.assertEqual(26, len(test_dict))

        # test a few points and edge cases
        self.assertEqual("n", test_dict["a"])
        self.assertEqual("q", test_dict["d"])
        self.assertEqual("z", test_dict["m"])
        self.assertEqual("a", test_dict["n"])
        self.assertEqual("g", test_dict["t"])
        self.assertEqual("m", test_dict["z"])

    def test_rot13_encryption(self):

        encryptor = Rot13()

        test_input = "My test string."

        output = encryptor.translate(test_input)

        # string should be rot13 "encrypted"
        self.assertNotEqual(output, test_input)

        output = encryptor.translate(output)

        # applying rot13 twice should reverse the "encryption"
        self.assertEqual(output, test_input)

if __name__ == "__main__":
    unittest.main()