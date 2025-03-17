## Creat States
## The number population
## eligible to vote of states
## create pre-president
## choose two pre-president among the states
## count on votes in country
## count on votes in  states
## percentage on votes in states

import random

class Brazil():
    def __init__(self): # The only object concrete
      self.states = {} ## The dicionary contaning the states and population
      self.voteStates = {} #Dicionary containing the president´s votes in the states
      self.votesCountry = {}
      self.president = {}

    def add_state(self, state, population):
        self.states[state] = {
            'Population': population, 
            # 'Vote': vote, 
            # 'President': president
        } #Add two parameter containing populaton, vote, president


    def pre_president(self, presidented) : #function that chooses two presidents
        self.pre_president[presidented] = presidented



    def votes_states(self, president, vote):

        self.voteStates[president] = {
            'President': president, 
            'Vote in states': vote
        }

    def votes_country(self, country, vote):
        self.votesCountry[country] = {
            'Country': country,
            'Vote of country': vote
        }



    # def  __str__(self): ## The function is returning an error because the method can only return a single string
    #     return '\n'.join(
    #         f'{president}: Votes of country: {info["Vote in states"]:.4f}' for president, info in self.voteStates.items()
    #     ), '\n'.join(
    #         f'{state}: Population: {population}' for state, population in self.states.items()
    #     )

    def __str__(self): ##The special function that returns two varible
            states_info = '\n'.join(
                f'{state}: Population: {info["Population"]:.4f}' for state, info in self.states.items()
            )
            votes_info = '\n'.join(
                f'{president}: Votes of state: {info["Vote in states"]:.4f}' for president, info in self.voteStates.items()
            )
            country_info = '\n'.join(
                f'{president}: Votes of country:{info['Vote of country']:.4f}' for president, info in self.votesCountry.items()
            )
            return f"{states_info} {votes_info } {country_info}"
    



if __name__ == '__main__':
    brasil = Brazil()
    brasil_election = Brazil()
    brasil_country = Brazil()
    brasil_chooses = Brazil()
    n_states = 3


    for i in range(n_states):
        state = str(input('Enter your states: '))

        population = float(input('Enter your population: '))

        vote = float(population * random.random())

        president = str(input('Whicht your president on you state: '))

        

        country =+ population

        brasil.add_state(state, population)

        brasil_election.votes_states(president, vote)

        brasil_country.votes_country(country, vote)



        
    print('Info of states')
    print(brasil_election)
    print(brasil_country)
 
    



