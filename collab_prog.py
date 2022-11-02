#This is a practice file for Git and GitHub

def winner(score):
    if score < 5:
        print("You are the winner")
    else:
        print("You lost")

firstround = {'Player': 'Sarah', 'score': 6}
secondround = {'Player2': 'Nina', 'score2': 2}
print(f"The winner of the firstround is {firstround['Player']} with \
{firstround['score']} points.")
print(f"Unfortunately for the second round, {secondround['Player2']} lost with \
a score of {secondround['score2']} points.")