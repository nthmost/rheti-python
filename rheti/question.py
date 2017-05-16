import random


class InvalidChoice(Exception):
    pass

class Choice(class):
    """ Describes a question option (choice), its reference code (e.g. Q21a), and the value that
    selecting this Choice represents to the test.
    """

    def __init__(self, text, code, value):
        self.text = text
        self.value = value
        self.code = code

    def select(self):
        """ Returns the value of this Choice. """
        return self.coded_value


class Question(class):
    """ Describes a question and its possible Choices. """

    def __init__(self, text, choices):
        self.text = text
        self.choices = choices

    def random_choice(self):
        return random.choice(self.choices)

    def choose(self, code):
        """ Takes the 'code' matching to the desired Choice and returns the 'value' of that Choice. """
        for choice in self.choices:
            if choice.code == code:
                return choice.select()
        raise InvalidChoice('Code "%s" does not match a Choice for this Question.' % code)



