import argparse
from proposer import Proposer
from governor import Governor
from executor import Executor
from logger import setup_logger
from tools.file_system import read_file, write_file, list_directory, remove_directory
from tools.web_search import search_web
from tools.system import open_file

def main():
    """
    Main entry point for the Conscience Agent.
    """
    parser = argparse.ArgumentParser(description="Conscience Agent CLI")
    parser.add_argument("--task", type=str, required=True, help="The task for the agent to perform.")
    args = parser.parse_args()

    logger = setup_logger()
    logger.info("Starting Conscience Agent")

    proposer = Proposer()
    governor = Governor("constitution.yaml")
    
    tools = {
        "read_file": read_file,
        "write_file": write_file,
        "list_directory": list_directory,
        "search_web": search_web,
        "open_file": open_file,
        "remove_directory": remove_directory,
    }
    executor = Executor(tools)

    task = args.task
    logger.info(f"Received task: {task}")
    print(f"Received task: {task}")

    actions = proposer.propose_action(task)
    logger.info(f"Proposed actions: {actions}")
    print(f"Proposed actions: {actions}")

    for action in actions:
        if governor.approve_action(action):
            logger.info(f"Action approved: {action}")
            print(f"Action approved: {action}")
            result = executor.execute_action(action)
            logger.info(f"Action result: {result}")
            print(f"Action result: {result}")
        else:
            logger.warning(f"Action denied: {action}")
            print(f"Action denied: {action}")

    logger.info("Conscience Agent finished task.")

if __name__ == "__main__":
    main()
