import random
from art import *
import getpass
question_bank_list_of_dicts = [{"Question": "Who was Pam engaged to before Jim? ", "Answer": "roy", "Value": 200},  # Question bank is a list of dictionaries
                               {"Question": "What was the name of Jan Levinson's assistant at corporate? ",
                                "Answer": "hunter", "Value": 300},
                               {"Question": "How many brothers does Jim Halpert have? ",
                                "Answer": "2", "Value": 200},
                               {"Question": "Who did Michael end up taking to Jamaica? ",
                                   "Answer": "jan", "Value": 100},
                               {"Question": "Pam and Jim's first kiss took place where? ",
                                   "Answer": "chilis", "Value": 300},
                               {"Question": "In what state does Pam go to school? ", "Answer": "new york", "Value": 100}]

category_questions1 = [{"Question" : "Test question 1" , "Answer" : "answer 1" , "Value" : 2},
            {"Question" : "Test question 2" , "Answer" : "answer 2" , "Value" : 4},
            {"Question" : "Test question 3" , "Answer" : "answer 3" , "Value" : 6},
            {"Question" : "Test question 4" , "Answer" : "answer 4" , "Value" : 8},
            {"Question" : "Test question 5" , "Answer" : "answer 5" , "Value" : 10}]

category_questions2 = [{"Question" : "Test question 6" , "Answer" : "answer 6" , "Value" : 4},
            {"Question" : "Test question 7" , "Answer" : "answer 7" , "Value" : 8},
            {"Question" : "Test question 8" , "Answer" : "answer 8" , "Value" : 12},
            {"Question" : "Test question 9" , "Answer" : "answer 9" , "Value" : 16},
            {"Question" : "Test question 10" , "Answer" : "answer 10" , "Value" : 20}]

categories = ["Category 1","Category 2","Category 3","Category 4","Category 5"]

bonus_questions = [
    {"Question": "What did Jan throw at Michael's TV?", "Answer": "dundie"}]


class Player:
    def __init__(self, name, position):
        '''Position allows me to increase the correct players money when stealing'''
        self.money = 0
        self.name = name
        self.postion = position
    
    
        


    def playerTurn(self, question_bank_list_of_dicts, position):
        '''Takes in user input for the answer and compares it to the correct answer.
        If user answers incorrectly, the other player has a chance to steal.
        Updates player money depending who answered correctly.'''
        r = random.choice(list(question_bank_list_of_dicts)
                          )  # assigns r to a random item(dictionary) in the list of dictionaries
        for answer, value in r.items():  # Iterates through the randomly selected dictionary to grab the values
            # assigns each value of the selected dictionary to a variable
            current_question = r["Question"]
            current_answer = r["Answer"]
            current_value = r["Value"]
            print(self.name + "'s turn!")
            print("Current score:", self.money, "\n")
            # prints question and takes in user input
            print("For ", current_value, "dollars:")
            response = input(current_question)

            if response == current_answer:  # if user input matches answer,
                print("You got it!")
                self.money += current_value  # increases current players score
                # prints both scores
                print(player1.name, "'s score:", player1.money)
                print(player2.name, "'s score:", player2.money)
                print("------------------------------------------\n")
            else:
                # if user input does not match, prompts the next player if they want a chance to answer
                print("Incorrect!\n")
                self.money -= current_value
                steal = input("Next player, would you like to try to steal? ")
                if steal == "yes":
                    print("Steal attempt!")
                    # reprints the question for the next player
                    print("For ", current_value, "dollars:")
                    response = input(current_question)
                    if response == current_answer:
                        # if user answers correctly, checks who is stealing from who
                        print("You got it! \n")
                        if position == 1:  # if its player 1's turn at the moment, then player 2 must be stealing, increases player 2's money
                            player2.money += current_value
                            print(player1.name, "'s score:", player1.money)
                            print(player2.name, "'s score:", player2.money)
                            print("------------------------------------------\n")
                        elif position == 2:  # if its player 2's turn at the moment, then player 1 must be stealing, increases player 1's money
                            player1.money += current_value
                            print(player1.name, "'s score:", player1.money)
                            print(player2.name, "'s score:", player2.money)
                            print("------------------------------------------\n")
                    else:
                        # if the steal attempt fails, checks who the stealing player is to decrease money
                        print("Incorrect!")
                        if position == 1:  # if its player 1's turn, player 2 must be stealing, and got it wrong, so decrease player 2's money
                            player2.money -= current_value
                            print(player1.name, "'s score:", player1.money)
                            print(player2.name, "'s score:", player2.money)
                            print("------------------------------------------\n")
                        elif position == 2:  # if its player 2's turn, player 1 must be stealing, and got it wrong, so decrease player 1's money
                            player1.money -= current_value
                            print(player1.name, "'s score:", player1.money)
                            print(player2.name, "'s score:", player2.money)
                            print("------------------------------------------\n")
                elif steal == "no":  # The steal attempt could be decline if the next player does not know the answer
                    print("No response.  The answer was", current_answer)
                    print(player1.name, "'s score:", player1.money)
                    # prints answer and moves to the next players turn.
                    print(player2.name, "'s score:", player2.money)
                    print("Next Question \n")

            # removing question from the question list
            question_bank_list_of_dicts.remove(r)
            break

