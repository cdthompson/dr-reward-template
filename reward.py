"""
AWS DeepRacer reward function
"""

#===============================================================================
#
# REWARD
#
#===============================================================================

def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']

    reward = calculate_distance_from_center_factor(track_width, distance_from_center)
    return float(reward)


#===============================================================================
#
# TRACK POSITION STRATEGY
#
#===============================================================================

def calculate_distance_from_center_factor(track_width, distance_from_center):
    '''
    Return a value 1e-3 to 1 based on the distance from center
    '''

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track
    return reward
