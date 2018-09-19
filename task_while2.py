question_answer = {"How are you?":          "I am fine!",
                    "What are you doing?":  " Chating with you ",
                    "Help me!":             "Help me somebody, blyat'!", 
                    "How to exit?":         "Say:'Bye!"}   
BYE_MSG = 'Well, bye!'

def ask_user(chat_dictionary):

    c = chat_dictionary

    print(" How are you ? ")

    while True:
        try:
            user_say = input("Chat with me.   ")
            user_say = str(user_say)
            user_say = user_say.capitalize()
            
            if user_say == 'Bye!':
                print(BYE_MSG)
                break
            elif user_say in c:
                print(c.get(user_say)) 
            else: #if user_say not in c.keys():
                print("I'm not understand")

        except KeyboardInterrupt as ex:

            print(BYE_MSG)
            break

            
    

ask_user(question_answer)