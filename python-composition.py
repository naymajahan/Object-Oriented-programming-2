
#### object oriented programming in python

class StoryBook:
    ## class variables
    no_of_books = 0

    discount = 0.5


    def __init__(self, name, price, authorName, authorBorne, no_of_pages):
        # setting the instance variables here
        self.name = name
        self.price = price
        self.authorName = authorName
        self.authorBorne = authorBorne
        self.publishingYear = 2020
        self.no_of_pages = no_of_pages
        StoryBook.no_of_books += 1



# Regular method 1
    def get_book_info(self):
        print(f'The book name: {self.name}, price: {self.price}, authorName: {self.authorName}')
# Regular method 2
    def get_author_info(self):
        print(f'The author name: {self.authorName}, born : {self.authorBorne}')

# regular method 3 (Applying discount to an instance)

    def applying_discount(self):
        self.price = int(self.price - self.price * self.discount)



class Library:
    def __init__(self, book_list = None):
        if book_list is None:
            self.book_list = []
        else:
            self.book_list = book_list



    def get_all_books(self):
        for book in self.book_list:
            print(f'Title: {book.name}, Author: {book.authorName}, Price: {book.price}')


    def add_book(self, book):
        self.book_list.append(book)


    def remove_book(self, book):
        self.book_list.remove(book)







# creating an instance/object of the storyBook class

book1 = StoryBook('hamlet', 350, 'Shakespeare', 1564, 500)

book2 = StoryBook('The knite runner', 200, 'khalid hossini', 1965, 230)

public_library = Library()

public_library.add_book(book1)

public_library.add_book(book2)

public_library.get_all_books()
public_library.remove_book(book2)

public_library.get_all_books()








