from torch.utils.data import Dataset

class my_map_dataset(Dataset):
    def __init__(self,*args):
        self.args = args

    def __len__(self):
        return 0

    def __get_item__(self,idx):
        return 0,0

class my_iter_dataset(Dataset):
    def __init__(self,*args):
        self.args = args

    def __iter__(self):
        return 0,0
