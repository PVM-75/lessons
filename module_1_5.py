immutable_var = (1, 3, 5, True, "apple")
print(immutable_var)
# immutable_var[1] = 6 - эта команда пытается изменить значение элемента с индексом 1,
#                       но Python выдает ошибку. Оставляю строку закомментированными.
mutable_list = [2, 4, 6, False, 'coconut']
print(mutable_list)
mutable_list[3] = True
mutable_list[4] = 'fish'
print(mutable_list)