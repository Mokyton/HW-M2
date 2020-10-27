account1 = {'login': 'ivan', 'password': 'q1'}
account2 = {'login': 'petr', 'password': 'q2'}
account3 = {'login': 'olga', 'password': 'q3'}
account4 = {'login': 'anna', 'password': 'q4'}

account = [account1, account2, account3, account4]

user1 = {'name': 'Иван', 'age': 20, 'account': 'account1'}
user2 = {'name': 'Петр', 'age': 25, 'account': 'account2'}
user3 = {'name': 'Ольга', 'age': 18, 'account': 'account3'}
user4 = {'name': 'Анна', 'age': 27, 'account': 'account4'}

user_list = [user1, user2, user3, user4]

task_1 = input("Введите ключ (name или account): ").lower()

try:
    print(f"значение ключа {task_1} для юзера 1 = {user1[task_1]}")
    print(f"значение ключа {task_1} для юзера 2 = {user2[task_1]}")
    print(f"значение ключа {task_1} для юзера 3 = {user3[task_1]}")
    print(f"значение ключа {task_1} для юзера 4 = {user4[task_1]}")
except KeyError:
    print("Введенный ключ не найден ")
except:
    print('Неизвестная ошибка')

task_2 = input("Введите порядковый номер: ")

try:  
    print(f'Данные по юзеру №: {user_list[int(task_2) - 1]["name"]}')
    print(f'имя: {user_list[int(task_2) - 1]["name"]}')
    print(f'возраст: {user_list[int(task_2) - 1]["age"]}')
    print(f'логин: {account[int(task_2) - 1]["login"]}')
    print(f'пароль: {account[int(task_2) - 1]["password"]}') # аналогично с ключом имя\аккаунт, только вызываем необходимые нам данные из различных словарей
except:
    print('Пользователь с указанным номером не найден')

age1 = user1['age']
age2 = user2['age']
age3 = user3['age']
age4 = user4['age']

average_age = (age1+age2+age3+age4)/len(user_list)

print(average_age)

el1 = user_list[0]
el2 = user_list[1]
el3 = user_list[2]
el4 = user_list[3]

print(user_list)

move = input('Введите номер пользователя, которого нужно переместить в конец:')

if move == str(1):
    print('Список до изменения: ' + str(user_list))
    user_list.remove(el1)
    user_list.append(el1)
    print('Список после изменения: ' + str(user_list))
elif move == str(2):
    print('Список до изменения: ' + str(user_list))
    user_list.remove(el2)
    user_list.append(el2)
    print('Список после изменения: ' + str(user_list))
elif move == str(3):
    print('Список до изменения: ' + str(user_list))
    user_list.remove(el3)
    user_list.append(el3)
    print('Список после изменения: ' + str(user_list))
elif move == str(4):
    print('Список до изменения: ' + str(user_list))
    user_list.remove(el4)
    user_list.append(el4)
    print('Список после изменения: ' + str(user_list))
else:
    print('Пользователь не найден')
