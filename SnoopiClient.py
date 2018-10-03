import requests
import sys
import urllib3
import logging
from time import sleep

# Disables SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class SnoopiClient:

    def __init__(self, api_key=None, logging_level=logging.ERROR):
        self.api_key = api_key
        self.logger = logging.getLogger("SnoopiClient")
        self.logger.setLevel(logging_level)
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def call_api(self, api_url, api_params=None, retry_count=1, max_retries=3, sleep_time=2, req_type='get', headers={}, data={}):
        base_url = "http://api.snoopi.io/v1/"
        api_key_suffix = "?api_key={}".format(self.api_key)

        if api_params is not None:
            url = base_url + api_url + api_params + api_key_suffix
        else:
            url = base_url + api_url + api_key_suffix

        response = ''

        self.logger.info("calling api url: ", url)

        if req_type == 'get':
            response = requests.get(url, headers=headers, verify=False)
        if req_type == 'put':
            response = requests.put(url, headers=headers, data=data)
        if req_type == 'post':
            response = requests.post(url, headers=headers, data=data)
        if req_type == 'head':
            response = requests.head(url, headers=headers)
        if req_type == 'delete':
            response = requests.delete(url, headers=headers)
        self.logger.info("early_response: {}".format(response.json()))
        if response.ok:
            self.logger.info("response is ok")
            return response.json()
        elif response.json()['Code'] == "429":
            if retry_count == max_retries:
                self.logger.error("tried too many times. exiting...")
                sys.exit(0)

            self.logger.warning("getting rate limited.  sleeping for {}s then retrying...[Retry_Count={}]".format(sleep_time, retry_count))
            sleep(sleep_time)
            result = self.call_api(api_url, api_params, retry_count=retry_count+1)
            return result
        else:
            response_data = response.json()
            self.logger.error(response_data)
            response.raise_for_status()

    def get_zip_code_radius(self, origin_zip_code, radius="5"):
        api_url = "zipcoderange/"
        params = origin_zip_code + "-" + radius
        result = self.call_api(api_url, params)
        return result

    def get_location_by_ip(self, ip_address):
        api_url = "ip/"
        params = ip_address
        result = self.call_api(api_url, params)
        return result

    def get_zip_code_distance(self, start_zip_code, end_zip_code):
        api_url = "zipcodedistance/"
        params = start_zip_code + "-" + end_zip_code
        result = self.call_api(api_url, params)
        return result

    def get_states(self):
        api_url = "getstates/"
        result = self.call_api(api_url)
        return result

    def get_state_abbreviation(self, state):
        api_url = "getstates/"
        params = state
        result = self.call_api(api_url, params)
        return result

    def get_cities(self, state_abbreviation=None):
        api_url = "getcities/"
        params = state_abbreviation
        result = self.call_api(api_url, params)
        return result
