Agent-Jones
===========

Agent-Jones is a web-service used to configure and retrieve info from Cisco devices.
Mostly switches, but it could as well be used for routers. Its goal is to serve as a back-end
for nice GUIs and collectors applications. As such, it does't have has any GUI.

The wholestuff is written in Python, using the [Flask](http://flask.pocoo.org/) micro-framework, and a very nice SNMP lib for Python called snimpy [1](http://vincent.bernat.im/en/blog/2013-snimpy.html), [2](https://github.com/vincentbernat/snimpy).


Status
------

It is deployed in a network with about 1'000 devices, WAN and LAN, routers and switches, all Cisco. It works, but I would gladly accept patches and enhancements.


Features
--------

- Get info from a single device.
- Save the running-config to startup-config.
- Assign a port to a VLAN.
- Get the vlan list from a device (currently only native vlans).
- GET interfaces from a device. Option to list the MAC addresses of devices connected to each port.
- Configure an interface : adminStatus and ifAlias (called description in Cisco language).
- List the connected MAC addresses : MAC(ethernet) to port mappings from a device.
- Get the interface counters of one interface.


Screenshots
-----------

Everyone wants [screenshots](http://FIXME).


Limitations
-----------

- not tested on non-Cisco devices. It could work because I used mostly "standard" MIBs (whatever "standard" means in this context).


Assumptions
-----------

The following IOS commands might be present on modeled devices to allow for long-term indices persistence, but their presence are not guaranteed. The modeling does not dependent on them. There are anyway a good starting point for your Cisco configuration templates.

    snmp-server ifindex persist
    snmp mib persist cbqos


Installation
------------

See INSTALL.md


Usage
-----

Using the web-service is as easy as any such web-service. This is an example with curl, adapt to your own language.

    curl -u user:password http://0.0.0.0:5000/aj/api/v1/device/switch1.domain.com


API Documentation
-----------------

    http://0.0.0.0:5000/xdoc/


Troubleshooting
---------------

There is a log file defined in config.py. Tail it. Same way, check the Apache log files if you implemented it as a WSGI application.


Dependencies
------------

- works as a virtualenv to protect your instance from courageaous system-admins using OS-upgrade without too much knowledge.
- python 2.6 (might work for higher versions)


Extension / development
-----------------------

be sure to understand Flask-restful and snimpy, then the code should be easy to extend.


License
-------

GPL V2.


Author
------

- [Charles Bueche](http://www.netnea.com/cms/netnea-the-team/charles-bueche/) wrote the initial version.


Support
-------

For easy questions, [feel free to email me](http://address-protector.com/frTvcQ8oOaRDkfAzpUdS3oXFYt7cPQ8kLrI4lg2n4TblNc83DGf4yhBUfdrndqvn). For more, I will be very happy to provide commercial support.


Credits
-------

- [Connectis AG, Bern](http://www.connectis.ch)
- [Vincent Bernat](http://vincent.bernat.im/en/)