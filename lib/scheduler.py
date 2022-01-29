from torch.optim.lr_scheduler import _LRScheduler


class my_scheduler(_LRScheduler):
    def __init__(self,optimizer,last_epoch=-1,verbose=False):
        super(my_scheduler,self).__init__(optimizer,last_epoch,verbose)

    def get_lr(self):
        return 0

    def load_state_dict(self):
        return 0

    def state_dict(self):
        return 0

    def step(self,closure=None):
        return 0
