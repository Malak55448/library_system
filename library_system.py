import csv 
import os 
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

    #get private
    def getAvalilable(self):
        return self.__available
    
    #Setter with validation
    def setAvalilable(self, statuss):
        if isinstance(statuss, bool):
            self.__available = statuss
        else:
            print("The value must be True or False!!!")

    def display(self):
        status = "available" if self.__available else "seconded"
        print(f" Id; {self.item_id} | The Title: {self.title} | The author: {self.author} | the year : {self.getYear()} | status; {status}")

# csv file 
file_of_library = "library_data.csv"

def saveBook(books):
    with open(file_of_library, "w", newline= "", encoding= "utf-8") as f: # I wanted to try a file that supports both Arabic and English to improve myself more in programming.
      pass