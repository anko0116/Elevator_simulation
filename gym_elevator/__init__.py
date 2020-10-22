from gym.envs.registration import register

register(
    id='elevator-v0',
    entry_point='gym_elevator.envs:Environment'
)