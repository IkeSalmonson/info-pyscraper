FROM python:3.12.3-alpine3.19


#RUN pip install --no-cache-dir -r requirements.txt  



WORKDIR /usr/share/src 
COPY /src ./ 

RUN  pip install -r ./requirements.txt

# PYTHONBUFFERED 1 >> StdOut from docker container w/o buffering  
ENV PYTHONBUFFERED 1 

#ENTRYPOINT  ["python3"]

#ENTRYPOINT [ "python3","-u", "compose_app"] 
#CMD ["echo"]
 