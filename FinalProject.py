""" A student class taking enhancer.
"""
from argparse import ArgumentParser
import sys
    
class Notes():
    """This is a class thats takes a students notes uploaded as text file
    
    Attributes:
        file(txt): a path to a text file containing students notes for their desired course
    """


    def __init__(self, file):
        """ Initializes note object using a text file containing students notes
        
        Args:
         file(txt): a path to the text file a path to a text file containing students notes for their desired course
    
        Side effects:
            Creates an attribute 
        """
        pass
    def add_courses(self):
        """takes the course name and adds it to the notes
        
        Args:
            str(courses): name of the course
    
        Returns:   
            Dict: Dictionary containing the name of the course
          
        """
        pass
    def add_chapter(self):
        """ takes the chapter of the course and adds it to the notes
        
         Args:
            str(chapter): chapter of the course 
    
        Returns:   
            Dict: Dictionary containing the chapter of the course
          
        """
        pass
    def pull_definition(self):
        """takes the definitions from a course and adds it to the notes
        
         Args:
            str: name of the course
    
        Returns:   
            list: A list of the definitions
          
        """
        pass

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
        pass
    def to_do(self, need_to_complete):
        """ Creates a list for the user on what they need to complete. 
        Args:
         need_to_complete(file): Contains are necessary tasks that are still 
         undone
        Returns:
        A list containing all assignments that the user needs to complete. 
        """
        pass
    def is_assignment_due(self, date):
        """ Creates a list that will compare the current date with the due 
        date of an assignment to see which ones need to be completed as soon as
        possible. 
        
        Args:
        date(datetime): stores an instant in time
        
        Returns:
        A list with the assignments due closer to the current date at the top 
        of the list. 
        """
        pass
 
def main(file, to_dos=None):
    """Creates an instance of Notes class for file. Creates an instance of 
    Planner to create the base of student works.
    
    Args:
        file(txt): a path to the text file
        Optional:
            to_dos(str): string of what user has to do
    
    Side effects:
        Creates instances of Planner and Notes class
    """
    pass

def parse_args(arglist):   
    """Parse command-line arguments.
    
    Expects one (not sure what others) mandatory argument for path to file
    
    Args:
        arglist(list of str): args from the command line
    
    Returns:
        namespace: the parsed args as a namespace
    """
    pass

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)