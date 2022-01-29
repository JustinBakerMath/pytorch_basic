import torch
import torch.nn as nn


class my_model(nn.Module):
    def __init__(self,*args):
        super(my_model,self).__init__()

        self.args = args

    """
    FORWARD METHOD
        - define forward method for when the model is called forward
    """
    def forward(self):

        return 0
