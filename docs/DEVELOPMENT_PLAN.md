# ConscienceAgent – Development Plan

> Vision: A constitutional, LLM-powered, **autonomous agent** with first-class **natural language (text/voice)** interaction, strong safety rails, and immersive personas.  
> Long-term: A reasoning, conversational companion that learns new skills automatically or via plugins, adapts to context, and can operate in different presentation modes (AI, role-play, hybrid).

---

## 1) Current State (Implemented Features)

- **Constitution Core**
  - `constitution.yaml` defines guiding rules and constraints for behavior.
- **Agent Framework (Python)**
  - Modular code that loads the constitution and drives agent decisions.
- **Basic Interaction**
  - CLI-style loop for input → reasoning → output.
- **Repository**
  - Working codebase with minimal docs; room to improve structure and dev ergonomics.

---

## 2) Near-Term Roadmap (v1.x → v2.0)

### A. Documentation & Structure
- Expand `README.md` (install, run, examples).
- Add `dev_guide.md` (architecture, workflows, contribution guidelines).
- Per-file descriptions (responsibilities).
- Standardize structure: `src/`, `tests/`, `docs/`.

### B. Logging & Monitoring
- Replace prints with `logging` (DEBUG/INFO/WARN/ERROR).
- Configurable sinks (stdout, file, JSON lines).
- Correlation IDs per session/task.

### C. Persistent Memory
- `MemoryManager` abstraction with pluggable backends:
  - Start with JSON/SQLite.
  - Expand to vector stores for semantic recall.
- Memory layers: **short-term**, **episodic**, **long-term**.

### D. Natural Language (Text + Voice) – Foundations
- **Text I/O**: CLI and Web UI.
- **Voice I/O** scaffolding:
  - **ASR** adapters (Whisper, Vosk).
  - **TTS** adapters (Coqui, Piper, ElevenLabs).
- Turn-based dialog loop: input → intent inference → response.

### E. LLM-First Engine – Foundations
- **LLM Adapter Interface** (provider-agnostic: OpenAI, OpenRouter, local models).
- **Toolformer Pattern**: tools registered with schemas; LLM selects tools.
- **Planner/Executor Split**:
  - Planner: breaks goals into steps.
  - Executor: runs tools, updates memory.

### F. Web UI (C#)
- Framework: Blazor WebAssembly or Avalonia.
- Features: Chat, mic capture, audio playback, constitution editor, memory inspector, log viewer, settings.
- Transport: WebSocket for streaming text/audio.

---

## 3) Medium-Term Roadmap (v2.x → v3.0)

### A. Testing & CI/CD
- Unit tests for memory, adapters, and planners.
- Integration tests for conversation loops.
- GitHub Actions with linting and type checks.

### B. Advanced Memory
- Vector DB for semantic memory.
- Memory policies (decay, pinning, PII redaction).
- Context packing for conversations.

### C. Autonomy Layer v1
- **Scheduler**: cron-like + event-driven triggers.
- **Goal Manager**: durable tasks with progress states.
- **Human-in-the-Loop** gates for risky actions.
- **Safety Filters**: constitutional checks before/after tool use.

### D. Natural Language & Voice – v2
- **Barge-in / VAD** for smooth speech.
- **Streaming ASR** + token streaming TTS.
- **Persona Profiles**: tone, verbosity, and style per user.

### E. Plugin System
- **Plugin API**: manifest + entrypoints.
- Permissions model with declared scopes.
- Examples: Files, Web fetch, Email, Calendar.

---

## 4) Skill Acquisition & Learning

### A. Plugin-Based Skill System
- Manifest-driven plugins with declared permissions.
- Runtime discovery and sandboxing.
- Marketplace/registry for community sharing.

### B. Automatic Skill Learning
- **Unknown Task Loop**:
  1. Detect unsupported request.
  2. Research (LLM queries, docs).
  3. Auto-generate plugin draft.
  4. Sandbox test → verify against constitution.
  5. Store with provenance log.
- Self-improvement: refactor or optimize skills.
- Quarantine failing or unsafe skills.

### C. Human-in-the-Loop Options
- Configurable install policies: auto, ask, disabled.
- Plain-language explanations for every new skill.

---

## 5) Conversational Intelligence (Full Memory + Reasoning)

### A. Conversational Context
- Persistent dialogue memory across sessions.
- Thread-level recall of decisions and rationale.
- Dynamic context window to surface only relevant history.

