grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] #дано
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}  # дано

# cоздам новую переменную для списка стдентов (тип список) и сразу отсортируем
students_sort_list = sorted(list(students))
# создам переменную для списка средних оценок
average_grades = (sum(grades[0]) / len(grades[0]), sum(grades[1]) / len(grades[1]), sum(grades[2]) / len(grades[2]),
                  sum(grades[3]) / len(grades[3]), sum(grades[4]) / len(grades[4]))
# создаем словарь
students_and_grades =dict(zip(students_sort_list, average_grades))
print(students_and_grades)




