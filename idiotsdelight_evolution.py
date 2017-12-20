from random import shuffle
from collections import defaultdict

# functions
def shuffle_deck(deck):
	shuffle(deck)
	return deck

def check_cards(played_cards, discarded_cards):
	'''determines if cards can be removed'''
	if len(played_cards) >= 4:
		last_card = list(played_cards[-1])
		last_card_suite = last_card[0]
		last_card_number = last_card[1]
		fourth_card = list(played_cards[-4])
		fourth_card_suite = fourth_card[0]
		fourth_card_number = fourth_card[1]
		if last_card_number == fourth_card_number:
			discarded_cards.append(played_cards[-4])
			discarded_cards.append(played_cards[-3])
			discarded_cards.append(played_cards[-2])
			discarded_cards.append(played_cards[-1])
			del played_cards[-4:]		
		elif last_card_suite == fourth_card_suite:
			discarded_cards.append(played_cards[-3])
			discarded_cards.append(played_cards[-2])
			del played_cards[-3:-1]
			check_cards(played_cards, discarded_cards)
	return played_cards, discarded_cards
	
def count_movements(deck, old_deck):
	movements = 0
	for x in range(0,52):
		if deck[x] != old_deck[x]:
			movements += 1
	return movements

def run_trial(deck, deck_size):
	played_cards = []
	discarded_cards = []
	movements_over_time = []
	played_decks = defaultdict(list)
	times_played = 0
	deck_repeat = 0
	stable = 0
	time_stable = 0
	for x in range(0,75):
		old_deck = list(deck)
		movements_in_run = 0
		played_cards = []
		discarded_cards = []
		for card in range(1,deck_size+1):
			movements=0
			played_cards.append(deck[0])
			deck.pop(0)
			cards = check_cards(played_cards, discarded_cards)
			played_cards = cards[0]
			discarded_cards= cards[1]
		deck = discarded_cards + played_cards
		movements = count_movements(deck, old_deck)
		movements_over_time.append(movements)
		times_played+=1
		if deck in played_decks.values():
			played_decks[times_played] = played_decks[times_played] + deck
			if stable == 0:
				time_stable = times_played
				stable = 1
		else:
			played_decks[times_played] = played_decks[times_played] + deck
	return(played_decks, times_played, movements_over_time, time_stable)

# This section writes file with data from using one deck of cards
myfile = open("idiotsdelight_evolution_1_deck.csv", 'w')
runx = ""
for run_number in range(75, 0, -1):
	runx = "run" + str(run_number) + ", " + runx
myfile.write("trial, time stable, " + runx)
myfile.close()

# create deck of cards	
diamonds = "DA D2 D3 D4 D5 D6 D7 D8 D9 D10 DJ DQ DK "
hearts = "HA H2 H3 H4 H5 H6 H7 H8 H9 H10 HJ HQ HK "
clubs =	"CA C2 C3 C4 C5 C6 C7 C8 C9 C10 CJ CQ CK "
spades = "SA S2 S3 S4 S5 S6 S7 S8 S9 S10 SJ SQ SK "


for x in range(1,101):
	deck = diamonds + hearts + clubs + spades.rstrip()
	unshuffled_deck = deck.split(" ")				
	shuffled_deck = shuffle_deck(unshuffled_deck)
	deck_size = 52
	trial_info = run_trial(shuffled_deck, deck_size)
	trial = x
	time_stable = trial_info[3]
	movement_list = trial_info[2]
	movements = ""
	for item in movement_list:
		movements = movements + str(item) + ", "

	myfile = open("idiotsdelight_evolution_1_deck.csv", 'a')
	myfile.write("\n" + str(trial) + ", " + str(time_stable) + ", " + movements)

	myfile.close()
	
# This section writes file with data from using two decks of cards
myfile = open("idiotsdelight_evolution_2_decks.csv", 'w')
runx = ""
for run_number in range(75, 0, -1):
	runx = "run" + str(run_number) + ", " + runx
myfile.write("trial, time stable, " + runx)
myfile.close()

# create double deck of cards	
diamonds = "DA D2 D3 D4 D5 D6 D7 D8 D9 D10 DJ DQ DK DA D2 D3 D4 D5 D6 D7 D8 D9 D10 DJ DQ DK "
hearts = "HA H2 H3 H4 H5 H6 H7 H8 H9 H10 HJ HQ HK HA H2 H3 H4 H5 H6 H7 H8 H9 H10 HJ HQ HK "
clubs =	"CA C2 C3 C4 C5 C6 C7 C8 C9 C10 CJ CQ CK CA C2 C3 C4 C5 C6 C7 C8 C9 C10 CJ CQ CK "
spades = "SA S2 S3 S4 S5 S6 S7 S8 S9 S10 SJ SQ SK SA S2 S3 S4 S5 S6 S7 S8 S9 S10 SJ SQ SK "


for x in range(1,101):
	deck = diamonds + hearts + clubs + spades.rstrip()
	unshuffled_deck = deck.split(" ")				
	shuffled_deck = shuffle_deck(unshuffled_deck)
	deck_size = 104
	trial_info = run_trial(shuffled_deck, deck_size)
	trial = x
	time_stable = trial_info[3]
	movement_list = trial_info[2]
	movements = ""
	for item in movement_list:
		movements = movements + str(item) + ", "

	myfile = open("idiotsdelight_evolution_2_decks.csv", 'a')
	myfile.write("\n" + str(trial) + ", " + str(time_stable) + ", " + movements)

	myfile.close()

