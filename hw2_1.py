a = int(447)
b = float(32.1718)
c = complex(4, 9)
d = str("Hello World")
e = ['p', 'y', 't', 'h', 'o', 'n']
f = ('p', 'y', 't', 'h', 'o', 'n')
g = set("python")
h = {1: "Hello", "key_2": 123}
i = True
j = "World".encode('ascii')
k = None
test_list = [a, b, c, d, e, f, g, h, i, j, k]

for i in test_list:
    print(type(i), " ", i)
