FROM python:2.7
ENV PYTHONUNBUFFERED 1 
RUN mkdir /scripts
WORKDIR /scripts 
ADD requirement.txt /scripts/ 
RUN pip install -r requirement.txt
ADD . /scripts/ 
