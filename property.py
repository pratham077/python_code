class Celsius(object):
    def __init__(self,value):
        self.temperature =value

    def to_fahreneit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("inside temperature property")
        return self._temperature

    @temperature.setter
    def temperature(self,value):
        print("inside temperature.setter")
        if value < -273:
            raise ValueError("Invalid temperature")
        else:
            self._temperature = value

    def __str__(self):
        return "celsius : " + str(self.temperature) + " fahreneit : " + str(self.to_fahreneit())


    def __lt__(self,other):
        return self.temperature < other.temperature




temp1 = Celsius(37)
temp2 = Celsius(500)
temp3 = Celsius(-72)

print()

print(temp1.temperature)
print(temp2.temperature)
print(temp3.temperature)


# print(temp1 < temp2)
# temperature_list = [temp1,temp2,temp3]
# print()
# for temperature in temperature_list:
#     print(temperature)
#
# print()
# temperature_list.sort()
#
# print("after sorting ..\n")
# for temperature in temperature_list:
#     print(temperature)


############################################################
# class Celsius(object):
#     def __init__(self,value):
#         self.expr =value
#
#     def to_fahreneit(self):
#         return (self.expr * 1.8) + 32
#
#     @property
#     def expr(self):
#         print("inside temperature property")
#         #return  15000
#         return self._foo
#
#     @expr.setter
#     def expr(self,value):
#         print("inside temperature.setter")
#         if value < -273:
#             raise ValueError("Invalid temperature")
#         else:
#             self._foo = value
#
#     def __str__(self):
#         return "celsius : " + str(self.expr) + " fahreneit : " + str(self.to_fahreneit())
#
#
#     def __lt__(self,other):
#         return self.expr < other.expr
#
#
#
#
# temp1 = Celsius(37)
# temp2 = Celsius(500)
# temp3 = Celsius(-72)
#
# print()
#
# print(temp1.expr)
# print(temp2.expr)
# print(temp3.expr)


# print(temp1 < temp2)
# temperature_list = [temp1,temp2,temp3]
# print()
# for temperature in temperature_list:
#     print(temperature)
#
# print()
# temperature_list.sort()
#
# print("after sorting ..\n")
# for temperature in temperature_list:
#     print(temperature)
