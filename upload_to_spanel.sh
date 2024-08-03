#!/bin/bash

# FTP server details
FTP_HOST=""
FTP_USER=""
FTP_PASS=""

# Local file path
LOCAL_DIR=""

# Name for the zip file
ZIP_FILE="control.zip"

REMOTE_DIR="/"

# creating a zip file of the directory
echo "Creating zip file..."
zip -r "$ZIP_FILE" "$LOCAL_DIR"

# ceck if zip wass successful
if [ $? -ne 0 ]; then
	echo " Failed to create zip file. Exiting."
	exit 1
fi

echo "Zip file created successfully."

# use ftp command to upload the file
# echo "Uploading zip file..."
# ftp -n $FTP_HOST <<END_SCRIPT
# quote USER $FTP_USER
# quote PASS $FTP_PASS
# binary
# cd $REMOTE_DIR
# put $ZIP_FILE
# quit
# END_SCRIPT

# cgecj uf ftp upload was seccessful
# if [ $? -ne 0]; then
# 	echo "Failed to upload zip file. Exiting."
# 	exit 1
# fi

# echo " File uploaded successfully!"
