account1 = {'login': 'ivan', 'password': 'q1'}
account2 = {'login': 'petr', 'password': 'q2'}
account3 = {'login': 'olga', 'password': 'q3'}
account4 = {'login': 'anna', 'password': 'q4'}


user1 = {'name': 'Иван', 'age': 20, 'account': ['account1']}
user2 = {'name': 'Петр', 'age': 25, 'account': ['account2']}
user3 = {'name': 'Ольга', 'age': 18, 'account': ['account3']}
user4 = {'name': 'Анна', 'age': 27, 'account': ['account4']}

user_list = [user1, user2, user3, user4]
el1 = user_list[0]
el2 = user_list[1]
el3 = user_list[2]
el4 = user_list[3]

print(user_list)

move = input('что-то')

if move == str(1):
    user_list.remove(el1)
    user_list.append(el1)
    print(user_list)
elif move == str(2):
    user_list.remove(el2)
    user_list.append(el2)
    print(user_list)
elif move == str(3):
    user_list.remove(el3)
    user_list.append(el3)
    print(user_list)
elif move == str(4):
    user_list.remove(el4)
    user_list.append(el4)
    print(user_list)
else:
    print('Неизвестная ошибка')