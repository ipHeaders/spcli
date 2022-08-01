
import lib

def main():

    options = lib.parser.parser()

    if (options.debug == True):
        print('debuging...options...',options)

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
    elif (options.args == "appliance"):
        lib.appliance.APPLIANCE()._get_appliances(options)
#########################################################################################    
    elif (options.args == "bgp" and options.config != None):
        lib.bgp.BGP()._get_appliance_bgp_config(options)
    elif (options.args == "bgp" and options.neighbors != None):
        lib.bgp.BGP()._get_appliance_bgp_neighbors(options)
    elif (options.args == "bgp" and options.summary != None):
        lib.bgp.BGP()._get_appliance_bgp_state(options)



if __name__ == "__main__":
    main()