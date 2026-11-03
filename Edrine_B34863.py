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