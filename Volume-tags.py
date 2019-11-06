import boto3
client = boto3.client('ec2')
response = client.create_tags(
    Resources=[
        'vol-id1','vol-id2'
    ],
    Tags=[
        {
            'Key': 'Application',
            'Value': 'CBS',
        },
        {
            'Key': 'Cost Center',
            'Value': 'Non-Production',
        },
        {
            'Key': 'Department',
            'Value': 'Finance',
        },
        {
            'Key': 'Environment',
            'Value': 'NPRD',
        },
        # {
        #     'Key': 'Name',
        #     'Value': '',
        # },
    ],
)
