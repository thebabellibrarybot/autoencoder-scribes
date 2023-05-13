import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf

@tf.function
def make_2d(row):
    image = tf.reshape(row, (28, 28))
    image = tf.cast(image, tf.float64)/255.
    image = tf.expand_dims(image, axis=-1)
    return image

def dataloader(data):
    url = 'https://raw.githubusercontent.com/thebabellibrarybot/autoencoder-scribes/main/dataloaders/data.csv'
    df = pd.read_csv(url)

    df, test_df = train_test_split(df, test_size=0.2, shuffle=True, random_state=42, stratify=df['label'])
    train_df, val_df = train_test_split(df, test_size = .2, shuffle = True, random_state=42, stratify=df['label'])

    train_ds = tf.data.Dataset.from_tensor_slices(train_df.drop(columns='label')).map(make_2d).batch(32)
    test_ds = tf.data.Dataset.from_tensor_slices(test_df.drop(columns='label')).map(make_2d).batch(1)
    val_ds = tf.data.Dataset.from_tensor_slices(test_df.drop(columns='label')).map(make_2d).batch(1)

    return {'train': train_ds, 'test': test_ds, 'val': val_ds}