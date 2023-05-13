import tensorflow as tf

def ssim(input_img, output_img):
    return 1 - tf.reduce_mean(tf.image.ssim(input_img, tf.cast(output_img, tf.float64), max_val=1))
