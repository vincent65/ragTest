from langchain_aws import BedrockEmbeddings
import boto3

def get_embedding_function():
    client = boto3.client(
        service_name="bedrock-runtime",
        region_name="us-east-1",
        aws_access_key_id="",      # optional - set this value if you haven't run `aws configure` 
        aws_secret_access_key="",  # optional - set this value if you haven't run `aws configure`
        # aws_session_token=SESSION_TOKEN,
    )
    embeddings = BedrockEmbeddings(client=client, credentials_profile_name="default", region_name="us-east-1")
    return embeddings