# Proposer Module

class Proposer:
    """
    The Proposer class is responsible for generating action proposals.
    """
    def __init__(self):
        pass

    def propose_action(self, task):
        """
        Propose a sequence of actions based on the given task.
        """
        actions = []
        if "list files and read readme" in task:
            actions.append({"action": "list_directory", "args": ["."]})
            actions.append({"action": "read_file", "args": ["README.md"]})
        elif "history of artificial intelligence" in task:
            actions.append({"action": "search_web", "args": [task]})
        elif "list files" in task:
            actions.append({"action": "list_directory", "args": ["."]})
        elif "doc" in task:
            actions.append({"action": "open_file", "args": ["USER_GUIDE.md"]})
        elif "clean" in task:
            actions.append({"action": "remove_directory", "args": ["dist"]})
            actions.append({"action": "remove_directory", "args": ["build"]})
        else:
            actions.append({"action": "write_file", "args": ["test.txt", "hello world"]})
        return actions
