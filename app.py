import argparse
from trainer import train
from trainer.dataloader import dataloader
from trainer.model import autoencoder

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train Autoencoder model")

    parser.add_argument('--epochs', type=int, default=10, help='Number of epochs to train (default: 10)')
    parser.add_argument('--data', type=str, default='../dataloaders/data.csv', help='Directory where the data is stored (default: data)')
    parser.add_argument('--learning_rate', type=float, default=0.001, help='Learning rate for the optimizer (default: 0.001)')

    args = parser.parse_args()

    train.train_model(args.epochs, args.data, args.learning_rate, dataloader, autoencoder)
