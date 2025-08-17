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

* **For a Quick Overview (Non-Technical):**
    * [**`SIMPLE_EXPLANATION.md`**](./SIMPLE_EXPLANATION.md) — Understand the project's core concepts through simple analogies.

* **For Users and Researchers:**
    * [**`RESEARCH_GUIDE.md`**](./RESEARCH_GUIDE.md) — Learn the workflow and strategies for using the agent as a powerful research assistant.

* **For Developers:**
    * [**`GEMINI.md`**](./GEMINI.md) — A guide for developers using the agent within the Gemini CLI.
    * [**`DEV_PLAN.md`**](./DEV_PLAN.md) — The development plan for the Conscience Agent.

* **For Ethicists and Philosophers:**
    * [**`ETHICS.md`**](./ETHICS.md) — An exploration of the philosophical and ethical principles behind the agent's design.

### Quick Start

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/fray/conscience_agent.git
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd conscience_agent
    ```
3.  **Start a chat with the agent:**
    ```bash
    gemini chat
    ```

### Contributing

This is an open-source experiment, and contributions are welcome! Whether you have ideas for new tools, improvements to the core logic, or new constitutional rules, please see our [**`CONTRIBUTING.md`**](./CONTRIBUTING.md) guide to get started.

### Testing

To run the tests, use the following command:

```bash
python3 -m unittest discover tests
```

### License

This project is licensed under the MIT License.