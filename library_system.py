# My library system

class Library_Sys_Item:
    def __init__(self, item_id, title, year):
        self.item_id = item_id 
        self.title = title 
        self.__year = year 

    # get private (self.__year)
    def getYear(self):
        return self.__year 
    
    #Setter with validation
    def setYear(self, year):
        if year >= 1988 and year <= 2026:
          self.__year = year 
        
        else:
            print("The year is incorrect!!")

class Books(Library_Sys_Item):
    def __init__(self, item_id, title, year, author, genre):
        super.__init__(self, item_id, title, year)
        self.author = author
        self.genre = genre
        self.__available = True 