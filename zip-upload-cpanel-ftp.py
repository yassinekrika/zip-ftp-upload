import os
import zipfile
from ftplib import FTP
from dotenv import load_dotenv

load_dotenv()

FTP_HOST = os.getenv('FTP_HOST')
FTP_USER = os.getenv('FTP_USER')
FTP_PASS = os.getenv('FTP_PASS')
LOCAL_DIR = os.getenv('LOCAL_DIR')

if not all([FTP_HOST, FTP_USER, FTP_PASS]):
    print("FTP credentials are not set in .env file")
    exit(1)

ZIP_FILE = "project_files.zip"

REMOTE_DIR = "/"

def zip_directory(path, zip_file):
    with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as ziph:
        for root, _, files in os.walk(path):
            for file in files:
                ziph.write(os.path.join(root, file),
                            os.path.relpath(os.path.join(root, file),
                                os.path.join(path, '..')))

def upload_to_ftp(ftp_host, ftp_user, ftp_pass, local_file, remote_dir):
    with FTP(ftp_host) as ftp:
        ftp.login(user=ftp_user, passwd=ftp_pass)
        ftp.cwd(remote_dir)
        with open(local_file, 'rb') as file:
            ftp.storbinary(f'STOR {os.path.basename(local_file)}', file)


def main():
    print("Creating zip file...")
    zip_directory(LOCAL_DIR, ZIP_FILE)
    print("Zip file created successfully.")

    print("Uploading zip file...")
    try:
        upload_to_ftp(FTP_HOST, FTP_USER, FTP_PASS, ZIP_FILE, REMOTE_DIR)
        print("File uploaded successfully")
    except Exception as e:
        print(f"Failed to upload zip file: {e}")
        return

if __name__ == "__main__":
    main()
