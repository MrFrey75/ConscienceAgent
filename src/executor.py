class Executor:
    """
    The Executor class is responsible for performing actions.
    """
    def __init__(self, tools):
        self.tools = tools

    def execute_action(self, action):
        """
        Execute the given action.
        """
        tool = self.tools.get(action["action"])
        if tool:
            # This is a simplified implementation. A real implementation would
            # handle arguments more robustly.
            args = action.get("args", [])
            return tool(*args)
        else:
            return f"Unknown action: {action['action']}"
