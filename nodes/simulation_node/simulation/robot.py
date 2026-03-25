import pybullet as p
import pybullet_data
import pyarrow as pa
import time
from dora import Node

node = Node()

# Connect to PyBullet in headless mode
p.connect(p.DIRECT)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)
p.loadURDF("plane.urdf")
robot = p.loadURDF("r2d2.urdf", [0, 0, 0.5])

print("Simulation node started")

for event in node:
    event_type = event["type"]

    if event_type == "INPUT":
        event_id = event["id"]

        if event_id == "cmd_vel":
            values = event["value"].to_pylist()
            linear = float(values[0])
            angular = float(values[1])
            print(f"[SIM] cmd_vel received: linear={linear}, angular={angular}")
        # Apply movement to robot
        p.resetBaseVelocity(
            robot,
            linearVelocity=[linear, 0, 0],
            angularVelocity=[0, 0, angular]
        )


        # Publish pose
        pos, orn = p.getBasePositionAndOrientation(robot)
        pose = pa.array([pos[0], pos[1], pos[2]], type=pa.float64())
        node.send_output("robot_pose", pose)
        p.stepSimulation()
