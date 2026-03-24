# 🤖 Agentic Dora Demo (GSoC 2026 Prototype)

A modular, real-time robotics pipeline built using **Dora-RS**, demonstrating an **agentic architecture** with structured messaging, safety validation, and simulation.

---

## 🚀 Overview

This project implements a complete **agent-driven robotics control system** using Dora dataflows:

```
Input Node → Agent Bridge → Safety Node → Simulation Node
```

### Key Features

* 🧠 Natural language → control signal conversion
* 🛡️ Dedicated safety validation layer
* 🔄 Structured message passing (JSON schema)
* ⚡ Real-time execution with Dora runtime
* 🎮 Live robot simulation using PyBullet

---

## 🧱 Architecture

### 🔹 Input Node

* Streams commands (e.g., `"move forward"`, `"turn left"`)
* Designed for **non-interactive Dora execution** (no `input()`)

---

### 🔹 Agent Bridge

* Converts natural language → structured control signals
* Current implementation: rule-based agent
* Output format:

```json
{
  "velocity": {
    "linear": 0.5,
    "angular": 0.0
  },
  "meta": {
    "source": "agent",
    "timestamp": 0,
    "command_id": "move forward"
  }
}
```

---

### 🔹 Safety Node

* Independent validation layer (aligned with Dora philosophy)
* Responsibilities:

  * Clamp velocity values
  * Detect unsafe commands
  * Ensure safe execution before simulation

---

### 🔹 Simulation Node

* Built using **PyBullet**
* Applies velocity in real time:

```python
p.resetBaseVelocity(
    robot,
    linearVelocity=[linear, 0, 0],
    angularVelocity=[0, 0, angular]
)
```

---

## 🔁 Data Flow

```
Input → Agent → Safety → Simulation
         ↓
   Structured JSON Messages
```

---

## 🧩 Structured Messaging

This project introduces a **schema-based communication system**:

### Python (runtime)

* JSON messages passed between nodes

### Rust (future integration)

* Typed schema defined in:

```
src/schemas/control.rs
```

Includes:

* `VelocityCommand`
* `CommandMeta`
* `ControlMessage`

👉 Enables:

* Traceability (command_id)
* Observability (source, timestamp)
* Extensibility (future fields)

---

## ⚙️ Setup

### 1. Clone the repo

```bash
git clone https://github.com/DEFAULTE-R/dora-agentic-demo.git
cd dora-agentic-demo
```

---

### 2. Create virtual environment

```bash
python3 -m venv dora-env
source dora-env/bin/activate
```

---

### 3. Install dependencies

```bash
pip install dora-rs pybullet smolagents
```

---

## ▶️ Run the Pipeline

```bash
dora run configs/dataflow.yml
```

---

## ⚠️ Important Notes

### ❌ No `input()` in Dora Nodes

Dora nodes are non-interactive.
Using `input()` will cause:

```
EOFError: EOF when reading a line
```

✅ Use streaming or predefined inputs instead.

---

### ⚠️ Simulation Exit Behavior

Closing the PyBullet window will:

* Terminate the simulation node
* Cause "broken pipe" logs in other nodes

This is expected in distributed systems.

---

## 📈 Current Status

### ✅ Completed

* Modular Dora pipeline
* Agent → Safety → Simulation flow
* Structured JSON messaging
* Real-time simulation control
* Safety abstraction layer

### 🚧 In Progress

* Metadata preservation across all nodes
* LLM-based agent integration
* Multi-step command execution
* Fault tolerance & node recovery

---

## 🎯 GSoC 2026 Direction

This project is evolving toward:

* 🤖 **Agentic robotics system**
* 🧠 LLM-powered decision making
* 🛡️ Robust safety guarantees
* 📡 Typed, schema-driven communication
* 🔁 Multi-node coordination

---

## 🧠 Key Learnings

* Dora requires **event-driven, non-blocking nodes**
* Separation of concerns is critical (Agent vs Safety)
* Structured messaging enables scalable systems
* Real-time systems require fault awareness

---

## 📌 Repository

👉 https://github.com/DEFAULTE-R/dora-agentic-demo

---

## 🧑‍💻 Author

**Hari L**
GSoC 2026 Aspirant – Agentic Systems & Robotics

---

## ⭐ If you find this useful

Star the repo and follow the progress 🚀
