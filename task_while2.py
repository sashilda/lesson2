question_answer = {"How are you?":          "I am fine!",
                    "What are you doing?":  " Chating with you ",
                    "Help me!":             "Help me somebody, blyat'!", 
                    "How to exit?":         "Say:'Bye!"}   


def ask_user(chat_dictionary):

    c = chat_dictionary

    print(" How are you ? ")
    while True:
        
        user_say = input("Chat with me.   ")
        user_say = str(user_say)
        user_say = user_say.capitalize()
           
        if user_say == 'Bye!':
            print('Well, bye!')
            break
        elif user_say in c.keys():
            print(c.get(user_say)) 
        else: #if user_say not in c.keys():
            print("I'm not understand")

ask_user(question_answer)