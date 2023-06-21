
# Простая реализация работника

# name = 'Даниил'
# salary = 200000
#
# print('У', name, 'зарплата в месяц =', salary)
# print(f'У {name} зарплата в месяц = {salary}')


# Реализация в виде словаря, 1 сотрудник:

# employee = {
#     'name': 'Даниил',
#     'salary': 200000
# }
#
# print(f'У {employee["name"]} зарплата в месяц = {employee["salary"]}')



# Реализация в виде словаря, много сотрудников

# employee_list = [{}, {}, {}, {}]

# employee_list = [
#     {
#         'name': 'Даниил',
#         'salary': 200000
#     },
#     {
#         'name': 'Олег',
#         'salary': 150000
#     },
#     {
#         'name': 'Петя',
#         'salary': 60000
#     }
# ]
#
# for employee in employee_list:
#     print(f'У {employee["name"]} зарплата в месяц = {employee["salary"]}')
#
# # Увольнение сотрудника:
# print('\n** УВОЛЬНЯЕМ СОТРУДНИКА **')
# name = input('Введите кого будем увольнять: ') # Даниил
# for employee in employee_list:
#     if employee['name'] == name:
#         employee_list.remove(employee)
#
# print()
# for employee in employee_list:
#     print(f'У {employee["name"]} зарплата в месяц = {employee["salary"]}')

# Нанимаем сотрудника
# print('\n** НАНИМАЕМ СОТРУДНИКА **')
# name = input('Введите имя сотрудника: ')
# salary = input('Введите ЗП сотрудника: ')
# new_employee = {
#     'name': name,
#     'salary': salary
# }
# employee_list.append(new_employee)
#
# print()
# for employee in employee_list:
#     print(f'У {employee["name"]} зарплата в месяц = {employee["salary"]}')



# Реализация через ООП

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.on_vacation = False

    def get_info(self):
        return f'У {self.name} зарплата в месяц = {self.salary}'


employee_list = [Employee('Данил', 200000), Employee('Олег', 150000), Employee('Петя', 600000)]

for employee in employee_list:
    print(employee.get_info())















