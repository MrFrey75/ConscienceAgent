import unittest
from unittest.mock import MagicMock
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from executor import Executor

class TestExecutor(unittest.TestCase):
    def setUp(self):
        self.mock_search = MagicMock()
        self.mock_list = MagicMock()
        self.mock_write = MagicMock()
        self.mock_read = MagicMock()
        
        tools = {
            "search_web": self.mock_search,
            "list_directory": self.mock_list,
            "write_file": self.mock_write,
            "read_file": self.mock_read,
        }
        self.executor = Executor(tools)

    def test_execute_search_web(self):
        action = {'action': 'search_web', 'args': ['testing']}
        self.executor.execute_action(action)
        self.mock_search.assert_called_once_with('testing')

    def test_execute_list_directory(self):
        action = {'action': 'list_directory', 'args': ['.']}
        self.executor.execute_action(action)
        self.mock_list.assert_called_once_with('.')

    def test_execute_write_file(self):
        action = {'action': 'write_file', 'args': ['test.txt', 'content']}
        self.executor.execute_action(action)
        self.mock_write.assert_called_once_with('test.txt', 'content')

    def test_execute_read_file(self):
        action = {'action': 'read_file', 'args': ['test.txt']}
        self.executor.execute_action(action)
        self.mock_read.assert_called_once_with('test.txt')

    def test_unknown_action(self):
        action = {'action': 'unknown_action'}
        result = self.executor.execute_action(action)
        self.assertEqual(result, "Unknown action: unknown_action")

if __name__ == '__main__':
    unittest.main()
