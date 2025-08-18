# ConscienceAgent – Developer Guide

This guide is for developers who want to understand, extend, and contribute to ConscienceAgent.

---

## 1. Getting Started

### Requirements
- Python 3.11+
- Git
- (Optional) C# for Web UI development
- (Optional) Docker for containerized runs

### Setup
```bash
git clone https://github.com/MrFrey75/ConscienceAgent.git
cd ConscienceAgent
pip install -r requirements.txt
```

### Running the Agent
```bash
python src/main.py
```

---

## 2. Project Structure

- `constitution.yaml` → Core rules that govern the agent’s behavior.
- `src/` → Main Python source files.
- `tests/` → Unit and integration tests.
- `docs/` → Documentation and guides.
- `dev_plan.md` → Development roadmap (this file).
- `dev_guide.md` → Developer reference (you are here).

---

## 3. Key Concepts

### Constitution
- The moral and operational backbone of the agent.
- YAML file that can be edited and extended.

### Memory
- Short-term: current session.
- Episodic: past events/conversations.
- Semantic: embeddings and retrieval-based recall.
- Procedural: plugins and learned skills.

### Personas
- Named roles with style, tone, and rules.
- Presentation modes:
  - **Transparent**: admits AI identity.
  - **Immersive**: presents as persona only.
  - **Hybrid**: mixes both.

### Planner / Executor / Critic
- Planner: generates steps to achieve a goal.
- Executor: carries them out (via plugins/tools).
- Critic: verifies safety, constitutionality, correctness.

---

## 4. Extending ConscienceAgent

### Adding a Plugin
1. Create a new file in `src/plugins/`.
2. Define plugin manifest (`manifest.json` with name, description, permissions).
3. Implement entrypoints in Python.
4. Register plugin in `plugin_manager.py`.

### Adding a Persona
1. Edit `personas.yaml` or `src/persona_manager.py`.
2. Define:
   - Name
   - Style (tone/voice)
   - Rules/constraints
3. Restart agent to load persona.

### Modifying the Constitution
- Edit `constitution.yaml`.
- Run with `--validate` to check syntax before applying.

---

## 5. Running Tests

```bash
pytest tests/
```

- Use `pytest -s` for verbose logs.
- CI/CD runs tests automatically via GitHub Actions.

---

## 6. Contributing

### Guidelines
- Follow PEP8 and type hints.
- Write docstrings for all public methods.
- Update `dev_plan.md` if your contribution changes roadmap or scope.

### Workflow
1. Fork repo, create a feature branch.
2. Make changes and commit with clear messages.
3. Push branch and open a PR.
4. Ensure CI passes before requesting review.

---

## 7. Roadmap for Developers

- Implement memory layers and LLM adapters.
- Develop plugin ecosystem and auto-skill learning.
- Build conversational reasoning with personas.
- Expand Web UI for immersive interaction.
- Add mobile (Android) companion.

---

## 8. Resources

- [PEP8 Style Guide](https://peps.python.org/pep-0008/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [FAISS for vector search](https://github.com/facebookresearch/faiss)
- [Blazor](https://dotnet.microsoft.com/en-us/apps/aspnet/web-apps/blazor)
