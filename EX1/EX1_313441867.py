import sys

# arguments
# type = sys.argv[0]
# length = sys.argv[1]
# value = sys.argv[2]
import sys

max_len = 0
# find the longest length for the 3rd parameter according to which set the size of the last column
try:
    csv_file = open("in.csv", "r")  # opening it again for reading
except IOError:
    print("error opening file")
    exit(1)
for line in csv_file:
    line = line.split(',')
    line_len = int(line[1])
    max_len = line_len if max_len < line_len else max_len


# headers
print("|{:<7}| {:<6}| {:<{length}}|".format('Type', 'Length', 'Value', length=max_len))
print("|{:<7}| {:<6}| {:<{length}}|".format('-------', '------', '-' * max_len, length=max_len))

try:
    csv_file = open("in.csv", "r")  # opening it again for reading
except IOError:
    print("error opening file")
    exit(1)
# print actual lines
for line in csv_file:
    args = line.split(',')
    arg_type = args[0].rstrip()  # ignore trailing characters
    length = args[1].rstrip()
    csv_file = args[2].rstrip()

    print("|{:<7}| {:<6}| {:<{length}}|".format(arg_type, length, csv_file, length=max_len))
