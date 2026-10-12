from enum import Enum 

class CommandErrors(Enum):
    TIMEOUT = 1
    CALLEDPROCESSERROR = 2
    COMMANDNOTFOUND = 3
