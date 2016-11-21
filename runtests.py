#!/usr/bin/env python3
#
# Author: Benjamin Esquivel <benjamin.esquivel@linux.intel.com>

import os
import time
import doctest
import unittest

from doctest import DocTestSuite as doctest_suite
from doctest import DocFileSuite as docfile_suite
try:
    from xmlrunner import XMLTestRunner as test_runner
except ImportError:
    from unittest import TextTestRunner as test_runner

if __name__ == '__main__':
    testlist = unittest.defaultTestLoader.discover(start_dir='.')
    testlist.addTest(docfile_suite('readme-python.txt'))
    results = os.path.join(os.getcwd(), 'results',
            time.strftime("%Y%m%d%H%M%S"))
    try:
        runner = test_runner(verbosity=5, output=results)
    except TypeError:
        # for when TextTestRunner took place instead of XMLTestRunner
        runner = test_runner(verbosity=5)
    runner.run(testlist)
