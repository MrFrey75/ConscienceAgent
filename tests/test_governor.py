import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from governor import Governor

class TestGovernor(unittest.TestCase):
    def setUp(self):
        self.governor = Governor(os.path.join(os.path.dirname(__file__), 'test_constitution.yaml'))

    def test_approve_action_allowed(self):
        action = {'action': 'search_web', 'args': ['test']}
        self.assertTrue(self.governor.approve_action(action))

    def test_approve_action_denied(self):
        action = {'action': 'write_file', 'args': ['test.txt', 'hello']}
        self.assertFalse(self.governor.approve_action(action))

if __name__ == '__main__':
    unittest.main()
