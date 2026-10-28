class Library:
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (
            f"Library: {self.city}, {self.street}, {self.zip_code}, "
            f"Open Hours: {self.open_hours}, Phone: {self.phone}"
        )


class Employee:
    def __init__(
        self, first_name, last_name, hire_date, birth_date,
        city, street, zip_code, phone
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (
            f"Employee: {self.first_name} {self.last_name}, "
            f"Hire Date: {self.hire_date}, Birth Date: {self.birth_date}, "
            f"Address: {self.city}, {self.street}, {self.zip_code}, "
            f"Phone: {self.phone}"
        )


class Student:
    def __init__(
        self, first_name, last_name, birth_date,
        city, street, zip_code, phone
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (
            f"Student: {self.first_name} {self.last_name}, "
            f"Birth Date: {self.birth_date}, "
            f"Address: {self.city}, {self.street}, {self.zip_code}, "
            f"Phone: {self.phone}"
        )


class Book:
    def __init__(
        self, library: Library, publication_date,
        author_name, author_surname, number_of_pages
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (
            f"Book: {self.author_name} {self.author_surname}, "
            f"Publication Date: {self.publication_date}, "
            f"Pages: {self.number_of_pages}, "
            f"Library: {self.library.city}, {self.library.street}, "
            f"{self.library.zip_code}"
        )


class Order:
    def __init__(
        self, employee: Employee, student: Student,
        books: list[Book], order_date
    ):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_info = "\n".join([str(book) for book in self.books])
        return (
            f"Order Date: {self.order_date}\n"
            f"Employee: {self.employee.first_name} {self.employee.last_name}\n"
            f"Student: {self.student.first_name} {self.student.last_name}\n"
            f"Books:\n{books_info}"
        )


lib1 = Library(
    "New York", "5th Avenue", "10001", "9 AM - 5 PM", "123-456-7890"
)
lib2 = Library(
    "Los Angeles", "Sunset Boulevard", "90001", "10 AM - 6 PM", "987-654-3210"
)

emp1 = Employee(
    "John", "Doe", "2020-01-15", "1990-05-20",
    "New York", "5th Avenue", "10001", "123-456-7890"
)
emp2 = Employee(
    "Jane", "Smith", "2021-03-20", "1985-12-10",
    "Los Angeles", "Sunset Boulevard", "90001", "987-654-3210"
)
emp3 = Employee(
    "Alice", "Johnson", "2019-07-10", "1992-08-15",
    "New York", "5th Avenue", "10001", "123-456-7890"
)

book1 = Book(lib1, "2022-01-01", "Author1", "Surname1", 300)
book2 = Book(lib1, "2021-05-15", "Author2", "Surname2", 250)
book3 = Book(lib2, "2020-10-10", "Author3", "Surname3", 400)
book4 = Book(lib2, "2019-07-20", "Author4", "Surname4", 150)
book5 = Book(lib1, "2023-03-05", "Author5", "Surname5", 200)

student1 = Student(
    "Emily", "Brown", "2000-02-15",
    "New York", "5th Avenue", "10001", "123-456-7890"
)
student2 = Student(
    "Michael", "Davis", "1999-11-30",
    "Los Angeles", "Sunset Boulevard", "90001", "987-654-3210"
)
student3 = Student(
    "Sarah", "Wilson", "2001-06-25",
    "New York", "5th Avenue", "10001", "123-456-7890"
)

order1 = Order(emp1, student1, [book1, book2], "2023-06-01")
order2 = Order(emp2, student2, [book3, book4], "2023-06-02")

print(order1)
print(order2)
