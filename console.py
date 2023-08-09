#!/usr/bin/python3

import cmd
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.base_models import BaseModel

class ABnBShell(cmd.Cmd):
    prompt = '(ABnB) '

    def do_create(self, line):
        '''creates a new instance of BaseModel'''
        if len(line) == 1:
            print("** class name missing **")
            return

        args = line.split()

        command = args[0]

        class_name = args[1]

        if command == "create" and class_name in globals() and  hasattr(globals()[class_name], "create"):
            my_instance = class_name()
            print(my_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        '''prints a string repsentation of an instance bassed
        on the class name and id'''

        if len(line) == 1:
            print("** class name missing **")
            return

        args = line.split()

        commmand = args[0]

        class_name = args[1]

        if class_name not in globals():
            print("** class doesn't exist **")
            return

        if class_name in globals() and len(args) == 2:
            print("** instance id missing **")

        instance_data = globals()[class_name].instances
        if instance_id in instance_data:
            instance = instance_data[instance_id]
            print(instance)
        else:
            print("** no instance found **")


    def do_destroy(self, line):
        '''Deletes an instance based on a class name and id
        (saves the changes into the JSON FILE)'''

        if len(line.split()) == 1:
            print("** class name missing **")
            return

        args = line.split()

        command = args[0]

        class_name = args[1]

        if class_name not in globals():
            print("** class doesn't exist **")

        if len(args) < 3:
            print("** instance id missing **")

        instance_id = args[2]

        instance_data = globals()[class_name].instances
        if instance_id in instances_data:
            del instances_data[instance_id]
        else:
            print("** no instance found **")


    def do_all(self, line):
        '''prints all string representation of instances
           based on class name
        '''
        args = line.split()

        if len(args) == 0:
            all_instances = []
            for class_name, class_obj in globals().items():
                if hasattr(class_obj, 'instances'):
                    all_instances.extend(class_instances.values())

            for instance in all_instances:
                print(instance)
            return

        class_name = args[0]

        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if hasattr(globals()[class_name], 'instances'):
            instance_data = globals()[class_name].instances
            
            for instance in instances_data.values():
                print(instance)

        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        '''updates an instance based on class name and id'''
        args = line.split()

        if len(args) == 1:
            print("** class name missing **")
            return

        class_name = args[1]

        if class_name not in globals():
            print("** class doesn't exist **")
            return

        if len(args) == 2:
            print("** instance id missing **")
            return

        instance_id = args[2]

        if class_name in globals():
            instances_data = globals()[class_name].instances

            if instance_id in instances_data:
                instance = instances_data[instance_id]

                if len(args) == 3:
                    print("** attribute name missing **")

                elif len(args) == 4:
                    print("** value missing **")

                else:
                    attribute_name = args[3]
                    attribute_value = args[4]

                    if hasattr(instance, attribute_name):
                        setattr(instance, attribute_name, attribute_value)
                    else:
                        print("** no attribute found **")

            else:
                print("** no instance found **")

        else:
            print("** class doesn't exist **")



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
