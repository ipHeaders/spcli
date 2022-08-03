from pyedgeconnect import Orchestrator
from .BaseConnection import BaseConnection,create_dict,create_dict_from_list,tablefmt
from .BaseConnection import print_dict,print_list
from tabulate import tabulate

class APPLIANCE(BaseConnection):
    def __init__(self,):
        super().__init__()   
    def _get_appliances(self,options):
        device_list = []
        if options.site == None:
            try:
                orch = Orchestrator(self.url, verify_ssl=True, api_key=self.token)
                orch_return = orch.get_appliances()
                for device in orch_return:
                    args = ['id','site','IP','serial','mode','hostName','softwareVersion','systemBandwidth','haPeer']
                    x = create_dict(device,args)
                    device_list.append(x)
                print(tabulate(device_list,headers='keys',tablefmt=tablefmt))
            except Exception as e:
                print(e)
        else:
            try:
                orch = Orchestrator(self.url, verify_ssl=True, api_key=self.token)
                orch_return = orch.get_appliances()
                for device in orch_return:
                    if device['site'] == options.site[0]:
                        args = ['id','site','IP','serial','mode','hostName','softwareVersion','systemBandwidth','haPeer']
                        x = create_dict(device,args)
                        device_list.append(x)
                #print(device_list)
                print(tabulate(device_list,headers='keys',tablefmt=tablefmt))
            except Exception as e:
                print(e)
    def _get_appliance_info(self,options):
        ne_pk = f"{options.info[0]}.NE"
        try:
            orch = Orchestrator(self.url, verify_ssl=True, api_key=self.token)
            orch_return = orch.get_appliance_info(ne_pk)
            print(tabulate(orch_return.items(),tablefmt=tablefmt))

        except Exception as e:
            print(e)

    def _get_appliance_stats_config(self):
        try:
            orch = Orchestrator(self.url, verify_ssl=True, api_key=self.token)
            orch_return = orch.get_appliance_stats_config()
            print(tabulate(orch_return.items(),tablefmt=tablefmt))

        except Exception as e:
            print(e)
    def _get_appliance_software_version(self,options):
        ne_pk = f"{options.os_version[0]}.NE"
        try:
            orch = Orchestrator(self.url, verify_ssl=True, api_key=self.token)
            orch_return = orch.get_appliance_software_version(ne_pk=ne_pk, cached=False)
            y = []
            for u in orch_return:
                args = ['partition','build_version','build_time','active','next_boot','fallback_boot']

                x = create_dict(u,args)    
                y.append(x)
            print(tabulate(y,headers='keys',tablefmt=tablefmt))

        except Exception as e:
            print(e)
    def _get_appliance_login_banners(self,options):
        ne_pk = f"{options.banner[0]}.NE"
        try:
            orch = Orchestrator(self.url, verify_ssl=True, api_key=self.token)
            orch_return = orch.get_appliance_login_banners(ne_id=ne_pk, cached=False)
            print(tabulate(orch_return.items(),tablefmt=tablefmt))

        except Exception as e:
            print(e)
    def _get_appliance_dns(self,options):
        ne_pk = f"{options.dns[0]}.NE"
        try:
            orch = Orchestrator(self.url, verify_ssl=True, api_key=self.token)
            orch_return = orch.get_appliance_dns(ne_id=ne_pk, cached=False)
            y = []
            #print_dict(orch_return)
            for u in orch_return.values():
                for u in u.values():
                    args = ['self','address','srcinf','vrf_id']
                    x = create_dict(u,args)    
                    y.append(x)
            print(tabulate(y,headers='keys',tablefmt=tablefmt))

        except Exception as e:
            print(e)