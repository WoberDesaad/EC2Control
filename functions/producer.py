import json
import datetime
import boto3
import os


def handler(event, context):
    queue_client = boto3.client("sqs")
    ec2_client = boto3.client("ec2")
    s3_client = boto3.client("s3")

    ec2_queue_url = queue_client.get_queue_url(QueueName=os.environ["EC2_QUEUE_NAME"], QueueOwnerAWSAccountId=os.environ["ACCOUNT_ID"])
    s3_queue_url = queue_client.get_queue_url(QueueName=os.environ["S3_QUEUE_NAME"], QueueOwnerAWSAccountId=os.environ["ACCOUNT_ID"])

    # Get information on all instnaces
    response = ec2_client.describe_instances()

    # Write Data to Queue
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            queue_client.send_message(QueueUrl=ec2_queue_url["QueueUrl"], MessageBody=json.dumps(instance, indent=4, sort_keys=True, default=str))

    # Get S3 information
    response = s3_client.list_buckets()

    # Write Data to Queue
    for bucket in response["Buckets"]:
        queue_client.send_message(QueueUrl=s3_queue_url["QueueUrl"], MessageBody=json.dumps(bucket, indent=4, sort_keys=True, default=str))


