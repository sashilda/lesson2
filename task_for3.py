
student_scores = [{'school_class': '4a','scores': [3,4,4,5,2]},
                  {'school_class': '4b','scores': [5,5,3,4,3,2,4]}]

def calc_sum_and_len(school_class):

    c = school_class

    print(c['school_class'])

    scores = c['scores']
    print(scores)
    
    sum_scores = 0
    len_scores = len(scores)

    # sum_scores = sum(scores)
    for score in scores:
        sum_scores += score

    return sum_scores, len_scores


s_sum = 0
s_len = 0

for c in student_scores:
    c_sum, c_len = calc_sum_and_len(c)
    
    s_sum += c_sum
    s_len += c_len

    c_avg = round(c_sum/c_len,2)
    print("{} average: {}".format(c['school_class'], c_avg))

s_avg = round(s_sum/s_len,2)
print("school average: {}".format(s_avg))