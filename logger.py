class Logger(object):
    ''' Utility class responsible for logging all interactions during the simulation. '''
    # TODO: Write a test suite for this class to make sure each method is working
    # as expected.

    # PROTIP: Write your tests before you solve each function, that way you can
    # test them one by one as you write your class.

    def __init__(self, file_name):
        # TODO:  Finish this initialization method.  The file_name passed should be the
        # full file name of the file that the logs will be written to.
        self.file_name = file_name
        self.saved_by_vaccine = 0

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        '''
        The simulation class should use this method immediately to log the specific
        parameters of the simulation as the first line of the file.
        '''
        # TODO: Finish this method. This line of metadata should be tab-delimited
        # it should create the text file that we will store all logs in.
        # TIP: Use 'w' mode when you open the file. For all other methods, use
        # the 'a' mode to append a new log to the end, since 'w' overwrites the file.
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        f = open(self.file_name, "w")
        answers = open("answers.txt", "w")

        f.write("Population Size: {} \tPercentage Vaccinated: {} \tVirus Name: {} \tMortality Rate {} \tVirus Reproduction Rate: {}".format(pop_size, vacc_percentage, virus_name, mortality_rate,
                           basic_repro_num))

        answers.write("Population Size: {} \tPercentage Vaccinated: {} \tVirus Name: {} \tMortality Rate {} \tVirus Reproduction Rate: {}".format(pop_size, vacc_percentage, virus_name, mortality_rate,
                           basic_repro_num))

    def log_interaction(self, person1, person2, did_infect=None,
                        person2_vacc=None, person2_sick=None):
        '''
        The Simulation object should use this method to log every interaction
        a sick person has during each time step.
        The format of the log should be: "{person.ID} infects {random_person.ID} \n"
        or the other edge cases:
            "{person.ID} didn't infect {random_person.ID} because {'vaccinated' or 'already sick'} \n"
        '''
        # TODO: Finish this method. Think about how the booleans passed (or not passed)
        # represent all the possible edge cases. Use the values passed along with each person,
        # along with whether they are sick or vaccinated when they interact to determine
        # exactly what happened in the interaction and create a String, and write to your logfile.
        f = open(self.file_name, "a")

        f.write("\nInfected Person: #{} \nExposed Person #{}".format(person1._id, person2._id))

        if did_infect == True:
            f.write("\nPerson #{} was infected by person #{}".format(person2._id, person1._id))
        elif person2_vacc == True:
            self.saved_by_vaccine += 1
            f.write("\nPerson #{} is vaccinated against the infection.".format(person2._id))
        elif person2_sick == True:
            f.write("\nPerson #{} is already infected.".format(person2._id))
        else:
            f.write("\nPerson #{} did not get infected by person #{}".format(person2._id, person1._id))

    def log_infection_survival(self, person, did_die_from_infection):
        ''' The Simulation object uses this method to log the results of every
        call of a Person object's .resolve_infection() method.
        The format of the log should be:
            "{person.ID} died from infection\n" or "{person.ID} survived infection.\n"
        '''
        # TODO: Finish this method. If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile
        f = open(self.file_name, "a")

        f.write("\nDid person #{} survive the infection?: {}".format(person._id, person.did_survive_infection()))
        if person.is_alive == True:
            did_die_from_infection = False
            f.write("\nPerson #{} survived infection.".format(person._id))
        else:
            did_die_from_infection = True
            f.write("\nPerson #{} died from infection.".format(person._id))

    def log_time_step(self, time_step_number):
        ''' STRETCH CHALLENGE DETAILS:

        If you choose to extend this method, the format of the summary statistics logged
        are up to you.

        At minimum, it should contain:
            The number of people that were infected during this specific time step.
            The number of people that died on this specific time step.
            The total number of people infected in the population, including the newly infected
            The total number of dead, including those that died during this time step.

        The format of this log should be:
            "Time step {time_step_number} ended, beginning {time_step_number + 1}\n"
        '''
        # TODO: Finish this method. This method should log when a time step ends, and a
        # new one begins.
        # NOTE: Here is an opportunity for a stretch challenge!
        f = open(self.file_name, "a")

        f.write("\nTime step #{} ended, beginning time step #{}.".format(time_step_number, time_step_number + 1))

    def stats(self, population, total_infected):
        total_dead = 0
        for person in population:
            if person.is_alive == False:
                total_dead += 1
            else:
                pass
        print("The total number of infected is {}".format(total_infected))
        print("The total number of dead is {}.".format(total_dead))

        answers = open("answers.txt", "a")
        answers.write("\nThe percentage of total infected for this simulation was {}% \nThe percentage of total dead for this simulation was {}% \nThe number of times someone was potentially saved because they were already vaccinated is {}".format(total_infected/len(population) * 100, total_dead/len(population) * 100, self.saved_by_vaccine))
