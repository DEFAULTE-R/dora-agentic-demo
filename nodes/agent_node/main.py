import json
import pyarrow as pa
from dora import Node
import requests

node = Node()

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "mistral"

def query_llm(command):
    prompt = f"""
You are a robot agent.

Convert the command into a tool call.

Available actions:
- move_forward
- move_backward
- turn_left
- turn_right
- stop

Output format:
{{
  "action": "string",
  "params": {{}}
}}

ONLY output JSON.

Command: {command}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()["response"]

    try:
        return json.loads(result)
    except:
        return {"action": "stop", "params": {}}

def action_to_velocity(action):
    if action == "move_forward":
        return {"linear": 0.5, "angular": 0.0}
    elif action == "move_backward":
        return {"linear": -0.5, "angular": 0.0}
    elif action == "turn_left":
        return {"linear": 0.0, "angular": 1.0}
    elif action == "turn_right":
        return {"linear": 0.0, "angular": -1.0}
    else:
        return {"linear": 0.0, "angular": 0.0}

print("LLM Agent node started", flush=True)

for event in node:
    if event.get("type") != "INPUT":
        continue

    try:
        cmd = event["value"].to_pylist()[0]
    except:
        continue

    print(f"[AGENT] Received: {cmd}", flush=True)

    action_data = query_llm(cmd)
    action = action_data.get("action", "stop")

    velocity = action_to_velocity(action)

    print(f"[AGENT] Action: {action}", flush=True)
    print(f"[AGENT] Velocity: {velocity}", flush=True)

    output = {
        "velocity": velocity,
        "meta": {
            "source": "llm_agent",
            "command": cmd
        }
    }

    arr = pa.array([json.dumps(output)], type=pa.string())
    node.send_output("velocity", arr)
