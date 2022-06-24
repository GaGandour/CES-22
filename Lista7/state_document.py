from abc import abstractmethod
from enum import Enum

class Document:
    def __init__(self, state):
        self.state = state
        
    
    def render(self):
        self.state.render(self)

    def publish(self):
        self.state.publish(self)

    def change_state(self):
        self.state.change_state(self)



class Publisher(Enum):
    USER = 1
    ADMIN = 2



class State:
    def __init__(self, document):
        self.document = document
    
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def publish(self):
        pass

    @abstractmethod
    def change_state(self):
        pass



class Draft(State):
    def __init__(self, document):
        super.__init__(document)
        self.publisher = Publisher.USER

    def render(self):
        print("Draft render function")

    def publish(self):
        print("Draft publish function")

    def change_state(self):
        if self.publisher == Publisher.USER:
            self.document.state = Moderation(self.document)
        else:
            self.document.state = Published(self.document)


class Moderation(State):
    def __init__(self, document):
        super.__init__(document)
        super.aproved

    def render(self):
        print("Moderation render function")

    def publish(self):
        print("Moderation publish function")

    def change_state(self):
        if self.aproved:
            self.document.state = Published(self.document)
        else:
            self.document.state = Draft(self.document)


class Published(State):
    def __init__(self, document):
        super.__init__(document)
        self.expired = False

    def render(self):
        print("Published render function")

    def publish(self):
        print("Published publish function")

    def change_state(self):
        if self.expired:
            self.document.state = Draft(self.document)