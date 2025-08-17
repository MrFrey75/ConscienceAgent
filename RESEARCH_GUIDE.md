# Unlocking Research Potential: A Guide to Using the Conscience Agent

### Introduction: Your New Research Partner

Welcome, researcher. The Conscience Agent is more than a simple script; it's designed to be your tireless, safe, and completely transparent research assistant.

This guide is about a **workflow**—a way of thinking and working with the agent to go from a broad question to a focused, well-supported conclusion. Think of yourself as the lead researcher; your role is to provide the strategy, while the agent handles the legwork of searching, collecting, and organizing information.

### The Core Workflow: A Cycle of Inquiry

Effective research with the agent is an iterative process:

1.  **Task (You):** You begin by giving the agent a high-level research goal.
2.  **Act (Agent):** The agent breaks down your goal into actions (searching, writing notes) and executes them after approval.
3.  **Review (You):** You examine the results in the `scratch/` directory and the agent's on-screen log.
4.  **Refine (You):** Based on what you've reviewed, you give the agent a new, more focused task. This cycle repeats, drilling deeper into the topic.

---

### Phase 1: The Exploration Phase - Casting a Wide Net

Start with a general, open-ended task to map the landscape of your topic.

**Example Task:**

./run.sh --task "Explore the current state of vertical farming technology and its main challenges."

Your Goal: Review the files created in the scratch/ directory. Look for recurring keywords, names, and specific technologies. These will inform your next steps.

Phase 2: The Deep Dive - Focusing Your Inquiry

Use the findings from Phase 1 to ask more specific questions.

Example Follow-up Tasks:
Bash

./run.sh --task "Find recent studies comparing the energy consumption of hydroponic vs. aeroponic vertical farms."

Over several cycles, the scratch/ directory becomes your centralized research hub.

Phase 3: Synthesis and Organization

This phase is about bringing it all together. Task the agent to consolidate its findings into a single report.

Example Synthesis Task (for a future, more capable agent):
Bash

./run.sh --task "Review all text files in the scratch directory about vertical farming and write a consolidated summary named 'vertical_farming_report.md'."

This becomes the first draft of your final deliverable.

Best Practices

    Start Broad, Then Narrow: Follow the three-phase approach.

    Think of scratch/ as Your Workbench: It's where all raw materials and findings are collected.

    Read the audit.log for Insights: See the exact path your assistant took to understand its process.

    Let the Agent Handle the Toil: Your job is strategy. The agent's job is execution.