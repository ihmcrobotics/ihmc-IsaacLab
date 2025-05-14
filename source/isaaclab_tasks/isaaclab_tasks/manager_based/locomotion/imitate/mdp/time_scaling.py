from __future__ import annotations

import torch
import numpy as np
from scipy.spatial.transform import Rotation as R
from scipy.spatial.transform import Slerp

from collections.abc import Sequence
from typing import TYPE_CHECKING

def scale_joints(input_dt: float, input_data: np.float64, output_dt: float) -> torch.Tensor:
    input_max_time = (input_data.shape[0]/(1/input_dt))
    output_time_steps = np.arange(input_dt, input_max_time, output_dt)
    input_time_steps = np.arange(input_dt, input_max_time+.00001, input_dt)
    data_converted = np.asarray([]).reshape(output_time_steps.shape[0],0)
    for i in range(input_data.shape[1]):
        ith_collum_data_converted = np.interp(output_time_steps, input_time_steps, input_data[:,i]).reshape(-1,1)
        data_converted = np.concatenate((data_converted, ith_collum_data_converted), axis=1)
    return torch.from_numpy(data_converted)


def scale_contacts(input_dt: float, input_data: np.float64, output_dt: float) -> torch.Tensor:
    input_max_time = (input_data.shape[0]/(1/input_dt))
    output_time_steps = np.arange(input_dt, input_max_time, output_dt)
    input_time_steps = np.arange(input_dt, input_max_time+.00001, input_dt)
    data_converted = np.asarray([]).reshape(output_time_steps.shape[0],0)
    for i in range(input_data.shape[1]):
        ith_collum_data_converted = np.interp(output_time_steps, input_time_steps, input_data[:,i]).reshape(-1,1)
        clipped_ith_collum_data_converted = (ith_collum_data_converted >= 0.5).astype(float)
        data_converted = np.concatenate((data_converted, clipped_ith_collum_data_converted), axis=1)
    return torch.from_numpy(data_converted)


def scale_roots(input_dt: float, input_data: np.float64, output_dt: float) -> torch.Tensor:
    input_max_time = (input_data.shape[0]/(1/input_dt))
    output_time_steps = np.arange(input_dt, input_max_time, output_dt)
    input_time_steps = np.arange(input_dt, input_max_time+.00001, input_dt)

    data_converted = np.asarray([]).reshape(output_time_steps.shape[0],0)
    for i in range(input_data.shape[1]):
        if i == 3:
            slerp = Slerp(input_time_steps, R.from_quat(input_data[:,3:7]))
            scaled_rotations = slerp(output_time_steps)
            ith_collum_data_converted = np.asarray(scaled_rotations.as_quat())
            data_converted = np.concatenate((data_converted, ith_collum_data_converted), axis=1)
        elif i >= 4 and i <= 6:
            pass
        elif i >= 10:
            # for j in range(input_data.shape[0]-1):
            #     if (input_data[j,i] - input_data[j+1,i]) <= -np.pi:
            #         input_data[j+1:,i] = input_data[j+1:,i] - 2*np.pi
            #     elif (input_data[j,i] - input_data[j+1,i]) >= np.pi:
            #         input_data[j+1:,i] = input_data[j+1:,i] + 2*np.pi
            # input_data_vel = np.gradient(input_data[:,i], axis=0)*input_dt
            # ith_collum_data_converted = np.interp(output_time_steps, input_time_steps, input_data_vel).reshape(-1,1)
            ith_collum_data_converted = np.interp(output_time_steps, input_time_steps, input_data[:,i]).reshape(-1,1)
            data_converted = np.concatenate((data_converted, ith_collum_data_converted), axis=1)
        else:
            ith_collum_data_converted = np.interp(output_time_steps, input_time_steps, input_data[:,i]).reshape(-1,1)
            data_converted = np.concatenate((data_converted, ith_collum_data_converted), axis=1)

    return torch.from_numpy(data_converted)
