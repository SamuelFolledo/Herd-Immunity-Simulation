from virus import Virus
from person import Person

class Logger(object):
    ''' Utility class responsible for logging all interactions during the simulation. '''
    # TODO: Write a test suite for this class to make sure each method is working
    # as expected.

    # PROTIP: Write your tests before you solve each function, that way you can
    # test them one by one as you write your class.

    def __init__(self, file_name):
        # TODO:  Finish this initialization method. The file_name passed should be the
        # full file name of the file that the logs will be written to.
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num):
        '''
        The simulation class should use this method immediately to log the specific
        parameters of the simulation as the first line of the file.
        '''
        # TODO: Finish this method. This line of metadata should be tab-delimited
        # it should create the text file that we will store all logs in.
        # TIP: Use 'w' mode when you open the file. For all other methods, use
        # the 'a' mode to append a new log to the end, since 'w' overwrites the file.
        # NOTE: Make sure to end every line with a '\n' character to ensure that each
        # event logged ends up on a separate line!

        log_file = open(self.file_name, "w+") #over WRITE
        log_file.write(f"Population size = {pop_size}\tVaccine Percentage = {vacc_percentage}\tVirus Name = {virus_name}\tMortality Rate = {mortality_rate}\tBasic Reprodution Number = {basic_repro_num}\n")
        log_file.close()


    def log_interaction(self, person, random_person, random_person_sick=None,
                        random_person_vacc=None, did_infect=None): #removed did_infect=  None
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
        if random_person.infection != None and random_person.infection == person.infection: #if random person has sickness and infection is the same as the person's infection, then we don't infect the random_person again
            print(f"\t{person._id} didn't infect {random_person._id} because already sick\n")
            return
        elif random_person.is_vaccinated == True:
            print(f"\t{person._id} didn't infect {random_person._id} because vaccinated\n")
            return
        else: #if user is not sick and not vaccinated, then infect
            random_person.infection = person.infection
            did_survive = self.log_infection_survival(random_person)
            return did_survive

    def log_infection_survival(self, person):
        ''' The Simulation object uses this method to log the results of every
        call of a Person object's .resolve_infection() method.

        The format of the log should be:
            "{person.ID} died from infection\n" or "{person.ID} survived infection.\n"
        '''
        # TODO: Finish this method. If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile
        if person.did_survive_infection():
            print(f"\t{person._id} survived infection\n")
            return True
        else:
            print(f"\t{person._id} died from infection\n")
            return False

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


       

        fd2 = open(self.file_name, "r+")
        print(fd2.read(100))
        fd2.write(" IS")
        fd2.close()
        pass

def test_log_interaction():
    hiv = Virus("HIV", 0.8, 0.8) #virus with 0.8 mortality rate, so it shouldn't make the random person sick
    person = Person(1, False, hiv)
    random_person = Person(2, False)
    log = Logger("kkk.txt")
    print(f"Result is {log.log_interaction(person, random_person)}")


if __name__ == "__main__":
    # log = Logger("logs.txt")
    # log.log_time_step(2)

    test_log_interaction()