from pyedgeconnect import Orchestrator
from lib.BaseConnection import BaseConnection,create_dict,create_dict_from_list,tablefmt
from lib.BaseConnection import print_dict,print_list
from tabulate import tabulate
import datetime


class BGP(BaseConnection):
    def __init__(self,):
        super().__init__()   

    def _get_appliance_bgp_config(self,options):
        ne_pk = f"{options.config[0]}.NE"
        try:
            args = ['stale_path_time','enable_gms_marked','enable','remote_as_path_advertise','log_nbr_msgs','rtr_id','asn','max_restart_time','graceful_restart_en']
            orch = Orchestrator(self.url, verify_ssl=True, api_key=self.token)
            orch_return = orch.get_appliance_bgp_config(ne_id=ne_pk)

            x = create_dict(orch_return,args)
            print(tabulate(x.items(),tablefmt=tablefmt))
        except Exception as e:
            print(e)
        
            
    def _get_appliance_bgp_neighbors(self,options):
        ne_pk = f"{options.neighbors[0]}.NE"
        try:
            orch = Orchestrator(self.url, verify_ssl=True, api_key=self.token)
            orch_return = orch.get_appliance_bgp_neighbors(ne_id=ne_pk)
            y = []
            for u in orch_return.values():
                #print(v)
                args = ['self','enable','hold','lcl_interface','next_hop_self','remote_as','rtmap_inbound','rtmap_outbound','type']

                x = create_dict(u,args)    
                y.append(x)
            print(tabulate(y,headers='keys',tablefmt=tablefmt))
            
        except Exception as e:
            print(e)

    def _get_appliance_bgp_state(self,options):
        ne_pk = f"{options.summary[0]}.NE"
        try:
            orch = Orchestrator(self.url, verify_ssl=True, api_key=self.token)
            orch_return = orch.get_appliance_bgp_state(ne_id=ne_pk)
            y = []
            #print(tabulate(orch_return['summary'].items(),tablefmt=tablefmt))
            #print(tabulate(orch_return['neighbor']['neighborState'],tablefmt=tablefmt))

            for u in orch_return['neighbor']['neighborState']:
                #print(u)
                args = ['local_ip','peer_ip','asn','peer_state_str','last_err','last_err_subcode',
                        'time_established','rcvd_pfxs','sent_pfxs']
            
                x = create_dict(u,args)    
                y.append(x)
                #print_dict(u)
            print(tabulate(y,headers='keys',tablefmt=tablefmt))
            
        except Exception as e:
            print(e)