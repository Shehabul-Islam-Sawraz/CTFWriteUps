message = "27 39 33 34 10 36 32 33 35 10 37 34 10 38 38 39 38 38 15 15 10 32 39 33 38 38 33 33 41 34 36 16 16 38 31 33 16 39 35 38 11 16 36 41"

# Converting string to list of integers

lstnumber = map(int, message.split())
print(lstnumber)
# Characters will be printed in this format (char_code = character code)
#   chr(char_code) | chr(char_code + 1) |  chr(char_code + 2)

printstr = "{0} | {1} | {2}"
for item in lstnumber:
    print(printstr.format(chr(item*3), chr(item*3+1), chr(item*3+2)))