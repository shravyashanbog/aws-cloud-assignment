import boto3
import json
import uuid
from datetime import datetime
import logging

# Initialize logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CloudAssignmentTable')

def lambda_handler(event, context):
    logger.info(f"Incoming Event Data: {json.dumps(event)}")

    try:
        # Process each uploaded file
        for record in event['Records']:

            bucket_name = record['s3']['bucket']['name']
            object_key = record['s3']['object']['key']
            file_size = record['s3']['object'].get('size', 0)

            logger.info(
                f"Ingesting object '{object_key}' from S3 bucket '{bucket_name}'"
            )

            record_id = str(uuid.uuid4())
            timestamp = datetime.utcnow().isoformat()

            item = {
                'id': record_id,
                'fileName': object_key,
                'bucketName': bucket_name,
                'fileSize': int(file_size),
                'processedTime': timestamp,
                'status': 'Completed',
                'metadata': {
                    'eventSource': record.get('eventSource', 'aws:s3'),
                    'awsRegion': record.get('awsRegion', 'ap-south-1'),
                    'sourceIp': record.get('requestParameters', {}).get(
                        'sourceIPAddress',
                        'Unknown'
                    )
                }
            }

            table.put_item(Item=item)

            logger.info(
                f"Successfully committed record {record_id} to DynamoDB"
            )

        return {
            "statusCode": 200,
            "body": json.dumps("Event processing completed successfully!")
        }

    except Exception as e:
        logger.error(f"Fatal error executing Lambda pipeline: {str(e)}")
        raise e
