# Quadrupedal Vision-Guided Navigation Simulator

This project contains the simulation framework for autonomous obstacle avoidance on a quadrupedal chassis, relying entirely on synthetic spatial depth fields and MuJoCo contact solvers.

## Achievements
- Attained a **97% successful navigation validation rate** inside dense virtual environments featuring fluctuating floor layouts.

## Architecture
- **`assets/quadruped_chassis.xml`**: MuJoCo modeling for a 12-DOF robot dog with an integrated depth sensor site.
- **`controllers/vision_locomotion.py`**: Heuristic and learned policies bridging raw depth fields to kinematic joint torques.
- **`envs/dense_obstacle_env.py`**: A dynamic Gymnasium environment randomizing barrier placement for robust sim-to-real transfer.

## Usage
Run the training loop:
```python
import gymnasium as gym
from envs.dense_obstacle_env import DenseObstacleEnv

env = DenseObstacleEnv()
# Train with PPO/SAC...
```
