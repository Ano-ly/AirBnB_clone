#!/usr/bin/python3
""" This module contains the class HBNBCommand"""


import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
    The following class creates a command line interface
    for the AirBnB project
    """

    prompt = "(hbnb) "

    __classes = {
        "BaseModel"
    }

    def emptyline(self):
        """Overwrites the emptyline function."""
        pass

    def do_EOF(self, line):
        """Exits the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_create(self, arg):
        """  Creates a new instance of a class, saves it (to the JSON file) and prints the id. """
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            arg = BaseModel()
            storage.save()
            print(arg.id)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
