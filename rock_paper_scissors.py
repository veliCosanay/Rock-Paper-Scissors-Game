import random

computer_win_status = {
    "Rock" : "Scissors",
    "Paper" : "Rock",
    "Scissors" : "Paper"
}
options = ["Rock","Paper","Scissors"]

def computer_choise():
    return random.choice(options)

def player_input_corrector(player_input):
    if player_input == "R":
        return "Rock"
    elif player_input == "P":
        return "Paper"
    elif player_input == "S":
        return "Scissors"

def results(computer_choise,player_input):
    if computer_win_status[computer_choise] == player_input_corrector(player_input):
        return "c"
    elif computer_choise == player_input_corrector(player_input):
        return "d"
    else:
        return "p"

def main():
    computer_score = 0
    player_score = 0

    
    print("Press 'R' for rock, 'P' for paper and 'S' for scissors")

    while True:
        player_input = input("")
        player_input = player_input.capitalize()
        if not (player_input == "R" or player_input == "P" or player_input == "S"):
            print("Please select one of the options")
            continue
        computer_move = computer_choise()
        if results(computer_move,player_input) == "c":
            computer_score += 1
        elif results(computer_move,player_input) == "p":
            player_score += 1 
        
        print()
        print(f"Choise of computer: {computer_move}")
        print(f"Choise of player: {player_input_corrector(player_input)}")
        print(f"Computer {computer_score} - {player_score} Player")            
        print()

        if computer_score == 3:
            print("Computer Won")
            break
        elif player_score == 3:
            print("Player won")
            break

if __name__ == "__main__":
    main()
