#This is a practice file for Git and GitHub

def winner(score):
    if score > 5:
        print("You are the winner")
    else:
        print("You lost")

firstround = {'Player': 'sarah', 'score': 6}
print(f"The winner of the firstround is {firstround['Player']} with {firstround['score']} points.")