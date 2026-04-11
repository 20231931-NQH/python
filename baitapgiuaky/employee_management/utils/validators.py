from exceptions.employee_exceptions import *

def validate_age(age):
    if age < 18 or age > 65:
        raise InvalidAgeError("Tuổi phải từ 18-65")

def validate_salary(salary):
    if salary <= 0:
        raise InvalidSalaryError("Lương phải > 0")

def validate_email(email):
    if "@" not in email:
        raise ValueError("Email không hợp lệ")
