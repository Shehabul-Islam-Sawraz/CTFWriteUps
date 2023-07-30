import binascii


str1 = binascii.unhexlify(
    '554252434452544c4407685a42015f6850075e5950680759685f04450416164a'
)
# print(str1)
for i in range(255):
    str2 = ''
    for c in str1:
        str2 += chr(c ^ i)
    if 'buetsec{' in str2:
        print(str2)
        break