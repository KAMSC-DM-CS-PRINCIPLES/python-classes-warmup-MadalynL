# TODO create class Student

if __name__ == "__main__":
    # create Student below this
    pass

class Student:
    def __init__(self, name, grade):
        self.name=name
        self.grade=grade

    def get_name(self):
        return self.name
    def get_grade(self):
        return self.grade
    def set_grade(self,newNum):
        self.grade= newNum