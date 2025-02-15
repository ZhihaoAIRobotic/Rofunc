import rofunc as rf
import numpy as np
from rofunc.config.get_config import *


def test_2d_cp_ilqr():
    cfg = get_config('./', 'ilqr')

    # Via-points
    Mu = np.array([[2, 1, -np.pi / 2], [3, 1, -np.pi / 2]])  # Via-points
    Rot = np.zeros([2, 2, cfg.nbPoints])  # Object orientation matrices

    # Object rotation matrices
    for t in range(cfg.nbPoints):
        orn_t = Mu[t, -1]
        Rot[t] = np.asarray([
            [np.cos(orn_t), -np.sin(orn_t)],
            [np.sin(orn_t), np.cos(orn_t)]
        ])

    u0 = np.zeros(cfg.nbVarU * (cfg.nbData - 1))  # Initial control command
    x0 = np.array([3 * np.pi / 4, -np.pi / 2, -np.pi / 4])  # Initial state

    rf.lqr.uni_cp(Mu, Rot, u0, x0, cfg, for_test=True)


if __name__ == '__main__':
    test_2d_cp_ilqr()
