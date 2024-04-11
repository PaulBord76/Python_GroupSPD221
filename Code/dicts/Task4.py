"""
Вирус повредил файлы.
Имеются следующие допустимые операции
Запись - W
Чтение - R
Запуск - X

На вход подается n - число файлов с доступными операциями
например, 3 - означает количество файлов после цифры

Далее на вход подается число m  - количество запросов к файлам
read test.txt

Вход:
3
python.exe X
test.txt R W
notes.exe R W X
5
read python.exe
read test.txt
write notes.exe
execute python.exe
write test.txt

Выход:
Failed
Ok
Ok
Ok
Ok
"""

operations = {
    "read": "r",
    "write": "w",
    "execute": "x"
}

files = {d[0]: d[1:] for d in [input().split() for _ in range(int(input("Num of files: ")))]}
res = []

# n = int(input("Num of files: "))
# for i in range(n):
#     data = input().split()
#     files[data[0]] = data[1:]

# print(files)
m = int(input("Num of requests: "))
for i in range(m):
    data = input().split()
    operation = operations.get(data[0])
    file_operations = files.get(data[1])
    if operation in file_operations:
        res.append("Ok")
    else:
        res.append("Failed")

print(*res, sep="\n")
    # print(operation)
    # print(file_operations)