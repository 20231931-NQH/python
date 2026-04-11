from exceptions.employee_exceptions import *
from models.manager import Manager
from models.developer import Developer
from models.intern import Intern

class Company:
    def __init__(self):
        self.employees = {}

    # ── CRUD ──────────────────────────────────────────────
    def add_employee(self, emp):
        if emp.emp_id in self.employees:
            raise DuplicateEmployeeError("Trùng ID!")
        self.employees[emp.emp_id] = emp

    def remove_employee(self, emp_id):
        if emp_id not in self.employees:
            raise EmployeeNotFoundError(emp_id)
        del self.employees[emp_id]

    def find_employee(self, emp_id):
        if emp_id not in self.employees:
            raise EmployeeNotFoundError(emp_id)
        return self.employees[emp_id]

    def list_employees(self):
        if not self.employees:
            raise IndexError("Chưa có dữ liệu")
        return list(self.employees.values())

    # ── TÌM KIẾM ──────────────────────────────────────────
    def find_by_name(self, keyword):
        result = [e for e in self.employees.values() if keyword.lower() in e.name.lower()]
        if not result:
            raise EmployeeNotFoundError(f"tên '{keyword}'")
        return result

    def find_by_language(self, lang):
        result = [e for e in self.employees.values()
                  if isinstance(e, Developer) and lang.lower() in [l.lower() for l in e.languages]]
        if not result:
            raise EmployeeNotFoundError(f"ngôn ngữ '{lang}'")
        return result

    # ── HIỂN THỊ ──────────────────────────────────────────
    def list_by_type(self, emp_type):
        type_map = {"manager": Manager, "developer": Developer, "intern": Intern}
        cls = type_map.get(emp_type.lower())
        if not cls:
            raise ValueError("Loại không hợp lệ (manager/developer/intern)")
        result = [e for e in self.employees.values() if isinstance(e, cls)]
        if not result:
            raise IndexError(f"Không có {emp_type} nào")
        return result

    def list_by_performance(self):
        emps = list(self.employees.values())
        if not emps:
            raise IndexError("Chưa có dữ liệu")
        return sorted(emps, key=lambda e: e.performance, reverse=True)

    # ── LƯƠNG ─────────────────────────────────────────────
    def total_salary(self):
        return sum(e.calculate_salary() for e in self.employees.values())

    def top_salary(self, n=3):
        emps = list(self.employees.values())
        if not emps:
            raise IndexError("Chưa có dữ liệu")
        return sorted(emps, key=lambda e: e.calculate_salary(), reverse=True)[:n]

    # ── DỰ ÁN ─────────────────────────────────────────────
    def assign_project(self, emp_id, project):
        emp = self.find_employee(emp_id)
        emp.assign_project(project)

    def remove_project(self, emp_id, project):
        emp = self.find_employee(emp_id)
        if project not in emp.projects:
            raise ProjectAllocationError(f"Nhân viên không có dự án '{project}'")
        emp.projects.remove(project)

    # ── HIỆU SUẤT ─────────────────────────────────────────
    def update_performance(self, emp_id, score):
        emp = self.find_employee(emp_id)
        emp.evaluate(score)

    def excellent_employees(self):
        return [e for e in self.employees.values() if e.performance > 8]

    def needs_improvement(self):
        return [e for e in self.employees.values() if e.performance < 5]

    # ── NHÂN SỰ ───────────────────────────────────────────
    def raise_salary(self, emp_id, amount):
        emp = self.find_employee(emp_id)
        if amount <= 0:
            raise InvalidSalaryError("Mức tăng phải > 0")
        emp.salary += amount

    def promote(self, emp_id):
        emp = self.find_employee(emp_id)
        if isinstance(emp, Intern):
            new_emp = Developer(emp.emp_id, emp.name, emp.age, emp.salary)
            new_emp.projects = emp.projects
            new_emp.performance = emp.performance
            self.employees[emp_id] = new_emp
            return "Intern → Developer"
        elif isinstance(emp, Developer):
            new_emp = Manager(emp.emp_id, emp.name, emp.age, emp.salary)
            new_emp.projects = emp.projects
            new_emp.performance = emp.performance
            self.employees[emp_id] = new_emp
            return "Developer → Manager"
        else:
            raise ValueError("Manager đã là chức vụ cao nhất!")

    # ── THỐNG KÊ ──────────────────────────────────────────
    def count_by_type(self):
        return {
            "Manager": sum(1 for e in self.employees.values() if isinstance(e, Manager)),
            "Developer": sum(1 for e in self.employees.values() if isinstance(e, Developer)),
            "Intern": sum(1 for e in self.employees.values() if isinstance(e, Intern)),
        }

    def salary_by_department(self):
        result = {}
        for e in self.employees.values():
            dept = getattr(e, "department", type(e).__name__)
            result[dept] = result.get(dept, 0) + e.calculate_salary()
        return result

    def avg_projects_per_employee(self):
        if not self.employees:
            raise IndexError("Chưa có dữ liệu")
        total = sum(len(e.projects) for e in self.employees.values())
        return total / len(self.employees)