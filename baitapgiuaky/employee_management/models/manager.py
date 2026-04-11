from .employee import Employee

class Manager(Employee):
    def __init__(self, emp_id, name, age, salary, department=None):
        super().__init__(emp_id, name, age, salary)
        self.department = department or "Chưa phân công"

    def calculate_salary(self):
        return self.salary * 2

    def __str__(self):
        return f"[Manager] ID: {self.emp_id} | Tên: {self.name} | Tuổi: {self.age} | Lương: {self.calculate_salary()} | Phòng ban: {self.department} | Hiệu suất: {self.performance}"