#!/usr/bin/python3
''' Define the console and it's commands '''
import cmd


class HBNBCommand(cmd.Cmd):
    ''' Make use of the cmd module to create an interactive console '''
    prompt = '(hbnb) '

    def emptyline(self):
        ''' By default pressing enter with an empty line would run
            the previous command. This method makes sure nothing
            happens if it was the case '''
        pass

    def do_EOF(self, line):
        ''' Leave the commandline interpreter when the user
            enters the EOF character '''
        print()
        return True

    def do_quit(self, line):
        ''' Leave the commandline interpreter when the user
            enters quit '''
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
