import yaml
from pathlib import Path

tablefmt = 'pretty'

class BaseConnection:

     def __init__(self):
        home = str(Path.home())
        with open(f"{home}/.spcli/creds.yml", "r") as stream:
            try:
                yml_vars = yaml.safe_load(stream)
                #print(yml_vars['url'])
                #print(yml_vars['token'])
            except yaml.YAMLError as exc:
                print(exc)        
    
        self.url = yml_vars['url']
        self.token = yml_vars['token']



def print_list(list:list):
    print("----------------------------------------------------------------------------")
    for i in list:
        for key,value in i.items():
            print(f"{key} : {value}")
        print("----------------------------------------------------------------------------")    


def print_dict(dict:dict):
    print("----------------------------------------------------------------------------")
    for key,value in dict.items():
        print(f"{key} : {value}")
    print("----------------------------------------------------------------------------")    


def create_dict(dict:dict,arguments:list):
    template = {}
    for arg in arguments:
        template[arg] = dict[arg]
    return template

def create_dict_from_list(list:list,header:str):
    template_list = []
    template_dict = {}

    for arg in list:
        template_dict[header] = arg
        template_list.append(template_dict)
    return template_list
