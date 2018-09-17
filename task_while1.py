question_answer = {"How are you ?":"I am fine!"," What are you doing?":" Chating with you ",
"Help me!":"Help me somebody, blyat'!", " How to exit?":"Say: 'I am fine!"}   

def ask_user():

    while True:
        user_say = input(" How are you ? ")
        if user_say == 'I am fine!':
            print('Well, bye!')
            break
        else:
            print(' Wrong answer {}'.format(user_say))

ask_user()

