from random import shuffle
import matplotlib.pyplot as plt
import numpy as np

# functions
def shuffle_deck(deck):
	shuffle(deck)
	return deck

def check_cards(played_cards):
	'''determines if cards can be removed'''
	if len(played_cards) >= 4:
		last_card = list(played_cards[-1])
		last_card_suite = last_card[0]
		last_card_number = last_card[1]
		fourth_card = list(played_cards[-4])
		fourth_card_suite = fourth_card[0]
		fourth_card_number = fourth_card[1]
		if last_card_suite == fourth_card_suite:
			del played_cards[-3:-1]
			check_cards(played_cards)
		elif last_card_number == fourth_card_number:
			del played_cards[-4:]
			check_cards(played_cards)
	return played_cards
		
# create deck of cards	
diamonds = "DA D2 D3 D4 D5 D6 D7 D8 D9 D10 DJ DQ DK "
hearts = "HA H2 H3 H4 H5 H6 H7 H8 H9 H10 HJ HQ HK "
clubs =	"CA C2 C3 C4 C5 C6 C7 C8 C9 C10 CJ CQ CK "
spades = "SA S2 S3 S4 S5 S6 S7 S8 S9 S10 SJ SQ SK "
deck = diamonds + hearts + clubs + spades.rstrip()


# This section is for determining the probability of winning Idiot's
# Delight

# run trials
number_trials = 1000
scores = []

for trial in range(1, number_trials+1):
	unshuffled_deck = deck.split(" ")
	shuffled_deck = shuffle_deck(unshuffled_deck)
	played_cards = []
	for card in range(1,53):
		played_cards.append(shuffled_deck[0])
		shuffled_deck.pop(0)
		played_cards = check_cards(played_cards)
	
	scores.append(len(played_cards))
total_score = 0
for score in scores:
	total_score += int(score)
average = total_score / number_trials
print("Average:" + str(average))

score_outcomes = {}
for possible_score in range(0,53,2):
	number_of_occurences = 0
	for score in scores:
		if score == possible_score:
			number_of_occurences += 1
	if possible_score == 0:
		number_of_wins = number_of_occurences
	score_outcomes[possible_score] = number_of_occurences



# print statistics	
print("Number of wins: " + str(number_of_wins))
probability_of_winning = number_of_wins / number_trials
odds_of_winning = 1 / probability_of_winning
print("Probability of winning: " + str(probability_of_winning * 100) +
	"%")
print("Odds of winning: 1/" + str(round(odds_of_winning)))

# plot outcomes
X = np.arange(len(score_outcomes))
plt.bar(X, score_outcomes.values(), align='center', width=0.5)
plt.xticks(X, score_outcomes.keys())
ymax = max(score_outcomes.values()) + 1
plt.xlabel("Scores")
plt.ylabel("Number of Occurences")
plt.title("Idiot's Delight: Frequency of possible scores after 1,000 attempts")
plt.ylim(0, ymax)
plt.show()	


	
	
		

				
