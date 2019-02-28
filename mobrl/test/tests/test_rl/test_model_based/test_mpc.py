from mobrl.envs.gym_env import make
from mobrl.core.core import EnvSpec
from mobrl.algo.rl.model_based.models.mlp_dynamics_model import ContinuousMLPGlobalDynamicsModel
from mobrl.common.sampler.sample_data import TransitionData
from mobrl.algo.rl.model_based.mpc import ModelPredictiveControl
import unittest
from mobrl.algo.rl.model_based.misc.terminal_func.terminal_func import RandomTerminalFunc
from mobrl.algo.rl.model_based.misc.reward_func.reward_func import RandomRewardFunc
import numpy as np
from mobrl.test.tests.set_up.setup import TestTensorflowSetup
from mobrl.algo.rl.policy.random_policy import UniformRandomPolicy
from mobrl.algo.rl.policy.random_policy import UniformRandomPolicy


class TestMPC(TestTensorflowSetup):

    def test_init_discrete(self):
        algo, locals = self.create_mpc()
        env_spec = locals['env_spec']
        env = locals['env']
        algo.init()
        for _ in range(100):
            assert env_spec.action_space.contains(algo.predict(env_spec.obs_space.sample()))

        st = env.reset()
        data = TransitionData(env_spec)

        for _ in range(10):
            ac = algo.predict(st)
            new_st, re, done, _ = env.step(action=ac)
            data.append(state=st,
                        new_state=new_st,
                        reward=re,
                        action=ac,
                        done=done)
        print(algo.train(batch_data=data))

    def test_init_continuous(self):
        algo, locals = self.create_mpc(env_id='Swimmer-v1')
        env_spec = locals['env_spec']
        env = locals['env']
        algo.init()
        for _ in range(100):
            assert env_spec.action_space.contains(algo.predict(env_spec.obs_space.sample()))

        st = env.reset()
        data = TransitionData(env_spec)

        for _ in range(10):
            ac = algo.predict(st)
            new_st, re, done, _ = env.step(action=ac)
            data.append(state=st,
                        new_state=new_st,
                        reward=re,
                        action=ac,
                        done=done)
        print(algo.train(batch_data=data))


if __name__ == '__main__':
    unittest.main()