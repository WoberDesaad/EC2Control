import json
import datetime
import os
import boto3
import datetime

def handler(event, context):
    sns_client = boto3.client('sns')
    for record in event["Records"]:
        instance = json.loads(record["body"])
        InstanceId = instance["InstanceId"]
        message = "Instance " + InstanceId + " Exists."
        sns_client.publish(TopicArn=os.environ["SNS_TOPIC"], Message=message)


