import requests
from kraken import binarization
from PIL import Image, ImageOps
import PIL
import numpy as np
import pandas as pd
import io

def url_2_binary_array(class_label, url):
    try:
        # Download the image from the URL
        response = requests.get(url)
        img = Image.open(io.BytesIO(response.content))

        # Binarize the image with Kraken
        img_bw = binarization.nlbin(img, threshold=0.5)

        # Invert the image
        img_bw = ImageOps.invert(img_bw)

        # Resize the image to 784x784 pixels
        img_resized = img_bw.resize((28, 28))
        print(img_resized, 'img size')

        # Convert the image to a numpy array and flatten it
        arr = np.array(img_resized)#.flatten()[:785]
        print(type(arr))  # <class 'numpy.ndarray'>
        print(arr.shape)  # (2, 3)
        print(arr.size)   # 6
        print(arr.dtype)  # int64
        print(arr.ndim)  
        arr = arr.ravel()
        print(type(arr))  # <class 'numpy.ndarray'>
        print(arr.shape)  # (2, 3)
        print(arr.size)   # 6
        print(arr.dtype)  # int64
        print(arr.ndim) 

        # Create a dictionary that represents the binary array as a Pandas DataFrame
        pixel_dict = {'label': class_label}
        pixel_dict.update({f"pixel{i+1}": [val] for i, val in enumerate(arr)})
        
        # Clip the pixel values to 0 or 1

#this is also clipping label values...        pixel_dict = {k: np.clip(v, 0, 1) for k, v in pixel_dict.items()}

        # Create the Pandas DataFrame
        df = pd.DataFrame(pixel_dict)
        print(df, 'df being added to data.csv')

        # Save the binarized image as a PNG file
        img_bw.save('binary_image.png')

        return df
    
    except (requests.exceptions.RequestException, PIL.UnidentifiedImageError):
        # Skip processing this image if there's an error
        print(f"Skipping image at URL: {url}")
        return None
