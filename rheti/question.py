import random


class InvalidChoice(Exception):
    pass


class Choice:
    """A question option (choice), its reference code (e.g. Q21a), and the type value."""

    def __init__(self, text, code, value):
        self.text = text
        self.code = code
        self.value = value

    def select(self):
        return self.value


class Question:
    """A question and its possible Choices."""

    def __init__(self, qnum, choices):
        self.qnum = qnum
        self.choices = choices  # list of Choice objects

    def random_choice(self):
        return random.choice(self.choices)

    def choose(self, code):
        """Takes the code (e.g. 'a' or 'b') and returns the type value of that Choice."""
        for choice in self.choices:
            if choice.code == code:
                return choice.select()
        raise InvalidChoice('Code "%s" does not match a Choice for this Question.' % code)
