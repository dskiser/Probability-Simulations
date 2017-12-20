'''Simulation of question #80 in chapter 4 of "Introduction to Probability"'''
from random import shuffle
import sys

# Create senate with democrats and republicans
def create_partisan_senate(democrats):
	senate = []
	for x in range(0, democrats-1):
		senate.append("D")
	for x in range(0, 99-democrats):
		senate.append("R")
	shuffle(senate)
	return senate

# Create senate of states
def create_state_senate():
	senate = []
	for x in range(1,51):
		senate.append(x)
		senate.append(x)
	shuffle(senate)
	return senate

# Check if state represented twice on committee
def check_states(committee):
	states_rep_twice = 0
	for x in range(0,len(committee)):
		for y in range(x+1, len(committee)):
			if committee[x] == committee[y]:
				states_rep_twice += 1
	return states_rep_twice
				

# Check and read arguments
if len(sys.argv) != 4:
	print(sys.argv[0] + ": requires number of democrats, size of committee, and number of repetitions")
	sys.exit()
democrats = int(sys.argv[1])
committee_size = int(sys.argv[2])
repetitions = int(sys.argv[3])

# Calculate expected number of democrats on the committee (question (a))
sum_dems_on_com = 0
for x in range(0, repetitions):
	senate_order = create_partisan_senate(democrats)
	committee = []
	for x in range(0, committee_size):
		committee.append(senate_order[x])
	sum_dems_on_com += committee.count("D")
aver_num_dems = sum_dems_on_com / repetitions
print("If there are " + str(democrats) + " in the senate and the committee size is " +
	str(committee_size) + " then the expected number of democrats on the committee is: " +
	str(aver_num_dems) + " (with " + str(repetitions) + " repetitions)")

# Calculate expected number of states on the committee (question (b)) and expected number of states appearing
# twice (question (c))
sum_states_on_com = 0
sum_states_rep_twice = 0
for x in range(0, repetitions):
	senate_order = create_state_senate()
	committee = []
	for x in range(0, committee_size):
		committee.append(senate_order[x])
	sum_states_on_com += len(set(committee))
	sum_states_rep_twice += check_states(committee)
aver_num_states = sum_states_on_com / repetitions
aver_states_rep_twice = sum_states_rep_twice / repetitions
print("If the committee has " + str(committee_size) + " members, then the expected number of " +
	"states represented is " + str(aver_num_states))
print("The average number of states represented twice is: " + str(aver_states_rep_twice))
	

				
