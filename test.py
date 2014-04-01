
import unittest

from rot13 import Rot13

class Tests(unittest.TestCase):

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