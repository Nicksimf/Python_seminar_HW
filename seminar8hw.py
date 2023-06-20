surname = []
phone_number = []

for i in range(3):
    new_name = input('Введите новое имя: ') 
    surname.append(str(new_name) + '\n')
    for i in surname:
        new_phone = int(input('Введите новый телефон: '))
        
print(surname)

data = open('phonebook.txt', mode='w', encoding='utf-8')
data.writelines(surname)
data.writelines(phone_number)
data.close


with open('test.txt', 'r', encoding='utf-8') as file:
    line_list = file.read().splitlines()
    beautiful_list = []
    person_list = []
    for i in line_list:
        if i != '':
            person_list.append(i)
        else:
            beautiful_list.append(person_list)
            person_list = []
    if person_list:
        beautiful_list.append(person_list)
with open('test.txt', 'r', encoding='utf-8') as file:
    line_list = file.read().splitlines()
    beautiful_list = []
    person_list = []
    for i in line_list:
        if i != '':
            person_list.append(i)
        else:
            beautiful_list.append(person_list)
            person_list = []
    if person_list:
        beautiful_list.append(person_list)

    surname = input('Введите фамилию: ')
    for person in beautiful_list:
        if surname == person[0]:
            print(*person, sep='\n')
            print()