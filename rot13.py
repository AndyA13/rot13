import sys


class Rot13(object):

    def translate(self, input_text):

        rot_map = {}

        # A to Z
        rot_map.update(self.get_rot_values("A", "Z"))

        # a to z
        rot_map.update(self.get_rot_values("a", "z"))

        output = ""

        for character in input_text:

            output = output + rot_map.get(character, character)

        return output

    def get_rot_values(self, start, end):

        ord_start = ord(start)
        ord_end = ord(end)

        split_point = ord_start + ((ord_end - ord_start) / 2)

        values = {}

        for ascii_code in range(ord_start, ord_end + 1):

            if ascii_code > split_point:
                values[chr(ascii_code)] = chr(ascii_code - 13)
            else:
                values[chr(ascii_code)] = chr(ascii_code + 13)

        return values

if __name__ == "__main__":
    rot13 = Rot13()
    print sys.argv[1]
    print rot13.translate(sys.argv[1])
