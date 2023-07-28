def encrypt_message(message, key):
    encrypted = []
    for c in message:
        encrypted.append(str(ord(c) // key))
    return ' '.join(encrypted)

message = "<redacted>"
key = 3
encrypted = encrypt_message(message, key)
print(encrypted)