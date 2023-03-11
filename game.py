"""
All classes for adventure game called 'Crystal chase'.
"""

class LvivStreats:
    """
    Lviv streats
    """
    def __init__(self, name: str) -> None:
        self.name = name
        self.description = ''
        self.linked_streats = {}
        self.command = None
        self.people = None
        self.place = None
        self.crystal = 'Crystal'

    def set_description(self, description: str):
        """
        Setting description.
        """
        self.description = description

    def set_people(self, people: object):
        """
        Setting people.
        """
        self.people = people

    def set_place(self, place: object):
        """
        Setting people.
        """
        self.place = place

    def link_streat(self, streat: object, direction: str):
        """
        Link adjacent streats.
        """
        self.linked_streats[streat] = direction

    def move(self, command: str):
        """
        Move to another streat.
        """
        return [i for i, j in self.linked_streats.items() if j == command][0]

    def get_details(self):
        """
        Details.
        """
        details = ['\33[92m' + self.name + '\033[00m', '------------------',
                   self.description, "\33[1m  Places to visit:\033[00m",
                   *[f"{i.name} is \33[34m{j}\033[00m." for i, j in self.linked_streats.items()]]
        print('\n'.join(details))

    def get_directions(self):
        """
        Getting all directions.
        """
        return list(self.linked_streats.values())


class Place:
    """
    Items on the streats.
    """
    def __init__(self, place: str) -> None:
        self.place = place
        self.description = ''
        self.action = ''

    def set_description(self, description: str):
        """
        Setting description.
        """
        self.description = description

    def set_action(self, describe_action: str):
        """
        Setting the name
        """
        self.action = describe_action


class People:
    """
    People class.
    """
    def __init__(self, name: str) -> None:
        self.name = name
        self.description = ''
        self.verbose = ''
        self.talk = ''

    def set_description(self, description: str):
        """
        Setting description.
        """
        self.description = description

    def set_verbose_description(self, description: str):
        """
        Setting verbose description.
        """
        self.verbose = description

    def set_talk(self, talk: str):
        """
        Setting talk.
        """
        self.talk = talk
