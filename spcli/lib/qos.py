from pyedgeconnect import Orchestrator
from .BaseConnection import BaseConnection,create_dict,create_dict_from_list,tablefmt
from .BaseConnection import print_dict,print_list
from tabulate import tabulate


class QOS(BaseConnection):
    def __init__(self,):
        super().__init__()   
    def _get_appliance_inbound_shaper(self,options):
        ne_pk = f"{options.inbound_shaper[0]}.NE"
        try:
            orch = Orchestrator(self.url, verify_ssl=True, api_key=self.token)
            orch_return = orch.get_appliance_inbound_shaper(ne_id=ne_pk,cached=False)
            y = []

            for u in orch_return['wan']['traffic-class'].values():
                args = ['name','excess','flow_limit','max_bw','max_bw_abs','max_wait','min_bw','min_bw_abs','priority']
                x = create_dict(u,args)    
                y.append(x)
            #x = create_dict(orch_return,args)
            #print(tabulate(orch_return,tablefmt=tablefmt))
            print(tabulate(y,headers='keys',tablefmt=tablefmt))
        except Exception as e:
            print(e)