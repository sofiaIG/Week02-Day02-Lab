from src import bus
from src import person

class BusStop:
    def __init__(self, name):
        self.name = name
        self.queue = []

    def queue_length(self):
        return(len(self.queue))

    def add_to_queue(self, person):
        self.queue.append(person)

    def clear(self):
        self.queue.clear()


    # def add_person(self, passenger):
    #     self.queue.append(passenger)

    def pick_up_from_stop(self, bus_stop):
        bus.pick_up(self.queue)
        self.clear()
        
        
