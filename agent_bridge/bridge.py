import pyarrow as pa
from dora import Node
import json

node = Node()

class MockAgent:
    def run(self, command):
        command = command.lower()

        if "forward" in command:
            linear, angular = 0.5, 0.0
        elif "back" in command:
            linear, angular = -0.5, 0.0
        elif "left" in command:
            linear, angular = 0.0, 0.5
        elif "right" in command:
            linear, angular = 0.0, -0.5
        elif "stop" in command:
            linear, angular = 0.0, 0.0
        else:
            print("[AGENT] Invalid command, stopping for safety")
            linear, angular = 0.0, 0.0

        # Safety clamp
        linear = max(min(linear, 1.0), -1.0)
        angular = max(min(angular, 1.0), -1.0)

        return {
            "linear": linear,
            "angular": angular
        }

agent = MockAgent()
print("Agent bridge node started")

for event in node:
    if event["type"] == "INPUT" and event["id"] == "command":
        command = event["value"].to_pylist()[0]
        print(f"[AGENT] Received command: {command}")

        result = agent.run(command)

        control_message = {
            "velocity": {
                "linear": result["linear"],
                "angular": result["angular"]
            },
            "meta": {
                "source": "agent",
                "timestamp": 0,
                "command_id": command
            }
        }

        output = pa.array([json.dumps(control_message)], type=pa.string())
        node.send_output("cmd_out", output)

        print(f"[AGENT] Sent structured message: {control_message}")
