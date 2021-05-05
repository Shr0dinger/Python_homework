str_1 = list(input("Введите что-нибудь: "))
print(str_1)
ln = len(str_1)

if ln % 2 != 0:
    ln = ln - 1

for i in range(0, ln-1, 2):
    str_1[i], str_1[i+1] = str_1[i+1], str_1[i]
print(str_1)
