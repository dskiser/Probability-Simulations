import random
import sys
import math
import numpy as np

# create stores and stock with customers
def create_stores(num, customers):
	stores = {}
	for x in range(1, num+1):
		stores[x] = np.random.poisson(1, customers)[0]
	return stores

def shuffle_stores(stores):
	new_stores = dict(zip(stores.keys(), random.sample(list(stores.values()),
		len(stores))))
	return new_stores

# determine number of stores with matching customers
def calc_matches(stores, stores2):
	matches_found = 0
	for store_num, customer_num in stores.items():
		for store2_num, customer2_num in stores.items():
			if store_num != store2_num:
				if customer_num == customer2_num: 
					matches_found+=0.5
	return matches_found

# determine number of stores with matching customers
# if a store can match itself
def alt_calc_matches(stores, stores2):
	alt_matches_found = 0
	for store_num, customer_num in stores.items():
		for store2_num, customer2_num in stores2.items():
			if customer_num == customer2_num:
				if store_num != store2_num:
					alt_matches_found+=1
				if store_num == store2_num:
					alt_matches_found+=1
	return alt_matches_found
	
# calculate permutations
def nCr(n, r):
	f = math.factorial
	return f(n) // f(r) // f(n-r)

# read in arguments
num_trials = int(sys.argv[1])
num_stores = int(sys.argv[2])
max_customers = int(sys.argv[3])

num_matches = 0
alt_num_matches = 0

# run trials for regular
for x in range(0, num_trials):
	stores = create_stores(num_stores, max_customers)
	stores2 = stores
	num_matches += calc_matches(stores, stores2)
	
# calculate probability that number of customers at two stores will
# match...
# if stores cannot match themselves	
permutations_per_trial = nCr(num_stores, 2)
permutations_total = num_trials * permutations_per_trial
prob = num_matches/(permutations_total)
	
# run trials for alternate
for x in range(0, num_trials):
	stores = create_stores(num_stores, max_customers)
	stores2 = shuffle_stores(stores)
	num_matches += calc_matches(stores, stores2)
	alt_num_matches += alt_calc_matches(stores, stores2)
	
# calculate probability that number of customers at two stores will
# match...
# if stores can match themselves
alt_permutations_per_trial = num_stores**2
alt_permutations_total = num_trials * alt_permutations_per_trial
alt_prob = alt_num_matches/alt_permutations_total

#output
print("Probability of match: " + str(prob))
print("Probability of match if stores can match themselves: " + 
		str(alt_prob))
prob_comparison = alt_prob / prob
print("Probability comparison: " + str(prob_comparison))



	
				
