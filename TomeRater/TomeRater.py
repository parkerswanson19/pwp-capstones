class User(object):
    def __init__(self, name, email):
        self.email = email
        self.name = name
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("User's email has been updated.")

    def __repr__(self):
        represent = "User " + self.name + ", email: " + self.email + ", books read: " + str(len(self.books))
        return represent

    def __eq__(self, other_user):
        if other_user == self.name and other_user.get_email() == self.email:
            return True
        else:
            return False

    def read_book(self, book, rating=None):
        if rating != None:
            self.books[book] = rating

    def get_average_rating(self):
        amt = 0
        for rating in self.books.values():
            amt += rating

        if len(self.books) > 0:
            avg = amt / len(self.books)
            return avg
        else:
            return 0

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, replacement):
        self.isbn = replacement
        print("Book's ISBN has been updated")

    def add_rating(self, rating):
        if rating != None:
            if rating >= 0 and rating <= 4:
                self.ratings.append(rating)
            else:
                print("Invalid Rating")

    def __eq__(self, book):
        if book.get_title() == self.title and book.get_isbn() == self.isbn:
            return True
        else:
            return False

    def get_average_rating(self):
        amt = 0
        for rating in self.ratings:
            amt += rating

        # check for div by zero
        avg = amt / len(self.ratings)
        return avg

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super(Fiction, self).__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        repr = self.title + " by " + self.author
        return repr


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super(Non_Fiction, self).__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        represent = self.title + ", a " + self.level + " manual on " + self.subject
        return represent


class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        isbns = []
        for book in self.books.keys():
            isbns.append(book.get_isbn())

        if isbn in isbns:
            print("Book has already been created.")
        else:
            story = Book(title, isbn)
            return story

    def create_novel(self, title, author, isbn):
        novel = Fiction(title, author, isbn)
        return novel

    def create_non_fiction(self, title, subject, level, isbn):
        non_f = Non_Fiction(title, subject, level, isbn)
        return non_f

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users.keys():
            for mail, person in self.users.items():
                if mail == email:
                    person.read_book(book, rating)
                    book.add_rating(rating)
                    if book in self.books:
                        self.books[book] += 1
                    else:
                        self.books[book] = 1
        else:
            print("No user with email " + email + "!")

    def add_user(self, name, email, user_books=None):
        if email in self.users.keys():
            print("This email is already in use.")
        else:
            if "@" in email and (".com" in email or ".edu" in email or ".org" in email):
                user = User(name, email)
                self.users[email] = user
                if user_books:
                    for book in user_books:
                        self.add_book_to_user(book, email)
            else:
                print("Invalid email was entered.(email must contain '@' and '.com'/'.edu'/'.org'")

    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def get_most_read_book(self):
        highest_value = list(self.books.values())[0]
        most_read = list(self.books.keys())[0]
        for key, value in self.books.items():
            if value > highest_value:
                highest_value = value
                most_read = key
        return most_read

    def highest_rated_book(self):
        highest_rating = list(self.books.keys())[0].get_average_rating()
        highest_rated_book = list(self.books.keys())[0]
        for book in self.books.keys():
            if book.get_average_rating() > highest_rating:
                highest_rating = book.get_average_rating()
                highest_rated_book = book
        return highest_rated_book

    def most_positive_user(self):
        users_in_users = self.users.values()
        highest_rating = list(users_in_users)[0].get_average_rating()
        highest_rated_user = list(self.users.values())[0]
        for user in self.users.values():
            if user.get_average_rating() > highest_rating:
                highest_rating = user.get_average_rating()
                highest_rated_user = user
        return highest_rated_user

