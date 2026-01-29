userName = "Chai aur code"


def func():
    userName="chai"
    print(userName)


print(userName)
func()



x = 99

# def func2(y):
#     z = x + y
#     return z

# result = func2(1)
# print(result)



#  -----Global----
# def func3():
#     global x
#     x=12

# func3()
# print(x)


# def fun4():
#     x=88
#     def fun5():
#         print(x)
#     fun5()
# fun4()



def fun4():
    x=88
    def fun5():
        print(x)
    return fun5
myresult=fun4()
myresult()



#  closure in python....

def chaiaurcode(num):
    def actual(x):
        return x **num
    return actual

# def chaiaurcode(2):
#     def actual(x):
#         return x **2
#     return actual

f = chaiaurcode(2)
g= chaiaurcode(3)

print(f(2))
print(g(3))

