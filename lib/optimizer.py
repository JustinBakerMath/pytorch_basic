from torch.optim import Optimizer

class my_optimizer(Optimizer):

    def __init__(self,params,defaults,*args):
        self.args=args
        self.param_groups={}

    def add_param_group(self):
        return 0

    def load_state_dict(self):
        return 0

    def state_dict(self):
        return 0

    def step(self,closure=None):
        return 0
    
    def zero_grad(self):
        return 0
