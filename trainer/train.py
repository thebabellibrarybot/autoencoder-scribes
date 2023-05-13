import tensorflow as tf
import tensorflow.keras as keras
import matplotlib.pyplot as plt
import numpy as np
import wandb

from tensorflow.keras.losses import MeanSquaredError

def ssim(input_img, output_img):
    return 1 - tf.reduce_mean(tf.image.ssim(input_img, tf.cast(output_img, tf.float64), max_val=1))

def train_model(epochs, data, learning_rate, dataloader, autoencoder, wandb_proj):

    # set up wandb logger
    wandb.login()
    wandb.init(project=wandb_proj)

    # load model
    model = autoencoder()

    # load data
    loaded_data = dataloader(data)
    train_ds = loaded_data['train']
    test_ds = loaded_data['test']
    val_ds = loaded_data['val']

    # set params
    optimizer = keras.optimizers.Adam(learning_rate)

    # training loop, epochs should be a hyper-parameter
    EPOCHS = epochs
    
    for epoch in range(EPOCHS):
        total_loss = 0
        for step, (image) in enumerate(train_ds):
            with tf.GradientTape() as tape:
                output = model(image, training=True)
                loss = ssim(image, output)
            grads = tape.gradient(loss, model.trainable_weights)
            optimizer.apply_gradients(zip(grads, model.trainable_weights))
            total_loss += loss.numpy()

        print(f"Epoch {epoch+1}: loss: {total_loss/(step+1)}")
        wandb.log({"loss": total_loss/(step+1), "epoch": epoch+1})
        
        fig, ax = plt.subplots(2, 5)
        for step, (image) in enumerate(val_ds.take(5)):
            output = model(image, training=False)
            loss = ssim(image, output)
            ax[0][step].imshow(image.numpy()[0], cmap="gray")
            ax[1][step].imshow(output.numpy()[0], cmap="gray")
            fig.suptitle(f"Epoch: {epoch+1}")
        
        wandb.log({"validation examples over training period": wandb.Image(fig)})

        
    all_loss = []
    for step, (image) in enumerate(test_ds):
        output = model(image, training=False)
        loss = ssim(image, output)
        wandb.log({"val_loss_for_threshold": loss.numpy()})
        all_loss.append(loss.numpy())

    _99th_percentile = np.percentile(all_loss,q=99)
    print(_99th_percentile)

    THRESH_LOSS = _99th_percentile

    outliers = []
    extreme_outliers = []
    all_loss = []
    for image in test_ds:
        output = model(image, training=False)
        loss = ssim(image, output)
        all_loss.append(loss.numpy())
        wandb.log({"test_loss":loss.numpy()})
        if loss.numpy() > THRESH_LOSS:
            fig, ax = plt.subplots(1, 2)
            ax[0].imshow(image.numpy()[0], cmap="gray")
            ax[0].title.set_text("Original")
            ax[1].imshow(output.numpy()[0], cmap="gray")
            ax[1].title.set_text("Reconstructed")
            wandb_img = wandb.Image(fig, caption=f"Loss: {loss.numpy():.5f}")
            if loss.numpy() < THRESH_LOSS+0.003:
                wandb.log({"test_outlier_loss":loss.numpy()})
                outliers.append(wandb_img)
                continue
            wandb.log({"extreme_test_outliers_loss":loss.numpy()})
            extreme_outliers.append(wandb_img)
    wandb.log({"test_outliers":outliers})
    wandb.log({"extreme_test_outliers":extreme_outliers})
