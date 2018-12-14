"""this is a class practice for the fact that i dont know much about them and wondered what is the point of classes"""
__author__ = " Mathew Reynolds"
__email__ = "mattyr@talktalk.net"
__date__ = "08-11-2018"


class Students:
    def __init__(self, names, age, course):
        self.names = names
        self.age = age
        self.course = course

    def name(self):
        return self.names + " is " + self.age + " and studies " + self.course


def name_of_students():
    y = Students((input("name: ")), (input("age: ")), (input("course: ")))
    print(y.name())


if __name__ == "__main__":
    name_of_students()
