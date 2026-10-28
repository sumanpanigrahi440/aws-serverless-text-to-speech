# AWS Serverless Text-to-Speech Pipeline

An automated, event-driven serverless pipeline built on AWS to convert uploaded text files into MP3 speech audio files using Amazon S3, AWS Lambda, and Amazon Polly.


### Workflow Steps:
1. **File Upload:** User uploads a `.txt` file to the Source Amazon S3 bucket.
2. **Event Trigger:** S3 triggers an `ObjectCreated` event notification for `.txt` files.
3. **Lambda Execution:** AWS Lambda reads the file content from the source bucket.
4. **Speech Synthesis:** Lambda invokes Amazon Polly (`Joanna` voice) to synthesize speech audio from the text.
5. **Output Delivery:** The resulting MP3 stream is stored into the Destination Amazon S3 bucket for download.

---

## 🛠️ AWS Services & Technologies Used
* **Amazon S3:** Source & destination object storage with event notification triggers.
* **AWS Lambda:** Serverless compute running Python runtime to handle business logic.
* **Amazon Polly:** AI-driven speech synthesis to convert text into natural-sounding speech.
* **AWS IAM:** Least-privilege execution role attached to Lambda.
* **Amazon CloudWatch:** Logging and operational monitoring