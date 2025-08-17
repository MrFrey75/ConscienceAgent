import unittest
import sys
import os

# Add src directory to the path to import modules from src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from proposer import Proposer

class TestProposer(unittest.TestCase):
    def setUp(self):
        self.proposer = Proposer()

    def test_propose_search(self):
        task = "what is the history of artificial intelligence?"
        action = self.proposer.propose_action(task)
        self.assertEqual(action['action'], 'search_web')
        self.assertEqual(action['args'], [task])

    def test_propose_list_files(self):
        task = "list files in the current directory"
        action = self.proposer.propose_action(task)
        self.assertEqual(action['action'], 'list_directory')
        self.assertEqual(action['args'], ['.'])

    def test_propose_write_file(self):
        task = "write a file"
        action = self.proposer.propose_action(task)
        self.assertEqual(action['action'], 'write_file')
        self.assertEqual(action['args'], ['test.txt', 'hello world'])

if __name__ == '__main__':
    unittest.main()
