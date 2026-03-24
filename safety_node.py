import pyarrow as pa
import json
from dora import Node

node = Node()

print("Safety node started")

for event in node:
    if event["type"] == "INPUT" and event["id"] == "cmd_in":
        msg = json.loads(event["value"].to_pylist()[0])
        linear = float(msg["velocity"]["linear"])
        angular = float(msg["velocity"]["angular"])

        print(f"[SAFETY] Received: linear={linear}, angular={angular}")

        # Safety clamp
        linear = max(min(linear, 1.0), -1.0)
        angular = max(min(angular, 1.0), -1.0)

        # Stop if invalid (extra safety)
        if abs(linear) > 1.0 or abs(angular) > 1.0:
            print("[SAFETY] Unsafe values detected, stopping")
            linear, angular = 0.0, 0.0

        output = pa.array([linear, angular], type=pa.float64())
        node.send_output("cmd_vel", output)

        print(f"[SAFETY] Sent: linear={linear}, angular={angular}")
