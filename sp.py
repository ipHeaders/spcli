
import argparse

parser = argparse.ArgumentParser()
parent_parser = argparse.ArgumentParser(add_help=False)
subparsers = parser.add_subparsers(title='subcommands', dest='action')


add_route_parser = subparsers.add_parser('bgp',
                                        parents=[parent_parser],
                                        description="bgp commands",
                                        help='bgp commands')

add_route_parser.add_argument('-status', #'-status',
                              #dest="route_domain_name",
                              required=False,
                              help="The route domain name to add")

add_route_parser.add_argument('-amount', #'-status',
                              #dest="route_domain_name",
                              required=False,
                              help="The route domain name to add")
                              
add_route_parser.add_argument('-stats', #'-stats',
                              #dest="route_domain_name",
                              required=False,
                              help="The route domain name to add")




options = parser.parse_args()
#print(options)

print(options)