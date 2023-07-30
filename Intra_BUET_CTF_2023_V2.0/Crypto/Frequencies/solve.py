# Read the content of the file
with open("jumbled.txt", "r") as file:
    content = file.read()

# Count the occurrences of each character in the file
chars = {}
for char in content:
    chars[char] = chars.get(char, 0) + 1

# Define the substitution dictionary
subs = {
    "c": " ",
    "1": "e",
    "T": "t",
    "k": "a",
    "\\": "o",
    "\"": "o",
    "|": "n",
    "w": "h",
    "0": "r",
    ":": "i",
    "2": "s",
    "V": "d",
    "S": "l",
    "K": "m",
    "E": "u",
    "7": "w",
    ")": "c",
    "x": "f",
    "u": "y",
    "]": "p",
    "L": "g",
    "C": "p",
    "i": "b",
    "m": "v",
    "G": "x",
    "e": "a",
    "W": "k",
    "/": "z",
    "h": "t",
    "$": "_",
    "R": "M",
    "r": "m",
    "f": "h",
    "-": "x",
    "a": "q",
    "X": "J",
    "v": "'",
    "#": "."
}

# Perform character substitution
result = ""
for char in content:      
    result += subs.get(char, char)

print(result)
