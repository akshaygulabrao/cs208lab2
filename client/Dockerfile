# Get the latest base image for python
FROM python:latest
# Put files at the image '/client/' folder.
ADD client.py /client_persistent_storage/
# '/server/' is base directory
WORKDIR /client_persistent_storage/
# execute the command
CMD [ "python3", "client.py" ]
