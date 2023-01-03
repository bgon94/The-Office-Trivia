import random
import time
import datetime

def player1_turn(question_bank_list_of_dicts,player1_money):
    r = random.choice(list(question_bank_list_of_dicts))
    for answer, value in r.items():
        current_question = r["Question"]
        current_answer = r["Answer"]
        current_value = r["Value"]
        print("Current score:" , player1_money , "\n")
        print("For " , current_value , "dollars:")
        response = input(current_question)
      
        if response == current_answer:
            print("You got it!")
            player1_money += current_value
            print("You now have " , player1_money , "dollars\n")
            print("------------------------------------------\n")
        else:
            print("Incorrect!")    
            player1_money -= current_value
            print("You now have " , player1_money , "dollars")
            print("------------------------------------------\n")
        question_bank_list_of_dicts.remove(r)
        break
    return [question_bank_list_of_dicts, player1_money]

def player2_turn(question_bank_list_of_dicts,player2_money):
    r = random.choice(list(question_bank_list_of_dicts))
    for answer, value in r.items():
        current_question = r["Question"]
        current_answer = r["Answer"]
        current_value = r["Value"]
        print("Current score:" , player2_money , "\n")
        print("For " , current_value , "dollars:")
        response = input(current_question)
        print("")
        if response == current_answer:
            print("You got it!")
            player2_money += current_value
            print("You now have " , player2_money , "dollars\n")
            print("------------------------------------------\n")
        else:
            print("Incorrect!")    
            player2_money -= current_value
            print("You now have " , player2_money , "dollars")
            print("------------------------------------------\n")
        question_bank_list_of_dicts.remove(r)
        break
    return [question_bank_list_of_dicts, player2_money]


