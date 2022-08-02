# spcli

### Description
This CLI tool is to query the Silverpeal/Aruba SD-WAN orchestrator and output the information in your terminal.


### Getting Started
###### Requierements
* Python >=3.7

To get started, instal the CLI tool using the python3 package manager [pip]

`pip3 install git+https://github.com/NetDevLazg/spcli.git`

Once the installation is successful, you can check with the following command

```
❯ sp -v
version...installed: 0.0.6
```

### Help Function

To check possible commands, use the `-h` flag after a command. for example.
```
❯ sp -h
usage: sp [-h] [-d] [-v] {orch,appliance,bgp} ...

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           debug the cli
  -v, --version         shows cli tool version

Silvperpeak Commands:
  {orch,appliance,bgp}
    orch                orchesrator commands
    appliance           edge connect appliance commands
    bgp                 edge connect bgp commands

```
