from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name, hostel):
        self.name = name
        self.hostel = hostel

    @abstractmethod
    def welcome(self):
        pass
