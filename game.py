import random
card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def win(p,c):
    print(f"""
              player cards = {player}
              Computer cards = {computer}
              playersum = {p}
              computersum = {c}
        """)
    if(p>c and p<=21 and c<=21):
        print(f"""
              Computer Lost --> You Won """)
    if(p<c and p<=21 and c<=21):
        print(f"""
              Computer Won --> You Lost """)
    if(p>21 and c>21):
        print(f"""
              Game Bust """)
    if(p==c and p<=21 and c<=21):
        print(f"""
              Game Draw """)    
    if(p>21 and c<=21):
        print(f"""
              Computer Won --> You Lost """)
    if(p<=21 and c>21):
        print(f"""
              Computer Lost --> You Won """)
        
def anothercard():
    another=random.choice(card)
    print(f"New card : { another }")
    player.append(another)
    playersum=sum(player)
    computer.append(another)
    computersum=sum(computer)
    win(playersum,computersum)
def nocard():
    playersum=sum(player)
    computersum=sum(computer)
    win(playersum,computersum)
while (True):
    player = []
    computer = []
    i = 2
    while (i):
        player.append(random.choice(card))
        if (i == 2):
            computer.append(random.choice(card))
        else:
            unknown = random.choice(card)
        i = i-1
    print(f"Your cards : {player}")
    print(f"Computer cards {computer}")
    chance = input(
        "Do you want another card or do you want to pass : (type 'yes' or 'pass') : ")
    computer.append(unknown)
    if(chance=='yes'):
       anothercard()
    elif(chance=='pass'):
       nocard()
    again=input("Do you want to play once again : (type 'yes' or 'no' ): ")
    if(again=='no'):
        break
    else:
        print("""    We continue the game one more time ...  """)
    
