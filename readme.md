# A Simple python BMI Calculator
## To calculate the BMI from the data in a very large JSON file using ijson

### Source Code : https://github.com/AnkDos/code-20201010-ankurpandey/blob/master/bmiankdos/module.py 

## Setup and install package

```
# Go to the root directoy of the project and install the build by typing :
sudo python3 setup.py install

# Using the package :
  ## import by typing : 
     from bmiankdos import BMICalc

  ## Create instance and pass the json file :
     obj = BMICalc('<your_path_to_json_file>')

  ## Call the driver method :
     obj.driver_method()

  ## Print table :
     print(obj._out[0])

  ## Print Conclusions:
     print(obj.__out[1]) 
```

## Using it from console :
## If you want to directly run it from your console without installing build package :

```
# Go to the root directoy of the project and install the requirements :
  sudo pip3 install -r requirements.txt

# For testing the file, go to root directory and type :
    python3 -m pytest bmiankdos/tests

# For running the file, go to root directory and type :
    python3 -m bmiankdos.module
```

## Screenshot taken from running it from console :

   ![output](https://raw.githubusercontent.com/AnkDos/code-20201010-ankurpandey/master/screenshots/vst_ss.png)

## Screenshot taken by using it as package :

   ![output](https://raw.githubusercontent.com/AnkDos/code-20201010-ankurpandey/master/screenshots/using_from_package.png)

## Idea and Implementation

The idea was to parse a very large JSON file . I was looking for some library that could stream the json file something like StreamingHttpResponse in Django for streaming large files . I came across this package called ijson which works efficiently with large JSON files by leveraging generator iterators and yield expressions to avoid loading the entire structure in memory at once.

Using ijson library we can process very large JSON files .
