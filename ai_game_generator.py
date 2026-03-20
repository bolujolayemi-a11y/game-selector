# Ask the user which game they want
user_prompt = input("what kind of game do you want? ") .strip()

# Match the imput and provide a response
if user_prompt.lower() == "candy crush":
    print("you chose Candy Crush! stepping into game environment")

elif user_prompt.lower() == "bubble shooter":
    print("you chose Bubble shooter! stepping into game environment")

elif user_prompt.lower() == "backgammon":
    print("you chose Backgammon! stepping into game environment")

elif user_prompt.lower() == "tetris":
    print("you chose Tetris! stepping into game environment")

else:
    print("this game is not supported yet")
