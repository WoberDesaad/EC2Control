import json
import datetime
import os
import boto3
import datetime

def handler(event, context):
    sns_client = boto3.client('sns')
    for record in event["Records"]:
        bucket = json.loads(record["body"])
        message = "Bucket " + bucket["Name"] + " Created on " + bucket["CreationDate"]
        sns_client.publish(TopicArn=os.environ["SNS_TOPIC"], Message=message)


