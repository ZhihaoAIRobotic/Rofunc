import rofunc as rf
import numpy as np
from rofunc.config.get_config import *


def test_7d_uni_ilqr():
    # <editor-fold desc="7-dim Uni example">
    cfg = get_config('./', 'ilqr')
    # via-points
    Mu = np.array([[2, 1, -np.pi / 6], [3, 2, -np.pi / 3]])  # Via-points
    Rot = np.zeros([cfg.nbPoints, 2, 2])  # Object orientation matrices
    # Object rotation matrices
    for t in range(cfg.nbPoints):
        orn_t = Mu[t, -1]
        Rot[t, :, :] = np.asarray([
            [np.cos(orn_t), -np.sin(orn_t)],
            [np.sin(orn_t), np.cos(orn_t)]
        ])
    u0 = np.zeros(cfg.nbVarU * (cfg.nbData - 1))  # Initial control command
    x0 = np.array([3 * np.pi / 4, -np.pi / 2, -np.pi / 4])  # Initial state
    rf.lqr.uni(Mu, Rot, u0, x0, cfg, for_test=True)
    # </editor-fold>


if __name__ == '__main__':
    test_7d_uni_ilqr()
