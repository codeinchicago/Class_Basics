class Employee:
    def __init__(self, firstname, lastname, title, salary, email):
        self.firstname = firstname
        self.lastname = lastname
        self.title = title
        self.salary = salary
        self.email = email

    def paymore(self):
        raiseamount = 1.05
        self.salary = self.salary * raiseamount
        #print(f"{self.lastname}'s salary is now {self.salary}.")
        return f"{self.lastname}'s salary is now {self.salary}."



worker1 = Employee("Last", "First", "CEO", 100, "me@example.com")
worker1.paymore()

"""
Create two more classes that inherit from the Employee class. One for Sales and one for Development. Both of these classes will have the same attributes as the Employee.

For the Sales employees, add a phone number attribute on instantiation using the super method.
Create a method on the Sales class that will Send a Follow Up Email. It should take in a customer name and "send" aka print a formatted email "Dear customer, Thank you for your interest in our product. Please let me know if you have any questions. My email is email or my phone number is phone number. Thanks, full name"
Create a method on the Development class called code that will print out "full name is writing code".
"""

class Sales(Employee):
    pass

class Development(Employee):
    pass