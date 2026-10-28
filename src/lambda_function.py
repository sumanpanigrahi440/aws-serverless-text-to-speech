import json
import os
import urllib.parse
import boto3

s3_client = boto3.client('s3')
polly_client = boto3.client('polly')

def lambda_handler(event, context):
    try:
        dest_bucket = os.environ.get('DEST_BUCKET')

        # S3 event se details retrieve karna
        source_bucket = event['Records'][0]['s3']['bucket']['name']
        source_key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])

        print(f"Reading file '{source_key}' from bucket '{source_bucket}'...")

        # S3 source bucket se text content fetch karna
        response = s3_client.get_object(Bucket=source_bucket, Key=source_key)
        text_content = response['Body'].read().decode('utf-8')

        print("Synthesizing speech using Amazon Polly...")
        # Amazon Polly API call
        polly_response = polly_client.synthesize_speech(
            Text=text_content,
            OutputFormat='mp3',
            VoiceId='Joanna'
        )

        # Output file name setup (.txt -> .mp3)
        file_base_name = os.path.splitext(source_key)[0]
        output_key = f"{file_base_name}.mp3"

        print(f"Saving '{output_key}' to destination bucket '{dest_bucket}'...")
        # Polly audio stream ko destination S3 bucket me store karna
        s3_client.put_object(
            Bucket=dest_bucket,
            Key=output_key,
            Body=polly_response['AudioStream'].read(),
            ContentType='audio/mpeg'
        )

        print("Processing completed successfully!")
        return {
            'statusCode': 200,
            'body': json.dumps(f"Successfully generated {output_key}")
        }

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        raise e