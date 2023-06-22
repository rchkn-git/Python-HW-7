# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов(т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во
# фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если
# с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.


# symbols = {1: 'а, я, у, ю, о, е, ё, э, и, ы',
#            0: 'б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ'}

# poem = input('Введите стих от Винни: ').lower()

# def getPhrase (countPoem):
#     resultArray = []
#     buffStr = ''
#     for i in range(len(countPoem)):
#         if (countPoem[i] != ' ') & (i != (len(countPoem) - 1)):
#             buffStr += countPoem[i]
#         elif i == (len(countPoem) - 1):
#             buffStr += countPoem[i]
#             resultArray.append(buffStr)
#             buffStr = ''
#         else:
#             resultArray.append(buffStr)
#             buffStr = ''
#     return resultArray

# def countPoem (resArray):
#     if (len(resArray) == 1) or (len(resArray) == 0):
#         print('Винни, в стихе должно быть хотя бы две фразы!!!')
#         return 1
#     else:
#         sumArray = []
#         for i in resArray:
#             sum = 0
#             for letter in i:
#                 for key, value in symbols.items():
#                     if letter in value:
#                         sum += key
#             sumArray.append(sum)
#         return sumArray

# def checkPoem (sArray):
#     res = 0
#     buf = 0
#     for i in range(len(sArray)):
#         if i == 0:
#             buf = sArray[i]
#         else:
#             if sArray[i] != buf:
#                 res += 1
#     if res == 0:
#         print('Парам пам-пам')
#     else:
#         print('Пам парам')

# counter = countPoem(getPhrase(poem))
# if counter != 1:
#     checkPoem(counter)


# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой ровно
# два аргумента, как, например, у операции умножения.


def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        print()
        for j in range(1, num_columns + 1):
            print(operation(i,j), end = ' ')

print_operation_table(lambda x, y: x * y,6,6)