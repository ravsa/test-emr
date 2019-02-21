print("HELLO WORLD")

from rudra import logger
from rudra.data_store.aws import AmazonS3
from sys import argv
from json import loads
import os



def load_hyper_params():
    """Load the hyper parameter from the command line args."""
    if len(argv) > 1:
        input_data = argv[1:]
        try:
            if input_data:
                input_data = loads(input_data[0])
                logger.info("Hyper Parameter", extra={
                            "hyper_params": input_data})
                return input_data
        except Exception as exc:
            logger.error("Unable to decode the hyper params")


bucket_name = 'boosters-manifest'
filename = 'test.json'
aws_s3 = AmazonS3(bucket_name=bucket_name,
                  aws_access_key_id=os.getenv('AWS_S3_ACCESS_KEY_ID'),
                  aws_secret_access_key=os.getenv('AWS_S3_SECRET_ACCESS_KEY'))
aws_s3.connect()
print(aws_s3.is_connected())
data = load_hyper_params()
print(data)
aws_s3.write_json_file(filename, data)
