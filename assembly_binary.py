import re


class Assembly:

    def __init__(self):
        self.opt = {
            'add': '000000',
            'addi': '001000',
            'div': '000000',
            'mfhi': '000000',
            'beq': '000100',
            'sub': '000000',
            'j': '000010',
        }

    def clean(self, file):
        """
        Creates a text file with all the instructions and then erase the
        unnecessary characters (',', '$' and '#')
        """
        pattern = r'[\w]+\s[$#][\d]+,?\s?[#$]?[\d]{0,},?\s?[$#]?[\d]{0,}'
        # fetch all the instructions
        with open(file, 'r') as original:
            for _ in original:
                file_data = original.read()
                instructions = re.findall(pattern, file_data)
        # Create a new file to store the instructions
        with open('copy.txt', 'w') as copy:
            for instruction in instructions:
                copy.write(instruction+'\n')
        # Erase unwanted symbols from instructions
        with open('copy.txt', 'r') as file:
            data = file.read()
            for _ in data:
                data = data.replace(',', '')
                data = data.replace('#', '')
                data = data.replace('$', '')

        with open('copy.txt', 'w') as file:
            file.write(data)

    def binary(self, file):
        """
        Translates assembly to binary and appends it to a new file"""
        def append_binary(file):
            """Append a 32 binary string to a text file in a 4 line style"""
            with open(file, 'a') as append_file:
                start = 0
                end = 8
                for _ in range(4):
                    append_file.write(binary[start:end] + '\n')
                    start = end
                    end += 8

        with open(file, 'r') as file_:
            for line in file_:
                instruction = line.split()
                binary = ''
                if instruction[0] == 'addi':
                    binary += self.opt['addi'] +\
                        format(int(instruction[2]), '05b') +\
                        format(int(instruction[1]), '05b') +\
                        format(int(instruction[3]), '016b')
                    append_binary('binary.txt')


if __name__ == '__main__':
    target = Assembly()
    target.clean('assembly.txt')
    target.binary('copy.txt')
