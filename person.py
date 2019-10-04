import random
random.seed(42)
from virus import Virus


class Person(object):
    ''' Person objects will populate the simulation. '''

    def __init__(self, _id, is_vaccinated, infection=None):
        ''' We start out with is_alive = True, because we don't make vampires or zombies.
        All other values will be set by the simulation when it makes each Person object.

        If person is chosen to be infected when the population is created, the simulation
        should instantiate a Virus object and set it as the value
        self.infection. Otherwise, self.infection should be set to None.
        '''
        self._id = _id # int
        self.is_alive = True  # boolean
        self.is_vaccinated = is_vaccinated # boolean
        self.infection = infection  # Virus object or None

    def did_survive_infection(self): #method that returns True if Person's immunity is higher than virus's mortality rate
        if self.infection == None:
            return
        random_num = random.randint(1,100)
        if random_num < self.infection.mortality_rate:
            return False
        return True



############################################## PERSON TESTS ##############################################
def test_vacc_person_instantiation():
    # create some people to test if our init method works as expected
    person = Person(1, True)
    assert person._id == 1
    assert person.is_alive is True
    assert person.is_vaccinated is True
    assert person.infection is None

    kid = Person(123, True)
    assert kid._id == 123
    assert kid.is_alive is True
    assert kid.is_vaccinated is True
    assert kid.infection is None


def test_not_vacc_person_instantiation():
    person = Person(2, False)
    assert person._id == 2
    assert person.is_alive is True
    assert person.is_vaccinated is False
    assert person.infection is None

    kid = Person(123, False)
    assert kid._id == 123
    assert kid.is_alive is True
    assert kid.is_vaccinated is False
    assert kid.infection is None


def test_sick_person_instantiation():
    virus = Virus("Dysentery", 0.7, 0.2)
    person = Person(3, False, virus) #person with the virus
    assert person._id == 3
    assert person.is_alive is True
    assert person.is_vaccinated is False
    assert person.infection is virus
    assert person.infection.name is "Dysentery"
    assert person.infection.repro_rate is 0.7
    assert person.infection.mortality_rate is 0.2

    hiv = Virus("HIV", 0.8, 0.3)
    kid = Person(123, False, hiv)
    assert kid._id == 123
    assert kid.is_alive is True
    assert kid.is_vaccinated is False
    assert kid.infection is hiv
    assert kid.infection.name == "HIV"
    assert kid.infection.repro_rate is 0.8
    assert kid.infection.mortality_rate is 0.3

def test_did_survive_infection():
    # TODO: Create a Virus object to give a Person object an infection
    virus = Virus("Dysentery", 0.7, 0.2)
    # TODO: Create a Person object and give them the virus infection
    person = Person(4, False, virus)

    # Resolve whether the Person survives the infection or not
    survived = person.did_survive_infection()
    # Check if the Person survived or not
    if survived:
        assert person.is_alive is True
        # TODO: Write your own assert statements that test
        # the values of each attribute for a Person who survived
        # assert ...
    else:
        assert person.is_alive is False
        # TODO: Write your own assert statements that test
        # the values of each attribute for a Person who did not survive
        # assert ...
        pass



if __name__ == "__main__":
    test_vacc_person_instantiation()
    test_not_vacc_person_instantiation()
    test_sick_person_instantiation()