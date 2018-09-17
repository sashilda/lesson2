names_list = ['gali','tali','gili','alon','adi','ori']

def find_person(lst, name):

    list_c = lst[:]

    while True:
        current_name = list_c.pop() 
        #print(current_name) 
        if current_name == name:
            print('{} found'.format(name))
            break

#s_name = input('Input name from names list  ')

for s_name in names_list:
    find_person(names_list, s_name)


