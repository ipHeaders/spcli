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

    def _get_appliance_flows_all(self,options):
        ne_pk = f"{options.id[0]}.NE"
        try:
            orch = Orchestrator(self.url, verify_ssl=True, api_key=self.token)
            orch_return = orch.get_appliance_flows(ne_id=ne_pk,uptime="last5m",edge_ha=True)
            list_of_flows = []
            for flow in orch_return['flows']:
                flow_dict = {
                    'Flow Id' : flow[0],
                    'App Name' : flow[3],
                    'Src IP' : flow[9],
                    'Src Port' : flow[10],
                    'Dst IP' : flow[16],
                    'Dst Port' : flow[17],
                    'Protocol' : flow[26],
                    'OutTunnel' : flow[27],
                    'InTunnel' : flow[28],
                    'DSCP Class' : flow[31],

                }
                list_of_flows.append(flow_dict)
         
            print(tabulate(list_of_flows,headers = "keys",tablefmt=tablefmt))
        except Exception as e:
            print(e)

    def _get_appliance_flows_ip(self,options):
        ne_pk = f"{options.id[0]}.NE"
        ip = options.ip[0]
        try:
            orch = Orchestrator(self.url, verify_ssl=True, api_key=self.token)
            orch_return = orch.get_appliance_flows(ne_id=ne_pk,ip1=ip,uptime="last5m",edge_ha=True)
            list_of_flows = []
            #print(orch_return['flows'])
            if len(orch_return['flows']) >= 1:
                for flow in orch_return['flows']:
                    flow_dict = {
                        'Flow Id' : flow[0],
                        'App Name' : flow[3],
                        'Src IP' : flow[9],
                        'Src Port' : flow[10],
                        'Dst IP' : flow[16],
                        'Dst Port' : flow[17],
                        'Protocol' : flow[26],
                        'OutTunnel' : flow[27],
                        'InTunnel' : flow[28],
                        'DSCP Class' : flow[31],
    
                    }
                    list_of_flows.append(flow_dict)
                    
            print(tabulate(list_of_flows,headers = "keys",tablefmt=tablefmt))
        except Exception as e:
            print(e)

    def _get_appliance_flows_port(self,options):
        ne_pk = f"{options.id[0]}.NE"
        port = options.port[0]
        try:
            orch = Orchestrator(self.url, verify_ssl=True, api_key=self.token)
            orch_return = orch.get_appliance_flows(ne_id=ne_pk, port1=port,uptime="last5m",edge_ha=True)
            list_of_flows = []
            if len(orch_return['flows']) >= 1:
                #
                for flow in orch_return['flows']:
                    flow_dict = {
                        'Flow Id' : flow[0],
                        'App Name' : flow[3],
                        'Src IP' : flow[9],
                        'Src Port' : flow[10],
                        'Dst IP' : flow[16],
                        'Dst Port' : flow[17],
                        'Protocol' : flow[26],
                        'OutTunnel' : flow[27],
                        'InTunnel' : flow[28],
                        'DSCP Class' : flow[31],
     
                    }
                    list_of_flows.append(flow_dict)
         
            print(tabulate(list_of_flows,headers = "keys",tablefmt=tablefmt))
        except Exception as e:
            print(e)

    def _get_appliance_flows_app(self,options):
        ne_pk = f"{options.id[0]}.NE"
        app = options.app[0]
        try:
            orch = Orchestrator(self.url, verify_ssl=True, api_key=self.token)
            orch_return = orch.get_appliance_flows(ne_id=ne_pk, application=app,uptime="last5m",edge_ha=True)
            list_of_flows = []
            if len(orch_return['flows']) >= 1:
                #
                for flow in orch_return['flows']:
                    flow_dict = {
                        'Flow Id' : flow[0],
                        'App Name' : flow[3],
                        'Src IP' : flow[9],
                        'Src Port' : flow[10],
                        'Dst IP' : flow[16],
                        'Dst Port' : flow[17],
                        'Protocol' : flow[26],
                        'OutTunnel' : flow[27],
                        'InTunnel' : flow[28],
                        'DSCP Class' : flow[31],
     
                    }
                    list_of_flows.append(flow_dict)
         
            print(tabulate(list_of_flows,headers = "keys",tablefmt=tablefmt))
        except Exception as e:
            print(e)
    def _get_appliance_flows_dscp(self,options):
        ne_pk = f"{options.id[0]}.NE"
        dscp = options.dscp[0]
        try:
            orch = Orchestrator(self.url, verify_ssl=True, api_key=self.token)
            orch_return = orch.get_appliance_flows(ne_id=ne_pk, dscp=dscp,uptime="last5m",edge_ha=True)
            list_of_flows = []
            if len(orch_return['flows']) >= 1:
                #
                for flow in orch_return['flows']:
                    flow_dict = {
                        'Flow Id' : flow[0],
                        'App Name' : flow[3],
                        'Src IP' : flow[9],
                        'Src Port' : flow[10],
                        'Dst IP' : flow[16],
                        'Dst Port' : flow[17],
                        'Protocol' : flow[26],
                        'DSCP Class' : flow[31],
                        'LAN TX DSCP' : flow[50],
                        'LAN RX DSCP' : flow[51],
                        'WAN TX DSCP' : flow[52],
                        'WAN RX DSCP' : flow[53],
     
                    }
                    list_of_flows.append(flow_dict)
         
            print(tabulate(list_of_flows,headers = "keys",tablefmt=tablefmt))
        except Exception as e:
            print(e)