
def load_books(filename='books.txt'):
    books = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                if ':' in line:
                    book, status = line.strip().split(':', 1)
                    books[book.strip()] = status.strip()
    except FileNotFoundError:
        books = {
            "Python 101": "available",
            "Clean Code": "available",
            "Algorithms": "available"
        }
    return books


def save_books(filename='books.txt'):
    with open(filename, 'w') as file:
        for book, status in books.items():
            file.write(f"{book}:{status}\n")


def list_books():
    for book, status in books.items():
        print(f"{book} - {status}")


def borrow_book(book_name):
    if book_name in books:
        if books[book_name] == "available":
            books[book_name] = "borrowed"
            print(f"You have borrowed '{book_name}'.")
        else:
            print(f"Sorry, '{book_name}' is currently borrowed.")
    else:
        print(f"'{book_name}' does not exist in the library.")


def return_book(book_name):
    if book_name in books:
        if books[book_name] == "borrowed":
            books[book_name] = "available"
            print(f"You have returned '{book_name}'.")
        else:
            print(f"'{book_name}' was not borrowed.")
    else:
        print(f"'{book_name}' does not exist in the library.")


books = load_books()
while True:
    user_cmd = input("> ").strip()
    if user_cmd == "list books":
        list_books()
    elif user_cmd.startswith("borrow book"):
        book_name = user_cmd[len("borrow book "):]
        borrow_book(book_name)
    elif user_cmd.startswith("return book"):
        book_name = user_cmd[len("return book "):]
        return_book(book_name)
    elif user_cmd == "exit":
        save_books()
        print("Changes saved. Exiting...")
        break
    else:
        print("Invalid command. Please try again.")

