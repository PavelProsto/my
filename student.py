class Student:
    def __init__(self, full_name="", group_number=0, progress=[]) -> None:
        self.full_name = full_name
        self.group_number = group_number
        self.progress = progress
    def __str__(self) -> str:
        txt = 'Студент: ' + self.full_name + 'Группа: ' + self.group_number
        txt += 'Оценки:'
        for x in self.progress:
            txt += ' ' + str(x)
        return txt

def SortParam(st):
    return st.full_name

st_size = 5

students = []
for i in range(st_size):
    print("Введите полное имя студента: ")
    full_name = input()
    print("Введите номер группы: ")
    group_number = input()
    n = 5
    print('Введите', n, 'оценок в столбик: ')
    progress = []
    for i in range(n):
        score = int(input())
        progress.append(score)
    st = Student(full_name, group_number, progress)
    students.append(st)

print("Students list :")
for st in students:
    print(st)

students = sorted(students, key=SortParam)

print("Sorted students :")
for st in students:
    print(st)

print("Bad students :")
n = 0
for st in students:
    for val in st.progress:
        if val < 3:
            print(st)
            n += 1
            break
if n == 0:
    print("No bad students")