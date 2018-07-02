import boto3
import logging
import json
import os
from botocore.exceptions import ClientError


def ec2_list():
    '''
    List EC2 resources
    '''
    # region = ['us-east-2','us-east-1','us-west-1','us-west-2','ap-northeast-1', \
    #         'ap-northeast-2','ap-northeast-3','ap-south-1','ap-southeast-1', \
    #         'ap-southeast-2','ca-central-1','cn-north-1','cn-northwest-1','eu-central-1','eu-west-1','eu-west-2', \
    #         'eu-west-3','sa-east-1']


    ARN = os.environ['ARN']
    external_id = os.environ['EXTERNAL_ID']
    region = ['us-east-2','us-east-1','us-west-1','us-west-2', \
           'ap-southeast-2','ca-central-1','sa-east-1']


    try:
        client = boto3.client('sts')
        response = client.assume_role(RoleArn=ARN,RoleSessionName='listing',ExternalId=external_id)

        #Init Dictionary
        ec2_dict = {}
        session = boto3.session.Session(aws_access_key_id=response['Credentials']['AccessKeyId'], \
                aws_secret_access_key=response['Credentials']['SecretAccessKey'], aws_session_token=response['Credentials']['SessionToken'])

        for r in range(len(region)):
            ec2 = session.resource('ec2',region[r])
            ec2_all = ec2.instances.all()
            ec2_dict[region[r]] = {}
            for e in ec2_all:
                ec2_dict[region[r]][e.instance_id] = {
                            'type': e.instance_type,
                            'platform' : e.platform,
                            'launch_time' : (e.launch_time).isoformat(),
                            'state': e.state['Name']

                    }
        #return json.dumps(ec2_dict)
        return ec2_dict

    except ClientError as e:

        return {'error':e.response['Error']['Message']}
