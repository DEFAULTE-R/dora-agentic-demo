# 🤖 Agentic Dora Demo (GSoC 2026 Prototype)

A modular, real-time robotics pipeline built using **Dora-RS**, demonstrating a **true agentic architecture** with LLM-driven reasoning, tool-based execution, safety validation, and simulation.

---

## 🚀 Overview

This project implements a complete **agent-driven robotics control system**:

```
Input → LLM Agent → Tool Mapping → Safety → Simulation
```

Unlike traditional pipelines, the agent:

* **understands natural language**
* **decides actions (tools)**
* **executes through structured control signals**

---

## 🔥 Key Highlights

* 🧠 **LLM-powered agent (Ollama + Mistral, fully local)**
* 🧰 **Tool-based architecture (action → execution mapping)**
* 🛡️ **Dedicated safety node for validation and constraints**
* 🔄 **Structured JSON messaging across nodes**
* ⚡ **Real-time execution using Dora runtime**
* 🎮 **Physics-based simulation with PyBullet**
* 🔌 **Fully modular — components can be swapped independently**

---

## 🧱 Architecture

### 🔹 Input Node

* Streams commands (`move forward`, `turn left`, etc.)
* Designed for **non-blocking Dora execution**

---

### 🔹 LLM Agent Node

* Converts natural language → **tool/action**
* Uses local LLM (**Mistral via Ollama**)
* Example output:

```json
{
  "action": "move_forward",
  "params": {}
}
```

---

### 🔹 Tool Mapping Layer (inside agent)

Maps agent decisions → executable control:

| Action       | Output Velocity            |
| ------------ | -------------------------- |
| move_forward | linear: 0.5, angular: 0.0  |
| turn_left    | linear: 0.0, angular: 1.0  |
| turn_right   | linear: 0.0, angular: -1.0 |
| stop         | linear: 0.0, angular: 0.0  |

---

### 🔹 Safety Node

* Validates and clamps control signals
* Prevents unsafe execution
* Decoupled from agent logic

---

### 🔹 Simulation Node

* Powered by **PyBullet**
* Executes velocity commands in real time

---

## 🔁 Data Flow

```
Command
   ↓
LLM Agent (reasoning)
   ↓
Action (tool)
   ↓
Velocity Mapping
   ↓
Safety Layer
   ↓
Simulation
```

---

## 🧠 Why This Matters

This project demonstrates a **core idea behind Agentic Dora**:

> Replace static pipelines with intelligent, modular agents that reason and act.

Key contributions:

* Shows **agent + tool execution pattern**
* Demonstrates **separation of reasoning and execution**
* Introduces **safety as an independent system component**
* Enables **LLM integration without breaking pipeline structure**

---

## ⚙️ Setup

```bash
git clone https://github.com/DEFAULTE-R/dora-agentic-demo.git
cd dora-agentic-demo

python3 -m venv dora-env
source dora-env/bin/activate

pip install dora-rs pybullet requests
```

---

## 🤖 Run the System

```bash
dora run configs/dataflow.yml --uv
```

---

## 🧠 LLM Setup (Local)

Install Ollama and run:

```bash
ollama run mistral
```

The agent will automatically connect to:

```
http://localhost:11434
```

---

## 📈 Current Status

### ✅ Completed

* Modular Dora pipeline
* LLM-based agent reasoning
* Tool-based action abstraction
* Action → execution mapping
* Safety validation layer
* Real-time simulation

### 🚧 Next Steps

* Multi-step planning (e.g., “move in a square”)
* Structured tool schema (typed actions)
* Observability & debugging tools
* Fault tolerance & node recovery
* Replace prompt logic with agent frameworks (e.g., smolagents)

---

## 🎯 GSoC 2026 Alignment

This prototype directly aligns with the **Agentic Dora** project:

* ✔ Minimal working agent pipeline
* ✔ Modular node composition
* ✔ LLM integration pathway
* ✔ Safety-aware execution
* ✔ Extensible architecture for advanced agents

---

## 🧠 Key Insight

> This is not just a simulation pipeline —
> it is a **foundation for agent-based robotic systems**.

---

## 🧑‍💻 Author

**Hari L**
GSoC 2026 Aspirant — Agentic Systems & Robotics

---

## ⭐ Support

If this project helped or inspired you, consider starring ⭐ the repo!
