calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    info = []
    info.append(len(string))
    info.append(string.upper())
    info.append(string.lower())
    info_tup = tuple(info)
    count_calls()
    return info_tup

def is_contains(string, list_to_search):
    count_calls()
    contain_ = False
    for i in range(len(list_to_search)):
        if list_to_search[i].lower() == string.lower():
            contain_ = True
    return contain_

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
