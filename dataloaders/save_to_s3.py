import boto3
from botocore.exceptions import NoCredentialsError
import io

def upload_to_s3(class_name, img_resized, url, bucket_name, access_key, secret_key):
    # Create a connection to S3
    s3 = boto3.client('s3', aws_access_key_id=access_key,
                      aws_secret_access_key=secret_key)
    
    # Convert the image to bytes and create the S3 object key (filename)
    img_bytes = io.BytesIO()
    img_resized.save(img_bytes, format='PNG')
    s3_filename = url + '_' + class_name + '.png'
    
    # Upload the image to S3
    try:
        s3.upload_fileobj(img_bytes, bucket_name, s3_filename)
        print(f"Successfully uploaded {s3_filename} to S3 bucket {bucket_name}")
    except NoCredentialsError:
        print("Unable to access AWS credentials")
    except Exception as e:
        print(f"Failed to upload {s3_filename} to S3 bucket {bucket_name}: {e}")
