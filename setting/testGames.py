import random as rd
from time import sleep
deck = [2,3,4,5,6,7,8,9,10,11,12,13,14] * 4
Stop = False
balance = 1000

def firstGame():
    '''игра в которой человек пытается угадать число'''
    count = 0
    secretNumber = rd.randint(1,100)
    while count < 6:
        answer = input(f"There are {6-count} left for your attempt to guess.\n")
        if answer == "stop":
            print(secretNumber)
            break
        answer = int(answer)
        if answer > secretNumber:
            print("your number is less than what you need, try again")
        elif answer < secretNumber:
            print("your number is higher than expected, try again")
        else:
            print("Вы выиграли!!! ")
            break
        count += 1  

def secondGame():
    '''BlackJack'''
    global deck, balance, Stop
    for i in deck:
        if i > 10 and i < 14:
            deck[deck.index(i)] = 10
        elif i == 14:
            deck[deck.index(i)] = 11
    random = rd.Random()
    random.shuffle(deck, random=None)
    '''if 10 + 11, 3:2
    if diler have 17+ point, he need stop '''
    
    PlayersHand = []
    DilersHand = []
    
    
    while True:
        PlayersHand.clear()
        DilersHand.clear()
        rate = input("how your rate?\n")
        if rate == "stop":
            print(f"you balance: {balance}")
            Stop = True
            break
        elif rate == 'balance':
            print(balance)
            continue
        rate = int(rate)
        balance -= rate
        if balance < 0:
            balance += rate 
            print("please, top up balance")
            continue
        
        round(deck=deck,PlayersHand=PlayersHand, DilersHand=DilersHand)
        sum = sumHand(hand = PlayersHand)
        print(f"your hand: {PlayersHand} and your sum: {sum}\n"
              f"diler's hand: {DilersHand[0]} and secret card")
        sleep(1)
        
        takeCard(PlayersHand=PlayersHand, deck=deck)
        
        sum = (sumHand(hand = PlayersHand))
        
        if sum > 21:
            print(f"you lose. You have {PlayersHand}")
            return
        
        elif sum == 21:
            print(f"you win!!! You have {PlayersHand}")
            balance += rate * 2
            return 
        
        elif sum < 21: 
            print(f"now your hand: {PlayersHand} and your sum: {sum}")
            # diler start play
            result = GameDiler(DilersHand=DilersHand, deck = deck, PlayersSum=sum)
            match result:
                case "Win":
                    balance += rate * 2
                    print("YOU WIN!!! ")
                case "Lose":
                    print("You Lose. ")
                case "Draw":
                    balance += rate
                    print("You have draw")      
    
            
def takeCard(PlayersHand, deck):
    '''process player cards'''
    trueWords = ["yes", "of course", "да", "конечно",'давай']
    falseWords = ["no", 'не',"хватит"]
    while True: # player put card 
        answer = input("do you want to get another card?\n").lower()
        
        if answer in trueWords:
            round(deck=deck,PlayersHand=PlayersHand, DilersHand=None)
            print(f"now your hand: {PlayersHand} and your sum: {sumHand(PlayersHand)}")
        elif answer in falseWords:
            return
            
        else:
            print("command andefine/ Try again!!! ", end="\n")
            continue
        
        
def GameDiler(DilersHand:list, PlayersSum:int, deck:list):
    '''comparison hands'''
    while True:
        DilerSum = sumHand(DilersHand)
        if DilerSum > 21:
            return "Win"
        
        elif DilerSum == 21:
            return "Lose"
        
        elif DilerSum > PlayersSum:
            return "Lose"
        
        else:
            if DilerSum <= 16: 
                
                if DilerSum < PlayersSum:
                    return "Win"
                
                if DilerSum == PlayersSum:
                    return "Draw"
            
            else:
                round(deck = deck, PlayersHand= DilersHand)
                continue
        
        
                    
def sumHand(hand:list):
    '''sum point in hand'''
    sum = 0
    for i in hand:
        sum += i
    return sum
 
    
def round(deck:list,PlayersHand:list,  DilersHand:list | None):
    '''add card for hand'''
    if DilersHand != None:
        for i in range(0,2):
            card = deck.pop(0)
            PlayersHand.append(card)
            card = deck.pop(0)
            DilersHand.append(card)
    else:
        card = deck.pop(0)
        PlayersHand.append(card)
        
        
    return deck, PlayersHand, DilersHand



if __name__ == '__main__':
    while balance > 0 and Stop != True:
        secondGame()
    