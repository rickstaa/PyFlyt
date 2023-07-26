"""PyFlyt - Multi UAV simulation environment for reinforcement learning research."""
import warnings

import pybullet
from gymnasium.utils import colorize

# Throw error if pybullet is not installed with numpy support.
if not pybullet.isNumpyEnabled():
    warnings.warn(
        colorize(
            (
                "PyBullet is not installed properly with Numpy functionality! This will "
                "result in a significant performance hit when vision is used.\n\n"
                "You can fix this by installing Numpy again and rebuilding PyBullet:\n"
                "\tpip3 uninstall pybullet -y\n"
                "\tpip3 install numpy\n"
                "\tpip3 install pybullet --no-cache-dir"
            ),
            color="yellow",
        ),
        category=RuntimeWarning,
    )
