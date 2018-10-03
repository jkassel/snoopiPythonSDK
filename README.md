# Snoopi.io Python SDK

This is an SDK written in Python 3 in order to facilitate the interaction with the Snoopi.io API.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

For paid users of this service, you will need to specify an api key in order to gain higher performance and additional api features.  Please ensure you have an account and the api key ready when calling this SDK.  Otherwise you will be limited to 1 API call per second.

If loading the SDK directory manually into your project, you will need to ensure that the packages specified in the requirements.txt are installed. 

```
pip install -r requirements.txt
```

### Installing

You can install the SDK in one of two ways.  The first way (not yet operational) is by installing directly from the PyPi repository.  This will ensure all dependencies are installed and will be callable in your project like any other python package. 

You can install the package via pip as shown below:

```
pip install snoopi-python-sdk
```

The other method is to [download](https://github.com/jkassel/snoopiPythonSDK/archive/master.zip) the directory or clone the repository and move it into the root of your project.

```
git clone https://github.com/jkassel/snoopiPythonSDK.git 
```

End with an example of getting some data out of the system or using it for a little demo


## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [urllib3](https://urllib3.readthedocs.io/en/latest/) - HTTP web client
* [requests](http://docs.python-requests.org/en/master/) - HTTP Library


## Methods

### get_zip_code_radius
This will give you a list of zip codes in a specified radius of an origin zip code

**Usage**: get_zip_code_radius(origin_zip_code, [radius])

#### parameters:

| parameter | data_type | required | default |
| --------- | --------- | -------- | ------- |
| origin_zip_code | *string* | YES | None |
| radius | *string* | NO | "5" |

**Response**:
array of zip codes
[*string*, *string*,...]


## Example
```python3
# import module  
# In this example the directory SnoopiClient exists in the root of the project
from SnoopiClient import SnoopiClient

# instantiate the SDK
# optional parameter is a String containing the api key
my_api = SnoopiClient("12345abcde")

# get list of zip codes within 5 miles of origin zip code
result = my_api.get_zip_code_radius("11214", "5")
print(result)
```




## Authors

* **Jeff Kassel** - *Initial work* - [jkassel](https://github.com/jkassel)

See also the list of [contributors](https://github.com/jkassel/snoopiPythonSDK/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/jkassel/snoopiPythonSDK/LICENSE.md) file for details
