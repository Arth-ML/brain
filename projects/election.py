## Creat States
## The number population
## eligible to vote of states
## create pre-president
## choose two pre-president among the states
## count on votes in country
## count on votes in  states
## percentage on votes in states

class Brazil():
    def __init__(self): # The only object concrete
        self.states = [] #List containing the states
        self.population = [] #List containing the population

    def add_states(self, states, population):
        self.states.append(states)
        self.population.append(population)

    def __str__(self):
       result = 'States and Population'
       for i in range(len(self.states)):
           return += f'{self.states[i]} - e'
    


if __name__ == '__main__':
    for _ in range(2):
        brazil = Brazil(
        str(input('Whats you states? ')),
        float(input('Enter you population: '))
    )
print(brazil)
