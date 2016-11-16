# Created by: Hamza Salman
# Created for: Ics3U
#Created on: November 2016
# This is a black jack game similar to our last assignment but this time it is using an actual deck lf cards rather than numbers.

import ui
import random
import console

player_total = 0
computer_total = 0
player_card_one = 0
player_card_two = 0
player_card_three = 0
computer_card_one = 0
computer_card_two = 0
computer_card_three = 0

def play_button_touch_up_inside(sender):
	# this function sets up the game to be played
	
    view['result_label'].text = ''

    global dealer_total
    global player_total_one
    global player_total_two
    global player_total_three
    global player_card_one
    global player_card_two
    global player_card_three
    global computer_card_one
    global computer_card_two
    global computer_card_three


    player_card_one_value = random.randint(0,51)
    player_card_two_value = random.randint(0,51)
    player_card_three_value = random.randint(0,51)
    computer_card_one_value = random.randint(0,51)
    computer_card_two_value = random.randint(0,51)
    computer_card_three_value = random.randint(0,51)


    cards = ["Diamonds", "Spades", "Clubs", "Hearts"]
    card_sizes = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "J", "K", "Q"]
    deck = []

    for i in cards:
        for v in card_sizes:
            deck.append(i + v)
    print deck
    computer_card_one = deck[computer_card_one_value]
    computer_card_two = deck[computer_card_two_value]
    computer_card_three = deck[computer_card_three_value]
    player_card_one = deck[player_card_one_value]
    player_card_two = deck[player_card_two_value]
    player_card_three = deck[player_card_three_value]
        
    deck_values = [2,3,4,5,6,7,8,9,10,1,10,10,10,2,3,4,5,6,7,8,9,10,1,10,10,10,2,3,4,5,6,7,8,9,10,1,10,10,10,2,3,4,5,6,7,8,9,10,1,10,10,10]
        
    player_total_one = deck_values[player_card_one_value]
    player_total_two = deck_values[player_card_two_value]
    player_total_three = deck_values[player_card_three_value]
    #player_total = player_total_one + player_total_two + player_total_three
    print player_total
    dealer_total = int(deck_values[computer_card_one_value]) + int(deck_values[computer_card_two_value]) +     int(deck_values[computer_card_three_value])


def check_button_touch_up_inside(sender):
	# this functionchecks and compares the final values. it also reveals the dealers cards.
	
    global dealer_total
	
    view['computer_card_one_imageview'].image = ui.Image('card:' + str(computer_card_one))
    view['computer_card_two_imageview'].image = ui.Image('card:' + str(computer_card_two))
    view['computer_card_three_imageview'].image = ui.Image('card:' + str(computer_card_three))
    view['computer_total_label'].text = 'Dealer Total: ' + str(dealer_total)
    
    if player_total <= 21:
        if dealer_total > 21:
            view['result_label'].text = 'You Win!'
        elif dealer_total <= 21:
            if dealer_total < player_total:
                view['result_label'].text = 'You Win!'
            elif dealer_total > player_total:
                view['result_label'].text = 'You Lose!'
            elif dealer_total == player_total:
                view['result_label'].text = 'It is a Tie! Dealer Wins!'
    if player_total > 21:
        view['result_label'].text = 'You Lose!'
        if dealer_total > 21:
            view['result_label'].text = 'You both Lose!'
    

def player_card_one_touch_up_inside(sender):
	# this function flips over the first card when it is touched.
	
    global player_total_one
    global player_total
    
    view['player_card_one_imageview'].image = ui.Image('card:' + str(player_card_one))
    if player_total_one == 1:
        ace = console.alert('info','would you like 1 or 11', '1', '11', hide_cancel_button=True)
        if ace == 1:
            player_total = player_total + player_total_one
            view['player_total_label'].text = 'Player Total: ' + str(player_total)
        else:
            player_total = int(player_total) + 11
            view['player_total_label'].text = 'Player Total: ' + str(player_total)
    else:
        player_total = player_total + player_total_one
        view['player_total_label'].text = 'Player Total: ' + str(player_total)
    
def player_card_two_touch_up_inside(sender):
	# this function flips over the second card when it is touched.
	
    global player_total
    global player_total_two
	
    view['player_card_two_imageview'].image = ui.Image('card:' + str(player_card_two))
    if player_total_two == 1:
        ace = console.alert('info','would you like 1 or 11', '1', '11', hide_cancel_button=True)
        if ace == 1:
            player_total = player_total + player_total_two
            view['player_total_label'].text = 'Player Total: ' + str(player_total)
        else:
            player_total = int(player_total) + 11
            view['player_total_label'].text = 'Player Total: ' + str(player_total)
    else:
        player_total = player_total + player_total_two
        view['player_total_label'].text = 'Player Total: ' + str(player_total)
    
def player_card_three_touch_up_inside(sender):
	# this function flips over the third card when it is touched.
	
    global player_total
    global player_total_two
	
    third_card = console.alert('Third Card', 'Would you like a third card?', 'Yes', 'No', hide_cancel_button=True)
    
    if third_card == 1:
        view['player_card_three_imageview'].image = ui.Image('card:' + str(player_card_three))
        if player_total_one == 1:
            ace = console.alert('info','would you like 1 or 11', '1', '11', hide_cancel_button=True)
            if ace == 1:
                player_total = player_total + player_total_three
                view['player_total_label'].text = 'Player Total: ' + str(player_total)
            else:
                player_total = int(player_total) + 11
                view['player_total_label'].text = 'Player Total: ' + str(player_total)
        else:
            player_total = player_total + player_total_three
            view['player_total_label'].text = 'Player Total: ' + str(player_total)
     
    else:
        pass

def reset_button_touch_up_inside(sender):
    # This function resets the game to be played again.
    
    global player_card_one_value
    global player_card_two_value
    global player_card_three_value
    global computer_card_one_value
    global computer_card_two_value
    global computer_card_three_value
    global player_total
    global dealer_total
    
    player_card_one_value = 0
    player_card_two_value = 0
    player_card_three_value = 0
    computer_card_one_value = 0
    computer_card_two_value = 0
    computer_card_three_value = 0
    player_total = 0
    dealer_total = 0
    
    view['computer_card_one_imageview'].image = ui.Image('card:BackBlue4')
    view['computer_card_two_imageview'].image = ui.Image('card:BackBlue4')
    view['computer_card_three_imageview'].image = ui.Image('card:BackBlue4')
    view['player_card_one_imageview'].image = ui.Image('card:BackBlue4')
    view['player_card_two_imageview'].image = ui.Image('card:BackBlue4')
    view['player_card_three_imageview'].image = ui.Image('card:BackGreen2')
    
    view['result_label'].text = 'PRESS PLAY TO START'
    view['player_total_label'].text = 'Player Total: '
    view['computer_total_label'].text = 'Dealer Total: '
    
    
view = ui.load_view()
view.present('full_screen')

view['computer_card_one_imageview'].image = ui.Image('card:BackBlue4')
view['computer_card_two_imageview'].image = ui.Image('card:BackBlue4')
view['computer_card_three_imageview'].image = ui.Image('card:BackBlue4')
view['player_card_one_imageview'].image = ui.Image('card:BackBlue4')
view['player_card_two_imageview'].image = ui.Image('card:BackBlue4')
view['player_card_three_imageview'].image = ui.Image('card:BackGreen2')
