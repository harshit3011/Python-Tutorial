class Employee:
    language="Py"
    salary=1000000

    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

Harry= Employee()
Harry.getInfo()
Harry.greet()