# This section writes file with data from using two decks of cards
myfile = open("idiotsdelight_evolution_3_decks.csv", 'w')
runx = ""
for run_number in range(75, 0, -1):
	runx = "run" + str(run_number) + ", " + runx
myfile.write("trial, time stable, " + runx)
myfile.close()

# create triple deck of cards	
diamonds = "DA D2 D3 D4 D5 D6 D7 D8 D9 D10 DJ DQ DK DA D2 D3 D4 D5 D6 D7 D8 D9 D10 DJ DQ DK DA D2 D3 D4 D5 D6 D7 D8 D9 D10 DJ DQ DK "
hearts = "HA H2 H3 H4 H5 H6 H7 H8 H9 H10 HJ HQ HK HA H2 H3 H4 H5 H6 H7 H8 H9 H10 HJ HQ HK HA H2 H3 H4 H5 H6 H7 H8 H9 H10 HJ HQ HK "
clubs =	"CA C2 C3 C4 C5 C6 C7 C8 C9 C10 CJ CQ CK CA C2 C3 C4 C5 C6 C7 C8 C9 C10 CJ CQ CK CA C2 C3 C4 C5 C6 C7 C8 C9 C10 CJ CQ CK "
spades = "SA S2 S3 S4 S5 S6 S7 S8 S9 S10 SJ SQ SK SA S2 S3 S4 S5 S6 S7 S8 S9 S10 SJ SQ SK SA S2 S3 S4 S5 S6 S7 S8 S9 S10 SJ SQ SK "


for x in range(1,101):
	deck = diamonds + hearts + clubs + spades.rstrip()
	unshuffled_deck = deck.split(" ")				
	shuffled_deck = shuffle_deck(unshuffled_deck)
	deck_size = 156
	trial_info = run_trial(shuffled_deck, deck_size)
	trial = x
	time_stable = trial_info[3]
	movement_list = trial_info[2]
	movements = ""
	for item in movement_list:
		movements = movements + str(item) + ", "

	myfile = open("idiotsdelight_evolution_3_decks.csv", 'a')
	myfile.write("\n" + str(trial) + ", " + str(time_stable) + ", " + movements)

	myfile.close()

# This section writes file with data from using two decks of cards
myfile = open("idiotsdelight_evolution_6_decks.csv", 'w')
runx = ""
for run_number in range(75, 0, -1):
	runx = "run" + str(run_number) + ", " + runx
myfile.write("trial, time stable, " + runx)
myfile.close()

# create triple deck of cards	
diamonds = "DA D2 D3 D4 D5 D6 D7 D8 D9 D10 DJ DQ DK DA D2 D3 D4 D5 D6 D7 D8 D9 D10 DJ DQ DK DA D2 D3 D4 D5 D6 D7 D8 D9 D10 DJ DQ DK DA D2 D3 D4 D5 D6 D7 D8 D9 D10 DJ DQ DK DA D2 D3 D4 D5 D6 D7 D8 D9 D10 DJ DQ DK DA D2 D3 D4 D5 D6 D7 D8 D9 D10 DJ DQ DK "
hearts = "HA H2 H3 H4 H5 H6 H7 H8 H9 H10 HJ HQ HK HA H2 H3 H4 H5 H6 H7 H8 H9 H10 HJ HQ HK HA H2 H3 H4 H5 H6 H7 H8 H9 H10 HJ HQ HK HA H2 H3 H4 H5 H6 H7 H8 H9 H10 HJ HQ HK HA H2 H3 H4 H5 H6 H7 H8 H9 H10 HJ HQ HK HA H2 H3 H4 H5 H6 H7 H8 H9 H10 HJ HQ HK "
clubs =	"CA C2 C3 C4 C5 C6 C7 C8 C9 C10 CJ CQ CK CA C2 C3 C4 C5 C6 C7 C8 C9 C10 CJ CQ CK CA C2 C3 C4 C5 C6 C7 C8 C9 C10 CJ CQ CK CA C2 C3 C4 C5 C6 C7 C8 C9 C10 CJ CQ CK CA C2 C3 C4 C5 C6 C7 C8 C9 C10 CJ CQ CK CA C2 C3 C4 C5 C6 C7 C8 C9 C10 CJ CQ CK "
spades = "SA S2 S3 S4 S5 S6 S7 S8 S9 S10 SJ SQ SK SA S2 S3 S4 S5 S6 S7 S8 S9 S10 SJ SQ SK SA S2 S3 S4 S5 S6 S7 S8 S9 S10 SJ SQ SK SA S2 S3 S4 S5 S6 S7 S8 S9 S10 SJ SQ SK SA S2 S3 S4 S5 S6 S7 S8 S9 S10 SJ SQ SK SA S2 S3 S4 S5 S6 S7 S8 S9 S10 SJ SQ SK "


for x in range(1,101):
	deck = diamonds + hearts + clubs + spades.rstrip()
	unshuffled_deck = deck.split(" ")				
	shuffled_deck = shuffle_deck(unshuffled_deck)
	deck_size = 312
	trial_info = run_trial(shuffled_deck, deck_size)
	trial = x
	time_stable = trial_info[3]
	movement_list = trial_info[2]
	movements = ""
	for item in movement_list:
		movements = movements + str(item) + ", "

	myfile = open("idiotsdelight_evolution_6_decks.csv", 'a')
	myfile.write("\n" + str(trial) + ", " + str(time_stable) + ", " + movements)

	myfile.close()

