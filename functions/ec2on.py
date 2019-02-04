import json
import datetime
import boto3


def handler(event, context):
    ec2_client = boto3.client("ec2")

    # Get information on all instnaces
    response = ec2_client.describe_instances()

    stopped_instances = []
    # GO through Each Instance and determine if it is on or not.
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            # Check instance stuff
            InstanceId = instance["InstanceId"]
            State = instance["State"]["Name"]

            # if running
            if not State is "running":
                # turn off
                stopped_instances.append( InstanceId )


    response = ec2_client.start_instances(InstanceIds=stopped_instances)

