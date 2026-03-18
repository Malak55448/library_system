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
        super().__init__( item_id, title, year)
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
        print(f" Id: {self.item_id} | The Title: {self.title} | The author: {self.author} | the year : {self.getYear()} | status: {status}")

# csv file 
file_of_library = "library_data.csv"

def saveBook(books):
    with open(file_of_library, "w", newline= "", encoding= "utf-8") as file: # I wanted to try a file that supports both Arabic and English to improve myself more in programming.
       writer = csv.writer(file)
       writer.writerow(["item_id", "title", "year", "author", "genre", "available"])
       for book in books:
           writer.writerow([
                book.item_id,
                book.title,
                book.getYear(),
                book.author,
                book.genre,
                book.getAvalilable()          
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
# menu
def addBook(our_books):
    print("\n Add book")
    item_id = input(" Book number: ").strip()
    title = input("Book name: ").strip()
    year = int(input("Year of publication:"))
    author = input("Author's Name: ").strip()
    genre = input("genre : ").strip()

    book = Books(item_id, title, year, author, genre)
    our_books.append(book)
    saveBook(our_books)
    print(" Book added successfully!")

def deleteBook(our_books):
    print("\n Delete book")
    item_id = input("Book number to delete: ").strip()
    for book in our_books:
        if book.item_id == item_id:
            our_books.remove(book)
            saveBook(our_books)
            print(" Book deleted successfully!")
            return
    print(" Book not found!")

def modifyBook(our_books):
    print("\n Modify book")
    item_id = input("Book number to modify: ").strip()
    for book in our_books:
        if book.item_id == item_id:
            book.title = input("New title: ").strip()
            book.author = input("New author: ").strip()
            saveBook(our_books)
            print("Book modified successfully!")
            return
    print(" Book not found!")

def displayBooks(our_books):
    print("\n All Books")
    if not our_books:
        print(" No books found!")
        return
    for book in our_books:
        book.display()

def menu():
    our_books = loadBook()
    while True:
        print("\n --Library System --")
        print("1. Add Book")
        print("2. Delete Book")
        print("3. Modify Book")
        print("4. Display Books")
        print("5. Exit")
        choice = input("Choose from the list  : ").strip()

        if choice == "1":
            addBook(our_books)
        elif choice == "2":
            deleteBook(our_books)
        elif choice == "3":
            modifyBook(our_books)
        elif choice == "4":
            displayBooks(our_books)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print(" Invalid choice!")

menu()