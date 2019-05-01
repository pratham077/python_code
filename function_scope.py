# x = 3
# y = 5
# def f(x):
#     x = x + 1
#     print("x = " + str(x))
#     print("y = " + str(y))
#     return x
#
# z = f(x)
# print("x = " + str(x))
# print("z = " + str(z))

# z = 1
# def test_scope():
#     global z
#     print("z = " + str(z))
#     z = 5
#     print("z = " + str(z))
#
# test_scope()
# print("z = " + str(z))

# def f1(x):
#   def g():
#       x = 'abc'
#   x = x + 1
#   print 'x =', x
#   g()
#   assert False
#   return x
#
# x = 3
# z = f1(x)
# x = 1
# def f():
#     def f1():
#         def f2():
#             print("x = " + str(x))
#         f2()
#     f1()
#
# f()

# class TestClass(object):
#
#     @staticmethod
#     def method_1():
#         l = [1,2,3]
#         TestClass.method_2()
#
#     @staticmethod
#     def method_2():
#         print(l)
#
# TestClass.method_1()



x = 1
def method_1():
    x = 2
    method_2()


def method_2():
    print(x)

method_1()
