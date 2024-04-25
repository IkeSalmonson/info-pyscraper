
## Introduction
 `pyscraper` is a dockerized python app to search for Logo images and phone contact information on simple html pages. 



## Usage 
 To run the application, make sure to have the prerequesit installed: 
    - Docker    

 To build Docker Image:
 ```
     docker build -f 'Dockerfile.prod' -t 'pyscraper'  .  
```

 To run with website.txt as input, copy website.txt to local repository or reference as a valid relative path: 
 ```
 cat website.txt | docker run -i pyscraper
```
 


# Development

Consider running the commands from within the `src` folder:

 To build a development Docker Image:
```
    docker build -t 'pyscraper:dev'  .   
```

 Running develpment image on local volume: 
```
cat test.txt |docker run -i -v $(pwd)/src:/usr/share/src    ikesalmonson/python-hello python3 -u compose_app
```


## Code quality

The package `pylint` is needed for this section.

Run the command `python3 -m pylint .` to run the linter toolkit.

## Unit testing

The package `pytest` is needed for this section.

Run the command ``python3 -m pytest test/ to run the unit tests.

## Improvments
 
 Add comprehensive phone library to parse phone information: 
 - https://pypi.org/project/phonenumbers/
     - https://github.com/google/libphonenumber/

 Add resilience to webscraper blocks by:
 - Using differente request headers 
 - Using a crawler browser 

