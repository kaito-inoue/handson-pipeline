import json

def lambda_handler(event, context):
    print("codepipelineが実行されました")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
