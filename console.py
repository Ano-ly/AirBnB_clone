#!/usr/bin/python3
""" This module contains the class HBNBCommand"""


import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    The following class creates a command line interface
    for the AirBnB project
    """

    prompt = "(hbnb) "

    __classes = {
        "BaseModel",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review",
        "User"
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
        """  Creates a new instance of a class, saves it (to the JSON file)
        and prints the id. """

        if len(arg) == 0:
            print("** class name missing **")
        elif len(arg) != 0:
            args_list = arg.split()
            if args_list[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                arg = eval(args_list[0])()
                storage.save()
                print(arg.id)

    def do_show(self, arg):
        """
        Prints the string representation of instances
        """

        if len(arg) == 0:
            print("** class name missing **")
        elif len(arg) != 0:
            args_list = arg.split()
            if args_list[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            elif len(args_list) == 1:
                print("** instance id missing **")
            else:
                check_dict = storage.all()
                check_str = ".".join(args_list)
                for instance in check_dict.keys():
                    if instance == check_str:
                        print(check_dict[instance])
                if check_str not in check_dict.keys():
                    print("** no instance found **")

    def do_destroy(self, arg):
        """
        Destroys an instance
        """

        if len(arg) == 0:
            print("** class name missing **")
        elif len(arg) != 0:
            args_list = arg.split()
            if args_list[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            elif len(args_list) == 1:
                print("** instance id missing **")
            else:
                check_dict = storage.all()
                check_str = ".".join(args_list)
                if check_str not in check_dict.keys():
                    print("** no instance found **")
                else:
                    del (check_dict[check_str])
                    storage.save()

    def do_all(self, arg):
        """
        Prints the string representation of all instances
        """

        check_dict = storage.all()
        print_list = []
        if len(arg) == 0:
            for instance in check_dict.keys():
                print_list.append(str(check_dict[instance]))
            print(print_list)
        elif len(arg) != 0:
            if arg not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                for instance in check_dict.keys():
                    if instance.startswith(arg):
                        print_list.append(str(check_dict[instance]))
                print(print_list)

    def onecmd(self, line):
        """Overwrite precmd"""

        if re.match("^[A-Za-z]+\.[a-z]+\(\".*\"\)", line):
            str_list = line.split(".")
            id_list = str_list[1].split("(")
            str_list[1] = id_list[0]
            id = id_list[1].strip('")')
            str_list.insert(0, id)
            #str = str_list[1]
            #str_list[1] = str.strip("()")
            super().onecmd(" ".join(reversed(str_list)))
        else:
            super().onecmd(line)

    def do_update(self, arg):
        """
        Updates an object stored in the file
        """

        if len(arg) == 0:
            print("** class name missing **")
        elif len(arg) != 0:
            args_list = arg.split(" ", 3)
            if args_list[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            elif len(args_list) == 1:
                print("** instance id missing **")
            elif len(args_list) > 1:
                check_dict = storage.all()
                check_str = ".".join(args_list[0:2])
                if check_str not in check_dict.keys():
                    print("** no instance found **")
                elif len(args_list) == 2:
                    print("** attribute name missing **")
                elif len(args_list) == 3:
                    print("** value missing **")
                else:
                    check_dict = storage.all()
                    check_str = ".".join(args_list[0:2])
                    atr = args_list[2]
                    for inst in check_dict.keys():
                        args_list[3] = args_list[3].strip('"')
                        if inst == check_str:
                            type_atr = type(check_dict[inst].__dict__[atr])
                            if type_atr == "int":
                                args_list[3] = int(args_list[3])
                            elif type_atr == "str":
                                args_list[3] = str(args_list[3])
                            if type_atr == "float":
                                args_list[3] = float(args_list[3])
                            check_dict[inst].__dict__[atr] = args_list[3]
                            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
