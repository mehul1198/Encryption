passwd = input("Enter password: ")
en = []
b = 0
while b < len(passwd):
    en.append(ord(passwd[b]))
    b += 1
crypt = [x - 5 for x in en]
encrypt = [chr(n) for n in crypt]
password = ''.join(encrypt)
print(password)
