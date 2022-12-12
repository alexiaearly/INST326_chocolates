""" A student class taking enhancer.
"""
from argparse import ArgumentParser
import sys
import json
    
class Notes():
    """This is a class thats takes a students notes uploaded as text file
    
    Attributes:
        Note_dict (dict): a dictionary of notes
    """

    def __init__(self):
        """ Initializes note object using a dictionary containing students notes
        
        Side effects:
            Initializes a dictionary Note_dict to store courses and definitions
        """
        self.Note_dict = {}
    def add_courses(self, course):
        """ The course name and adds it to the notes
        
        Args:
            course (str): name of the course
    
        Returns:   
            Note_dict (dict): Dictionary containing the name of the course
        
        Side effects:
            Adds a new key to the dictionary
        
        Raises:
            TypeError if the course is not a string
        """
        if type(course) is not str:
            raise TypeError('The course needs to be a str')
        
        self.Note_dict[course] = []
    
    def add_definition(self, course, definition):
        """ Adds definitions to a course
        
        Args:
            course (str): the name of the course
            definition (str): the definition
        
        Returns:
            An f string that prints the course and its definitions
            
        Raises:
            TypeError if the course and definitoin are not strings
        """
        if type(course) and type(definition) is not str:
            raise TypeError('The definition and course need to be str')
        if course in self.Note_dict:
            self.Note_dict[course].append(definition)
        else:
            self.add_courses(course)
            self.Note_dict[course].append(definition)   
        return 

    def view_definitions(self):
        """ Takes the definitions from all courses and adds it to a text file
        
        Side effects:
            Creates a text file 
        """
        with open('mynotes.json', 'w') as f:
            json.dump(self.Note_dict, f)
                

class Planner():
    """ Creates a schedule for students to know their uncomplete tasks and 
    changes their schedule to accomadate to assignments that will soon be due. 
    
    Attributes:
        planner(dict): a dictionary containing assignments and due dates
    """
    def __init__(self):
        """ Initializes a planner object. 
        
        Side Effects:
        Sets a new value to the object's attribute. 
        """
        self.planner = {}

    def to_do(self, assignments, duedate):
        """ Creates a list for the user on what they need to complete. 
        Args:
         assignment (str): name of the assignment due
         
         duedate: date the assignment is due
        
        Returns:
        A list containing all assignments that the user needs to complete. 
        """
        self.planner[assignments] = duedate
        
        sort_assignments = sorted(self.planner.items(), key=lambda x: x[1])
        return sort_assignments
    
    def due_soon(self):
        """ Creates a list for the user on the next assignments due
        
        Returns:
            list of strings
        """
        duenext = [x for x, y in self.planner.items() if y < 3]
        return duenext
        
    
 
def main(name):
    """Creates an instance of Notes class for file. Creates an instance of 
    Planner to create the base of student works.
    
    Args:
    
    Side effects:
        Creates instances of Planner and Notes class
    """
    notes = Notes()
    planner = Planner()
    while True:
        welcome = input("Hi! " + name + ", are you interested in seeing your" +
                        " Notes or To-Do assignments? To quit type q ")
        if welcome == "Notes":
            note_input = input("Type viewdef, adddef, or addcourse: ")
            if note_input == "viewdef":
                notes.view_definitions()
                
            elif note_input == "adddef":
                course = input("Type the name of your course: ")
                definition = input("Type the definition for the course: ")
                notes.add_definition(course, definition)
                
            elif note_input == "addcourse":
                course = input("Type the name of your course: ")
                notes.add_courses()
        if welcome == "To-Do":
            todo_input = input("Type AA for add assignment or"+
                            " DS to view due soon: ")
            if todo_input == "AA":
                assignment = input("Type the assignment name: ")
                date = input("How many days until it's due?: ")
                planner.to_do(assignment, date)
            elif todo_input == "DS":
                planner.due_soon()
        if welcome == "q":
            print("Goodbye")
            notes.view_definitions()
            return

def parse_args(arglist):   
    """ Parse command-line arguments.
    
    Expects one (not sure what others) mandatory argument for path to file
    
    Args:
        arglist(list of str): args from the command line
    
    Returns:
        namespace: the parsed args as a namespace
    """
    parser = ArgumentParser()
    parser.add_argument("name", help="name of user")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.name)