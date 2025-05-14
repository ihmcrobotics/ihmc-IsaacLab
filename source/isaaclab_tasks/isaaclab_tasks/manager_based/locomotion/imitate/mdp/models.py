from __future__ import annotations

import torch
import torch.nn as nn
# import numpy as np
# from scipy.spatial.transform import Rotation as R
# from scipy.spatial.transform import Slerp

# from collections.abc import Sequence
# from typing import TYPE_CHECKING

# # NN training function
class Autoencoder(nn.Module):
    def __init__(self, input_size, output_size):
        super(Autoencoder, self).__init__()
        hidden_size = [2048,1024,512,8]
        self.encoder = nn.Sequential(
        nn.Dropout(.2),
        nn.Linear(input_size, hidden_size[0]), # nn.BatchNorm1d(hidden_size[0]),nn.Dropout(.2),
        nn.ReLU(),
        nn.Linear(hidden_size[0], hidden_size[1]), # nn.BatchNorm1d(hidden_size[1]),nn.Dropout(.2),
        nn.ReLU(),
        nn.Linear(hidden_size[1], hidden_size[2]),
        nn.ReLU(),
        nn.Linear(hidden_size[2], hidden_size[3]),
        )
        self.decoder = nn.Sequential(
        nn.Linear(hidden_size[3], hidden_size[2]),
        nn.ReLU(),
        nn.Linear(hidden_size[2], hidden_size[1]), # nn.BatchNorm1d(hidden_size[1]),nn.Dropout(.2),
        nn.ReLU(),
        nn.Linear(hidden_size[1], hidden_size[0]), # nn.BatchNorm1d(hidden_size[1]),nn.Dropout(.2),
        nn.ReLU(),
        nn.Linear(hidden_size[0], output_size),
        )
    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded
    


    # # NN training function
class LatentAutoencoder(nn.Module):
    def __init__(self, input_size, latent_addition_size, output_size):
        super(LatentAutoencoder, self).__init__()
        hidden_size = [2048,1024,512,8]
        self.encoder = nn.Sequential(
        nn.Dropout(0),
        nn.Linear(input_size, hidden_size[0]),
        nn.ReLU(),
        nn.Linear(hidden_size[0], hidden_size[1]),
        nn.ReLU(),
        nn.Linear(hidden_size[1], hidden_size[2]),
        nn.ReLU(),
        nn.Linear(hidden_size[2], hidden_size[3]),
        )
        self.decoder = nn.Sequential(
        nn.Linear(hidden_size[3]+latent_addition_size, hidden_size[2]), 
        nn.ReLU(),
        nn.Linear(hidden_size[2], hidden_size[1]), 
        nn.ReLU(),
        nn.Linear(hidden_size[1], hidden_size[0]), 
        nn.ReLU(),
        nn.Linear(hidden_size[0], output_size),
        )
    def forward(self, x1, x2):
        encoded = self.encoder(x1)
        latent = torch.concatenate((encoded, x2), dim=1)
        decoded = self.decoder(latent)
        return decoded
    


class Encoder(nn.Module):
    def __init__(self, input_size, output_size):
        super(Encoder, self).__init__()
        hidden_size = [2048,1024,512]
        self.encoder = nn.Sequential(
        nn.Linear(input_size, hidden_size[0]), # nn.BatchNorm1d(hidden_size[0]), nn.Dropout(.2),
        nn.ReLU(),
        nn.Linear(hidden_size[0], hidden_size[1]), # nn.BatchNorm1d(hidden_size[1]), nn.Dropout(.2),
        nn.ReLU(),
        nn.Linear(hidden_size[1], hidden_size[2]),
        nn.ReLU(),
        nn.Linear(hidden_size[2], output_size),
        )
    def forward(self, x1):
        encoded = self.encoder(x1)
        return encoded