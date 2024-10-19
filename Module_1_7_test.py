grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] #дано
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}  # дано

# grades_ = [5, 3, 3, 5, 4] #тестовый промежуточный элемент для тренировки
# print(sum(grades_)) #сложила
# print(len(grades_))  #узнала кол во объектов
# print(sum(grades_) / len(grades_)) # нашла среднеарифметич
# print(sum(grades[0]) / len(grades[0])) #нашла стреднее первого элемента в списке из дано
print(sum(grades[0]) / len(grades[0]), sum(grades[1]) / len(grades[1]), sum(grades[2]) / len(grades[2]),
      sum(grades[3]) / len(grades[3]), sum(grades[4]) / len(grades[4]))  #нашла среднее каждого объекта
print(list(students)) #сделала из множества список
print(sorted(list(students)))  #сортировала список студентов по алфавиту.
                               # не брала команду sort чтобы не изменить исходный список
# a = ['n1', 'n2']  #тестовый список

# b = [5, 4]     #тестовый список
# c = dict(zip(a,b))    #   делаем словарь
# print(c) # ура!! )) есть словарь!!!

# создами новую переменную для списка стдентов тип список и сразу отсортируем см строку 12
students_sort_list = sorted(list(students))
print(students_sort_list)   #ага. есть
# создам переменную для списка средних оценок
average_grades = (sum(grades[0]) / len(grades[0]), sum(grades[1]) / len(grades[1]), sum(grades[2]) / len(grades[2]),
      sum(grades[3]) / len(grades[3]), sum(grades[4]) / len(grades[4]))
print(average_grades)
# создаем словарь
students_and_grades =dict(zip(students_sort_list, average_grades))
print(students_and_grades) #ура! финиш!!!!




