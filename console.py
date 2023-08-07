#!/usr/bin/python3

import cmd

class ABnBShell(cmd.Cmd):
    prompt = '(ABnB) '

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

if __name__ == "__main__":
    ABnBShell().cmdloop()
