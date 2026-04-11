from models import Manager, Developer, Intern
from services import Company
from utils import validate_age, validate_salary

company = Company()

SEP = "=" * 60

def header():
    print(SEP)
    print("   HỆ THỐNG QUẢN LÝ NHÂN VIÊN CÔNG TY ABC")
    print(SEP)

def menu():
    header()
    print("1. Thêm nhân viên mới")
    print("2. Hiển thị danh sách nhân viên")
    print("3. Tìm kiếm nhân viên")
    print("4. Quản lý lương")
    print("5. Quản lý dự án")
    print("6. Đánh giá hiệu suất")
    print("7. Quản lý nhân sự")
    print("8. Thống kê báo cáo")
    print("9. Thoát")
    print(SEP)

def menu_add():
    print("\n  a. Thêm Manager")
    print("  b. Thêm Developer")
    print("  c. Thêm Intern")
    choice = input("  Chọn: ").strip().lower()
    try:
        emp_id = input("  ID: ").strip()
        name = input("  Tên: ").strip()
        age = int(input("  Tuổi: "))
        salary = float(input("  Lương cơ bản: "))
        validate_age(age)
        validate_salary(salary)
        if choice == "a":
            dept = input("  Phòng ban: ").strip()
            emp = Manager(emp_id, name, age, salary, dept)
        elif choice == "b":
            langs = input("  Ngôn ngữ lập trình (cách nhau bởi dấu phẩy): ").strip()
            lang_list = [l.strip() for l in langs.split(",") if l.strip()]
            emp = Developer(emp_id, name, age, salary, lang_list)
        elif choice == "c":
            emp = Intern(emp_id, name, age, salary)
        else:
            print("  Sai lựa chọn!"); return
        company.add_employee(emp)
        print("  Thêm thành công!")
    except Exception as e:
        print("  Lỗi:", e)

def menu_list():
    print("\n  a. Tất cả nhân viên")
    print("  b. Theo loại (Manager/Developer/Intern)")
    print("  c. Theo hiệu suất (cao -> thấp)")
    choice = input("  Chọn: ").strip().lower()
    try:
        if choice == "a":
            for e in company.list_employees(): print(" ", e)
        elif choice == "b":
            t = input("  Loại (manager/developer/intern): ").strip()
            for e in company.list_by_type(t): print(" ", e)
        elif choice == "c":
            for e in company.list_by_performance(): print(" ", e)
        else:
            print("  Sai lựa chọn!")
    except Exception as e:
        print(" ", e)

def menu_search():
    print("\n  a. Theo ID")
    print("  b. Theo tên")
    print("  c. Theo ngôn ngữ lập trình (Developer)")
    choice = input("  Chọn: ").strip().lower()
    try:
        if choice == "a":
            emp_id = input("  ID: ").strip()
            print(" ", company.find_employee(emp_id))
        elif choice == "b":
            name = input("  Tên (hoặc một phần tên): ").strip()
            for e in company.find_by_name(name): print(" ", e)
        elif choice == "c":
            lang = input("  Ngôn ngữ: ").strip()
            for e in company.find_by_language(lang): print(" ", e)
        else:
            print("  Sai lựa chọn!")
    except Exception as e:
        print(" ", e)

def menu_salary():
    print("\n  a. Tính lương cho từng nhân viên")
    print("  b. Tính tổng lương công ty")
    print("  c. Top 3 nhân viên lương cao nhất")
    choice = input("  Chọn: ").strip().lower()
    try:
        if choice == "a":
            emp_id = input("  ID nhân viên: ").strip()
            emp = company.find_employee(emp_id)
            print(f"  Lương của {emp.name}: {emp.calculate_salary():,.0f}")
        elif choice == "b":
            print(f"  Tổng lương công ty: {company.total_salary():,.0f}")
        elif choice == "c":
            for i, e in enumerate(company.top_salary(3), 1):
                print(f"  {i}. {e.name} ({type(e).__name__}): {e.calculate_salary():,.0f}")
        else:
            print("  Sai lựa chọn!")
    except Exception as e:
        print(" ", e)

