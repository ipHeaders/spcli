from pyedgeconnect import Orchestrator
from .BaseConnection import BaseConnection,create_dict,create_dict_from_list,tablefmt
from .BaseConnection import print_dict,print_list
from tabulate import tabulate


class ORCH(BaseConnection):
    def __init__(self,):
        super().__init__()   
    def _get_orchestrator_server_brief(self):
        try:
            orch = Orchestrator(self.url, verify_ssl=True, api_key=self.token)
            orch_return = orch.get_orchestrator_server_brief()

            print(tabulate(orch_return.items(),tablefmt=tablefmt))
        except Exception as e:
            print(e)
    def _get_ipAllowList(self):
        try:
            orch = Orchestrator(self.url, verify_ssl=True, api_key=self.token)
            orch_return = orch.get_ip_allow_list()
            if len(orch_return) == 0:
                orch_return = ['0.0.0.0/0']
                ip_list = create_dict_from_list(orch_return,'IP')
            else:
                ip_list = create_dict_from_list(orch_return,'IP')
            print(tabulate(ip_list,headers='keys',tablefmt=tablefmt))

            #print(orch.get_ip_allow_list())

        except Exception as e:
            print(e)
    def _get_get_all_users(self):
        try:
            orch = Orchestrator(self.url, verify_ssl=True, api_key=self.token)
            orch_return = orch.get_all_users()
            y = []
            for u in orch_return:
                args = ['userPk','username','firstName','lastName','phone','email','status',
                        'role','isCurrentlyLoggedIn','isTwoFactorEmail','isTwoFactorTime','userTwoFactorKey']
                x = create_dict(u,args)    
                y.append(x)
            print(tabulate(y,headers='keys',tablefmt=tablefmt))
        except Exception as e:
            print(e)

    def _get_orchestrator_server_info(self):
        try:
            orch = Orchestrator(self.url, verify_ssl=True, api_key=self.token)
            orch_return = orch.get_orchestrator_server_info()
            print(tabulate(orch_return.items(),tablefmt=tablefmt))
            #print_dict(orch_return)

        except Exception as e:
            print(e)

    def _get_orchestrator_sessions(self):
        try:
            orch = Orchestrator(self.url, verify_ssl=True, api_key=self.token)
            orch_return = orch.get_orchestrator_sessions()
            y = []
            for u in orch_return:
                args = ['userName','lastInteractionTime','loggedInTime','webClient','role','lastAccessTime','isMtoSsoSession']

                x = create_dict(u,args)    
                y.append(x)
            print(tabulate(y,headers='keys',tablefmt=tablefmt))

        except Exception as e:
            print(e)
    def _get_orchestrator_backup_config(self):
        try:
            orch = Orchestrator(self.url, verify_ssl=True, api_key=self.token)
            orch_return = orch.get_orchestrator_backup_config()
            #print(tabulate(orch_return.items(),tablefmt=tablefmt))
            #print_dict(orch_return)
        except Exception as e:
            print(e)