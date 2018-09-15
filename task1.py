
def occupation_by_age(age):

    MAX_KG_AGE = 6
    MAX_SCH_AGE = 17
    MAX_HSCH_AGE = 23

    if age < 0 or age > 120:
        raise RuntimeError("invalid age {}".format(age))
    if age < MAX_KG_AGE:
        result = 'kindergarden'
    elif age <= MAX_SCH_AGE:
        result = 'school'
    elif age <= MAX_HSCH_AGE:
        result = 'high scool'
    else:           
        result = 'work'
    return result    

#----maim module
age = input("What's your age?")
int_age = int(age)

try:
    occupation = occupation_by_age(int_age)
    print('Go to {}'.format(occupation))
except RuntimeError as ex:
    print("oops!!! It says: {}".format(ex)) 


