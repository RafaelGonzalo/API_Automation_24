"""
Test module for the TestFolder class.

This module contains tests for the 'Folders' point of the "Clickup" application API
API's Doc: https://clickup.com/api/

Author: Rafael G. Alfaro Martinez
Date: 03/26/24
Version: 1.0
"""
import logging
import random
import allure
import pytest

from clickup_api.conftest import get_authorized_teams, create_space, read_input_data_json
from config.config import URL_CLICKUP
from helpers.rest_client import RestClient
from helpers.validate_response import ValidateResponse
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


class TestFolder:
    """
    This class contains tests for the 'Folders' endpoint
    """

    @classmethod
    @pytest.fixture(autouse=True)
    def setup_class(cls, create_space):
        """
        Setup class Method
        """
        cls.list_folders = []
        LOGGER.debug("Setup Class Method")
        authorized_teams = get_authorized_teams()
        LOGGER.info("Authorized Teams: %s", authorized_teams)
        cls.space_id = create_space
        LOGGER.info("Space ID: %s", cls.space_id)
        cls.rest_client = RestClient()
        cls.validate = ValidateResponse()

    @allure.feature("Folders")
    @allure.title("Test get all folders")
    @allure.description("Test that the folders are obtained in a space.")
    @allure.tag("acceptance", "folder")
    def test_get_all_folders(self, create_folder):
        """
        Test get all folders
        """
        LOGGER.debug("Folder: %s", create_folder)
        url_clickup = URL_CLICKUP + "space/" + self.space_id + "/folder"
        response = self.rest_client.request("get", url_clickup)
        self.validate.validate_response(response, "get_all_folders")

    @allure.feature("Folders")
    @allure.title("Test create folder")
    @allure.description("Verify that a new folder can be added to a space.")
    @allure.tag("acceptance", "folder")
    def test_create_folder(self):
        """
        Test create folder
        """
        url_clickup = URL_CLICKUP + "space/" + self.space_id + "/folder"
        payload = read_input_data_json("post_folder")
        payload["name"] = "New Folder Name API"
        response = self.rest_client.request("post", url_clickup, body=payload)
        id_folder_created = response["body"]["id"]
        self.list_folders.append(id_folder_created)
        self.validate.validate_response(response, "post_create_folder")

    @allure.feature("Folders")
    @allure.title("Test get a folder")
    @allure.description("Test that a folder is obtained")
    @allure.tag("acceptance", "folder")
    def test_get_folder(self, create_folder):
        """
        Test Get folder
        :param create_folder: folder's ID
        """
        LOGGER.debug("Folder to get: %s", create_folder)
        url_clickup_update = URL_CLICKUP + "folder/" + create_folder
        response = self.rest_client.request("get", url_clickup_update)
        self.list_folders.append(create_folder)
        self.validate.validate_response(response, "get_folder")

    @allure.feature("Folders")
    @allure.title("Test update a folder")
    @allure.description("Test that a folder can be updated")
    @allure.tag("acceptance", "folder")
    def test_update_folder(self, create_folder):
        """
        Test Update folder
        :param create_folder: folder's ID
        """
        LOGGER.debug("Folder to update: %s", create_folder)
        url_clickup_update = URL_CLICKUP + "folder/" + create_folder
        payload = read_input_data_json("post_folder")
        payload["name"] = "Updated Folder Name"
        response = self.rest_client.request("put", url_clickup_update, payload)
        self.list_folders.append(create_folder)
        self.validate.validate_response(response, "put_update_folder")

    @allure.feature("Folders")
    @allure.title("Test delete a folder")
    @allure.description("Test that a folder can be deleted from the workspace..")
    @allure.tag("acceptance", "folder")
    def test_delete_folder(self, create_folder):
        """
        Test Delete folder
        :param create_folder: folder's ID
        """
        LOGGER.debug("Folder to delete: %s", create_folder)
        url_clickup = URL_CLICKUP + "folder/" + create_folder
        response = self.rest_client.request("delete", url_clickup)
        self.validate.validate_response(response, "delete_folder")

    @allure.feature("Folders")
    @allure.title("Test that a folder with the same name cannot create")
    @allure.description("Test that a folder with the same name cannot created")
    @allure.tag("functional", "folder")
    def test_that_creates_a_folder_with_the_same_name_cannot_create(self):
        """
        Test that a folder with the same name cannot create
        """
        response = None
        url_clickup = URL_CLICKUP + "space/" + self.space_id + "/folder"
        random_number = random.randint(1, 1000)
        payload = read_input_data_json("post_folder")
        payload["name"] = f"New Folder Name API {random_number}"
        for i in range(2):
            response = self.rest_client.request("post", url_clickup, body=payload)
            if i == 0:
                id_folder_created = response["body"]["id"]
                self.list_folders.append(id_folder_created)
        self.validate.validate_response(response, "error_existing_folder")

    @allure.feature("Folders")
    @allure.title("Test empty json input returns 400 error")
    @allure.description("response : folder Name Invalid with an invalid JSON input")
    @allure.tag("functional", "folder")
    def test_empty_json_input_returns_400_error(self):
        """
        Test create folder
        """
        url_clickup = URL_CLICKUP + "space/" + self.space_id + "/folder"
        payload = {}
        response = self.rest_client.request("post", url_clickup, body=payload)
        self.validate.validate_response(response, "error_folder_name_Invalid")

    @classmethod
    def teardown_class(cls):
        """
        Delete all folders used iin test
        """
        LOGGER.info('Cleanup space ...')
