# Conscience Agent User Guide

Welcome to the Conscience Agent desktop application! This guide will walk you through the features of the user interface.

### Launching the Application

To start the application, run the executable file located in the `dist` directory:

```bash
./dist/ConscienceAgent
```

### The Main Window

The user interface is divided into two main sections: a control pane on the left and the main interaction pane on the right.

![Main Window Layout](https-placeholder-for-screenshot.com) *(Placeholder for a screenshot of the UI)*

#### Left Pane: Controls & Configuration

This pane contains two tabs:

1.  **File Explorer:** This tab shows a live tree view of the project's directory. You can use it to see the files the agent creates or modifies in real-time.
2.  **Constitution Editor:** This tab displays the contents of `constitution.yaml`. You can edit the agent's rules directly in this text box. Click the **"Save Constitution"** button to apply your changes.

#### Right Pane: Task & Agent Output

This is where you will interact with the agent.

1.  **Task Input Field:** Enter the task you want the agent to perform in this text box at the top.
2.  **Control Buttons:**
    *   **Run Task:** Starts the agent with the task from the input field.
    *   **Stop Task:** Becomes active when a task is running. Click it to stop the agent's current task.
3.  **Log Viewer:** This large, read-only area displays the agent's thought process in real-time. To make it easy to follow, messages are color-coded:
    *   **System Messages:** General messages about the agent's state.
    *   **Proposer:** The agent's proposed actions.
    *   **Governor:** Green for approved actions, red for denied actions.
    *   **Executor:** The results of the executed actions.

### Basic Workflow

1.  Enter a task in the **Task Input Field**.
2.  Click **Run Task**.
3.  Observe the agent's thought process in the **Log Viewer**.
4.  View any created or modified files in the **File Explorer**.
5.  If needed, modify the agent's rules in the **Constitution Editor** and save them for the next run.
