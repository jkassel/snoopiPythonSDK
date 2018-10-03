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
["string", "string",...]


### get_location_by_ip
This will give you location information based on a supplied IP address

**Usage**: get_location_by_ip(ip_address)

#### parameters:

| parameter | data_type | required | default |
| --------- | --------- | -------- | ------- |
| ip_address | *string* | YES | None |


**Response**:
```json
{
    CountryCode: "string",
    CountryName: "string",
    GeoID: number,
    State: "string",
    StateCode: "string",
    City: "string",
    Postal: "string",
    Latitude: float,
    Longitude: float,
    RequestTime: int,
    RequestedIP: "string"
}
```

### get_zip_code_distance
Gives you the distance between two zip codes

**Usage**: get_zip_code_distance(start_zip_code, end_zip_code):

#### parameters:

| parameter | data_type | required | default |
| --------- | --------- | -------- | ------- |
| start_zip_code | *string* | YES | None |
| end_zip_code | *string* | YES | None |


**Response**:
```json
{
    miles: float
    kilometers: float
}
```

### get_states
Displays a list of US states

**Usage**: get_states():

#### parameters:
None

**Response**: an array of dictionaries
```json
[
    {
        id: int,
        code: "string",
        name: "string"
    },
    {...}
]
```

### get_state_abbreviation
Gives you the distance between two zip codes

**Usage**: get_state_abbreviation(state):

#### parameters:

| parameter | data_type | required | default |
| --------- | --------- | -------- | ------- |
| state| *string* | YES | None |


**Response**:
```json
{
  code: "string",
  name: "string"
}
```

### get_cities
Gives you the distance between two zip codes

**Usage**: get_cities([state_abbreviation]):

#### parameters:

| parameter | data_type | required | default |
| --------- | --------- | -------- | ------- |
| state_abbreviation | *string* | NO | None |


**Response**:
```json
[
  {
    id: int,
    zip_code: "string",
    state_prefix: "string",
    city: "string",
    county: "string",
    lon: "string",
    lat: "string"
  },
  {...}
]
```

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
