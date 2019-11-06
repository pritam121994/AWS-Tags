import boto3
client = boto3.client('ec2')
response = client.create_tags(
    Resources=[
        'vol-0ec1447bec52fdc79','vol-0bc289afffd27607b','vol-02ac50e62b7f389bf'
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
# response1 = client.delete_tags(
#     Resources=[
#         'vol-045768f9c3f7edb88',
#     ],
#     Tags=[
#         {
#             'Key': 'Name1',
#             'Value': 'Mohan',
#         },
#     ],
# )