from mbrl.algo.rl.policy.policy import Policy
from typeguard import typechecked
from mbrl.envs.env_spec import EnvSpec
import overrides
import numpy as np
import tensorflow as tf
from mbrl.tf.mlp import MLP


class NormalDistributionMLPPolicy(Policy):

    def __init__(self, env_spec: EnvSpec, name_scope: str, mlp_config: list):
        super().__init__(env_spec)
        obs_dim = env_spec.flat_obs_dim
        action_dim = env_spec.flat_action_dim
        assert action_dim == mlp_config[-1]['OUTPUT_DIM']
        with tf.variable_scope(name_scope):
            self.state_ph = tf.placeholder(shape=[None, obs_dim], dtype=tf.float32, name='state_ph')
        self.mlp_net = MLP(config_list=mlp_config,
                           input_ph=self.state_ph,
                           mlp_net_name='normal_mlp_policy',
                           name_scope=name_scope)
        self.action_tensor = self.mlp_net.output

    @typechecked
    @overrides.overrides
    def sample(self, obs: (np.ndarray, list), *arg, **kwargs):
        res = self.mlp_net.forward(input=obs)
        return res

    @overrides.overrides
    def copy_from(self, obj) -> bool:
        assert isinstance(obj, (type(self), MLP))
        self.mlp_net.copy_from(obj=obj.mlp_net if isinstance(obj, type(self)) else obj)
        return super().copy_from(obj)