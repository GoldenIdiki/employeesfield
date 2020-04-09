import string
import random


class Employee():

    def __init__(self, first_name, last_name, email, password):
        """Initialize an Employee"""
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email

    def register():
        """Register an employee"""
        first_name = input("what is your first name ")
        last_name = input("what is your last name ")
        email = input("What is your email ")

        full_name = [first_name, last_name]

        characters = string.ascii_letters
        length = 5

        generated_pass = ''.join(random.choice(characters) for i in range(length))

        pass_word = str(full_name[0][0:2] + full_name[1][-2:] + generated_pass)
        print(pass_word)

        response = input("Are you Okay with the password: Yes/No")
        if response == "Yes":
            password = generated_pass
            print("Thank you for registering")
            Employee.store(first_name, last_name, password, email)
            Employee.register()
        elif response == "No":
            user_password = input("Choose your Password")
            if len(user_password) < 7:
                print("Error: Password must be greater than 7 characters")
                Employee.register()
            else:
                password = user_password
                print("Thank you for registering")
                Employee.store(first_name, last_name, password, email)
                Employee.register()

    def login():
        """Initialize login"""
        email = input("what is your email")
        password = input("what is your password")

    def store(first_name, last_name, password, email):
        """store the employee details"""
        filename = "employees.txt"

        with open(filename, 'a') as data:
            data.write(first_name)
            data.write(last_name)
            data.write(password)
            data.write(email)

    def fetch_employees():
        """Fetch employees"""
        filename = "employees.txt"
        try:
            with open(filename) as data:
                contents = data.read()
                print(contents)
        except FileNotFoundError:
            error = "Sorry" + filename + "does not exist"
            print(error)


register = Employee.register()