# Write a Library class with no_of_books and books as two instance variables.
# Create a library from this Library class and show how you can print all books,
# add a book, and get the number of books using different methods.
# The book list is kept in memory only, so it is not persisted after the program stops.
class Library1:
    def __init__(self):
        self.books = []
        self.no_of_books = 0

    def add_books(self, book_name):
        self.books.append(book_name)
        self.no_of_books += 1 

    def remove_books(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            self.no_of_books -= 1
        else:
            print(f"Error: '{book_name}' is not in the library.")

    def print_books(self):
        print("Books in library:", self.books)

    def many_books(self):
        print("Total number of books:", self.no_of_books)

# Testing the code
a = Library1()
a.add_books("raft")     # First, add a book so it can be removed
a.remove_books("raft")  # This will successfully remove it
a.add_books("gift")     # Add the new book
a.print_books()         # Print books in library
a.many_books()          # Print total count
