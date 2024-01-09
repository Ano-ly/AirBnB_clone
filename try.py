#!/usr/bin/python3
import cmd

class My_comm(cmd.Cmd):
    def do_add(self, x):
        listt = x.split()
        listt = [int(x) for x in listt]
        print(listt[0] + listt[1])

Command1 = My_comm()
Command1.cmdloop("This is a friggin' python shell")
