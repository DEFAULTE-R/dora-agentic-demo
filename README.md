# Agentic Dora — GSoC 2026 Prototype

A working proof-of-concept for **Agent-Driven Robot Control inside Dora Dataflows**.

## Overview

This project demonstrates how an agent can be embedded directly inside a Dora dataflow to control a robot in real time. The system translates natural language commands into structured control signals and executes them through Dora's message-passing runtime.

## Architecture
```
[User Command] → [MockAgent] → [Agent Bridge Node] → [Dora Runtime] → [Simulation Node (PyBullet)]
```

## Features

- Natural language → robot velocity command pipeline
- MockAgent (fully offline, no API key required)
- Real-time command execution via Dora dataflows
- Modular node-based architecture (easy to swap agent or simulator)
- PyBullet-based physics simulation

## Status

- ✅ Dora dataflow executes successfully
- ✅ Agent Bridge node generates velocity commands
- ✅ Simulation node receives and executes commands
- 🔧 Structured schema validation — in progress
- 🔧 Watchdog safety mechanism — planned

## Run
```bash
python3 -m venv dora-env
source dora-env/bin/activate
pip install dora-rs pybullet smolagents
dora run configs/dataflow.yml
```

## Next Steps

- Add structured message schema
- Implement validation layer in Agent Bridge
- Add watchdog / safety timeout mechanism
- Extend to multi-command sequences

## Context

Built as a hands-on exploration of [GSoC 2026 Project #10 — Agentic Dora](https://github.com/dora-rs/dora/wiki/GSoC-2026) with the dora-rs organization. Demonstrates that Dora can serve as a runtime for agent-driven robotics — safe, testable, and modular.
