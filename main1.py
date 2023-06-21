
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

onV = False

employee_list = [
    {
        'name': 'Даниил',
        'salary': 200000,
        'is_good_employee': True
    },
    {
        'name': 'Олег',
        'salary': 150000,
        'is_good_employee': False
    },
    {
        'name': 'Дмитрий',
        'salary': 100000,
        'is_good_employee': True
    },
    {
        'name': 'Никита',
        'salary': 90000,
        'is_good_employee': True
    },
    {
        'name': 'Петя',
        'salary': 60000,
        'is_good_employee': True
    }
]

for employee in employee_list:
    print(f'У {employee["name"]} зарплата в месяц = {employee["salary"]}')

# Увольнение сотрудника:
print('\n** УВОЛЬНЯЕМ СОТРУДНИКА **')
#name = input('Введите кого будем увольнять: ') # Даниил  ]]employee['name'] == name and [[
for employee in employee_list:
    if employee['is_good_employee'] == False:
        employee_list.remove(employee)

for employee in employee_list:
    print(f'У {employee["name"]} зарплата в месяц = {employee["salary"]}')

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
    def __int__(self, name, salary, onV, is_good_employee):
        self.name = name
        self.salaty = salary
        self.on_vacation = onV
        self.is_good_employee = is_good_employee

    def get_info(self):
        return f'У {self.name} зарплата в месяц = {self.salary}'

