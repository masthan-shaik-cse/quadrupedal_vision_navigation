import argparse
import numpy as np
from src.quadrupedal_vision_navigation.alignment.control_barrier_functions import ControlBarrierFunctionFilter
from src.quadrupedal_vision_navigation.alignment.semantic_vision_aligner import SemanticVisionAligner
from src.quadrupedal_vision_navigation.alignment.sim2real_preference_tuner import Sim2RealPreferenceTuner

def run_cbf_safety_filter():
    print("\n--- Executing Hardware Safety CBF Envelope ---")
    cbf = ControlBarrierFunctionFilter(safe_torque_limit=25.0)
    
    # Mocking a dangerous torque command from a hallucinating RL agent
    state = np.zeros(12)
    dangerous_nominal_action = np.array([45.0, 10.0, -50.0, 5.0]) # Massive torques
    
    print(f"Neural Network Requested Torques: {dangerous_nominal_action}")
    safe_action = cbf.filter_action(state, dangerous_nominal_action)
    print(f"CBF Mathematically Projected Torques: {safe_action}")

def run_semantic_vlm_audit():
    print("\n--- Executing Semantic Vision-Language Alignment ---")
    vlm_aligner = SemanticVisionAligner()
    
    # Mocking a visual frame representing a frozen lake
    visual_frame = "RGB_Depth_Frame_Data"
    
    audit_result = vlm_aligner.audit_terrain(visual_frame)
    if not audit_result["safe_to_traverse"]:
        print("Locomotion Engine Action: HALT. Route replanning initiated.")

def execute_preference_tuning():
    print("\n--- Executing Sim-to-Real Preference Tuning ---")
    tuner = Sim2RealPreferenceTuner()
    
    # Mocking negative human feedback on an aggressive gait
    human_preference_score = -0.7 
    tuner.align_domain_parameters(human_preference_score)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enterprise Quadrupedal Vision Alignment Engine")
    parser.add_argument("--run_cbf_safety_filter", action="store_true", help="Execute the Control Barrier Function Mathematical Filter")
    parser.add_argument("--run_semantic_vlm_audit", action="store_true", help="Audit the terrain using the Vision-Language Model Constitution")
    parser.add_argument("--execute_preference_tuning", action="store_true", help="Align domain randomization with human feedback")
    parser.add_argument("--run_all", action="store_true", help="Execute the full End-to-End Alignment Pipeline")
    
    args = parser.parse_args()
    
    if args.run_all:
        run_cbf_safety_filter()
        run_semantic_vlm_audit()
        execute_preference_tuning()
    else:
        if args.run_cbf_safety_filter:
            run_cbf_safety_filter()
        if args.run_semantic_vlm_audit:
            run_semantic_vlm_audit()
        if args.execute_preference_tuning:
            execute_preference_tuning()
            
        if not any(vars(args).values()):
            print("Please specify an execution flag. Use --help for options.")
