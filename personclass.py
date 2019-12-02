# Troy Jeffrey Amegashie
# 11/20/2019
# Textbook Programming Assignment

class Person():

    def __init__(self, first, last, age):
        self.first_name = first
        self.last_name = last
        self.age = age

    def description(self):
        author =(f"The name of this person is "
                f"{self.first_name} {self.last_name}."
                f"Their age is {self.age}")
        return author
