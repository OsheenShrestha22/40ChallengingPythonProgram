import random
import math
import tkinter

class Simulation():

    def __init__(self):
        """Initialize attributes"""

        self.day_number = 1

        # Get simulation initial conditions from the user
        print("To simulate the epidemic outbreak, we must know the population size")
        self.population_size = int(input("Enter the population size:"))

        # Convert users population size to the nearest perfect square for visual purposes
        root = math.sqrt(self.population_size)
        #For eg,if the population size is 79, root = 8.8881

        # User did not enter a perfect square for the population
        if int(root + .5)**2 != self.population_size:
            #int(8.8881 + .5)**2 =int(9.3881)**2 = 9**2 = 81! = 79
            root = round(root,0)
            # round(8.881,0) = 9.0
            self.grid_size = int(root)
            #grid_size = 9
            self.population_size = self.grid_size **2
            #population size = 9*9 = 82
            print(f"Rounding population size to {self.population_size} for visual purposes")

        # The user did enter a perfect square for the population
        else:
            self.grid_size = int(math.sqrt(self.population_size))

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
    """A class  to model  a whole population of Person objects"""
    def __int__(self,simulation):
        """Initialize attributes"""
        # This will be a list of N lists, where n is a simulation grid size.
        # Each list within the list will represent a row in an NXN grid
        # Each element of the row will represent an individual person object.
        # Each of these lists will hold N person objects and there will be N lists
        self.population = [] # A list to hold all the persons in the population

        # Loop through the needed number of rows
        for i in range(simulation.grid_size):
            row = []
            # Loop through the needed number of Person objects for each row
            for j in range(simulation.grid_size):
                person = Person()
                row.append(person)


    def initial_infection(self,simulation):
        """Infect the initial portion of the population based on the initial condition of sim"""
        # Infect the infection percentage * population size gives the total number to infect
        # We must round to 0 decimals and cast to an int so we can use infected count in for loop
        infected_count = int(round(simulation.infection_percentage * simulation.population_size,0))
        infections = 0
        # Infect the population until you have infected correct starting amount
        while infections < infected_count:
            # X is a random row in the population, y is the random person in a random row
            # self.population [x][y] represents the random person in the population list
            x= random.randint(0,simulation.grid_size-1)
            y= random.randint(0, simulation.grid_size - 1)

            # If the person is not infected, infect them!!
            if not self.population[x][y].is_infected:
                self.population[x][y].is_infected = True
                self.population[x][y].days_infected = 1
                infections +=1

        # Shuffle the population list so we can spread the infection out randomly
        random.shuffle(self.population)

    def update(self,simulation):
        """Update the whole population by updating each individual person in the population."""
        simulation.day_number +=1
        # Loop through the population to access each row
        for person in self.population:
            # Loop through the row to update each person
            person.update(simulation)

    def spread_infection(self,simulation):
        """Spread the infection in a 2D array to all adjacent people to a given person.
        A given person in the population attribute is referenced as self.population[i][j]
        A person to the right of the given person is referenced as self.population[i][j+1]
        A person to the left of the given person is referenced as self.population[i][j-1]
        A person below the given person is referenced as self.population[i+1][j]
        A person above the given person is referenced as self.population[i-1][j]"""

        # Loop through all rows of the population
        for i in range(simulation.grid_size):
            # Loop through all the person objects in the given row
            for j in range(simulation.grid_size):
                # Check to see if this given person self.population[i][j] is not dead
                if self.population[i][j].is_dead == False:
                    # We will try to infect the given person if an adjacent person is already infected
                    # If i == 0, we are in the first row
                    if i == 0:
                        # If j == 0, we are in the first column so we can't look left.
                        if j == 0:
                            if self.population[i][j+1].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(simulation)

                            # If we are in the last column, we can't look right
                            elif j ==simulation.grid_size-1:
                                if self.population[i][j-1].is_infected or self.population[i+1][j].is_infected:
                                    self.population[i][j].infect(simulation)

                            # If we are in any other column, we can look left, right or below
                            else:
                                if self.population[i][j-1].is_infected or self.population[i][j+1].is_infected or self.population[i+1][j].is_infected:
                                    self.population[i][j].infect(simulation)

                    # IF i == simulation.grid_size-1 we are in the last row,so we can't look below
                    elif i == simulation.grid_size-1:
                        # If j == 0, we are in the first column so we can't look left.
                        if j == 0:
                            if self.population[i][j+1].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(simulation)

                            # If we are in the last column, we can't look right
                            elif j == simulation.grid_size-1:
                                if self.population[i][j-1].is_infected or self.population[i-1][j].is_infected:
                                    self.population[i][j].infect(simulation)

                            # If we are in any other column, we can look left, right or above
                            else:
                                if self.population[i][j-1].is_infected or self.population[i][j+1].is_infected or self.population[i-1][j].is_infected:
                                    self.population[i][j].infect(simulation)
                    # Otherwise we are in a row in between, we can look left, right, above or below
                    else:
                        # If j == 0, we are in the first column so we can't look left.
                        if j == 0:
                            if self.population[i][j+1].is_infected or self.population[i+1][j].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(simulation)

                            # If we are in the last column, we can't look right
                            elif j == simulation.grid_size - 1:
                                if self.population[i][j-1].is_infected or self.population[i+1][j].is_infected or self.population[i-1][j].is_infected:
                                    self.population[i][j].infect(simulation)

                            # If we are in any other column, we can look left, right or above or below
                            else:
                                if self.population[i][j - 1].is_infected or self.population[i][j + 1].is_infected or self.population[i+1][j].is_infected or self.population[i-1][j].is_infected:
                                    self.population[i][j].infect(simulation)






    def display_statistics(self,simulation):
        """Display the current statistics of population"""
        # Initialize values
        total_infected_count = 0
        total_death_count = 0
        # Loop through whole population to access each row
        for row in self.population:
            #Loop through the row to access each person
            for person in row:
                # Person is infected
                if person.is_infected:
                    total_infected_count +=1
                    # Person is dead
                    if person in self.population:
                        total_death_count +=1

        # Calculate percentage of population that is infected and dead
        infected_percent =round(100*(total_infected_count/simulation.population_size),4)
        death_percent = round(100 * (total_death_count / simulation.population_size), 4)

        # Statistics summary
        print(f"\n--------------------Day # {simulation.day_number} ---------------")
        print(f"Percentage of Population Infected: {infected_percent}%")
        print(f"Percentage of Population Death: {death_percent}%")
        print(f"Total people infected: {total_infected_count} / {simulation.population_size}")
        print(f"Total people death: {total_death_count} / {simulation.population_size}")


    # A helper function to create graphics
    def graphics(simulation,population,canvas):
        """A helper function to update the display"""
        # Get the dimensions of an individual square in a grid
        # Each square represents a person in the populaiton
        # Use 600 for a GUI window that is 600*600, changed if desired
        # To get the dimension of the square take the dimensions of the window and divide by the total number
        square_dimension = 600//simulation.grid_size

        # Loop through all rows in the population
        for i in range(simulation.grid_size):
            y = i* square_dimension
            # Loop through all person in the row
            for j in range(simulation.grid_size):
                x= j * square_dimension

                # Check to see if the given person is dead
                if population.population[i][j].is_dead:
                    # Create a red square at the correct position
                    canvas.create_rectangle(x,y,x+square_dimension, y+square_dimension, fill= 'red')
                # The current person is not dead, check if they are infected or healthy
                else:
                    if population.population[i][j].is_infected:
                        # Create a yellow square at the correct location
                        canvas.create_rectangle(x,y,x+square_dimension,y+square_dimension, fill='yellow')
                    else:
                        canvas.create_rectangle(x, y, x + square_dimension, y + square_dimension, fill='green')



# The main code
# Create a simulation object
sim = Simulation()

# Create a constant variable for window size
window_width = 600
window_height = 600

# Create a tkninter window and canvas
sim_window =  tkinter.Tk()
sim_window.title("Epidemic Outbreak")
sim_canvas = tkinter.Canvas(sim_window, width =window_width,height= window_height,bg='lightblue')
sim_canvas.pack(side=tkinter.LEFT)

#Create a population object
pop = Population(sim)

#Set the initial conditions of the population
pop.initial_infection(sim)
pop.display_statistics(sim)
input("Press Enter to begin Simulation")


#Run the simulation
for i in range(1,sim.sim_days):
    pop.spread_infection(sim)
    pop.update(sim)
    pop.display_statistics(sim)
    graphics(sim, pop, sim_canvas)

    #Update the tkinter window to enter the graphics changes
    sim_window.update()

    #If we are currently not on the last day of the simulation, wipe the  canvas clean
    if i != sim.sim_days-1:
        sim_canvas.delete('all')



