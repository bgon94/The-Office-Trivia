import random
question_bank_list_of_dicts = [{"Question" : "What is michaels last name? " , "Answer" : "scott" , "Value" : 100}, {"Question" : "What is Jim's last name? ", "Answer" : "Halpert" , "Value" : 200}]

player1_money = 0
player2_money = 0

""" def player1_turn(dictionary,player1_money):
    for i in question_bank_list_of_dicts:
        for answer,value in i.items():
            current_question = i["Question"]
            current_answer = i["Answer"]
            current_value = i["Value"]
            print("For " , current_value , "dollars:")
            response = input(current_question)
            if response == current_answer:
                print("You got it!")
                player1_money += current_value
                print("You now have " , player1_money , "dollars")
            else:
                print("Incorrect!")    
                player1_money -= current_value
                print("You now have " , player1_money , "dollars")
            break
        break """
def player1_turn(question_list,player1_money):
    r = random.choice(list(question_bank_list_of_dicts))
    for answer, value in r.items():
        current_question = r["Question"]
        current_answer = r["Answer"]
        current_value = r["Value"]
        print("For " , current_value , "dollars:")
        response = input(current_question)
        if response == current_answer:
            print("You got it!")
            player1_money += current_value
            print("You now have " , player1_money , "dollars")
        else:
            print("Incorrect!")    
            player1_money -= current_value
            print("You now have " , player1_money , "dollars")
        question_bank_list_of_dicts.remove(r)
        break
    return [question_bank_list_of_dicts, player1_money]

player1_update = player1_turn(question_bank_list_of_dicts, player1_money)
question_bank_list_of_dicts = player1_update[0]
player1_money = player1_update[1]
print(question_bank_list_of_dicts)
print(player1_money)






