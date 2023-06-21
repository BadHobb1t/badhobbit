class Year: 
    def __init__(self, days): 
        self.days = days 

    @property 
    def days(self): 
        return self.__days 

    @days.setter 
    def days(self, days): 
        if days == 366 or days == 365: 
            self.__days = days 
        else: 
            raise Exception('Некорректное значение') 

year = Year(365) 

year.days = 365