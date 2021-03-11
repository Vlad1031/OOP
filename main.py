from employees_all_functions import add_employees, del_employees,\
    print_employees, search_employees, edit_employees, save_employees
import pickle


def main():
    employees = [
        {
            "name": "Vlad",
            "age": 18
        },
        {
            "name": "Влад",
            "age": 27
        }
    ]
    with open("employees.txt", "rb") as read_file:
        employees = pickle.load(read_file)

    while True:
        menu = input("Виберіть один із варіантів\n"
                     "(1) Додати\n"
                     "(2) Видалити\n"
                     "(3) Вивід інформації\n"
                     "(4) Пошук\n"
                     "(5) Редагування\n"
                     "(6) Збереження\n"
                     "(0) Вихід\n"
                     "Ведіть варіант: ")

        if menu == "1":
            add_employees(employees)
        elif menu == "2":
            del_employees(employees)
        elif menu == "3":
            print_employees(employees)
        elif menu == "4":
            search_employees(employees)
        elif menu == "5":
            edit_employees(employees)
        elif menu == "6":
            save_employees(employees)
        elif menu == "0":
            save_employees(employees)
            break
        else:
            print("Такого варіанту немає!!!\n"
                  "Спробуй ще раз")


main()
