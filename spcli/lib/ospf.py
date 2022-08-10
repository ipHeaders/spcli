from pyedgeconnect import Orchestrator
from lib.BaseConnection import BaseConnection,create_dict,create_dict_from_list,tablefmt
from lib.BaseConnection import print_dict,print_list
from tabulate import tabulate


class OSPF(BaseConnection):
    def __init__(self,):
        super().__init__()   

    def _get_appliance_ospf_config(self,options):
        ne_pk = f"{options.config[0]}.NE"
        try:
            args = ['redistMapToOSPF','enable','enable','routerId']
            orch = Orchestrator(self.url, verify_ssl=True, api_key=self.token)
            orch_return = orch.get_appliance_ospf_config(ne_id=ne_pk)
            #print(orch_return)
            x = create_dict(orch_return,args)
            print(tabulate(x.items(),tablefmt=tablefmt))

            orch_return = orch.get_appliance_ospf_interfaces_config(ne_id=ne_pk)

            y = []
            for key,value in orch_return.items():
                args = ['cost','area','authKey','md5Password','authType','priority','helloInterval','deadInterval','adminStatus']
                
                x = create_dict(value,args)    
                interface = {'interface': key}
                x = {**interface, **x}
                y.append(x)

            print(tabulate(y,headers='keys',tablefmt=tablefmt))

            #print(orch_return)
        except Exception as e:
            print(e)
    def _get_appliance_ospf_state(self,options):
        ne_pk = f"{options.state[0]}.NE"
        try:
            args = ['redistMapToOSPF','enable','enable','routerId']
            orch = Orchestrator(self.url, verify_ssl=True, api_key=self.token)
            orch_return = orch.get_appliance_ospf_interfaces_state(ne_id=ne_pk)

            y = []
            for u in orch_return['interfaceState']:
                args = ['ifname','ip_addr','area','desig_rtr','bkup_desig_rtr','admin_status','ospf_if_type','hello_interval','dead_interval','totalNeighbors','activeNeighbors']
                x = create_dict(u,args)    
                y.append(x)
            print(tabulate(y,headers='keys',tablefmt=tablefmt))

        except Exception as e:
            print(e)