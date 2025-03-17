
# ##Create of states
# Created electoral system
# Created a system for choosing the president

import random

class Brazil:

    def __init__(self):
        self.states = {}
        self.VoteElection = {}  # Testing vote separation
        self.Cpresident = {} # Created for dicionary the president
        self.candidates = [] #The list containig candidates


    def add_states(self, state, population, vote, candidate): ## Add population and votes
            self.states[state] = {
                'Population': population,
                'Vote': vote,
                'Candidate': candidate
             }

    def presidented(self,president,  president_one, president_two):
        self.Cpresident[president] = {
            'President_One': president_one,
            'President_two': president_two
        }
    
        
    def Election(self, state, valid_votes, valid_votes_two):
         self.VoteElection[state] = {
              'President': valid_votes,
              'President_two': valid_votes_two
         }

    def __str__(self):
        state_info = '\n'.join(
            f"State: {state}; Population: {info['Population']: .6f}; Vote: {info['Vote']:.5f}; Candidate: {info['Candidate']}" 
            for state, info in self.states.items()
        )
        test_info = '\n'.join(
            f"State: {state}; President votes: {info['President']: .6f}; President two: {info['President_two']: .6f}" 
            for state, info in self.VoteElection.items()
        )
        president_info = '\n'.join(
            f'The candidate for president: {value["President_One"]} and {value["President_two"]}'
            for key, value in self.Cpresident.items()
            )

        return f"{state_info}\n\n{test_info}\n\n{president_info}"


if __name__ == '__main__':
    brasil = Brazil()
    n = 5

    for i in range(n):
        state = str(input('What is your state: '))
        population = float(input('What is the population of the state: '))
        candidate = str(input('Who is the candidate your states: '))


        brasil.candidates.append(candidate)


        vote = float(population * random.random())
        valid_votes = float(population * random.random())
        valid_votes_two = float((population - valid_votes) * random.random())


        president_one = random.choice(candidate)
        president_two = random.choice(candidate)
      

        brasil.add_states(state, population, vote, candidate )
        brasil.Election(state, valid_votes, valid_votes_two)
       


        if len(brasil.candidates) >= 2:
             president_one, president_two = random.sample(brasil.candidates, 2)
             brasil.presidented('Candidate choosing', president_one, president_two)

    print('Info of states:')
    print(brasil)
