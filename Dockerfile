FROM python:3.12.3-alpine3.19

WORKDIR /usr/share/src 

COPY /src/requirements.txt  ./requirements.txt 

COPY /src/requirements.dev.txt  ./requirements.dev.txt 


RUN  pip install -r ./requirements.txt \
   && pip install  -r ./requirements.dev.txt 
   
COPY /src/  ./ 


ENV PYTHONBUFFERED 1 


#ENTRYPOINT [ "python3","-u", "main"] 
#CMD ["echo"]
 