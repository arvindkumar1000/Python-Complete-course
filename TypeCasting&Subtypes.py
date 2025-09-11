# Converion of one datatype to another is called as type-casting.

# there are two types of type-casting  1. implicit conversion  2. Explicit conversion


# implicit conversion

# a=123
# b=1.25
# print(type (a))
# print(type (b))

# c=a+b
# print(c)
# print(type(c))


# explicit conversion

a="123"
b=1.25
print(type (a))
print(type (b))

a=int(a)
print("after conversion", type(a))

c=a+b
print(c)
print(type(c))