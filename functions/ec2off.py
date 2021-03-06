import json
import datetime
import boto3


def handler(event, context):
    ec2_client = boto3.client("ec2")

    # Get information on all instnaces
    response = ec2_client.describe_instances()

    running_instances = []
    # GO through Each Instance and determine if it is on or not.
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            # Check instance stuff
            InstanceId = instance["InstanceId"]
            State = instance["State"]["Name"]

            # if running
            if State == "running":
                # add to off list
                running_instances.append( InstanceId )


    if len(running_instances) > 0:
        response = ec2_client.stop_instances(InstanceIds=running_instances)

    return len(running_instances)
