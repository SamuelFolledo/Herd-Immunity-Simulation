import pytest
import person
import virus

""" Tests for the Person class in Herd Immunity """


def test_person_init():
    exposed_person = person.Person(12, is_vaccinated=False, infection=None)

    assert exposed_person._id == 12
    assert exposed_person.is_vaccinated == False
    assert exposed_person.infection == None

def test_did_survive_infection_certain_death():
    # mortality rate is impossibly high, so exposed_person2 should always die
    new_virus = virus.Virus("new_virus", 1.01, 1.01)
    exposed_person2 = person.Person(34, is_vaccinated=False, infection=new_virus)

    assert new_virus.name == "new_virus"
    assert new_virus.mortality_rate == 1.01
    assert new_virus.repro_rate == 1.01

    assert exposed_person2._id == 34
    assert exposed_person2.is_vaccinated == False
    assert exposed_person2.infection == new_virus
# unsure how to implement this test; trying to make sure that did_survive_infection() returns a value
    assert exposed_person2.did_survive_infection() == False
    assert exposed_person2.is_alive == False



def test_is_alive():
    # written while pair coding with Nolan
    test_person = person.Person(22, is_vaccinated=False,)
    print(test_person)
    assert test_person.is_alive == True
    assert test_person.infection == None

def test_infection():
    # written while pair coding with Nolan
    test_virus = virus.Virus("supervirus", 2.00, 2.00)
    infected_person = person.Person(49, is_vaccinated=False, infection=test_virus)
    # testing to make sure that the virus object that is on the parameter infection is indeed an object
    assert isinstance(infected_person.infection, virus.Virus)

def test_vaccionation():
    vacc_person = person.Person(12, is_vaccinated=True, infection=None)
    unvacc_person = person.Person(99, is_vaccinated=False, infection=None)
    # make sure that the correct people are vaccinated
    assert vacc_person.is_vaccinated == True
    assert unvacc_person.is_vaccinated == False

# written while pair coding with Nolan; relevant to his code not mine
# def test_uninfected_does_nothing():
#     uninfected = person.Person(65, is_vaccinated=True, infection=None)
#     assert uninfected.did_survive_infection() == None

def test_infected_did_survive_infection():
    weak_virus = virus.Virus("weak virus", -1.0, -1.0)
    print(weak_virus.name)
    print(weak_virus)
    print(weak_virus.mortality_rate)
    survivor = person.Person(0, is_vaccinated=False, infection=weak_virus)
    print()


    assert survivor.did_survive_infection() == True
