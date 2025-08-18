# Conscience Agent

![Version](https://img.shields.io/badge/version-2.0-blue.svg)
![Status](https://img.shields.io/badge/status-stable-green.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/python-3.9+-brightgreen.svg)

An experimental framework for building autonomous AI agents with a verifiable, safety-first architecture.

### The Core Idea

This project explores a fundamental question: How can we build powerful AI agents that we can trust?

Our solution is a "Three-Box" architecture that separates thought from action. Every task is handled by a team of three specialists:
1.  **The Proposer:** A creative engine that suggests possible actions.
2.  **The Governor:** A cautious rule-checker that approves or denies every action against a human-written "Constitution."
3.  **The Executor:** A careful worker that *only* performs actions that have been cryptographically approved by the Governor.

This design makes the agent's behavior auditable, controllable, and transparent by default.

### Dive Deeper

This repository contains extensive documentation for different audiences. Find the guide that's right for you.

* **For Users:**
    * [**`USER_GUIDE.md`**](./docs/USER_GUIDE.md) — Your primary guide to installing and using the desktop application.
    * [**`SIMPLE_EXPLANATION.md`**](./docs/SIMPLE_EXPLANATION.md) — Understand the project's core concepts through simple analogies.

* **For Researchers:**
    * [**`RESEARCH_GUIDE.md`**](./docs/RESEARCH_GUIDE.md) — Learn the workflow and strategies for using the agent as a powerful research assistant.

* **For Developers:**
    * [**`DEV_PLAN.md`**](./docs/DEV_PLAN.md) — The development plan that was followed to build the agent.
    * [**`GEMINI.md`**](./docs/GEMINI.md) — A guide for developers using the agent's core logic.

* **For Ethicists and Philosophers:**
    * [**`ETHICS.md`**](./docs/ETHICS.md) — An exploration of the philosophical and ethical principles behind the agent's design.

### Quick Start

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/conscience_agent.git
    cd conscience_agent
    ```

2.  **Create a Virtual Environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Application:**
    ```bash
    python3 src/main.py
    ```

5.  **Follow the User Guide:** For detailed instructions, please see the [**`USER_GUIDE.md`**](./docs/USER_GUIDE.md).

You can also build a distributable application using a tool like PyInstaller.

### Usage Examples

To give you a better idea of how the Conscience Agent works, here are a few examples of how you might interact with it.

**Example 1: Asking a simple question**

> **You:** "What is the capital of France?"
>
> **Agent:**
> *   **Proposer:** Suggests searching the web for "capital of France."
> *   **Governor:** Approves the action, as it aligns with the constitution's rules on information gathering.
> *   **Executor:** Runs the web search and returns the answer: "Paris."

**Example 2: A more complex task**

> **You:** "Write a Python script that prints the first 10 prime numbers."
>
> **Agent:**
> *   **Proposer:** Suggests writing a Python script with a function to check for prime numbers and a loop to print the first 10.
> *   **Governor:** Approves the action, as it falls within the agent's capabilities and doesn't violate any rules.
> *   **Executor:** Writes the script and provides it to you.

For more detailed examples and a deeper dive into the agent's capabilities, please see the [**`RESEARCH_GUIDE.md`**](./docs/RESEARCH_GUIDE.md).

### Contributing

This is an open-source experiment, and contributions are welcome! Whether you have ideas for new tools, improvements to the core logic, or new constitutional rules, please see our [**`CONTRIBUTING.md`**](./docs/CONTRIBUTING.md) guide to get started.

### Testing

To run the tests, use the following command:

```bash
./run_tests.sh
```

Alternatively, you can run the tests manually:

```bash
python3 -m unittest discover tests
```

### License

This project is licensed under the MIT License.
