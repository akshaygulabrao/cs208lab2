# Get the latest base image for python
FROM python:latest
# Put files at the image '/server/' folder.
ADD server.py /server_persistent_storage/
ADD mydata.txt /server_persistent_storage/
# '/server/' is base directory
WORKDIR /server_persistent_storage/
# Expose port 9898 in the container
EXPOSE 9898
# execute the command
CMD [ "python3", "server.py" ]
