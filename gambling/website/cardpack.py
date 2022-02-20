import random

class PlayingCard:

    Visible = True

    def __init__(self, suit, cardnumber) -> None:
        self.suit = suit
        self.cardnumber = cardnumber

        suitName = ""
        cardName = ""

        if self.suit == 1:
            suitName="Spades"            
        elif self.suit == 2:
            suitName="Clubs"
        elif self.suit == 3:
            suitName="Hearts"
        elif self.suit == 4:
            suitName="Diamonds"

        if self.cardnumber == 1:
            cardName = "Ace"
        elif self.cardnumber == 11:
            cardName = "Jack"
        elif self.cardnumber == 12:
            cardName = "Queen"
        elif self.cardnumber == 13:
            cardName = "King"
        else:
            cardName = str(self.cardnumber)             
    
        self.suitName = suitName
        self.cardName = cardName

        if self.cardnumber == 10:
            self.cardImageName = "10" + suitName[:1] + ".jpg"
        else:
            self.cardImageName = cardName[:1] + suitName[:1] + ".jpg" 

        self.cardDescription = cardName + " of " + suitName    

class PackOfCards:     

    def __init__(self) -> None:
        self.cards = []  
        cardposition = 1
        for suit in range(1,5):
            for cardno in range(1,14):
                self.cards.append(PlayingCard(suit,cardno))

        self.Shuffle()        

    def Shuffle(self):
        random.shuffle(self.cards)