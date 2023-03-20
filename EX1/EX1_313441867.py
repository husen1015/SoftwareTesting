import sys

# command line arguments
file_name = sys.argv[1]
# file_name = "in.csv"


def valid_args(line_args: list):
    if len(line_args) == 3:
        first = line_args[0]
        second = int(line_args[1])
        third = line_args[2]
        # validate first & second arg

        # if 3rd arg is string
        if first == '1' and second == len(third):
            return True

        # if 3rd arg is int make sure 2nd argument = how many bytes needed for 3rd argument
        if (second != 0) and (second & (second-1) == 0):  # check if second arg is power of 2
            binary_form = bin(int(third))  # 3rd arg in binary
            negative = False
            if binary_form[0] == '-':
                negative = True
            binary_form = binary_form[3:] if negative else binary_form[2:]  # remove - from negative numbers
            bytes_num = (len(binary_form) + 1) / 8  # how many bytes to represent the 3rd arg,
            # + 1 to account for the signed bit

            # here im basically doing a ceil(bytes_num) manually since I cant import math
            if not float(bytes_num).is_integer():
                bytes_num = int(bytes_num) + 1
            else:
                bytes_num = int(bytes_num)

            if first == '2' and second == bytes_num:
                return True

    return False


try:
    with open(file_name, "r") as csv_file:
        # Find the maximum length of the third parameter.
        max_len = 0
        for line in csv_file:
            args = line.strip().split(",")

            if not valid_args(args):
                raise ValueError("bad CSV file format or illegal values")
            max_len = max(max_len, len(args[2]))

        # Print the table headers.
        print("|{:<7}| {:<6}| {:<{length}}|".format("Type", "Length", "Value", length=max_len))
        print("|{:<7}| {:<6}| {:<{length}}|".format("-------", "------", "-" * max_len, length=max_len))

        # Print the actual lines.
        csv_file.seek(0)  # Go back to the beginning of the file.
        for line in csv_file:
            args = line.strip().split(",")
            # if len(args) != 3:
            #     raise ValueError("CSV file is not well-formed")
            arg_type, length, csv_value = args
            print("|{:<7}| {:<6}| {:<{length}}|".format(arg_type.strip(), length.strip(), csv_value.strip(),
                                                        length=max_len))

except IOError:
    print("IOError raised: can't opening file")
    sys.exit(1)
except ValueError as err:
    print(err)
    sys.exit(1)