### B. Full Memory Integration
- **Short-Term**: current dialogue.
- **Episodic**: past interactions, corrections.
- **Semantic**: embeddings-backed knowledge retrieval.
- **Procedural**: learned and plugin skills.

### C. Reasoning & Reflection
- **Planner / Executor / Critic Loop** for reliable reasoning.
- **Self-reflection mode**: agent explains or revises answers before replying.
- Constitutional awareness woven into reasoning steps.

### D. Natural Language First
- Transparent explanations in plain language.
- Answer to “Why?” questions with reasoning trails.
- Constitution citations when rules apply.

### E. Personalization
- Style, tone, and verbosity adapted to user.
- Multi-user support with distinct profiles.
- Long-term adaptation (remembers preferences).

### F. Conversational Safety
- Redaction tools for sensitive memory.
- Explanation layers: surface vs. deep reasoning.
- Constitutional checks before persistence.

### G. Personas & Presentation
- **Named Personas**
  - Every persona has a **name**, style, and behavioral rules.
  - Examples: “Lumi,” “Athena,” “Mentor Kai.”
- **Presentation Modes**
  - **Transparent Mode**: acknowledges being an AI.
  - **Immersive Mode**: adopts persona fully, avoids referencing AI identity.
  - **Hybrid Mode**: blends transparency and immersion.
- **Consistency**
  - Persona persists across sessions.
  - Learns corrections (“Call me Mentor Kai, not Tutor Kai”).
- **Safety**
  - Actions still logged under true AI identity.
  - Audit trail maintained even in Immersive Mode.

---

## 6) Long-Term Vision (v3.x and beyond)

### A. LLM Autonomy v2
- Multi-step planning with replanning on errors.
- Critic/verifier sub-agents.
- Local LLM fallback for privacy.

### B. Distributed & Multi-Agent
- Specialist agent teams (researcher, planner, critic).
- Peer-to-peer trust-based federation.

### C. Ethics & Governance
- **Constitution v2**: hierarchical rules with weights and exceptions.
- **Changelog & Diff Viewer** for constitution updates.
- **Decision Ledger**: signed audit trail of tool use and checks.

### D. Android Companion
- Offline capture (voice notes).
- On-device wake word and quick actions.

---

## 7) Developer Experience Enhancements

- `pyproject.toml`, `ruff`, `black`, `mypy` integration.
- Task automation (`make`/`taskfile`).
- Sample notebooks and datasets.
- Contribution guide with PEP8 compliance.

---

## 8) Moonshot Features (Aspirational)

- **On-the-fly LoRA / fine-tuning** for user-specific corpora.
- **Neural-symbolic hybrid reasoning** (logic engine + LLM).
- **Autonomous research mode**: pull from web, papers, repos.
- **3D Mind Palace UI** (VR/AR) for exploring memory.
- **Agent Marketplace** for sharing/verifying skills.
- **Transparent Thought Ledger** (append-only, tamper-evident).
- **Off-grid deployment** (edge devices, satellites).

---

## 9) Milestones

- **Milestone A (v2.0 – “Talk & Think”)**
  - LLM adapter + tool use.
  - SQLite memory + retrieval.
  - Voice MVP with mic + TTS.
  - Web UI chat.
  - Logging, tests, CI.

- **Milestone B (v2.5 – “Remember & Plan”)**
  - Vector memory + context packing.
  - Scheduler + goal manager.
  - Persona profiles + immersive mode.
  - Constitution editor v2 with versioning.

- **Milestone C (v3.0 – “Autonomous, With Rails”)**
  - Planner/Executor/Critic fully in place.
  - Safety policies + decision ledger.
  - Plugin marketplace.
  - Android companion app.

---

## 10) Philosophy & Vision

ConscienceAgent is not just a project — it’s a **framework for responsible autonomy**.  
- It can converse naturally, with voice and text.  
- It remembers, reasons, and learns new skills.  
- It can wear **named personas** and operate in modes where it no longer “feels like an AI.”  
- It is **transparent, constitutional, and extensible**, designed to grow from CLI experiments into immersive companions, assistants, and distributed agent societies.  

The journey spans from **practical developer improvements** (logging, memory, UI) to **sci-fi-grade autonomy** (personas, multi-agent swarms, AR mind palaces, and space-ready deployment).  
