import gym
env = gym.make('CartPole-v0')
# for i_episode in range(20):
#     print('environment has been reseted\n'*10)
#     observation = env.reset()
#     for t in range(100):
#         env.render()
#         print(observation)
#         action = env.action_space.sample()
#         observation, reward, done, info = env.step(action)
#         if done:
#             print('Episode finished after {} timesteps'.format(t+1))
#             break
# env.close()


class Agent():
    def __init__(self, env):
        self.action_size = env.action_space.n
        print('the action size is: ', self.action_size)

    def get_action(self, state):
        pole_angle = state[2]
        action = 0 if pole_angle < 0 else 1
        return action


agent = Agent(env)
state = env.reset()

for _ in range(200):
    action = agent.get_action(state)
    state, reward, done, ifno = env.step(action)
    env.render()
# print(env.action_space)
# print(env.observation_space)
# print(env.observation_space.high)
# print(env.observation_space.low)
# spaces = gym.spaces.Discrete(8)
# x = spaces.sample()
# assert spaces.contains(x)
# assert spaces.n == 8
env.close()
