# This program uses a dictionary as a deck of cards.
import random 

def main():
    # Create a deck of cards.
    deck_dict = create_deck()
   

    # Get the number of cards to deal.
    num_cards = int(input('How many cards should I deal? '))



    # Deal the cards.
    deal_cards(deck_dict, num_cards) #not assign a variable cause its not returning a value


    
    

# The create_deck function returns a dictionary
# representing a deck of cards.
def create_deck(): 
    # Create a dictionary with each card and its value
    # stored as key-value pairs.
    deck = {'Ace of Spades':1, '2 of Spades':2, '3 of Spades':3,
            '4 of Spades':4, '5 of Spades':5, '6 of Spades':6,
            '7 of Spades':7, '8 of Spades':8, '9 of Spades':9,
            '10 of Spades':10, 'Jack of Spades':10,
            'Queen of Spades':10, 'King of Spades': 10,
            
            'Ace of Hearts':1, '2 of Hearts':2, '3 of Hearts':3,
            '4 of Hearts':4, '5 of Hearts':5, '6 of Hearts':6,
            '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9,
            '10 of Hearts':10, 'Jack of Hearts':10,
            'Queen of Hearts':10, 'King of Hearts': 10,
            
            'Ace of Clubs':1, '2 of Clubs':2, '3 of Clubs':3,
            '4 of Clubs':4, '5 of Clubs':5, '6 of Clubs':6,
            '7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9,
            '10 of Clubs':10, 'Jack of Clubs':10,
            'Queen of Clubs':10, 'King of Clubs': 10,
            
            'Ace of Diamonds':1, '2 of Diamonds':2, '3 of Diamonds':3,
            '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6,
            '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
            '10 of Diamonds':10, 'Jack of Diamonds':10,
            'Queen of Diamonds':10, 'King of Diamonds': 10}
            #because the name of the card is unique #KEYS NEED TO BE UNIQUE, the value can be repeated, that why the numbers are  the values

    # Return the deck.
    return deck #if you are returning you ned to  assign thw function to a variable dict = function



# The deal_cards function deals a specified number of cards
# from the deck.

def deal_cards(deck, number):
    # Initialize an accumulator for the hand value.
    hand_value = 0


    
    
    # DATA VALIDATION
    # Make sure the number of cards to deal is not
    # greater than the number of cards in the deck (52).
    if number > len(deck):
        number =  len(deck)  #you can also use a while loop asking again for the number 

    
    

    # Deal the cards and accumulate their values.
    for num in range(number):  #num is irrelevant, we are repeating the for loop as long as the user put in the num
        card = random.choice(list(deck)) #it is going to create a list of the keys
        value =  deck[card]   
        print(card)
        hand_value += value




    

    # Display the value of the hand.
    print(hand_value)
    
    

# Call the main function.
main()
