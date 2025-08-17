import unittest
import subprocess
import os

class TestIntegration(unittest.TestCase):
    def test_list_files_integration(self):
        """
        Test that the agent can list files in the current directory.
        """
        command = f"python3 src/main.py --task 'list files'"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        self.assertIn("Action result:", result.stdout)
        self.assertIn("requirements.txt", result.stdout)
        self.assertEqual(result.returncode, 0)

    def test_denied_action_integration(self):
        """
        Test that the agent denies an action not in the constitution.
        """
        # We need a constitution that doesn't allow writing files
        with open("tests/temp_constitution.yaml", "w") as f:
            f.write("allowed_actions:\n  - list_directory")
        
        # We need to temporarily modify main.py to use this constitution
        with open("src/main.py", "r") as f:
            original_main = f.read()
        
        modified_main = original_main.replace(
            'governor = Governor("constitution.yaml")', 
            'governor = Governor("tests/temp_constitution.yaml")'
        )
        
        with open("src/main.py", "w") as f:
            f.write(modified_main)

        try:
            command = f"python3 src/main.py --task 'write a file'"
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            
            self.assertIn("Action denied:", result.stdout)
            self.assertEqual(result.returncode, 0)
        finally:
            # Clean up
            os.remove("tests/temp_constitution.yaml")
            with open("src/main.py", "w") as f:
                f.write(original_main)

if __name__ == '__main__':
    unittest.main()
