import random

computer_win_status = {
    "Rock" : "Scissors",
    "Paper" : "Rock",
    "Scissors" : "Paper"
}
options = ["Rock","Paper","Scissors"]

def computer_choise():
    return random.choice(options)

def user_input_corrector(user_input):
    if user_input == "R":
        return "Rock"
    elif user_input == "P":
        return "Paper"
    elif user_input == "S":
        return "Scissors"

def results(computer_choise,user_input):
    if computer_win_status[computer_choise] == user_input_corrector(user_input):
        return "c"
    elif computer_choise == user_input_corrector(user_input):
        return "d"
    else:
        return "u"

def main():
    computer_score = 0
    user_score = 0

    # print("Taş için 'T', kağıt için 'K', Scissors için 'M' ye basınız")
    print("Press 'R' for stone, 'P' for paper and 'S' for scissors")

    while True:
        user_input = input("")
        user_input = user_input.capitalize()
        if not (user_input == "R" or user_input == "P" or user_input == "S"):
            print("Please select one of the options")
            continue
        computer_move = computer_choise()
        if results(computer_move,user_input) == "c":
            computer_score += 1
        elif results(computer_move,user_input) == "u":
            user_score += 1 
        
        print()
        print(f"Choise of computer: {computer_move}")
        print(f"Choise of player: {user_input_corrector(user_input)}")
        print(f"Computer {computer_score} - {user_score} Player")            
        print()

        if computer_score == 3:
            print("Computer Won")
            break
        elif user_score == 3:
            print("Player won")
            break

if __name__ == "__main__":
    main()