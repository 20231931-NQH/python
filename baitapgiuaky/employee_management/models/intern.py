from .employee import Employee

class Intern(Employee):
    def calculate_salary(self):
        return self.salary * 0.5

    def __str__(self):
        return f"[Intern]   ID: {self.emp_id} | Tên: {self.name} | Tuổi: {self.age} | Lương: {self.calculate_salary()} | Hiệu suất: {self.performance}"