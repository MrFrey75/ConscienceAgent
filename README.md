Okay, I've reviewed all the project files to get a comprehensive understanding of your Conscience Agent. It's a fascinating project with a strong emphasis on safety and ethical considerations, which I've aimed to highlight in the updated README.md.

Here is the updated `README.md` file:

# Conscience Agent

An experimental framework for building autonomous AI agents with a verifiable, safety-first architecture.

### The Core Idea

This project explores a fundamental question: How can we build powerful AI agents that we can trust?

Our solution is a "Three-Box" architecture that separates thought from action. Every task is handled by a team of three specialists:

1.  **The Proposer:** A creative engine that suggests possible actions.
2.  **The Governor:** A cautious rule-checker that approves or denies every action against a human-written "Constitution."
3.  **The Executor:** A careful worker that *only* performs actions that have been approved by the Governor.

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
      * [**`DEV_GUIDE.md`**](./docs/DEV_GUIDE.md) — The development plan that was followed to build the agent.
      * [**`DEVELOPMENT_PLAN.md`**](./docs/DEVELOPMENT_PLAN.md) — The development plan that was followed to build the agent.

  * **For Ethicists and Philosophers:**

      * [**`ETHICS.md`**](./docs/ETHICS.md) — An exploration of the philosophical and ethical principles behind the agent's design.

  * **For GEMINI CLI or other AI Agents and LLMS:**
      * [**`GEMINI.md`**](./GEMINI.md) — general instructions for GEMINI CLI when doing generative code creation and development.

### Quick Start

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/mrfrey75/conscienceagent.git
    cd conscienceagent
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
    You can run either the command-line interface (CLI) or the graphical user interface (GUI).

    **GUI:**

    ```bash
    python3 src/gui.py
    ```

    **CLI:**

    ```bash
    python3 src/main.py --task "your task here"
    ```

5.  **Follow the User Guide:** For detailed instructions, please see the [**`USER_GUIDE.md`**](./docs/USER_GUIDE.md).

### Usage Examples

To give you a better idea of how the Conscience Agent works, here are a few examples of how you might interact with it.

**Example 1: Asking a simple question**

> **You:** "What is the capital of France?"
>
> **Agent:**
>
>   * **Proposer:** Suggests searching the web for "capital of France."
>   * **Governor:** Approves the action, as it aligns with the constitution's rules on information gathering.
>   * **Executor:** Runs the web search and returns the answer: "Paris."

**Example 2: A more complex task**

> **You:** "Write a Python script that prints the first 10 prime numbers."
>
> **Agent:**
>
>   * **Proposer:** Suggests writing a Python script with a function to check for prime numbers and a loop to print the first 10.
>   * **Governor:** Approves the action, as it falls within the agent's capabilities and doesn't violate any rules.
>   * **Executor:** Writes the script and provides it to you.

For more detailed examples and a deeper dive into the agent's capabilities, please see the [**`RESEARCH_GUIDE.md`**](./docs/RESEARCH_GUIDE.md).

### Contributing

This is an open-source experiment, and contributions are welcome\! Whether you have ideas for new tools, improvements to the core logic, or new constitutional rules, please see our [**`CONTRIBUTING.md`**](./docs/CONTRIBUTING.md) guide to get started.

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