# Developer Guide

Welcome, developer. This guide provides a comprehensive overview of the Conscience Agent's architecture, development workflows, and contribution guidelines.

## Architecture

The Conscience Agent is built on a "Three-Box" architecture that separates the process of thinking from the act of doing. This design ensures that the agent's behavior is auditable, controllable, and transparent by default.

The three core components are:

1.  **The Proposer:** A creative engine that suggests possible actions.
2.  **The Governor:** A cautious rule-checker that approves or denies every action against a human-written "Constitution."
3.  **The Executor:** A careful worker that *only* performs actions that have been cryptographically approved by the Governor.

## File Descriptions

Here's a breakdown of the key files in the `src/` directory and their responsibilities:

*   **`main.py`**: The main entry point for the application. This script initializes the three core components and starts the main application loop.

*   **`proposer.py`**: Contains the logic for the Proposer, the creative engine that suggests possible actions based on the user's input.

*   **`governor.py`**: Contains the logic for the Governor, the rule-checker that approves or denies every action against the "Constitution."

*   **`executor.py`**: Contains the logic for the Executor, the component that performs actions that have been approved by the Governor.

*   **`gui.py`**: The graphical user interface for the application. This is the primary way for users to interact with the agent.

*   **`logger.py`**: Handles logging for the application. This is used to record the agent's actions and decisions for auditing and debugging purposes.

*   **`persona.py`**: Manages the agent's persona, which defines its personality and style of interaction.

*   **`tools/`**: This directory contains the various tools that the agent can use to interact with the outside world.
    *   **`file_system.py`**: Tools for file system operations, such as reading, writing, and listing files.
    *   **`system.py`**: Tools for system-level operations, such as running shell commands.
    *   **`web_search.py`**: Tools for searching the web.

## Development Workflows

Our development process is designed to be as transparent and collaborative as possible. We use a standard Git workflow with feature branches, pull requests, and code reviews.

### Getting Started

1.  **Fork the repository:** Start by forking the main repository to your own GitHub account.
2.  **Clone your fork:** Clone your fork to your local machine and set up the development environment.
3.  **Create a feature branch:** Create a new branch for each new feature or bug fix.

### Making Changes

1.  **Write your code:** Make your changes, following the existing code style and conventions.
2.  **Write tests:** Add or update tests to ensure that your changes are working correctly.
3.  **Run tests:** Run the full test suite to make sure that your changes haven't broken anything.

### Submitting Changes

1.  **Push your changes:** Push your changes to your fork on GitHub.
2.  **Create a pull request:** Create a pull request from your feature branch to the main repository.
3.  **Request a review:** Request a review from one of the project maintainers.

## Contribution Guidelines

We welcome contributions from the community. To ensure a smooth and collaborative process, please follow these guidelines:

*   **Be respectful:** Treat all other contributors with respect.
*   **Be clear:** Write clear and concise commit messages, pull request descriptions, and comments.
*   **Be patient:** The review process may take some time, so please be patient.

For more detailed information, please see our [**`CONTRIBUTING.md`**](./CONTRIBUTING.md) guide.