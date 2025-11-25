import boto3
import os
import io
from docx import Document

LOCAL_TEXT_FILE = "temp_resume_text.txt"
def extract_text_from_docx(docx_bytes):
 
    # Extract text from a DOCX file (bytes) using python-docx.

    file_stream = io.BytesIO(docx_bytes)
    document = Document(file_stream)
    text = "\n".join([para.text for para in document.paragraphs])
    return text

def extract_and_save_text(bucket_name, source_key, local_path):

    s3 = boto3.client('s3')

    try:
        print(f"1. Downloading {source_key} from S3...")
        response = s3.get_object(Bucket=bucket_name, Key=source_key)
        file_bytes = response['Body'].read()

        # Detect file extension
        _, ext = os.path.splitext(source_key.lower())

        print("Extracting text...")
        
        full_text = extract_text_from_docx(file_bytes)

        if not full_text.strip():
            raise ValueError("❌ Could not extract text from the document.")

        # Save text locally
        with open(local_path, 'w', encoding='utf-8') as f:
            f.write(full_text)

        print(f"3. Extracted text saved to {local_path}")
        return full_text

    except Exception as e:
        print(f"❌ Extraction Error: {e}")
        return None