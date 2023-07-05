from collections import Counter
import re
import csv
import json
import string

# TASK1
print("TASK 1 \n")

with open("text_read_task_1.txt", "r") as text_file:

    data = text_file.readlines()
    new_data = []
    words = []

    for i in range(0, len(data)):
        new_data.append(data[i].split())
        print(*new_data[i])
    print("\n")

    punctuation = string.punctuation

    for i in range(0, len(new_data)):
        for j in range(0, len(new_data[i])):
            new_data[i][j] = new_data[i][j].lower()
            new_data[i][j] = new_data[i][j].translate(str.maketrans('', '', punctuation))
        words.append(Counter(new_data[i]).most_common(1))
        print(words[i])

with open("text_write_task_1.txt", "w") as text_file:
    text_file.write(str(words))
    print("\n")

# TASK2
print("TASK 2 \n")

with open("text_task2.txt", "r") as text_file, open("stop_words_task2.txt", "r") as stop_words:

    text = text_file.read()
    text_1 = list(text)
    text = text.lower()
    stop_words = stop_words.read().split()

    for i in stop_words:
        text = re.sub(i, '*' * len(i), text)
        text_2 = list(text)

    for i in range(0, len(text_1)):
        if text_1[i] != text_2[i]:
            text_2[i] = text_2[i].upper()

    result = ''.join(text_2)
    print(result, "\n")

# TASK3
print("TASK 3 \n")

with open("task_3.csv", encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter=",")
    count = 0

    for row in file_reader:
        if count == 0:
            print(f'Файл содержит столбцы:\n{", ".join(row)}')
            print("Учащиеся с оценкой ниже 3 баллов:")
        else:
            if len(row) == 3 and int(row[2]) < 3:
                print(f'{row[0]} {row[1]} оценка {row[2]}')
            else:
                pass
        count += 1

print("\n")

# TASK4
print("TASK 4 \n")

with open("task_4.txt", "r") as text_file:

    data = text_file.read()
    numbers = re.findall(r'\d+', data)
    print(numbers)
    sum_numbers = sum(map(int, numbers))
    print(f"Sum of the numbers: {sum_numbers}")
    print("\n")

# TASK5
print("TASK 5 \n")

with open("task_5.csv", encoding='utf-8') as r_file:

    file_reader = csv.reader(r_file, delimiter=",")
    count = 0
    shift = 0

    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = alphabet_lower.upper()
    first_letter_lower = ord('a')
    first_letter_upper = ord('A')

    new_text = ''

    for row in file_reader:
        if count == 0:
            print("Input data", "   ", "Output data")
        else:
            if len(row) == 1:
                for i in row[0]:
                    if i in alphabet_lower:
                        new_text += chr((ord(i) - first_letter_lower + shift) % 26 + first_letter_lower)
                    elif i in alphabet_upper:
                        new_text += chr((ord(i) - first_letter_upper + shift) % 26 + first_letter_upper)
                    else:
                        new_text += i
                    if len(new_text) == len(row[0]):
                        print(row[0], "        ", new_text)
                        new_text = ""
        count += 1
        shift += 1

    print("\n")

# TASK6
print("TASK 6 \n")


def json_to_csv():

    with open("employees.json", "r") as json_file, open("employees.csv", mode="w", encoding='utf-8') as w_file:

        # 6.1 task
        data = json.load(json_file)
        names = ["name", "birthday", "height", "weight", "car", "languages"]
        file_writer = csv.DictWriter(w_file, delimiter=",", lineterminator="\r", fieldnames=names)
        print("1) The data has been read from JSON file and converted to CSV format")
        cont_exit = str(input("Would you like to continue or exit?: cont/exit "))
        match cont_exit:
            case 'cont':
                pass
            case 'exit':
                exit()

        # 6.2 task
        file_writer.writeheader()
        file_writer.writerows(data)
        print("2) The data has been saved in CSV file")
        cont_exit = str(input("Would you like to continue or exit?: cont/exit "))
        match cont_exit:
            case 'cont':
                pass
            case 'exit':
                exit()


json_to_csv()


# 6.3 task
def add_to_json():

    print("Add information about new employee:")

    with open("employees.json", "r") as json_file:
        name = input("name")
        birthday = input("birthday")
        height = int(input("height"))
        weight = float(input("weight"))
        car = input("car")
        languages = input("languages")

    json_data = {
        "name": name,
        "birthday": birthday,
        "height": height,
        "weight": weight,
        "car": car,
        "languages": languages.split(),
    }

    data = json.load(open("employees.json"))
    data.append(json_data)

    # 6.3 task
    with open("employees.json", "w") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
        print("3) The data has been added in JSON file")
        add_in_csv = str(input("Would you like to add this information in CSV-file?: yes/no "))
        if add_in_csv == 'yes':
            # 6.4 task
            with open("employees.csv", mode="w", encoding='utf-8') as w_file:
                names = ["name", "birthday", "height", "weight", "car", "languages"]
                file_writer = csv.DictWriter(w_file, delimiter=",", lineterminator="\r", fieldnames=names)
                file_writer.writeheader()
                file_writer.writerows(data)
                print("4) The data has been added in CSV file")
                cont_exit = str(input("Would you like to continue or exit?: cont/exit "))
                match cont_exit:
                    case 'cont':
                        pass
                    case 'exit':
                        exit()
        else:
            cont_exit = str(input("Would you like to continue or exit?: cont/exit "))
            match cont_exit:
                case 'cont':
                    pass
                case 'exit':
                    exit()


add_to_json()


# 6.5 task
def emp_name():

    print("The information about employee by his name:")

    with open("employees.csv", encoding='utf-8') as read_file:
        reader_file = csv.reader(read_file, delimiter=",")
        counter = 0
        employee_name = str(input("Enter the name of employee: "))

        for row in reader_file:
            if len(row) == 6 and row[0] == employee_name:
                print(f"5) Basic information about {employee_name}:")
                print(f'name: {row[0]}\nbirthday: {row[1]}\nheight: {row[2]}\nweight: {row[3]}\ncar: {row[4]}\nlanguages: {row[5]}')
            else:
                pass

        counter += 1

    cont_exit = str(input("Would you like to continue or exit?: cont/exit "))
    match cont_exit:
        case 'cont':
            pass
        case 'exit':
            exit()


emp_name()


# 6.6 task
def lang():

    print("The information about programming language:")

    with open("employees.csv", encoding='utf-8') as read_file:
        reader_file = csv.reader(read_file, delimiter=",")
        employee_lang = str(input("Enter the language: "))
        print(f"6) The list of employees who know {employee_lang}: ")

        for row in reader_file:
            if employee_lang in row[5]:
                print(f'{row[0]}')

    cont_exit = str(input("Would you like to continue or exit?: cont/exit "))
    match cont_exit:
        case 'cont':
            pass
        case 'exit':
            exit()


lang()


# 6.7 task
def year_of_birth():

    print("The filter by year:")

    with open("employees.csv", encoding='utf-8') as read_file:
        reader_file = csv.reader(read_file, delimiter=",")
        employee_year = int(input("Enter the year: "))
        print(f"7) The average height of employees whose year of birth is less than {employee_year}: ")

        for row in reader_file:
            if '9' >= row[1] >= '0':
                if int(row[1][-4:]) < employee_year:
                    print(f'{row[0]} - {row[2]} cm')


year_of_birth()
print("This is it!)")
