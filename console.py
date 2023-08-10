#!/usr/bin/python3
''' Define the console and it's commands '''
import cmd
import re
import models.base_model
from models import BaseModel, User, State, City, Amenity, Place, Review
from models import storage



class HBNBCommand(cmd.Cmd):
    ''' Make use of the cmd module to create an interactive console '''
    prompt = '(hbnb) '
    OBJECT_NAMES = ['BaseModel', 'User', 'State', 'City',
                    'Amenity', 'Place', 'Review']
    
    def cmd_handler(self, string, count):
        if not string:
            print("** class name missing **")
        elif string.split()[0] not in self.OBJECT_NAMES:
            print("** class doesn't exist **")
        elif count > 1 and len(string.split()) < 2:
            print("** instance id missing **")
        elif count == 4 and len(string.split()) < 3:
            print("** attribute name missing **")
        elif count == 4 and len(string.split()) < 4:
            print("** value missing **")
        else:
            return False
        return True

    def emptyline(self):
        ''' By default pressing enter with an empty line would run
            the previous command. This method makes sure nothing
            happens if it was the case '''
        pass

    def do_create(self, line):
        '''creates a new instance of BaseModel'''
        if not self.cmd_handler(line, 1):
            save = eval(line)()
            print(save.id)
            save.save()

    def do_show(self, line):
        '''prints a string representation of an instance based
        on the class name and id'''

        if not self.cmd_handler(line, 2):
            save = storage.all()
            command = line.split()
            if "{}.{}".format(command[0], command[1]) in save.keys():
                print(save["{}.{}".format(command[0], command[1])])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        '''Deletes an instance based on a class name and id
        (saves the changes into the JSON FILE)'''
        if not self.cmd_handler(line, 2):
            save = storage.all()
            command = line.split()
            if "{}.{}".format(command[0], command[1]) in save.keys():
                del save["{}.{}".format(command[0], command[1])]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        '''prints all string representations of instances
           based on class name
        '''
        if not self.cmd_handler(line, 1):
            save = storage.all()
            output = [str(save[key]) for key in save.keys()
                      if key.split('.')[0]== line]
            print(output)

    def do_update(self, line):
        '''updates an instance based on class name and id'''
        if not self.cmd_handler(line, 4):
            save = storage.all()
            command = line.split()
            key = "{}.{}".format(command[0], command[1])
            if key in save.keys():
                attr = re.search(r"<class '(\w+)'>",
                                 str(type(getattr(save[key], command[2]))))
                temp =attr.group(1)
                setattr(save[key], command[2], eval(temp)(command[3]))
                save[key].save()
            else:
                print("** no instance found **")

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
