FROM python:3.12.3-alpine3.19


#RUN pip install --no-cache-dir -r requirements.txt  

WORKDIR /usr/share/src 
COPY /src ./ 

# PYTHONBUFFERED 1 >> StdOut from docker container w/o buffering  
ENV PYTHONBUFFERED 1 


#CMD ["sh"]
ENTRYPOINT ["python3","-u", "hello.py"] 