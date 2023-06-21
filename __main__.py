# class Infeterator: 
#     def __init__(self, start): 
#         self.start = start 
 
#     def __iter__(self): 
#         return self 
 
#     def __next__(self): 
#         self.start += 1 
#         return self.start - 1

# class Year: 
# def __init__(self, days): 
# self.days = days 

# @property 
# def days(self): 
# return self.__days 

# @days.setter 
# def days(self, days): 
# if days == 366 or days == 365: 
# self.__days = days 
# else: 
# raise Exception('Некорректное значение') 

# year = Year(365) 

# year.days = (36) 

# print(year.days)