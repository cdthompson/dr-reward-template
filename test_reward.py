"""
Reward function unit tests
"""
import unittest
import reward


def default_params():
    '''
    Return a params structure resembling what DeepRacer will use
    '''
    return {
        "all_wheels_on_track": True,    # flag to indicate if the vehicle
                                        #  is on the track
        "x": 0.0,                       # vehicle's x-coordinate in meters
        "y": 0.0,                       # vehicle's y-coordinate in meters
        "distance_from_center": 0.0,    # distance in meters from the track
                                        #  center
        "is_left_of_center": False,     # Flag to indicate if the vehicle is
                                        #  on the left side to the track
                                        #  center or not.
        "is_reversed": False,           # Flat to indicate if the vehicle is
                                        #  going the wrong direction
        "heading": 0,                   # vehicle's yaw in degrees
        "progress": 0,                  # percentage of track completed
        "steps": 0,                     # number steps completed
        "speed": 0.0,                   # vehicle's speed in meters per
                                        #  second (m/s)
        "steering_angle": 0.0,          # vehicle's steering angle in degrees
        "track_width": 10.0,            # width of the track
        "waypoints": [[0, 0], [0, 0]],  # list of [x,y] as milestones along
                                        # the track center
        "closest_waypoints": [0, 1]     # indices of the two nearest waypoints
    }

class TestReward(unittest.TestCase):
    '''
    Test the reward.py module
    '''

    def test_calculate_distance_from_center_factor(self):
        '''
        Verify the distance factor falls off as we get further from the center
        '''
        self.assertEqual(reward.calculate_distance_from_center_factor(10.0, 0.0), 1.0)
        self.assertEqual(reward.calculate_distance_from_center_factor(10.0, 2.0), 0.5)
        self.assertEqual(reward.calculate_distance_from_center_factor(10.0, 3.5), 0.1)
        self.assertEqual(reward.calculate_distance_from_center_factor(10.0, 5.5), 1e-3)

if __name__ == '__main__':
    unittest.main()
