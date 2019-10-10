import random, sys

random.seed(42)

from person import Person
from logger import Logger
from virus import Virus

class Simulation(object):
    ''' Main class that will run the herd immunity simulation program.
    Expects initialization parameters passed as command line arguments when file is run.
    Simulates the spread of a virus through a given population.  The percentage of the
    population that are vaccinated, the size of the population, and the amount of initially
    infected people in a population are all variables that can be set when the program is run.
    '''

    def __init__(self, population_size, vacc_percentage, virus_name,
                 mortality_rate, basic_repro_num, initial_infected=1):
        
        ''' Logger object logger records all events during the simulation.
        Population represents all Persons in the population.
        The next_person_id is the next available id for all created Persons,
        and should have a unique _id value.
        The vaccination percentage represents the total percentage of population
        vaccinated at the start of the simulation.
        You will need to keep track of the number of people currently infected with the disease.
        The total infected people is the running total that have been infected since the
        simulation began, including the currently infected people who died.
        You will also need to keep track of the number of people that have die as a result
        of the infection.

        All arguments will be passed as command-line arguments when the file is run.
        HINT: Look in the if __name__ == "__main__" function at the bottom.
        '''
        # TODO: Create a Logger object and bind it to self.logger.
        # Remember to call the appropriate logger method in the corresponding parts of the simulation.
        # TODO: Call self._create_population() and pass in the correct parameters.
        # Store the array that this method will return in the self.population attribute.
        # TODO: Store each newly infected person's ID in newly_infected attribute.
        # At the end of each time step, call self._infect_newly_infected()
        # and then reset .newly_infected back to an empty list.

        self.population_size = population_size
        self.population = []
        self.total_infected = 0
        self.current_infected = 0
        self.next_person_id = 0
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected
        self.virus = virus
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus_name, population_size, vacc_percentage, initial_infected)

        self.logger = Logger(self.file_name)
        self.logger.write_metadata(population_size, vacc_percentage, virus.name, virus.mortality_rate, virus.basic_repro_num)
        self.newly_infected = []

        self.population += self._create_population(initial_infected)
        print(self.population_size)

    def _create_population(self, initial_infected):
        '''This method will create the initial population.
            Args:
                initial_infected (int): The number of infected people that the simulation
                will begin with.
            Returns:
                list: A list of Person objects.
        '''
        # TODO: Finish this method!  This method should be called when the simulation
        # begins, to create the population that will be used. This method should return
        # an array filled with Person objects that matches the specifications of the
        # simulation (correct number of people in the population, correct percentage of
        # people vaccinated, correct number of initially infected people).

        # Use the attributes created in the init method to create a population that has
        # the correct intial vaccination percentage and initial infected.
        print("running _create_population")
        population = []
        infected_count = 0
        while len(population) != self.population_size:
            # to do : Create all the infected people first, and then worry about the rest.
            # Don't forget to increment infected_count every time you create a
            # new infected person!
            if infected_count != initial_infected:
                infected_person = Person(self.next_person_id, is_vaccinated=False, infection=self.virus)
                self.population.append(infected_person)
                infected_count += 1
                self.next_person_id += 1
            else:
                # Now create all the rest of the people.
                # Every time a new person will be created, generate a random number between
                # 0 and 1.  If this number is smaller than vacc_percentage, this person
                # should be created as a vaccinated person. If not, the person should be
                # created as an unvaccinated person.
                should_be_vacc = random.uniform(0, 1)
                if should_be_vacc < self.vacc_percentage:
                    vacc_person = Person(self.next_person_id, is_vaccinated=True, infection=None)
                    population.append(vacc_person)
                    self.next_person_id += 1
                else:
                    unvacc_person = Person(self.next_person_id, is_vaccinated=False, infection=None)
                    population.append(unvacc_person)
                    self.next_person_id += 1
            # to do : After any Person object is created, whether sick or healthy,
            # you will need to increment self.next_person_id by 1. Each Person object's
            # ID has to be unique!
        return population

    def _simulation_should_continue(self):
        ''' The simulation should only end if the entire population is dead
        or everyone is vaccinated.
            Returns:
                bool: True for simulation should continue, False if it should end.
        '''
        # TODO: Complete this helper method.  Returns a Boolean.

        # check all objects in list; check is_alive attribute of each object if True or False
        print("running _simulation_should_continue")
        someone_still_alive = False
        someone_still_infected = False
        for person in self.population:
            if person.is_alive == True:
                someone_still_alive = True
            # else:
            #     pass
            if person.infection != None:
                someone_still_infected = True
            # else:
            #     pass
        if someone_still_infected and someone_still_infected:
            return True
        else:
            return False


    def run(self):
        ''' This method should run the simulation until all requirements for ending
        the simulation are met.
        '''
        # TODO: Finish this method.  To simplify the logic here, use the helper method
        # _simulation_should_continue() to tell us whether or not we should continue
        # the simulation and run at least 1 more time_step.

        # TODO: Keep track of the number of time steps that have passed.
        # HINT: You may want to call the logger's log_time_step() method at the end of each time step.
        # TODO: Set this variable using a helper
        print("running run")
        time_step_counter = 0
        
        should_continue = self._simulation_should_continue()
        print(should_continue)
        while should_continue:
            # TODO: for every iteration of this loop, call self.time_step() to compute another
            # round of this simulation.
            self.time_step()
            time_step_counter += 1
            print(time_step_counter)
            self.logger.log_time_step(time_step_counter)
            should_continue = self._simulation_should_continue()
            print(should_continue)
        print('The simulation has ended after {} time steps.'.format(time_step_counter))
        self.logger.stats(self.population, self.total_infected)

    def choose_random_person(self):
        choose_person = random.choice(self.population)
        while choose_person.is_alive == False:
            choose_person = random.choice(self.population)
        return choose_person

    def time_step(self):
        ''' This method should contain all the logic for computing one time step
        in the simulation.

        This includes:
            1. 100 total interactions with a randon person for each infected person
                in the population
            2. If the person is dead, grab another random person from the population.
                Since we don't interact with dead people, this does not count as an interaction.
            3. Otherwise call simulation.interaction(person, random_person) and
                increment interaction counter by 1.
            '''
        # TODO: Finish this method.
        print("running time_step")
        for person in self.population:
            if person.infection is not None and person.is_alive == True:
                print("doing time step")
                interaction_counter = 0
                while interaction_counter < 100:
                    random_person = self.choose_random_person()
                    if random_person.is_alive == False:
                        continue
                    elif random_person._id == person._id:
                        continue
                    else:
                        self.interaction(person, random_person)
                        interaction_counter += 1
                        print(interaction_counter)
        for person in self.population:
            if person.infection is not None and person.is_alive == True:
                self.logger.log_infection_survival(person, False)
            # else:
            #     print("Time step complete.")
        self._infect_newly_infected()

    def interaction(self, person, random_person):
        '''This method should be called any time two living people are selected for an
        interaction. It assumes that only living people are passed in as parameters.
        Args:
            person1 (person): The initial infected person
            random_person (person): The person that person1 interacts with.
        '''
        # Assert statements are included to make sure that only living people are passed
        # in as params
        assert person.is_alive == True
        assert random_person.is_alive == True

        # TODO: Finish this method.
        #  The possible cases you'll need to cover are listed below:
            # random_person is vaccinated:
            #     nothing happens to random person.
            # random_person is already infected:
            #     nothing happens to random person.
            # random_person is healthy, but unvaccinated:
            #     generate a random number between 0 and 1.  If that number is smaller
            #     than repro_rate, random_person's ID should be appended to
            #     Simulation object's newly_infected array, so that their .infected
            #     attribute can be changed to True at the end of the time step.
        # TODO: Call slogger method during this method.

        if random_person.is_vaccinated == True:
            self.logger.log_interaction(person, random_person, did_infect=None, person2_vacc=True, person2_sick=None)
        elif random_person.infection != None:
            self.logger.log_interaction(person, random_person, did_infect=None, person2_vacc=None, person2_sick=True)
        else:
            random_number = random.uniform(0,1)
            if random_number < basic_repro_num:
                self.newly_infected.append(random_person._id)
                self.logger.log_interaction(person, random_person, did_infect=True, person2_vacc=None, person2_sick=None)
            else:
                self.logger.log_interaction(person, random_person, did_infect=False, person2_vacc=None, person2_sick=None)

    def _infect_newly_infected(self):
        ''' This method should iterate through the list of ._id stored in self.newly_infected
        and update each Person object with the disease. '''
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        
        for id in self.newly_infected:
            # then search the population list for that person
            for person in self.population:
                # make sure that the IDs match
                if person._id == id:
                    # then infect them with the virus; .infected attribute cannot be set to True
                    person.infection = self.virus
        print(self.newly_infected)
        newly_infected_set = set(self.newly_infected)
        print("this is the set {}".format(newly_infected_set))
        # input("just stopping to let you see result.")
        # need to set total infected number
        self.total_infected += len(newly_infected_set)
        print("current total infected {}".format(self.total_infected))
        # input("stopping again to let you see")

        # clear out the newly infected list
        self.newly_infected = []


if __name__ == "__main__":
    
    params = sys.argv[1:]
    population_size = int(params[0])
    vacc_percentage = float(params[1])
    virus_name = str(params[2])
    mortality_rate = float(params[3])
    basic_repro_num = float(params[4])

    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1

    virus = Virus(virus_name, mortality_rate, basic_repro_num)
    simulation = Simulation(population_size, vacc_percentage, virus.name, virus.mortality_rate,
                            virus.basic_repro_num, initial_infected)
    simulation.run()
