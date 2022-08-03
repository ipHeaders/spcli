from pyedgeconnect import Orchestrator
from .BaseConnection import BaseConnection,create_dict,create_dict_from_list,tablefmt
from .BaseConnection import print_dict,print_list
from tabulate import tabulate

class FLOWS(BaseConnection):
    def __init__(self,):
        super().__init__()   
    def _get_appliance_flows_active(self,options):
        ne_pk = f"{options.id[0]}.NE"
        try:
            args = ['total_flows','stale_flows','inconsistent_flows','flows_with_issues','flows_optimized','flows_with_ignores','flows_passthrough','flows_management',
            'flows_asymmetric','flows_route_dropped','flows_firewall_dropped']

            orch = Orchestrator(self.url, verify_ssl=True, api_key=self.token)
            orch_return = orch.get_appliance_flows(ne_id=ne_pk)

            x = create_dict(orch_return['active'],args)
            flow_type = {'Flow Type': "Active Flows"}
            x = {**flow_type, **x}
            print(tabulate(x.items(),tablefmt=tablefmt))
        except Exception as e:
            print(e)
            
    def _get_appliance_flows_inactive(self,options):
        ne_pk = f"{options.id[0]}.NE"
        try:
            args = ['total_flows','stale_flows','inconsistent_flows','flows_with_issues','flows_optimized','flows_with_ignores','flows_passthrough','flows_management',
            'flows_asymmetric','flows_route_dropped','flows_firewall_dropped']

            orch = Orchestrator(self.url, verify_ssl=True, api_key=self.token)
            orch_return = orch.get_appliance_flows(ne_id=ne_pk)

            x = create_dict(orch_return['inactive'],args)
            flow_type = {'Flow Type': "Inactive Flows"}
            x = {**flow_type, **x}
         
            print(tabulate(x.items(),tablefmt=tablefmt))
        except Exception as e:
            print(e)