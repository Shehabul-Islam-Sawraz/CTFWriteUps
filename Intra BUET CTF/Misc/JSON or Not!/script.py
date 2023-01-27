indexes = [1,20,4,19,27,18,14,13,26,14,5,26,0,26,1,18,14,13,28]
str = "abcdefghjiklmnopqrstuvwxyz_{}"
flag = ""
for i in indexes:
    flag += str[i]
print(flag)