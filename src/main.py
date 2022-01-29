import argparse
import torch
from torch.utils.data import DataLoader
from tqdm import trange

import sys
sys.path.append('./')

from lib.model import my_model
from lib.data_loader import my_map_dataset, my_iter_dataset
from lib.optimizer import my_optimizer
from lib.scheduler import my_scheduler
from lib.loss import my_loss


"""INPUTS"""
parser = argparse.ArgumentParser(description='Example Pytorch File Structure')
parser.add_argument('--num_epochs', type=int, default=1, help='number of training epochs')
args = parser.parse_args()


"""LOAD DATA"""
train_data = my_map_dataset() #my_iter_dataset()
test_data = my_map_dataset() #my_iter_dataset()

train_loader = DataLoader(train_data)
test_loader = DataLoader(test_data)

"""INITIALIZE MODEL"""
model = my_model()
optimizer = my_optimizer(params=None,defaults=None)
scheduler = my_scheduler(optimizer)
loss_fn = my_loss()

"""TRAINING"""
epochs = trange(args.num_epochs, desc='Training')
for epoch in epochs:
    epochs.set_description("Training")
    for data, label in train_loader:
        optimizer.zero_grad()
        prediction = model(data)
        loss = loss_fn(prediction, target)
        loss.backward()
        optimizer.step()
    scheduler.step()

    """VALIDATING"""
    epochs.set_description("Validating")
    for data,label in test_loader:
        optimizer.zero_grad()
        prediction = model(data)
        loss = loss_fn(prediction)
        valid_loss = loss.item()

