#!/usr/bin/python
#
# commitmessage.py Version 2.0-alpha1
# Copyright 2002, 2003 Stephen Haberman
#

"""Some minor tests of the CVS utility functions."""
import os
import sys
import unittest

if __name__ == '__main__':
    sys.path.append('.')

from commitmessage.controllers.cvs import cvs_status, cvs_diff

class TestStatus(unittest.TestCase):
    """Test the cvs_status utility function."""

    def testBasic(self):
        os.chdir(os.path.expanduser('~/test/module1'))
        rev, delta = cvs_status('x.txt')
        self.assertEqual('1.6', rev)
        self.assertEqual('+2 -0', delta)

class TestDiff(unittest.TestCase):
    """Tests the cvs_diff utility function."""

    def testBasic(self):
        os.chdir(os.path.expanduser('~/test/module1'))
        diff = cvs_diff('x.txt', '1.6')
        self.assertEqual(318, diff.find('+More...down...here'))

if __name__ == '__main__':
    unittest.main()
