my_dict = {'Vladimir': 1975, 'Elena': 1975, 'Nadezda': 2009, 'Yakov': 2010}
print(my_dict)
print(my_dict["Yakov"])
print(my_dict.get('Denis'))
my_dict.update({'Denis': 2012, 'Liliya':2013})
print(my_dict)
delited = my_dict.pop('Vladimir')
print(delited)
print(my_dict)
print('Множества') # Множества
my_set = {2, 10, 15, 20, 15, 20, True, 'Vova', 'Victor', 'Vova'}
print('Множество: ', my_set)
my_set.update({9, 14})
my_set.discard('Vova')
print('Модифицированное множество: ', my_set)
