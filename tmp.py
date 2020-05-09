print('hi')

a = (1, 2, 3, 4, 5, 6)
b = [1, 2, 3, 4, 5, 6]
a.__sizeof__()
b.__sizeof__()
d = {(1, 1, 1) : 1}
d
a = tuple()
a
a = ('s')
a
a = tuple('hello, world!')
a

#Dict
d = {}
d
d = {'dict': 1, 'dictionary': 2}
d
d = dict(short='dict', long='dictionary')
d
d = dict([(1, 1), (2, 4)])
d
d = dict.fromkeys(['a', 'b'])
d
d = {1: 2, 2: 4, 3: 9}
d[1]

#множество

a = set()
a
a = set('hello')
a
a = {'a', 'b', 'c', 'd'}
a
a = {i ** 2 for i in range(10)}
a
words = ['hello', 'daddy', 'hello', 'mum']
set(words)

#bytes

b'bytes'
bytes('bytes', encoding = 'utf-8')
bytes([50, 100, 76, 72, 41])
chr(50)
chr(100)
chr(76)
b = bytearray(b'hello world!')
b
b[0]
b[0] = 105



#Numbers

x = 50
y = 100

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)
print(x%y)
print(-x)
print(abs(x))
print (divmod(x,y))
print(x**y)

#Lines

S1 = 'vlad'
S2 = 'gutuleac'

print(S1+S2)
print('vlad'*3)
len('vlad')

S = 'spam'
S[0]
S[2]
S[-2]

s = 'vladgutuleac'
s[3:5]
s[2:-2]
s[:6]

#List

list = ('a','b','c')

list.count('b')

list.insert(b,x)

list.remove('a')


#Index

a = [1, 3, 8, 7]
a[1]
a[2]
a[4]
a[-1]
a[-4]
a[-5]
a[1:]
a[:]
a[:3]
a[::2]
a[::-1]
a[:-2]
a[-2::-1]


