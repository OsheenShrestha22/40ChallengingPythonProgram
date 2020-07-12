import random


class Simulation():

    def __init__(self):
        """Initialize attributes"""

        self.day_number = 1

        # Get simulation initial conditions from the user
        print("To simulate the epidemic outbreak, we must know the population size")
        self.population_size = int(input("Enter the population size:"))

        print("\nWe must start by infecting the portion of the population")
        self.infection_percentage = float(input("------Enter the percentage (0-100) of the population to initially "
                                                "infect:"))
        self.infection_percentage /= 100

        print("\nWe must know the risk a person has to contract the disease when exposed.")
        self.infection_probability = float(input("------Enter the probability (0-100) that a person get infected when "
                                                 "exposed to the disease:"))

        print("\nWe must know how long the infection will last when exposed:")
        self.infection_duration = int(input("----------Enter the duration  in days of the infection: "))

        print("\nWe must know the mortality rate of those infected:")
        self.mortality_rate = float(input("-------------Enter the mortality rate (0-100) of the infection:"))

        print("\nWe must know how long to run the simulation")
        self.sim_days = int(input("------------------Enter the number of days to simulate:"))


class Person():
    """A class to model an individual person in a population"""

    def __init__(self):
        """Initialize attributes"""
        self.is_infected = False  # Person start healthy not infected
        self.is_dead = False  # Person start alive
        self.days_infected = 0  # Keeps track of days infected for individual person

    def infect(self, simulation):
        """Infect a person based on sim conditions"""
        # Random number generated must be less than infection probability to infect
        if random.randint(0, 100) < simulation.infection_probability:
            self.is_infected = True

    def heal(self):
        """Heals a person from infection"""
        self.is_infected = False
        self.days_infected = 0

    def die(self):
        """Kill a person"""
        self.is_dead = True

    def update(self, simulation):
        """Update an individual person if  the person is not dead.Check if they are infected.If they are, increase the days infected count,
        then check if they should die or heal"""
        # Check if the person is not dead before updating
        if not self.is_dead:
            """Check if the person is infected"""
            if self.is_infected:
                self.days_infected += 1
                # Check to see if the person will die
                if random.randint(0, 100) < simulation.mortality_rate:
                    self.die()
                # Check if the infections is over, if it is heal the person
                elif self.days_infected == simulation.infection_duration:
                    self.heal()


class Population():
    """A class to model a whole population of person objects"""
    def __init__(self,simulation):
        self.population =[] # A list to hold all person instances once created
        # Create  the correct number of person instances based on the sim condition
        for i in range(simulation.population_size):
            person = Person()
            self.population.append(person)


    def initial_infection(self,simulation):
        """Infect the initial portion of the population"""
        # The number of people to infect is found by taking the pop size * infection percentage

        # We must round to 0 decimals and cast to an int so we can use infected count in for loop
        infected_count = int(round(simulation.infection_percentage * simulation.population_size,0))

        # Infect the correct number of people
        for i in range(infected_count):
            #Infect the ith person in the population attribute
            self.population[i].is_infected = True
            self.population[i].days_infected = 1
        # Shuffle the population list so we can spread the infection out randomly
        random.shuffle(self.population)

    def spread_infection(self,simulation):
        """Spread the infection to all  adjacent people in the list population"""
        for i in range(len(self.population)):
            # ith person is alive, see if they should be infected.
            # Don't bother infecting a dead person, they are infected and dead
            # Check to see if the adjancent Person in infected or not
            if self.population[i].is_dead == False:
                #i is the first person in the list, can only check to the right [i+1]
                if i == 0:
                    if self.population[i+1].is_infected:
                        self.population[i].infect(simulation)

                #i is in the middle of the list, can check to the left [i-1] and right [i+1]
                elif i < len(self.population)-1:
                    if self.population[i + 1].is_infected or self.population[i-1].is_infected:
                        self.population[i].infect(simulation)

                # i is the last person in the list, can only check to the left[i-1]
                elif i == len(self.population)-1:
                    if self.population[i-1].is_infected:
                        self.population[i].infect(simulation)

    def update(self,simulation):
        """Update the whole population by updating each individual person in the population."""
        simulation.day_number +=1

        #Call the update method for all person instances in the population
        for person in self.population:
            person.update(simulation)

    def display_statistics(self,simulation):
        """Display the current statistics of population"""
        # Initialize values
        total_infected_count = 0
        total_death_count = 0
        # Loop through whole population
        for person in self.population:
            # Person is infected
            if person.is_infected:
                total_infected_count +=1
                # Person is dead
                if person in self.population:
                    total_death_count +=1
        # Calculate percentage of population that is infected and dead
        infected_percent =round(100*(total_infected_count/simulation.population_size),4)
        death_percent = round(100 * (total_death_count / simulation.population_size), 4)

        print(f"\n--------------------Day # {simulation.day_number} ---------------")
        print(f"Percentage of Population Infected: {infected_percent}%")
        print(f"Percentage of Population Death: {death_percent}%")
        print(f"Total people infected: {total_infected_count} / {simulation.population_size}")
        print(f"Total people death: {total_death_count} / {simulation.population_size}")


    def graphics(self):
        """A graphical representation for a population. 0 is healthy, I is infected and x is dead"""
        status = [] # A list to hold all X, I, O to represent the status of each person
        for person in self.population:
            # Person is dead, X
            if person.is_dead:
                char = 'X'
            # Person is alive, are they healthy or infected?
            else:
                # person is infected, I
                if person.is_infected:
                    char = 'I'
                # person is dead, 0
                else:
                    char = '0'

            status.append(char)
        # Print out all status characters separated by -
        for letter in status:
            print(letter,end='-')


# The main code
# Create a simulation and population object
sim = Simulation()
pop = Population(sim)

#Set the initial infection conditions of the population
pop.initial_infection(sim)
pop.display_statistics(sim)
pop.graphics()
input("\n Press Enter to begin the simulation")

#Run the simulation
for i in range (1,sim.sim_days):
    # For a single day, spread the infection, update the population, display statistic and graph
    pop.spread_infection(sim)
    pop.update(sim)
    pop.display_statistics(sim)
    pop.graphics()

    # If it is not the last day of simulation, pause the progran
    if i != sim.sim_days -1:
        input("\nPress enter to advance to the next day.")