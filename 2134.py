# class Year:
#     def __init__(self):
#         self.__days = 365

#     def get_days(self):
#         return self.__daysФ

#     def set_days(self, days):
#         if days == 365 or days == 366:
#             self.__days = days
#         else:
#             raise Exception('Некорректное значение!')
            
# print(year1.get_days())
# year1 = Year()
# year1.set_days(50)
# print(year1.get_days())

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property #getter
    def age(self):
        return self.__age

    @age.setter #setter
    def age(self, age):
        if age >= 0:
            self.__age = age
        else:
            raise Exception('Вы ещё не родились!!!')
    @name.deleter 
    def name(self): 
        del self.__name
    @age.deleter 
    def name(self): 
        del self.__age


person = Person('Иван', 25)
person.age = -15