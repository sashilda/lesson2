def get_summ(num_one, num_two):

    try:

        return int(num_one) + int(num_two)

    except ValueError:
          
        return None
    

a=5
b=6

print("sum of {a}, {b}: {s}".format(a=a, b=b, s=get_summ(a, b)))

a = "qq"
print("sum of {a}, {b}: {s}".format(a=a, b=b, s=get_summ(a, b)))
