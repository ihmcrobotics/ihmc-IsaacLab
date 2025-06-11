# This is the complete and final version of this file.

from __future__ import annotations

import isaaclab.sim as sim_utils
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg


H1_2_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path="C:/Users/khammoud/Git/Robots/h1_2.usd",
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(enabled_self_collisions=True, solver_position_iteration_count=4, solver_velocity_iteration_count=0
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.05),
        joint_pos={
            ".*_hip_yaw_joint": 0.0,
            ".*_hip_roll_joint": 0.0,
            ".*_hip_pitch_joint": -0.28,
            ".*_knee_joint": 0.79,
            ".*_ankle_pitch_joint": -0.52,
            ".*_ankle_roll_joint": 0.0,
            "torso_joint": 0.0,
            ".*_shoulder_pitch_joint": 0.28,
            ".*_shoulder_roll_joint": 0.0,
            ".*_shoulder_yaw_joint": 0.0,
            ".*_elbow_pitch_joint": 0.52,
            ".*_elbow_roll_joint": 0.0,
            ".*_wrist_yaw_joint": 0.0,
            ".*_wrist_pitch_joint": 0.0,
        },
        joint_vel={".*": 0.0},
    ),
    actuators={
        "legs_and_torso": ImplicitActuatorCfg(
            joint_names_expr=[".*hip.*_joint", ".*knee_joint", ".*ankle.*_joint", "torso_joint"],
            effort_limit=300,
            velocity_limit=100.0,
            stiffness=200.0,
            damping=5.0,
        ),
        "arms": ImplicitActuatorCfg(
            joint_names_expr=[".*shoulder.*_joint", ".*elbow.*_joint", ".*wrist.*_joint"],
            effort_limit=300,
            velocity_limit=100.0,
            stiffness=50.0,
            damping=10.0,
        ),
       
        # We define a group for the fingers but give them no motor force.
        # This makes them passive and solves the warning without trying to control them.
        "fingers": ImplicitActuatorCfg(
            joint_names_expr=[".*(index|middle|pinky|ring|thumb).*_joint"],
            effort_limit=300,
            velocity_limit=100.0,
            stiffness=0.0, # ZERO stiffness = no active motor force
            damping=0.0,   # ZERO damping = no active motor resistance
        ),
    },
)