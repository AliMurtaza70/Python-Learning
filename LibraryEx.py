class Library: 
    def __init__(self, books):
        self.books = books
        self.numberOfBooks = len(books)
    def printAllBooks(self):
        print(self.books)
    def addBook(self, bookName):
        self.books.append(bookName)
        self.numberOfBooks = len(self.books)
    def quantityOfBooks(self):
        print(len(self.books))


books = ["You", "Joe", "Lie"]
a = Library(books)
a.addBook("Fry")
a.printAllBooks()
a.quantityOfBooks()
print(a.numberOfBooks)

print(books)