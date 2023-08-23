#!/usr/bin/python3
""" My Console Module """
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Contains all the possible functionalities of the HBNB console"""

    # determines prompt(s) for interactive or non-interactive modes
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
             'number_rooms': int, 'number_bathrooms': int,
             'max_guest': int, 'price_by_night': int,
             'latitude': float, 'longitude': float
            }

    def preloop(self):
        """Prints kana isatty iri false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """Re-formats command line 4 advanced command(s) syntax.

        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        (Brackets denote optional fields in usage example.)
        """
        _cmd = _cls = _id = _args = ''  # initializes line el

        # scanns 4 general formating - i.e '.', '(', ')'
        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:  # parse_liny left 2 right
            pline = line[:]  # parsed line

            # isolate <class_name>
            _cls = pline[:pline.find('.')]

            # isolate && validate <command(s)>
            _cmd = pline[pline.find('.') + 1:pline.find('(')]
            if _cmd not in HBNBCommand.dot_cmds:
                raise Exception

            # if parantheses("_") contain args, parse_them
            pline = pline[pline.find('(') + 1:pline.find(')')]
            if pline:
                # partition args: (<id>, [<delim>], [<*args>])
                pline = pline.partition(', ')  # pline_convert 2 tuple

                # isolate _id, strippin_Quotes
                _id = pline[0].replace('\"', '')
                # possible bug if it is here:
                # empty quotes_regist£r as £mpty _id wh£n repl@c£d

                # if args exlst bey0nd _id
                pline = pline[2].strip()  # pline is now str
                if pline:
                    # check 4 *args // **kwargs
                    if pline[0] is '{' and pline[-1] is'}'\
                            and type(eval(pline)) is dict:
                        _args = pline
                    else:
                        _args = pline.replace(',', '')
                        # _args = _args.replace('\"', '')
            line = ' '.join([_cmd, _cls, _id, _args])

        except Exception as mess:
            pass
        finally:
            return line

    def postcmd(self, stop, line):
        """Prints kana isatty iri fals£"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, command):
        """ Method yeku ita exit iHBNB console"""
        exit()

    def help_quit(self):
        """ Prints help documentation four quit  """
        print("Exits iprogram ne formatting\n")

    def do_EOF(self, arg):
        """ Handles EOF kuti iyite exit program """
        print()
        exit()

    def help_EOF(self):
        """ Prints help documentation for EOF """
        print("Exits iprogram pasina formatting\n")

    def emptyline(self):
        """ Overrides ma emptyline methods e CMD """
        pass

    def do_create(self, args):
        """Creates imwe new instance ye class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            new_dict = self._key_value_parser(args[1:])
            instance = classes[args[0]](**new_dict)
        else:
            print("** class is not existing **")
            return False
        print(instance.id)
        instance.save()

    def help_create(self):
        """ Help information kuti ive  create method """
        print("Creates a class ye chero type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """ Method ino ratidza an individual object """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]

        # guards kubva kuma trailing args
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class_name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class hayisi existing **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id
        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")

    def help_show(self):
        """ Help information ye show command """
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        """ Destroys ma specified objects """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id

        try:
            del(storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """ Help information yema destroy commands """
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, args):
        """ Shows ma  objects, or ese ma objects e class"""
        print_list = []

        if args:
            args = args.split(' ')[0]  # remove all possible trailing_args
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for k, v in storage._FileStorage__objects.items():
                if k.split('.')[0] == args:
                    print_list.append(str(v))
        else:
            for k, v in storage._FileStorage__objects.items():
                print_list.append(str(v))

        print(print_list)

    def help_all(self):
        """ Help inf for the all_commands """
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def do_count(self, args):
        """Count_current num of class instances"""
        count = 0
        for k, v in storage._FileStorage__objects.items():
            if args == k.split('.')[0]:
                count += 1
        print(count)

    def help_count(self):
        """ """
        print("Usage: count <class_name>")

    def do_update(self, args):
        """ Updates a certain object with new info """
        c_name = c_id = att_name = att_val = kwargs = ''

        # isolate cls from id/args, ex: (<cls>, delim, <id/args>)
        args = args.partition(" ")
        if args[0]:
            c_name = args[0]
        else:  # class_naam not present
            print("** class name missing **")
            return
        if c_name not in HBNBCommand.classes:  # class_nam invalid
            print("** class doesn't exist **")
            return

        # isolat_id from args
        args = args[2].partition(" ")
        if args[0]:
            c_id = args[0]
        else:  # id hayisi present
            print("** instance id missing **")
            return

        # generate_key kubva ku_class ne id
        key = c_name + "." + c_id

        # determine if key kana iri present
        if key not in storage.all():
            print("** no instance found **")
            return

        # first determine kana kwargs // args
        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = []  # reformat kwargs ive list, ex: [<name>, <value>, ...]
            for k, v in kwargs.items():
                args.append(k)
                args.append(v)
        else:  # isolate args
            args = args[2]
            if args and args[0] is '\"':  # check for quoted arg
                second_quote = args.find('\"', 1)
                att_name = args[1:second_quote]
                args = args[second_quote + 1:]

            args = args.partition(' ')

            # if att_name kana isina ku quoted arg
            if not att_name and args[0] is not ' ':
                att_name = args[0]
            # tarisa for quoted val arg
            if args[2] and args[2][0] is '\"':
                att_val = args[2][1:args[2].find('\"', 1)]

            # if att_val kana isiri quoted arg
            if not att_val and args[2]:
                att_val = args[2].partition(' ')[0]

            args = [att_name, att_val]

        # retrieve_dictionary of current obj
        new_dict = storage.all()[key]

        # iterate through attr naams and vals
        for i, att_name in enumerate(args):
            # block chete runs on even_iterations
            if (i % 2 == 0):
                att_val = args[i + 1]  # following item is value
                if not att_name:  # check for att_name
                    print("** attribute name missing **")
                    return
                if not att_val:  # check for att_value
                    print("** value missing **")
                    return
                # type cast as necessary
                if att_name in HBNBCommand.types:
                    att_val = HBNBCommand.types[att_name](att_val)

                # update_dict with name, value pair
                new_dict.__dict__.update({att_name: att_val})

        new_dict.save()  # save updates to a file

    def help_update(self):
        """ Help information kuita  update class """
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")

if __name__ == "__main__":


	HBNBCommand().cmdloop()
