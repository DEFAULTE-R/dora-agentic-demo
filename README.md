# Agentic Dora — Real-Time Robot Control with Dataflows

A working proof-of-concept demonstrating **agent-driven robot control using Dora dataflows**, where natural language commands are translated into control signals and executed in a physics simulation.

---

##  Overview

This project shows how an **agent can be embedded inside a Dora dataflow** to control a robot in real time.

It implements a modular pipeline:

```
Input Node → Agent Bridge → Dora Runtime → Simulation (PyBullet)
```

---

##  Key Features

* ⚡ Real-time command execution using Dora runtime
* 🧩 Modular node-based architecture (easy to extend or swap components)
* 🤖 Natural language → velocity command pipeline
* 🖥️ PyBullet simulation with optional GUI
* 🔌 Agent abstraction (currently rule-based, replaceable with LLM)

---

##  Architecture

### 1. Input Node

Streams commands into the Dora dataflow.

### 2. Agent Bridge

Converts natural language commands into structured velocity outputs:

* linear velocity
* angular velocity

### 3. Simulation Node

Executes commands in a PyBullet environment and updates robot state.

---

## ▶️ How to Run

```bash
git clone https://github.com/DEFAULTE-R/dora-agentic-demo.git
cd dora-agentic-demo

python3 -m venv dora-env
source dora-env/bin/activate

pip install dora-rs pybullet smolagents

dora run configs/dataflow.yml
```

---

## 🎮 Example Commands

The system supports:

* `move forward`
* `move left`
* `move right`
* `stop`

Commands are processed in real time and applied to the robot.

---

## 📌 Current Status

✅ End-to-end Dora dataflow working
✅ Real-time agent → control pipeline
✅ PyBullet simulation with live control

---

## 🔧 Next Steps

* Add structured command schema + validation
* Introduce safety mechanisms (timeouts, constraints)
* Replace rule-based agent with LLM (smolagents)
* Support multi-step commands (e.g., "move in a square")

---

##  Goal

This project explores how **Dora can serve as a runtime for agent-driven robotics**, emphasizing:

* modularity
* composability
* real-time execution

---

## Context

Built as a hands-on exploration for **GSoC 2026 — Agentic Dora project idea**.

---

## ⭐ If you find this interesting

Feel free to star the repo or contribute!
