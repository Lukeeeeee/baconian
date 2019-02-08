import tensorflow as tf

from src.core.parameters import Parameters
from src.envs.env_spec import EnvSpec
from src.rl.value_func.value_func import PlaceholderInputValueFunction


class MLPQValueOnActions(PlaceholderInputValueFunction):

    def __init__(self, env_spec: EnvSpec, parameters: Parameters = None, input: tf.Tensor = None):
        super().__init__(env_spec, parameters, input)

    def copy(self, obj) -> bool:
        return super().copy(obj)

    def forward(self, *args, **kwargs):
        pass

    def update(self, *args, **kwargs):
        pass
