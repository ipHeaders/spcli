=======================
spcli
=======================

.. image:: https://img.shields.io/badge/License-Apache_2.0-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0
.. image:: https://img.shields.io/github/issues/ipHeaders/spcli
   :target: https://img.shields.io/github/issues/ipHeaders/spcli
.. image:: https://img.shields.io/github/v/tag/ipHeaders/spcli
   :target: https://img.shields.io/github/v/tag/ipHeaders/spcli
.. image:: https://github.com/ipHeaders/spcli/actions/workflows/publish-to-pypi.yml/badge.svg
   :target: https://github.com/ipHeaders/spcli/actions/workflows/publish-to-pypi.yml


Silverpeak/Aruba SD-WAN Command Line Interface
This CLI tool is to query the Silverpeal/Aruba SD-WAN orchestrator and output the information in your terminal.


Getting Started
---------------
Requierements
~~~~~~~~~~~~~~~~~~~~
* Python >=3.7
* User with API KEY

To get started, install the CLI tool from Pypi ::

    pip3 install pyspcli


or download it directly from github::

    pip3 install git+https://github.com/NetDevLazg/spcli.git

Once the installation is successful, you will need to create a file with your api credentials.

* Create a folder in the following directory `mkdir ~/.spcli`
* Create a yml file with your credentials in `.spcli` directory
* Using `vim` 
   * `vim ~/.spcli/creds.yml`
* Using `nano`
   * `nano ~/.spcli/creds.yml`

The yml file needs to have the following variables.
Example::

    url: silverpeak-orch-use1.silverpeak.cloud
    token: a38b3360bb4d06fed7e53f77c8752d74bb4faeb4295385a25e02ebc2594d9074a16bb115fce4d4dc9826d824950504b6d23373


After the file is created and saved, please verify the cli tool version using the following command::

    sp -v
    version...installed: 0.0.6


Possible Errors
~~~~~~~~~~~~~~~~~~~~
If you receive an error saying "Command not found" make sure to add the location where the package is installed to your $PATH

Possible error::

    WARNING: The script sp is installed in '/Users/John/Library/Python/3.8/bin' which is not on PATH.


Fix::

    export PATH='$PATH:/Users/John/Library/Python/3.8/bin'


Help Function
---------------

To check possible commands, use the `-h` flag after a command. for example::

    sp -h
    usage: sp [-h] [-d] [-v] {orch,appliance,bgp} ...
    
    optional arguments:
      -h, --help            show this help message and exit
      -d, --debug           debug the cli
      -v, --version         shows cli tool version
    
    Silvperpeak Commands:
      {orch,appliance,bgp,flows}
        orch                orchesrator commands
        appliance           edge connect appliance commands
        bgp                 edge connect bgp commands
        flows               flows statistics on edge connect
    


