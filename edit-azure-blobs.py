from azure.storage.blob import BlobServiceClient
import re

connection = "connection-string-here"
container_name = "container-name-here"
blob_service_client = BlobServiceClient.from_connection_string(connection)
container_client = blob_service_client.get_container_client(container_name)

pattern = re.compile(r'"(password|remember_token)":"[^"]{1,100}"')

def process_blob(blob_name):
    blob_client = container_client.get_blob_client(blob_name)
    blob_data = blob_client.download_blob().readall().decode('utf-8')

    modified_data = re.sub(pattern, r'"\1":"***"', blob_data)

    blob_client.upload_blob(modified_data, overwrite=True)

blob_list = container_client.list_blobs()
for blob in blob_list:
    print(f"Processing blob: {blob.name}")
    process_blob(blob.name)
    print(f"Blob {blob.name} processed.")
