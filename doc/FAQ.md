FAQ - Frequently Asked Questions
================================


MIB issues
----------

Why not use the system  MIBs ?

- Because I found some broken MIBs on some distros. I prefer to use a bit more disk space, and have a consistent and tested set of MIBs instead of spending time telling Cisco how messy they are.


Why is SMIPATH defined in the code ?

- This is not strictly necessary, but I have found that on some platform (notably Ubuntu), SMI has built-in default compiled SMIPATH, making it to go to its own PATH to find and load MIBs. It then produce all sorts of strange problems like segfaults and SMI lint errors.
