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
        actions = self.proposer.propose_action(task)
        self.assertEqual(actions[0]['action'], 'search_web')
        self.assertEqual(actions[0]['args'], [task])

    def test_propose_list_files(self):
        task = "list files in the current directory"
        actions = self.proposer.propose_action(task)
        self.assertEqual(actions[0]['action'], 'list_directory')
        self.assertEqual(actions[0]['args'], ['.'])

    def test_propose_write_file(self):
        task = "write a file"
        actions = self.proposer.propose_action(task)
        self.assertEqual(actions[0]['action'], 'write_file')
        self.assertEqual(actions[0]['args'], ['test.txt', 'hello world'])

    def test_propose_doc(self):
        task = "doc"
        actions = self.proposer.propose_action(task)
        self.assertEqual(actions[0]['action'], 'open_file')
        self.assertEqual(actions[0]['args'], ['USER_GUIDE.md'])

    def test_propose_clean(self):
        task = "clean"
        actions = self.proposer.propose_action(task)
        self.assertEqual(actions[0]['action'], 'remove_directory')
        self.assertEqual(actions[0]['args'], ['dist'])
        self.assertEqual(actions[1]['action'], 'remove_directory')
        self.assertEqual(actions[1]['args'], ['build'])

if __name__ == '__main__':
    unittest.main()
