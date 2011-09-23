CMakeHelp
=========


CMake is a great build system and it has comprehensive reference
documentation, but if you have used the documentation (either online or
build into cmake) after a while of searching for help becomes tiresome
especially if you wan't to find what you are looking for fast.

That's why I created this small utility that enables you to quickly
search and read CMake's documentation.

The utility is a interactive command line where you can Tab your way
to the documentation you wan.

The following commands are available to you::

    command   -  Print help for a single command
    module    -  Print help for a single module
    property  -  Print help for a single property
    variable  -  Print help for a single variable

To get a list of available elments use Tab completetion::

    [CMake Help] command fi<TAB>
    file          find_file     find_library  

Compatibility
=============

This utility was developed on a Linux based system, so it
most likely will work on most Unix based systems where
CMake is available. There are only two requirements apart
from python that this utility requires. You need the 
cmake executable available on you system path and the
less pasger.

Testing
=======

Currently there is no unit tests and the amount of testing
done was very minimal so there might be some bugs.

If command completion does not work there might be 2 causes,
either you don't have readline or there was a problem while
getting keywords from cmake. No error is printed if cmake
was executed incorectly(all exceptions are caught during
command completion)...



