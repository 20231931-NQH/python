def calculate_total_salary(employees):
    return sum(emp.calculate_salary() for emp in employees)
