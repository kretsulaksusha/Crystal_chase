"Game classes."

class Room:
    """
    Room class.
    """
    def __init__(self, room: str) -> None:
        self.room = room
        self.description = ""
        self.linked_rooms = {}
        self.item = None
        self.character = None

    def __str__(self) -> str:
        return self.room

    def __repr__(self) -> str:
        return f"Room(room={self.room})"

    def set_description(self, description: str):
        """
        Setting description.
        """
        self.description = description

    def link_room(self, room: object, direction: str):
        """
        Add linked rooms.
        """
        self.linked_rooms[room] = direction

    def set_item(self, item: object):
        """
        Setting item.
        """
        self.item = item

    def get_item(self):
        """
        Getting item.
        """
        return self.item

    def set_character(self, character: object):
        """
        Setting character.
        """
        self.character = character

    def get_character(self):
        """
        Getting character.
        """
        return self.character

    def get_details(self):
        """
        Getting details.
        """
        details = [self.room, '--------------------', self.description,
                   *[f"The {room} is {direct}" for room, direct in self.linked_rooms.items()]]
        print("\n".join(details))

    def move(self, command: str) -> str:
        """
        Move to another room.
        """
        try:
            return [i for i, j in self.linked_rooms.items() if j == command][0]
        except IndexError:
            print('\nInvalid command!')
            return self


class Enemy:
    """
    Enemy class.
    """
    defeated = 0

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description
        self.conversation = ""
        self.weakness = None

    def set_conversation(self, text: str):
        """
        Setting conversation.
        """
        self.conversation = text

    def set_weakness(self, weakness: str):
        """
        Setting weakness.
        """
        self.weakness = weakness

    def describe(self):
        """
        Description of the character.
        """
        if self.name and self.description:
            print(f"{self.name} is here!\n{self.description}")

    def talk(self):
        """
        On talk command.
        """
        print(f"[{self.name} says]: {self.conversation}")

    def fight(self, fight_with: str):
        """
        Fighting.
        """
        if fight_with == self.weakness:
            Enemy.defeated += 1
            print(Enemy.defeated)
            return True
        return False

    def get_defeated(self):
        """
        Getting the number of defeats.
        """
        return self.defeated


class Item:
    """
    Item class.
    """
    def __init__(self, item_name: str) -> None:
        self.item_name = item_name
        self.description = ''

    def get_name(self):
        """
        Getting name.
        """
        return self.item_name

    def set_description(self, text: str):
        """
        Doc
        """
        self.description = text

    def describe(self):
        """
        Description on a character.
        """
        if self.item_name and self.description:
            print(f"The [{self.item_name}] is here - {self.description}")
