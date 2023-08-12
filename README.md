# AirBnB_clone

In our AirBnb Clone project, we've developed a powerful command interpreter. This essential tool allows you to efficiently manage a wide range of AirBnb objects, providing seamless control over listings, users, bookings, and more. With this command interpreter, you can effortlessly create, update, and access crucial information related to the AirBnb ecosystem. Whether you're a host, guest, or administrator, this intuitive command-line interface empowers you to handle AirBnb objects with ease.

## Runing the console

The Commandline Interpreter can be started by executing the command **./console.py**. The console can **create**, **destroy**, and **update** objects.
For more information use the **help** command.

## Example

```console
achraf@ash-logs-ubuntu:~/Desktop/AirBnB_clone$ ./console.py 
(hbnb) create User
a87947dc-eed2-441d-b52e-97d644757cf4
(hbnb) show User
** instance id missing **
(hbnb) show
** class name missing **
(hbnb) show User a87947dc-eed2-441d-b52e-97d644757cf4
[User] (a87947dc-eed2-441d-b52e-97d644757cf4) {'id': 'a87947dc-eed2-441d-b52e-97d644757cf4', 'created_at': datetime.datetime(2023, 8, 12, 23, 37, 16, 196465), 'updated_at': datetime.datetime(2023, 8, 12, 23, 37, 16, 196566)}
(hbnb) destroy User a87947dc-eed2-441d-b52e-97d644757cf4
(hbnb) User.all()
[]
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) quit
achraf@ash-logs-ubuntu:~/Desktop/AirBnB_clone$
```
