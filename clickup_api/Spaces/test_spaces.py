"""
Test module for the TestSpace class.

This module contains tests for the 'Spaces' endpoint of the "Clickup" application API
API's Doc: https://clickup.com/api/

Author: Rafael G. Alfaro Martinez
Date: 03/26/24
Version: 1.0
"""
import logging
import random

import allure

from clickup_api.conftest import get_authorized_teams, read_input_data_json
from config.config import URL_CLICKUP
from helpers.rest_client import RestClient
from helpers.validate_response import ValidateResponse
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


class TestSpace:
    """
    This class contains tests for the 'Spaces' endpoint
    """

    @classmethod
    def setup_class(cls):
        """
        Setup class Method
        """
        LOGGER.debug("Setup Class Method")
        cls.team_id = get_authorized_teams()
        LOGGER.info("Authorized Teams: %s", cls.team_id)
        cls.rest_client = RestClient()
        cls.validate = ValidateResponse()
        cls.list_spaces = []

    @allure.feature("Spaces")
    @allure.title("Test Get All Spaces")
    @allure.description("Test that all spaces are obtained")
    @allure.tag("acceptance", "Spaces")
    def test_get_all_spaces(self, create_space_fixture):
        """
        Test get all spaces
        """
        self.list_spaces.append(create_space_fixture)
        url_clickup = URL_CLICKUP + "team/" + self.team_id + "/space"
        response = self.rest_client.request("get", url_clickup)
        self.validate.validate_response(response, "get_all_spaces")

    @allure.feature("Spaces")
    @allure.title("Test Create Space")
    @allure.description("Test that a space can be created")
    @allure.tag("acceptance", "Spaces")
    def test_create_space(self):
        """
        Test create space
        """
        url_clickup = URL_CLICKUP + "team/" + self.team_id + "/space"
        payload = read_input_data_json("put_space")
        payload["name"] = "Space_Name"
        response = self.rest_client.request("post", url_clickup, body=payload)
        id_space_created = response["body"]["id"]
        self.list_spaces.append(id_space_created)
        self.validate.validate_response(response, "post_create_space")

    @allure.feature("Spaces")
    @allure.title("Test Get Space")
    @allure.description("Test that space is obtained")
    @allure.tag("acceptance", "Spaces")
    def test_get_space(self, create_space_fixture):
        """
        Test to Get space
        :param create_space: space's ID
        """
        LOGGER.debug("space to get: %s", create_space_fixture)
        url_clickup_update = URL_CLICKUP + "space/" + create_space_fixture
        response = self.rest_client.request("get", url_clickup_update)
        self.list_spaces.append(create_space_fixture)
        self.validate.validate_response(response, "get_space")

    @allure.feature("Spaces")
    @allure.title("Test Update space")
    @allure.description("Test that Update the space")
    @allure.tag("functional", "Spaces")
    def test_update_space(self, create_space_fixture):
        """
        Test Update space information
        :param create_space: space's ID
        """
        LOGGER.debug("Space to update: %s", create_space_fixture)
        url_clickup_update = URL_CLICKUP + "space/" + create_space_fixture
        payload = read_input_data_json("put_space")
        payload["name"] = "Updated Space Name"
        response = self.rest_client.request("put", url_clickup_update, body=payload)
        self.validate.validate_response(response, "update_space")

    @allure.feature("Spaces")
    @allure.title("Test Delete Space")
    @allure.description("Test that space is deleted")
    @allure.tag("acceptance", "Spaces")
    def test_delete_space(self, create_space_fixture):
        """
        Test Delete space
        :param create_space: space's ID
        """
        LOGGER.debug("Space to delete: %s", create_space_fixture)
        url_clickup = URL_CLICKUP + "space/" + create_space_fixture
        response = self.rest_client.request("delete", url_clickup)
        self.validate.validate_response(response, "delete_space")

    @allure.feature("Spaces")
    @allure.title("Test Space with this name already exists")
    @allure.description("Test that a space with the same name cannot be created")
    @allure.tag("functional", "Spaces")
    def test_cannot_create_space_with_existing_name(self):
        """
        Test create space
        """
        response = None
        url_clickup = URL_CLICKUP + "team/" + self.team_id + "/space"
        random_number = random.randint(1, 1000)
        payload = read_input_data_json("put_space")
        payload["name"] = f"Space_Name {random_number}"
        for i in range(2):
            response = self.rest_client.request("post", url_clickup, body=payload)
            if i == 0:
                id_space_created = response["body"]["id"]
                self.list_spaces.append(id_space_created)
        self.validate.validate_response(response, "error_existing_space")

    @allure.feature("Spaces")
    @allure.title("Test Space not found")
    @allure.description("Test for the inability to retrieve information from an invalid space ID.")
    @allure.tag("functional", "Spaces")
    def test_space_not_found(self):
        """
        Test for space: Verify API message for incorrect space ID
        """
        create_space = str(90130733342)
        url_clickup_update = URL_CLICKUP + "space/" + create_space
        response = self.rest_client.request("get", url_clickup_update)
        self.validate.validate_response(response, "error_space_not_found")

    @allure.feature("Spaces")
    @allure.title("Test empty json input returns 400 error")
    @allure.description("response : space  Name Invalid with an invalid JSON input")
    @allure.tag("functional", "Spaces")
    def test_create_space(self):
        """
        Test create space
        """
        url_clickup = URL_CLICKUP + "team/" + self.team_id + "/space"
        payload = {}
        response = self.rest_client.request("post", url_clickup, body=payload)
        self.validate.validate_response(response, "error_space_name_Invalid")

    @classmethod
    def teardown_class(cls):
        """
         Delete all spaces used in test
        """
        LOGGER.info('Cleanup space ...')
        for id_space in cls.list_spaces:
            url_clickup = URL_CLICKUP + "space/" + id_space
            LOGGER.info("URL: %s", url_clickup)
            response = cls.rest_client.request("delete", url_clickup)
            if response["status_code"] == 200:
                LOGGER.info("space Id: %s deleted", id_space)
