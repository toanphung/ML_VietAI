n_x = 3.0
print(type(n_x))
s_x = "abc"
print(type(s_x))
b_t = True
print(type(b_t))
a = [3, 4, 5, 6, 7, 8]
a[2:4] = [7, 8]
d = {'cat': 'cute', 'dog': 'furry'}  # dictionary
print('cat' in d)
animals = {'cat', 'dog'}  # set
for animal in animals:
    print(animal)
for idx, animal in enumerate(animals):
    print("%d: %s" % (idx+1, animal))

d_c = {'person': 2, 'cat': 4, 'spider': 8}
for a in d_c:
    print("A %s has %d legs" % (a, d_c[a]))
nums = [0, 1, 2, 3, 4]
even_square = {x: x ** 2 for x in nums if x % 2 == 0}
print(even_square)