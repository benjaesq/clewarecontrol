To build the Python code:
 - install the Python development package
   on Debian this is called e.g. "python2.7-dev" or "python3.2-dev"
   on Fedora "python-devel" for python 2 or "python3-devel" for python 3

 - install the swig package
   on Debian and Fedora this is called "swig"

 - create the python module and install it in your system:

    # make cleware_python

   or for python3:

    # make cleware_python3

   Note that the # symbol at the beginning of a line means it has to be
   executed with sufficient priviledges.

   This will produce the appropriate _cleware.so and cleware.py modules and
   copy them to your system's module path.

 - use the cleware.py package:
   open a python or a python3 command line interpreter and import the cleware
   module:

    >>> import cleware

   Instantiate a Cleware USB access object:

    >>> c = cleware.CUSBaccess()

   Enumerate the cleware devices attached to the system

    >>> num = c.OpenCleware()

   More information on how to use the cleware.py module can be found at the
   example.py script. (e.g. execute python example.py)
   make sure that the user you run your scripts with has enough rights to
   access the USB devices!
