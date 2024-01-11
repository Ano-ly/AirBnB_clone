#!/usr/bin/python3
""" This module contains the class HBNBCommand"""


import cmd


class HBNBCommand(cmd.Cmd):
    """
    The following class creates a command line interface
    for the AirBnB project
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """Overwrites the emptyline function."""
        pass

    def do_EOF(self, line):
        """Exits the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