def print_board(categories):
        print(categories)

def bonus_round(bonus_questions):
    '''Bonus round lets players bet their won money on a final question.
    Grabs random question from list of dictionaries, just like the normal question list
    '''
    r = random.choice(list(
        bonus_questions))  # assigns r to a random item(dictionary) in the list of dictionaries
    for key, value in r.items():  # Iterates through the randomly selected dictionary to grab the values
        # assigns each value of the selected dictionary to a variable
        current_bonus_question = r["Question"]
        current_bonus_answer = r["Answer"]
        print("Now its time for the bonus round.  Take a look at the clue and then place your bets!\n")
        print(current_bonus_question)  # prints bonus question
        # user input for players' bets
        player1_bet = int(getpass.getpass(
            player1.name + ", please place your bet: "))
        player2_bet = int(getpass.getpass(
            player2.name + ", please place your bet: "))

        player1_bonus_answer = getpass.getpass(
            player1.name + ", please submit your answer: ")  # user input for players guess
        player2_bonus_answer = getpass.getpass(
            player2.name + ", please submit your answer: \n")
        print("The answer is: A Dundy")  # prints answer
        print("Lets see who got it correct\n")

        print(player1.name, " answered", player1_bonus_answer,
              ", and bet", player1_bet)  # prints both players' guesses
        print(player2.name, "answered", player2_bonus_answer,
              ", and bet", player2_bet, "\n")

        # if both players get it correct
        if (player1_bonus_answer == current_bonus_answer) and (player2_bonus_answer == current_bonus_answer):
            print("Both players got it correct!")
            player1.money += player1_bet
            player2.money += player2_bet
            return
        # if player 2 only gets it correct
        elif (player1_bonus_answer == current_bonus_answer) and (player2_bonus_answer != current_bonus_answer):
            print(player1.name, "got it correct!")
            player1.money += player1_bet
            player2.money -= player2_bet
            return
        # if player 2 only gets it correct
        elif (player1_bonus_answer != current_bonus_answer) and (player2_bonus_answer == current_bonus_answer):
            print(player2.name, "got it correct!")
            player1.money -= player1_bet
            player2.money += player2_bet
            return
        else:
            # if neither player gets it correct
            print("Neither player got it correct")
            player1.money -= player1_bet
            player2.money -= player2_bet
            return














welcome = text2art("Welcome  to The  Office Trivia!")
print(welcome)
p1name = input("Player 1, enter your name: ")  # takes in players name
p2name = input("Player 2, enter your name: ")
print("")
player1 = Player(p1name, 1)  # creates player instances
player2 = Player(p2name, 2)

# the actual game loops running the player turn functions until the question list is empty.
while question_bank_list_of_dicts != []:
    player1.playerTurn(question_bank_list_of_dicts, 1)
    player2.playerTurn(question_bank_list_of_dicts, 2)

print("Round complete! Lets take a look at the scores:\n")
print(player1.name, "has", player1.money, "dollars")
print(player2.name, "has", player2.money, "dollars")


bonus_round(bonus_questions)  # starts bonus round

print("")
print("Game over, lets check the scores!\n")
print(player1.name, "has", player1.money, "dollars")
print(player2.name, "has", player2.money, "dollars")

if player1.money > player2.money:
    print(text2art("Congrats", player1.name))
elif player1.money < player2.money:
    print(text2art("Congrats", player2.name))
else:
    print(text2art("Wow, its a tie!"))
