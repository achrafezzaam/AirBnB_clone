#!/usr/bin/python3
''' Define the console and it's commands '''
import cmd
<<<<<<< HEAD
import sys
import os

import models.base_model
from models import BaseModel, User, State, City, Amenity, Place, Review
from models import storage


class HBNBCommand(cmd.Cmd):
    ''' Make use of the cmd module to create an interactive console '''
    prompt = '(hbnb) '
    OBJECT_NAMES = ['BaseModel', 'User', 'State', 'City',
                    'Amenity', 'Place', 'Review']

    def do_create(self, line):
        '''creates a new instance of BaseModel'''

        if len(line.split()) == 0:
            print("** class name missing **")
            return

        args = line.split()

        class_name = args[0]

        if hasattr(models.base_model, class_name):
            class_obj = getattr(models.base_model, class_name)
            my_instance = class_obj.create()
            print(my_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        '''prints a string representation of an instance based
        on the class name and id'''

        if len(line.split()) == 0:
            print("** class name missing **")
            return

        args = line.split()

        class_name = args[0]

        if len(args) < 2:
            print("** instance id missing **")
            return
        
        instance_id = args[1]

        if hasattr(models.base_model, class_name):
            class_obj = getattr(models.base_model, class_name)

            if instance_id in class_obj.instances:
                instance = class_obj.instances[instance_id]
                print(instance)

            else:
                print("** no instance found **")

        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        '''Deletes an instance based on a class name and id
        (saves the changes into the JSON FILE)'''

        if len(line.split()) == 0:
            print("** class name missing **")
            return

        args = line.split()

        class_name = args[0]

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]

        if hasattr(models.base_model, class_name):
            class_obj = getattr(models.base_model, class_name)

            if instance_id in class_obj.instances:
                del class_obj.instances[instance_id]
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")
            return

    def do_all(self, line):
        '''prints all string representations of instances
           based on class name
        '''
        args = line.split()

        if len(args) == 0:
            all_instances = []
            for class_name, class_obj in globals().items():
                if hasattr(class_obj, 'instances'):
                    all_instances.extend(class_obj.instances.values())

            for instance in all_instances:
                print(instance)
            return

        class_name = args[0]

        if hasattr(models.base_model, class_name):
            class_obj = getattr(models.base_model, class_name)
            if hasattr(class_obj, 'instances'):
                instance_data = class_obj.instances
                for instance in instance_data.values():
                    print(instance)
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        '''updates an instance based on class name and id'''
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in globals():
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        instance_id = args[1]

        if class_name in globals():
            instances_data = globals()[class_name].instances

            if instance_id in instances_data:
                instance = instances_data[instance_id]

                if len(args) == 2:
                    print("** attribute name missing **")

                elif len(args) == 3:
                    print("** value missing **")

                else:
                    attribute_name = args[2]
                    attribute_value = args[3]

                    if hasattr(instance, attribute_name):
                        setattr(instance, attribute_name, attribute_value)
                    else:
                        print("** no attribute found **")

            else:
                print("** no instance found **")

        else:
            print("** class doesn't exist **")

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

   ''' def do_create(self, line):
        if not line:
            print("** class name missing **")
        elif line not in self.OBJECT_NAMES:
            print("** class doesn't exist **")
        else:            
            save = eval(line)()
            print(save.id)
            storage.save()

    def do_show(self, line):
        command = line.split(' ')
        if not line:
            print("** class name missing **")
        elif command[0] not in self.OBJECT_NAMES:
            print("** class doesn't exist **")
        elif len(command) < 2:
            print("** instance id missing **")
        else:
            save = storage.all()
            if "{}.{}".format(command[0], command[1]) in save.keys():
                print(save["{}.{}".format(command[0], command[1])])
            else:
                print("** no instance found **")
    '''


if __name__ == '__main__':
    HBNBCommand().cmdloop()
