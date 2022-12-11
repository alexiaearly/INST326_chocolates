""" A student class taking enhancer.
"""
from argparse import ArgumentParser
import sys
    
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
    
    def add_definition(self, course, definition, notes):
        """ Adds definitions to a course
        
        Args:
            course (str): the name of the course
            definition (str): the definition
            notes (obj): an instance of the notes class
        
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
            notes.add_courses(course)
            self.Note_dict[course].append(definition)
            
        return f"{course}: {self.Note_dict[course]}"

    def view_definitions(self):
        """ Takes the definitions from all courses and adds it to a text file
        
        Side effects:
            Creates a text file 
        """
        with open('mynotes.txt', 'w') as f:
            f.write(self.Note_dict)

class Planner():
    """Creates a schedule for students to know their uncomplete tasks and 
    changes their schedule to accomadate to assignments that will soon be due. 
    
    Attributes:
        date(datetime): stores an instant in time 
    """
    def __init__(self):
        """ Initializes a planner object. 
        
        Side Effects:
        Sets a new value to the object's attribute. 
        """
        self.planner = {}

    def to_do(self, need_to_complete):
        """ Creates a list for the user on what they need to complete. 
        Args:
         need_to_complete(file): Contains are necessary tasks that are still 
         undone
        Returns:
        A list containing all assignments that the user needs to complete. 
        """
        pass
    
 
def main(name):
    """Creates an instance of Notes class for file. Creates an instance of 
    Planner to create the base of student works.
    
    Args:
    
    Side effects:
        Creates instances of Planner and Notes class
    """
    
    pass

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
    main(args.file)