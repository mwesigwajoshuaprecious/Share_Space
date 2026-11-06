from abc import ABC, abstractmethod

from Edrine_B34863 import ShareSpace


class User(ABC):
    def __init__(self, name, hostel):
        self.name = name
        self.hostel = hostel

    @abstractmethod
    def welcome(self):
        pass

class Student(User):
    def welcome(self):
        return "Welcome, " + self.name


class Admin(User):
    def welcome(self):
        return "Welcome, Administrator " + self.name


class Item:
    def __init__(self, name, owner, hostel):
        self.name = name
        self.owner = owner
        self.hostel = hostel
        self.__available = True

    def is_available(self):
        return self.__available

    def borrow(self):
        if self.__available:
            self.__available = False
            return True
        return False

    def return_item(self):
        self.__available = True













## Timothy's contribution
 def show_menu(self):
        while True:
            print("\n=== ShareSpace Hostel Borrowing Club ===")
            print("1. Register student")
            print("2. Choose user")
            print("3. List an item")
            print("4. Browse items")
            print("5. Request an item")
            print("6. Approve or reject requests")
            print("7. Return an item")
            print("0. Exit")

            choice = input("Choose: ")

            if choice == "1":
                self.register_student()
            elif choice == "2":
                self.choose_user()
            elif choice == "3":
                self.add_item()
            elif choice == "4":
                self.browse_items()
            elif choice == "5":
                self.request_item()
            elif choice == "6":
                self.review_requests()
            elif choice == "7":
                self.return_item()
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Please choose a number from the menu.")

def greet_user(user):
    print(user.welcome())

sample_student = Student("Amina", "North Hostel")
sample_admin = Admin("Sam", "Campus")

greet_user(sample_student)
greet_user(sample_admin)
# Initialize and start the ShareSpace program
program = ShareSpace()
program.show_menu()
class ShareSpace:
    # =========================================================
    # COMPOSITION
    # ShareSpace contains lists of Item and BorrowRequest objects.
    # These objects are used as parts of the ShareSpace system.
    # =========================================================
    def __init__(self):
        self.students = []
        self.items = []
        self.requests = []
        self.current_user = None

    def register_student(self):
        print("\nRegister a student")
        name = input("Name: ")
        hostel = input("Hostel: ")

        student = Student(name, hostel)
        self.students.append(student)

        print("Student registered.")

    def choose_user(self):
        if len(self.students) == 0:
            print("Register a student first.")
            return

        print("\nStudents:")
        for number, student in enumerate(self.students, start=1):
            print(number, "-", student.name)

        choice = input("Choose a student number, or enter A for Admin: ")

        # Make a simple Admin account for demonstrating the role.
        if choice.lower() == "a":
            self.current_user = Admin("ShareSpace Admin", "Campus")
            print(self.current_user.welcome())
            return

        if choice.isdigit():
            number = int(choice) - 1
            if 0 <= number < len(self.students):
                self.current_user = self.students[number]

                # =================================================
                # POLYMORPHISM
                # This calls welcome() without needing to write
                # separate code for Student and Admin here.
                # The object's class decides which method runs.
                # =================================================
                print(self.current_user.welcome())
                return

        print("Invalid choice.")

    def add_item(self):
        if self.current_user is None:
            print("Choose a user first.")
            return

        if isinstance(self.current_user, Admin):
            print("Admins cannot list student items.")
            return

        name = input("Item to share: ")
        item = Item(name, self.current_user, self.current_user.hostel)
        self.items.append(item)

        print("Item listed.")
