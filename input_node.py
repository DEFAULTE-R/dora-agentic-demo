import pyarrow as pa
from dora import Node
import time

node = Node()

commands = [
    "move forward",
    "move left",
    "move forward",
    "move right",
    "stop"
]

print("Input node started (auto commands)")

i = 0

while True:
    command = commands[i % len(commands)]
    print(f"[INPUT] Sending: {command}")
    
    output = pa.array([command], type=pa.string())
    node.send_output("user_command", output)
    
    i += 1
    time.sleep(2)
