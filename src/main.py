from extract import *
from transform import *
from load import *
from config_reader import load_config

config = load_config()
bucket_name = config["aws"]["bucket_name"]
resume_key = config["aws"]["resume_key"]

def main():
    raw_data=extract_and_save_text(bucket_name,resume_key,LOCAL_TEXT_FILE)
    dataframe=parse_resume_text(raw_data)
    print(dataframe)
    dataframe.to_csv('dataframe.csv',index=False)
    establish_connection()
    load_data(dataframe,'parsed_resume_docx')
    close_connection()

    pass

if __name__=='__main__':
    main()