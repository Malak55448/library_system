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
    with open(file_of_library, "w", newline= "", encoding= "utf-8") as file: # I wanted to try a file that supports both Arabic and English to improve myself more in programming.
       writer = csv.writer(file)
       writer.writerow(["item_id", "title", "year", "author", "gener", "available"])
       for book in books:
           writer.writerow([
                book.item_id,
                book.title,
                book.getYear(),
                book.author,
                book.genre,
                book.setAvalilable()          
            ])
           
def loadBook():
    our_books =[]
    if not os.path.exists(file_of_library):
        return our_books
    with open(file_of_library, "r", encoding="utf-8") as file:
        read = csv.DictReader(file)
        for row in read:
            book = Books(
                row["item_id"],
                row["title"],
                int(row["year"]),
                row["author"],
                row["genre"]
            )
            book.setAvalilable(row["available"] == "True")
            our_books.append(book)
    return our_books  