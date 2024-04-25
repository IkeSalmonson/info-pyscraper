
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

 To build a development Docker Image:
```
docker build -t 'pyscraper:dev'  .   
```

 Running develpment image on local volume: 
```
cat test.txt |docker run -i -v $(pwd)/src:/usr/share/src pyscraper:dev python3 -u main.py
```


## Code quality

The dev docker image is needed for this section.  Run the command:
```
docker run -i -v $(pwd)/src:/usr/share/src  pyscraper:dev python3  -m pylint .
```
To run the linter toolkit.
Last run results: Your code has been rated at 5.93/10

## Unit testing [NO TESTS]
The dev docker image is needed for this section.  Run the command:

```
docker run -i -v $(pwd)/src:/usr/share/src  pyscraper:dev python3  -m pytest
```
to run the unit tests.

## Improvments
 Add unitest coverage 
 
 Add comprehensive phone library to parse phone information: 
 - https://pypi.org/project/phonenumbers/
     - https://github.com/google/libphonenumber/

 Add resilience to webscraper blocks by:
 - Using differente request headers 
 - Using a crawler browser 
 
 Add loggin module


## Current Response for text.txt using Async [no multiprocess]
```
cat test.txt |docker run -i -v $(pwd)/src:/usr/share/src    pyscraper python3 -u main.py
Exception  Exception Type: <class 'AssertionError'>
Exception  Exception Type: <class 'AssertionError'>
Exception  Exception Type: <class 'AssertionError'>
Exception 'src' Exception Type: <class 'KeyError'>
{'logo': 'https://www.illion.com.au/wp-content/uploads/2019/03/ION-RGB-Gradient-64.png', 'phones': ['13 23 33', '13 23 33', '24 April 2024', '24 April 2024', '22 April 2024', '22 April 2024', '2 April 2024', '2 April 2024'], 'website': 'https://www.illion.com.au'}
{'logo': 'https://www.illion.com.au/wp-content/uploads/2019/03/ION-RGB-Gradient-64.png', 'phones': ['13 23 33', '13 23 33', '13 23 33', '+61 3 9828 3200', '1800 233 533'], 'website': 'https://www.illion.com.au/contact-us'}
```