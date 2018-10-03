from SnoopiClient import SnoopiClient

my_api = SnoopiClient()

# get list of zip codes within 5 miles of origin zip code
result = my_api.get_zip_code_radius("11214", "5")
print(result)

# get location by ip
my_ip = "173.56.45.134"
result = my_api.get_location_by_ip(my_ip)
print(result)

# get distance between two zip codes
start_zip = "10314"
end_zip = "27513"
result = my_api.get_zip_code_distance(start_zip, end_zip)
print(result)

# get list of states
result = my_api.get_states()
print(result)

# get state abbreviation
state = "NY"
result = my_api.get_state_abbreviation(state)
print(result)

# get a list of cities
result = my_api.get_cities()
print(result)

# get a list of cities in New York
state_abbreviation = "New York"
result = my_api.get_cities(state_abbreviation)
print(result)

# loops through results running the function recursively
# used to test api limits
# for zip_code in result:
#     sub_result = my_api.get_zip_code_radius(zip_code, "5")
#     print(sub_result)


