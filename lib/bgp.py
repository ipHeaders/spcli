from pyedgeconnect import Orchestrator
from .BaseConnection import BaseConnection,create_dict,create_dict_from_list,tablefmt
from .BaseConnection import print_dict,print_list
from tabulate import tabulate

class BGP(BaseConnection):
    def __init__(self,):
        super().__init__()   
