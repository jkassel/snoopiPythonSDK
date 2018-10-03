from SnoopiClient import SnoopiClient

my_api = SnoopiClient()

# get list of zip codes within 5 miles of origin zip code
result = my_api.get_zip_code_radius("11214", "5")
print(result)


# get location by ip
my_ip = "173.56.45.134"
result = my_api.get_location_by_ip(my_ip)
print(result)





# loops through results running the function recursively
# used to test api limits
# for zip_code in result:
#     sub_result = my_api.get_zip_code_radius(zip_code, "5")
#     print(sub_result)


