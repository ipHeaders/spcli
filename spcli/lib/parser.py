import argparse

def parser():
    parser = argparse.ArgumentParser()
    parent_parser = argparse.ArgumentParser(add_help=False)

    subparsers = parser.add_subparsers(title='Silvperpeak Commands', dest='args')
##############################################################################    
#                            OTHER COMMANDS
##############################################################################
    parser.add_argument('-d', '--debug',
                                  required=False,
                                  #choices='ec',
                                  action='store_true',
                                  help="debug the cli")
    parser.add_argument('-v', '--version',
                                  required=False,
                                  #choices='ec',
                                  action='store_true',
                                  help="shows cli tool version")
##############################################################################    
#                            ORCHESTRATOR COMMANDS
##############################################################################
    orch_parser = subparsers.add_parser('orch',
                                            parents=[parent_parser],
                                            help="orchesrator commands",
                                            description='''''')
    orch_parser.add_argument('-info',
                                  required=False,
                                  #choices='ec',
                                  action='store_true',
                                  help="general information about the orchestrator")

    orch_parser.add_argument('-allowedip',
                                  required=False,
                                  #choices='ec',
                                  action='store_true',
                                  help="allowed ip's to access the orchestrator")
    
    orch_parser.add_argument('-users',
                                  required=False,
                                  #choices='ec',
                                  action='store_true',
                                  help="list of local users")
    orch_parser.add_argument('-sessions',
                                  required=False,
                                  #choices='ec',
                                  action='store_true',
                                  help="list user sessions on the orchestrator")
    orch_parser.add_argument('-backup',
                                  required=False,
                                  #choices='ec',
                                  action='store_true',
                                  help="orchestrator backup configuration")

##############################################################################    
#                            APPLIANCE COMMANDS
##############################################################################

    appliance_parser = subparsers.add_parser('appliance',
                                            parents=[parent_parser],
                                            help="edge connect appliance commands",
                                            description='''''')
    appliance_parser.add_argument('-site',
                                  required=False,
                                  metavar='',
                                  #choices='ec',
                                  nargs=1,
                                  #action='store_true',
                                  help="list of appliances for given site, must pass site [name]")
    appliance_parser.add_argument('-info',
                                  required=False,
                                  metavar='',
                                  nargs=1,
                                  help="appliance information, must pass [id]")
    appliance_parser.add_argument('-stat_config',
                                  required=False,
                                  #metavar='ID',
                                  #nargs='?',
                                  action='store_true',
                                  help="get appliance statistics configuration")
    appliance_parser.add_argument('-os_version',
                                  required=False,
                                  metavar='',
                                  nargs=1,
                                  #action='store_true',
                                  help="get software version information, must pass [id]")
    appliance_parser.add_argument('-banner',
                                  required=False,
                                  metavar='',
                                  nargs=1,
                                  #action='store_true',
                                  help="configured message of the day (motd) and issue banners for Edge Connect appliance, must pass [id]")

##############################################################################    
#                            BGP COMMANDS
##############################################################################
    bgp_parser = subparsers.add_parser('bgp',
                                            parents=[parent_parser],
                                            help="edge connect bgp commands",
                                            description='''''')
    bgp_parser.add_argument('-config',
                                  required=False,
                                  metavar='',
                                  nargs=1,
                                  #action='store_true',
                                  help="returns BGP configuration, must pass [id]")

    bgp_parser.add_argument('-neighbors',
                                  required=False,
                                  metavar='',
                                  nargs=1,
                                  #action='store_true',
                                  help="BGP neighbor configuration, must pass [id]")

    bgp_parser.add_argument('-summary',
                                  required=False,
                                  metavar='',
                                  nargs=1,
                                  #action='store_true',
                                  help="appliance BGP neighbors current state, must pass [id]")


    options = parser.parse_args()
    return options