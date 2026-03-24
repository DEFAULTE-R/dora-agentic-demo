import pyarrow as pa
from dora import Node

node = Node()

class MockAgent:
    def run(self, command):
        command = command.lower()
        if "forward" in command:
            return {"tool": "cmd_vel", "linear": 0.5, "angular": 0.0}
        elif "back" in command:
            return {"tool": "cmd_vel", "linear": -0.5, "angular": 0.0}
        elif "left" in command:
            return {"tool": "cmd_vel", "linear": 0.0, "angular": 0.5}
        elif "right" in command:
            return {"tool": "cmd_vel", "linear": 0.0, "angular": -0.5}
        elif "stop" in command:
            return {"tool": "cmd_vel", "linear": 0.0, "angular": 0.0}
        else:
            return {"tool": "cmd_vel", "linear": 0.0, "angular": 0.0}

agent = MockAgent()
print("Agent bridge node started")

for event in node:
    if event["type"] == "INPUT" and event["id"] == "command":
        command = "move forward"
        print(f"[AGENT] Received command: {command}")
        
        result = agent.run(command)
        
        output = pa.array(
            [result["linear"], result["angular"]],
            type=pa.float64()
        )
        node.send_output("cmd_vel", output)
        print(f"[AGENT] Sent: linear={result['linear']}, angular={result['angular']}")
