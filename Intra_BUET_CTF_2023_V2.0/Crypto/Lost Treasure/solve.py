#!/usr/bin/env python3
import string

def rot(n):
	from string import ascii_lowercase as lc, ascii_uppercase as uc
	lookup = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
	return lambda s: s.translate(lookup)

ciphertext = "RGLQGSVZGSCMKZTXKGCUDRZOZZXKK"
print("C", ciphertext)

plaintext = ""
for i, ch in enumerate(ciphertext):
	result = rot(i%26)(ch)
	plaintext += result	
print("P", plaintext)

for t in range(26):
	result = rot(t%26)(plaintext)
	print(t, result)