class Employee:
    language="Py"
    salary=1000000

    def __init__(self,language):
        self.language=language
        print("I am creating an object")
    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

Harry= Employee("Java")
Harry.getInfo()
Harry.greet()