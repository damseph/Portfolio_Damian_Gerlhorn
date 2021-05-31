from utils import database


def menu():
    database.create_book_table()
    option = int(input("""
What do you want to do?
1- Enter a book's info.
2- Retrieve a book's info.
3- Retrieve book's list.
4- Mark a book that you finished reading.
5- Delete a book from the list.
6- Stop the app.
Please type your choice (1-6):
    """))
    while option != 6:
        if option == 1:
            add_new_book()
        elif option == 2:
            retrieve_book_info()
        elif option == 3:
            retrieve_book_list()
        elif option == 4:
            mark_book_as_read()
        elif option == 5:
            delete_book_from_list()
        else:
            print("The option you typed is not valid.")
        option = int(input("""
What do you want to do?
1- Enter a book's info.
2- Retrieve a book's info.
3- Retrieve book's list.
4- Mark a book that you finished reading.
5- Delete a book from the list.
6- Stop the app.
Please type your choice (1-6):
    """))

    print("Program closing. Goodbye.")


def add_new_book():
    title = input("Type the title of the book: ")
    author = input("Type the author's name: ")

    database.add_book(title, author)


def retrieve_book_info():
    books = database.retrieve_book_list()

    search_criteria = input("Type how you want to look for books (by title or author): ")
    search = input("What do you want to look for: ")

    found_books = []
    for book in books:
        if search == book[search_criteria]:
            found_books.append(book)

    for book in found_books:
        print(f"The book {book['title']} was written by {book['author']}")
        if book["read"] == 1:
            print("You have already read this book. ")
        elif book["read"] == 0:
            print("You haven't read this book yet. ")

    if len(found_books) == 0:
        print("No matching books were found. ")


def retrieve_book_list():
    books = database.retrieve_book_list()

    for book in books:
        print(f"The book {book['title']} was written by {book['author']}")
        if book["read"] == 1:
            print("You have already read this book. ")
        elif book["read"] == 0:
            print("You haven't read this book yet. ")


def mark_book_as_read():
    read_book = input("Type the title of the book you want to mark as read: ")
    database.mark_as_read(read_book)


def delete_book_from_list():
    to_delete_book = input("Type the title of the book you want to delete: ")
    database.delete_book(to_delete_book)


menu()
