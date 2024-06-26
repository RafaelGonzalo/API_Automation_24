import json
import logging

from config.config import abs_path
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


class ValidateResponse:

    def validate_response(self, actual_response=None, endpoint=None):
        """
        Validate responses
        :param actual_response
        :param endpoint
        """
        expected_response = self.read_input_data_json(f"{abs_path}/clickup_api/input_data/{endpoint}.json")

        if "body" in actual_response:
            self.validate_value(expected_response["status_code"], actual_response["status_code"], "status_code")
            self.validate_value(expected_response["response"]["body"], actual_response["body"], "body")
            if "headers" in actual_response:
                self.validate_value(expected_response["headers"],  actual_response["headers"], "headers")

    def validate_value(self, expected_value, actual_value, key_compare):
        """
        Validate the values
        :param expected_value:
        :param actual_value:
        :param key_compare:
        """
        LOGGER.info("Validating %s", key_compare)
        error_message = f"Expecting '{expected_value}' but received '{actual_value}'"
        if key_compare == "body":
            if isinstance(actual_value, list):
                assert self.compare_json(expected_value[0], actual_value[0]), error_message
            else:
                assert self.compare_json(expected_value, actual_value), error_message
        elif key_compare == "headers":
            LOGGER.debug("Expected Headers: %s", expected_value.items())
            LOGGER.debug("Actual Headers: %s", actual_value.items())
            assert expected_value.items() <= actual_value.items(), error_message
        else:
            LOGGER.debug("Expected Status Code: %s", expected_value)
            LOGGER.debug("Actual Status Code: %s", actual_value)
            assert expected_value == actual_value, error_message

    @staticmethod
    def read_input_data_json(file_name):
        """
        Read json
        :param file_name: filer's name
        :return: json
        """
        LOGGER.debug("Reading file %s", file_name)
        with open(file_name, encoding="utf8") as json_file:
            data = json.load(json_file)
        LOGGER.debug("Content of '%s' : %s", file_name, data)
        json_file.close()
        return data

    @staticmethod
    def compare_json(expected_json, response_json):
        """
        Compare two jsons
        :param expected_json: expected json
        :param response_json: response json
        :return: boolean
        """
        for key in expected_json.keys():
            if key in response_json.keys():
                LOGGER.info("Key '%s' found in response json", key)
            else:
                LOGGER.info("Key '%s' not found in response json", key)
                return False
        return True


if __name__ == '__main__':
    v = ValidateResponse()
    v.validate_response()
