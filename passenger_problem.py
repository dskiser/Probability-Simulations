'''Script demonstrating the symmetry of the passengers probability
problem. Suppose n passengers are assigned to n seats, but the first
passenger randomly takes a seat that was not assigned to him/her. Every
subsequent passenger then sits in their seat if it is available.
However, if it is not available, they randomly choose another seat to 
sit in.  What is the probability that the last passenger will sit in 
his/her assigned seat?'''

import itertools
import sys

# check arguments
passengers = sys.argv[1]
if int(passengers) > 20:
	print("Due to computational limitations, you cannot have more" +
		" than 20 passengers!")
	sys.exit()

# get probabilities not including 1/passengers
probabilities = []
for j in range(1, int(passengers)-1):
	probabilities.append(1/(int(passengers) - j))

	
# get every combination of probabilities excluding 1/passengers
probability_combinations = []
for j in range(1,(len(probabilities)+1)):
	combinations = itertools.combinations(probabilities, j)
	for combination in combinations:
		probability_combinations.append(combination)	


# for every combination of probability (including 1/passengers), 
# calculate probability and add to sum
total_probability = 1/int(passengers)
for probability_combination in probability_combinations:
	prob_of_combination = 1/int(passengers)
	for probability in probability_combination:
		prob_of_combination = prob_of_combination * probability
	total_probability+=prob_of_combination

# display result
total_probability = round(total_probability, 4)
print(total_probability)
			
		
	
	
