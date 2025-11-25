📄 README.md — Resume Parsing ETL Pipeline

🚀 Project Overview

This project performs an end-to-end ETL (Extract → Transform → Load) pipeline for resume parsing using:

AWS S3 (input storage)

Python (ETL processing)

Regex-based text extraction (Name, Email, Skills, Education, Projects, Certifications, Experience)

MySQL Database (final storage)

Resumes can be uploaded in PDF or DOCX format.
The pipeline extracts text → cleans → structures → loads into MySQL.

🗂 Project Structure

      UNSTRUCTURED_DATA_2/
      │
      ├── config/
      │   └── config.ini
      │
      ├── src/
      │   ├── extract.py
      │   ├── transform.py
      │   ├── load.py
      │   ├── main.py
      │   ├── config_reader.py
      │   ├── temp_resume_text.txt     # Generated file (ignored by Git)
      │   └── dataframe.csv            # Generated output
      │
      ├── .gitignore
      └── README.md

⚙️ Features

✔ Extract

Download resume file from AWS S3

Read PDF using PyPDF2

Read DOCX using python-docx

Save text into temp_resume_text.txt

✔ Transform

Your custom parser extracts:

Field	Description

  Name	First line detected in resume
  Email	Regex-based
  Summary	Objective / Summary section
  Skills	Detected from predefined skill keywords
  Experience_List	Extracted from INTERNSHIPS / numbered blocks
  Education	Academic details
  Certifications	Certificates / Licenses section
  Projects	Academic or personal projects
  Others	Everything not matching above sections

Output → Clean DataFrame with 1 row per resume.

✔ Load

MySQL table is created dynamically based on DataFrame columns

Python objects → converted to SQL-friendly types

Lists → stored as semicolon-separated strings

Inserts rows into MySQL safely

⚙️ Configuration

📍 config/config.ini

[aws]
  bucket_name = s3-bucket-for-resume-parsing
  resume_key = incoming/resume1.pdf
  aws_access_key = YOUR_AWS_ACCESS_KEY
  aws_secret_key = YOUR_AWS_SECRET_KEY
  aws_region = ap-south-1
  
  [mysql]
  host = localhost
  user = root
  password =
  database = PythonLearningDB
  port = 3306


Never commit real credentials — .gitignore protects config.ini.

🛠 How It Works

Step 1 — Extract

extract.py downloads and extracts text:

  raw_text = extract_and_save_text("temp_resume_text.txt")

Step 2 — Transform

transform.py parses the resume text:

  df = parse_resume_text(raw_text)

Step 3 — Load

load.py creates table and inserts data:

  conn = establish_connection()
  load_data(df, "parsed_resume")

▶️ Running the Full Pipeline

From the root folder:

  cd src
  python main.py


This performs:

Download →

Text Extraction →

Parsing →

MySQL Insertion

🧪 Example Output (DataFrame)

  Name	Email	Skills	Summary	Experience_List	Education	Projects	Certifications	Others

Automatically generated from the resume text.

📦 Installation Requirements

Create a requirements.txt:

  boto3
  PyPDF2
  python-docx
  pandas
  mysql-connector-python


Install dependencies:

  pip install -r requirements.txt

🔐 Security Notes

config.ini contains sensitive information

✔ Should never be committed

✔ Protected via .gitignore

Use IAM User with restricted permissions for S3 access

Consider environment variables for production deployments

🚧 Future Enhancements

Add phone number extraction

Improve section detection using AI/LLMs

Add support for .doc using textract / antiword

Build REST API using FastAPI

Deploy ETL pipeline on AWS Lambda

📞 Support

If you need help improving the parser or extending the ETL pipeline, feel free to reach out!
