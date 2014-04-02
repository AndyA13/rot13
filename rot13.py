import sys

class Rot13(object):

    def translate(self, input_text):

        rot_map = {}

        # a to z
        self.add_to_dictionary(rot_map, 65, 91)
        
        # A to Z
        self.add_to_dictionary(rot_map, 97, 123)

        output = ""

        for character in input_text:

            output = output + rot_map.get(character, character)

        return output

    def add_to_dictionary(self, rot_map, start, end):

        split_point = start + ((end - start) / 2)

        for ascii_code in range(start, end):

            if ascii_code >= split_point:
                rot_map[chr(ascii_code)] = chr(ascii_code - 13)
            else:
                rot_map[chr(ascii_code)] = chr(ascii_code + 13)

if __name__ == "__main__":
    rot13 = Rot13()
    print sys.argv[1]
    print rot13.translate(sys.argv[1])
