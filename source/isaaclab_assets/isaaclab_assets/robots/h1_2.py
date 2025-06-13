# This is the complete and final version of this file.

from __future__ import annotations

import isaaclab.sim as sim_utils
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg


H1_2_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path="C:/Users/khammoud/Git/Robots/h1_2_new_test.usd",
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
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
           enabled_self_collisions=False, solver_position_iteration_count=8, solver_velocity_iteration_count=4
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

    # Custom:
    # actuators={
    #     "legs_and_torso": ImplicitActuatorCfg(
    #         joint_names_expr=[".*hip.*_joint", ".*knee_joint", ".*ankle.*_joint", "torso_joint"],
    #         effort_limit=300,
    #         velocity_limit=100.0,
    #         stiffness=200.0,
    #         damping=5.0,
    #     ),
    #     "arms": ImplicitActuatorCfg(
    #         joint_names_expr=[".*shoulder.*_joint", ".*elbow.*_joint", ".*wrist.*_joint"],
    #         effort_limit=300,
    #         velocity_limit=100.0,
    #         stiffness=50.0,
    #         damping=10.0,
    #     ),
       
    #     # This makes them passive and solves the warning without trying to control them.
    #     "fingers": ImplicitActuatorCfg(
    #         joint_names_expr=[".*(index|middle|pinky|ring|thumb).*_joint"],
    #         effort_limit=300,
    #         velocity_limit=100.0,
    #         stiffness=0.0, # ZERO stiffness = no active motor force
    #         damping=0.01,   # ZERO damping = no active motor resistance
    #     ),

    # Unitree:
    actuators={
        "legs": ImplicitActuatorCfg(
            joint_names_expr=[
                ".*_hip_yaw_joint",
                ".*_hip_roll_joint",
                ".*_hip_pitch_joint",
                ".*_knee_joint",
                "torso_joint",
            ],
            effort_limit=300,
            velocity_limit=100.0,
            stiffness={
                ".*_hip_yaw_joint": 150.0,
                ".*_hip_roll_joint": 150.0,
                ".*_hip_pitch_joint": 200.0,
                ".*_knee_joint": 200.0,
                "torso_joint": 200.0,
            },
            damping={
                ".*_hip_yaw_joint": 5.0,
                ".*_hip_roll_joint": 5.0,
                ".*_hip_pitch_joint": 5.0,
                ".*_knee_joint": 5.0,
                "torso_joint": 5.0,
            },
            armature={
                ".*_hip_.*": 0.01,
                ".*_knee_joint": 0.01,
                "torso_joint": 0.01,
            },
        ),
        "feet": ImplicitActuatorCfg(
            joint_names_expr=[".*_ankle_pitch_joint", ".*_ankle_roll_joint"],
            effort_limit=100,
            velocity_limit=100.0,
            stiffness={
                ".*_ankle_pitch_joint": 20.0,
                ".*_ankle_roll_joint": 20.0,
            },
            damping={
                ".*_ankle_pitch_joint": 4.0,
                ".*_ankle_roll_joint": 4.0,
            },
            armature=0.005,
        ),
        "arms": ImplicitActuatorCfg(
            joint_names_expr=[".*_shoulder_pitch", ".*_shoulder_roll", ".*_shoulder_yaw", ".*_elbow"],
            effort_limit=300,
            velocity_limit=100.0,
            stiffness={
                ".*_shoulder_pitch": 40.0,
                ".*_shoulder_roll": 40.0,
                ".*_shoulder_yaw": 40.0,
                ".*_elbow": 40.0,
            },
            damping={
                ".*_shoulder_pitch": 10.0,
                ".*_shoulder_roll": 10.0,
                ".*_shoulder_yaw": 10.0,
                ".*_elbow": 10.0,
            },
            armature={
                ".*_shoulder_pitch": 0.005,
                ".*_shoulder_roll": 0.005,
                ".*_shoulder_yaw": 0.005,
                ".*_elbow": 0.005,
            },
        ),
        "fingers": ImplicitActuatorCfg(
            joint_names_expr=[".*(index|middle|pinky|ring|thumb).*_joint"],
            effort_limit=300,
            velocity_limit=100.0,
            stiffness=0.0, # ZERO stiffness = no active motor force
            damping=0.01,   # ZERO damping = no active motor resistance
            armature={
                ".*_index_.*": 0.001,
                ".*_middle_.*": 0.001,
                ".*_pinky_.*": 0.001,
                ".*_ring_.*": 0.001,
                ".*_thumb_.*": 0.001,
            },
        ),
    },
)