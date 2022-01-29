from torch.nn.modules.loss import _Loss


class my_loss(_Loss):
    def __init__(self, size_average=None, reduce=None, reduction: str='mean'):
        super(my_loss,self).__init__(size_average,  reduce, reduction)


    def forward(self):
        return 0
