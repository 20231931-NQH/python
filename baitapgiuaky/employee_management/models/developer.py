from .employee import Employee

class Developer(Employee):
    def __init__(self, emp_id, name, age, salary, languages=None):
        super().__init__(emp_id, name, age, salary)
        self.languages = languages or []

    def calculate_salary(self):
        return self.salary * 1.5

    def __str__(self):
        return f"[Developer] ID: {self.emp_id} | Tên: {self.name} | Tuổi: {self.age} | Lương: {self.calculate_salary()} | Ngôn ngữ: {', '.join(self.languages)} | Hiệu suất: {self.performance}"