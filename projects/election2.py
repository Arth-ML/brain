
# ##Create of states
# Created electoral system
# Created a system for choosing the president
# Containing votes for countrt and states 

import random

class Brazil:

    def __init__(self):
        self.states = {}
        self.VoteElection = {}  # Testing vote separation
        self.voteCountry = {} # list containing votes sum the country
        self.Cpresident = {} # Created for dicionary the president
        self.candidates = [] #The list containig candidates
        self.country = [] #List containing votes the country


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

    def count(self, votes, votes_country_president1, votes_country_president2):
         self.voteCountry[votes] = {
              'total votes president 1': votes_country_president1,
              'total votes president 2': votes_country_president2
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
        votes_country = '\n'.join(
             f'Vote the canditate 1 {value['total votes president 1']: .6f}; Vote the canditate 2: {value['total votes president 2']}'
             for key, value in self.voteCountry.items()
        )

        return f"{state_info}\n\n{test_info}\n\n{president_info}\n\n{votes_country}"


if __name__ == '__main__':
    brasil = Brazil()
    n = 2

    for i in range(n):
        state = str(input('What is your state: '))
        population = float(input('What is the population of the state: '))
        candidate = str(input('Who is the candidate your states: '))


        brasil.candidates.append(candidate)


        vote = float(population * random.random())
        valid_votes = float(population * random.random())
        valid_votes_two = float((population - valid_votes) * random.random())
        
        brasil.country.append(valid_votes)
        brasil.country.append(valid_votes_two)

        president_one = random.choice(candidate)
        president_two = random.choice(candidate)

        votes_country_president1 = sum(info['President'] for info in brasil.VoteElection.values())
        votes_country_president2 = sum(info['President_two'] for info in brasil.VoteElection.values())
      

        brasil.add_states(state, population, vote, candidate )
        brasil.Election(state, valid_votes, valid_votes_two)
        brasil.count("", votes_country_president1, votes_country_president2)
        # brasil.test('test votes', t)
       


        if len(brasil.candidates) >= 2:
             president_one, president_two = random.sample(brasil.candidates, 2)
             brasil.presidented('Candidate choosing', president_one, president_two)
        

        

      

    print('Info of states:')
    print(brasil)
