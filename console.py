#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_EOF(self, line):
        ''' Leave the commandline interpreter when the user
            enters the EOF character
        '''
        return True
    
    def do_quit(self, line):
        ''' Leave the commandline interpreter when the user
            enters quit
        '''
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
