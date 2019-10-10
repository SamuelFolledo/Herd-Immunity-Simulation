class Virus(object):
    """Properties and attributes of the virus used in Simulation"""

    def __init__(self, name, mortality_rate, basic_repro_num):
        """Attributes instatiated with each virus."""
        self.name = name
        self.mortality_rate = mortality_rate
        self.basic_repro_num = basic_repro_num

    
def test_virus_instatiation():
    #TODO: Create your own test that models the virus you are working with
    '''Check to make sure that the virus instantiator is working.'''

    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.mortality_rate == 0.8
    assert virus.basic_repro_num == 0.3
