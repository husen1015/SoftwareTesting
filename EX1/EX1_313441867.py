import sys

# command line arguments
file_name = sys.argv[1]

# file_name = "in.csv"
try:
    with open(file_name, "r") as csv_file:
        # Find the maximum length of the third parameter.
        max_len = 0
        for line in csv_file:
            args = line.strip().split(",")
            if len(args) != 3:
                raise ValueError("bad CSV file format")
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

