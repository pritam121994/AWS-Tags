import boto3
client = boto3.client('ec2')
response1 = client.delete_tags(
    Resources=[
        'vol-id',
    ],
    Tags=[
        {
            'Key': 'Name1',
            'Value': 'xyz',
        },
    ],
)
