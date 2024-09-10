grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} # множество - set
students_list = list(students) # преобразуем в список
students_list.sort() # сортируем список
# Решение первым способом
print("Решение первым способом")
dict_={
    students_list[0]:sum(grades[0])/len(grades[0]),
students_list[1]:sum(grades[1])/len(grades[1]),
students_list[2]:sum(grades[2])/len(grades[2]),
students_list[3]:sum(grades[3])/len(grades[3]),
students_list[4]:sum(grades[4])/len(grades[4])
}
print(dict_)
# через zip
print("Решение вторым способом через функцию zip")
grades_mid = [sum(grades[0])/len(grades[0]),
              sum(grades[1])/len(grades[1]),
              sum(grades[2])/len(grades[2]),
              sum(grades[3])/len(grades[3]),
              sum(grades[4])/len(grades[4])]
# print(grades_mid)
zipped_values = zip(students_list, grades_mid)
zipped_dict = dict(zipped_values)
# print(zipped_values)
print(zipped_dict)
