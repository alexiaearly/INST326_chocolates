""" A student class taking enhancer.
"""
from argparse import ArgumentParser
import sys
    
class Notes():
    """This is a class thats takes a students notes uploaded as text file
    
    Attributes:
        file(txt): a path to a text file containing students notes for their 
        desired course
    """

    def __init__(self):
        """ Initializes note object using a text file containing students notes
        
        Side effects:
            Creates an attribute 
        """
        self.Note_dict = {}
    def add_courses(self, course):
        """takes the course name and adds it to the notes
        
        Args:
            course (str): name of the course
    
        Returns:   
            Note_dict (dict): Dictionary containing the name of the course
        """
        if type(course) is not str:
            raise TypeError('The course needs to be a str')
        
        self.Note_dict[course] = None
    
    def add_definition(self, course, definition, notes):
        if type(course) and type(definition) is not str:
            raise TypeError('The definition and course need to be str')
        
        if course in self.Note_dict:
            self.Note_dict[course] = definition
        else:
            notes.add_courses(course)
            self.Note_dict[course] = definition
            
        return self.Note_dict[course] 

    def view_definitions(self, course):
        """takes the definitions from a course and adds it to the notes
        
         Args:
            course (str): name of the course
    
        Returns:   
            list: A list of the definitions
            or a string that indicates the course is not in your notes
          
        """
        if type(course) is not str:
            raise TypeError('The course needs to be a str')
        
        if course in self.Note_dict:
            return f"{course} : {self.Note_dict[course]}"
        else:
            return f"{course} is not in your notes"

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
    """Collects information from the user about what information they would
    like to work with. 
    
    Args: 
        User: represents th us
    
    """
    name = input("Enter your name")
    welcome = input(("Hi! " + name + ",Are you interested in seeing your notes"+ 
                     "or To-Do List Assignments Today?"))
    notes = Notes()
    planner = Planner()
    if welcome == "Notes":
        note_input = input("type viewdef, adddef, or addcourse")
        if note_input == "viewdef":
            notes.view_definitions()
        elif note_input == "adddef":
            course = input("Type the name of your course: ")
            definition = input("Type the definition for the course: ")
            notes.add_definition(course, definition)
        elif note_input == "addcourse":
            course = input("Type the name of your course: ")
            notes.add_courses(course)
        else:
            raise ValueError("Must be either viewdef, adddef, or addcourse")
                  
    if welcome == "To-Do":
        todo_assignment = input()
       planner.to_do
        

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