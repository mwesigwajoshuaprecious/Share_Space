from abc import ABC, abstractmethod


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