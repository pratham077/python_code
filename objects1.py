class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

    def __lt__(self,other):
        return self.age < other.age

    def __str__(self):
        return self.name + " " + str(self.age)

p1 = Person("Dean Winchestor",30)
p2 = Person("Sam Winchestor",26)
p3 = Person("Castiel",1000)

person_list = [p1,p2,p3]

#print()
# print("person list : ")
# for person in person_list:
#     print(person)
#
# person_list.sort(reverse = True)
#
# print("sorted person list : ")
# for person in person_list:
#     print(person)

print(Person.__dict__['__dict__'])
# class Detective(Person):
#     next_id = 0
#     def __init__(self,name,age):
#         super().__init__(name,age)
#         self.id = Detective.next_id
#         Detective.next_id += 1
#
#     # def __str__(self):
#     #     return super().__str__() + " " + str(self.id)
#
# s1 = Detective("Patrick Jane",40)
# s2 = Detective("Teresa Lisbon",35)
# s3 = Detective("Kimbal Cho",32)
#
# print(s1)
# print(s2)
# print(s3)