def menu_project():
    print("\n  a. Phân công nhân viên vào dự án")
    print("  b. Xóa nhân viên khỏi dự án")
    print("  c. Hiển thị dự án của 1 nhân viên")
    choice = input("  Chọn: ").strip().lower()
    try:
        emp_id = input("  ID nhân viên: ").strip()
        if choice == "a":
            project = input("  Tên dự án: ").strip()
            company.assign_project(emp_id, project)
            print("  Phân công thành công!")
        elif choice == "b":
            project = input("  Tên dự án cần xóa: ").strip()
            company.remove_project(emp_id, project)
            print("  Đã xóa khỏi dự án!")
        elif choice == "c":
            emp = company.find_employee(emp_id)
            projects = emp.projects if emp.projects else ["Chưa có dự án"]
            print(f"  Dự án của {emp.name}: {', '.join(projects)}")
        else:
            print("  Sai lựa chọn!")
    except Exception as e:
        print(" ", e)

def menu_performance():
    print("\n  a. Cập nhật điểm hiệu suất")
    print("  b. Hiển thị nhân viên xuất sắc (điểm > 8)")
    print("  c. Hiển thị nhân viên cần cải thiện (điểm < 5)")
    choice = input("  Chọn: ").strip().lower()
    try:
        if choice == "a":
            emp_id = input("  ID nhân viên: ").strip()
            score = float(input("  Điểm (0-10): "))
            company.update_performance(emp_id, score)
            print("  Cập nhật thành công!")
        elif choice == "b":
            result = company.excellent_employees()
            print("  Không có nhân viên xuất sắc." if not result else "")
            for e in result: print(" ", e)
        elif choice == "c":
            result = company.needs_improvement()
            print("  Tất cả nhân viên đều đạt yêu cầu." if not result else "")
            for e in result: print(" ", e)
        else:
            print("  Sai lựa chọn!")
    except Exception as e:
        print(" ", e)

def menu_hr():
    print("\n  a. Xóa nhân viên (nghỉ việc)")
    print("  b. Tăng lương cơ bản")
    print("  c. Thăng chức (Intern->Developer, Developer->Manager)")
    choice = input("  Chọn: ").strip().lower()
    try:
        emp_id = input("  ID nhân viên: ").strip()
        if choice == "a":
            company.remove_employee(emp_id)
            print("  Đã xóa nhân viên!")
        elif choice == "b":
            amount = float(input("  Mức tăng lương: "))
            company.raise_salary(emp_id, amount)
            print("  Đã tăng lương!")
        elif choice == "c":
            result = company.promote(emp_id)
            print(f"  Thăng chức thành công: {result}")
        else:
            print("  Sai lựa chọn!")
    except Exception as e:
        print(" ", e)

def menu_report():
    print("\n  a. Số lượng nhân viên theo loại")
    print("  b. Tổng lương theo phòng ban")
    print("  c. Số dự án trung bình trên mỗi nhân viên")
    choice = input("  Chọn: ").strip().lower()
    try:
        if choice == "a":
            for k, v in company.count_by_type().items():
                print(f"  {k}: {v} người")
        elif choice == "b":
            for dept, total in company.salary_by_department().items():
                print(f"  {dept}: {total:,.0f}")
        elif choice == "c":
            avg = company.avg_projects_per_employee()
            print(f"  Trung bình: {avg:.2f} dự án/nhân viên")
        else:
            print("  Sai lựa chọn!")
    except Exception as e:
        print(" ", e)

def main():
    actions = {
        "1": menu_add, "2": menu_list, "3": menu_search,
        "4": menu_salary, "5": menu_project, "6": menu_performance,
        "7": menu_hr, "8": menu_report,
    }
    while True:
        menu()
        choice = input("Chọn chức năng (1-9): ").strip()
        if choice == "9":
            print("Tạm biệt!")
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("Sai lựa chọn!")

if __name__ == "__main__":
    main()