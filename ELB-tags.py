import boto3
client = boto3.client('elbv2')
response = client.add_tags(
    ResourceArns=[
        'arn:aws:elasticloadbalancing:eu-west-1:378457291432:loadbalancer/app/CBSUATAE/f7e453515bf16ed1',
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
            'Value': 'EBSFESUAT01',
        },
    ]
)