#!python
import lib
import pkg_resources

def main():

    options = lib.parser.parser()

    if (options.debug == True):
        print('debuging...options...',options)
    if (options.version == True):
        from importlib_metadata import version
        print(f'version...installed:',version('pyspcli'))

    if (options.args == "orch" and options.allowedip == True):
        lib.orch.ORCH()._get_ipAllowList()
    elif (options.args == "orch" and options.users == True):
        lib.orch.ORCH()._get_get_all_users()
    elif (options.args == "orch" and options.info == True):
        lib.orch.ORCH()._get_orchestrator_server_info()
    elif (options.args == "orch" and options.sessions == True):
        lib.orch.ORCH()._get_orchestrator_sessions()
    elif (options.args == "orch" and options.backup == True):
        lib.orch.ORCH()._get_orchestrator_backup_config()
    elif (options.args == "orch" and options.info == False):
        lib.orch.ORCH()._get_orchestrator_server_brief()
#########################################################################################
    elif (options.args == "appliance" and options.info != None):
        lib.appliance.APPLIANCE()._get_appliance_info(options)
    elif (options.args == "appliance" and options.stat_config == True):
        lib.appliance.APPLIANCE()._get_appliance_stats_config()
    elif (options.args == "appliance" and options.os_version != None):
        lib.appliance.APPLIANCE()._get_appliance_software_version(options)
    elif (options.args == "appliance" and options.banner != None):
        lib.appliance.APPLIANCE()._get_appliance_login_banners(options)
    elif (options.args == "appliance" and options.dns != None):
        lib.appliance.APPLIANCE()._get_appliance_dns(options)
    elif (options.args == "appliance"):
        lib.appliance.APPLIANCE()._get_appliances(options)
#########################################################################################    
    elif (options.args == "bgp" and options.config != None):
        lib.bgp.BGP()._get_appliance_bgp_config(options)
    elif (options.args == "bgp" and options.neighbors != None):
        lib.bgp.BGP()._get_appliance_bgp_neighbors(options)
    elif (options.args == "bgp" and options.summary != None):
        lib.bgp.BGP()._get_appliance_bgp_state(options)
#########################################################################################  
    elif (options.args == "flows" and options.active == True):
        lib.flows.FLOWS()._get_appliance_flows_active(options)
    elif (options.args == "flows" and options.inactive == True):
        lib.flows.FLOWS()._get_appliance_flows_inactive(options)
    elif (options.args == "flows" and options.all == True):
        lib.flows.FLOWS()._get_appliance_flows_all(options)
    elif (options.args == "flows" and options.ip != None):
        lib.flows.FLOWS()._get_appliance_flows_ip(options)
    elif (options.args == "flows" and options.port != None):
        lib.flows.FLOWS()._get_appliance_flows_port(options)
    elif (options.args == "flows" and options.app != None):
        lib.flows.FLOWS()._get_appliance_flows_app(options)
    elif (options.args == "flows" and options.dscp != None):
        lib.flows.FLOWS()._get_appliance_flows_dscp(options)
if __name__ == "__main__":
    main()