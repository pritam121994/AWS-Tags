import boto3
client = boto3.client('elbv2')
response = client.add_tags(
    ResourceArns=[
        'arn:aws:elasticloadbalancing:',
    ],
    Tags=[
        {
            'Key': 'Application',
            'Value': 'EBS',
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
        {
            'Key': 'Name',
            'Value': 'Instancename',
        },
    ]
)
