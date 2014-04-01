import sys

class Rot13(object):

    def translate(self, input_text):

        rot_map = {}

        for c in range(65, 91): # A to Z

            if c > 77:
                rot_map[chr(c)] = chr(c - 13)
            else:
                rot_map[chr(c)] = chr(c + 13)

        for c in range(97, 123): # a to z

            if c > 109:
                rot_map[chr(c)] = chr(c - 13)
            else:
                rot_map[chr(c)] = chr(c + 13)

        output = ""

        for character in input_text:

            if character in rot_map:
                output = output + rot_map[character]
            else:
                output = output + character

        return output

if __name__ == "__main__":
    rot13 = Rot13()
    print sys.argv[1]
    print rot13.translate(sys.argv[1])
