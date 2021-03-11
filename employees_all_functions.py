from utilits import enter_int, find_employees
import pickle


def add_employees(employees: list):
    print("\nФункція додавання")
    name = input("Введіть ім`я: ")
    age = enter_int("Введіть вік співробітника: ", error_number="Може бути тільке число!!!")
    new_employees = {"name": name, "age": age}
    employees.append(new_employees)
    return employees


def del_employees(employees: list):
    print("\nФункція видалення")
    name = input("Введіть ім`я: ")
    find = find_employees(employees, name)
    employees.remove(find)
    return employees


def print_employees(employees: list):
    print("\nФункція виведення")
    for i in employees:
        print(f'{i["name"]}, {i["age"]}')
    return


def search_employees(employees: list):
    print("\nФункція пошуку")
    new_list = []
    menu = input("Виберіть за яким параметром хочете шукати\n"
                 "(1) Повне ім`я\n"
                 "(2) Перші літери ім`я\n"
                 "(3) За віком\n"
                 "Введіть номер варіанту: ")
    if menu == "1":
        name = input("Введіть ім`я: ")
        new_list = list(filter(lambda x: x["name"] == name, employees))
    elif menu == "2":
        start_name = input("Введіть початкові літери імені: ")
        new_list = list(filter(lambda x: x["name"].startswith(start_name), employees))
    elif menu == "3":
        age = enter_int("Введіть вік співробітника: ", error_number="Може бути тільке число!!!")
        new_list = list(filter(lambda x: x["age"] == age, employees))

    print_employees(new_list)
    return


def edit_employees(employees: list):
    print("\nФункція заміни")
    name = input("Введіть ім`я: ")
    find = find_employees(employees, name)

    new_name = input("Введіть нове ім`я: ")
    new_age = enter_int("Введіть новий вік співробітника: ", error_number="Може бути тільке число!!!")
    find["name"] = new_name
    find["age"] = new_age
    return employees


def save_employees(employees: list):
    print("\nФункція збереження")
    with open("employees.txt", "wb") as save_file:
        pickle.dump(employees, save_file)
