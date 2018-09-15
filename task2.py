def str_compare(str1, str2):

    both_are_strings = (type(str1) == str and type(str2) == str)

    if not both_are_strings:
        result = 0
    elif str1 == str2:
        result = 1
    elif len(str1) > len(str2):
        result = 2
    elif str2 == 'learn':
        result = 3  

    return result

# should print 0
print(str_compare(None, "learn"))

# should print 1
print(str_compare("python", "python"))

# should print 2
print(str_compare("learn1", "learn"))

# should print 3
print(str_compare("go", "learn"))



        
         
    
