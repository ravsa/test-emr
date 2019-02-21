print("HELLO WORLD")
import os, json

print(os.getenv('AWS_S3_ACCESS_KEY_ID'))
print(os.getenv('HYPER_PARAMS'))
print(json.loads(os.getenv('HYPER_PARAMS')))
