"""
Test module for the TestList class.

This module contains tests for the 'Lists' endpoint of the "Clickup" application API
API's Doc: https://clickup.com/api/

Author: Rafael G. Alfaro Martinez
Date: 03/26/24
Version: 1.0
"""
import logging
import random
import time

import allure
import pytest

from clickup_api.conftest import read_input_data_json, create_list, create_list_in_folder, delete_list, create_task, \
    add_task_to_secondary_list
from config.config import URL_CLICKUP
from helpers.rest_client import RestClient
from helpers.validate_response import ValidateResponse
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


class TestList:
    """
    This class contains tests for the 'Lists' endpoint
    """
    space_id = None
    folder_id = None
    list_lists = []

    @classmethod
    @pytest.fixture(autouse=True)
    def setup_class(cls, create_folder_in_space_fixture):
        """
        Setup class Method
        """
        LOGGER.debug("Setup Class Method")
        cls.rest_client = RestClient()
        cls.validate = ValidateResponse()
        cls.space_id, cls.folder_id = create_folder_in_space_fixture

    @allure.feature("Lists")
    @allure.title("Test Get Lists in folder")
    @allure.description("Test that lists in a folder are obtained from a space")
    @allure.tag("acceptance", "lists")
    def test_get_lists_in_folder(self):
        """
        Get Lists in folder
        """
        list_id = create_list_in_folder(self.folder_id)
        self.list_lists.append(list_id)
        LOGGER.debug("List ID: %s", list_id)
        url_clickup = URL_CLICKUP + "folder/" + self.folder_id + "/list"
        response = self.rest_client.request("get", url_clickup)
        self.validate.validate_response(response, "get_list_in_folder")

    @allure.feature("Lists")
    @allure.title("Test Create List in Folder")
    @allure.description("Verify that a new list can be added to a folder.")
    @allure.tag("acceptance", "lists")
    def test_create_lists_in_folder(self):
        """
        Test Create List in Folder
        """
        LOGGER.debug("Create list in the folder: %s", self.folder_id)
        url_clickup = URL_CLICKUP + "folder/" + self.folder_id + "/list"
        random_number = random.randint(1, 1000)
        payload = read_input_data_json("post_list")
        payload["name"] = f"New list API {random_number}"
        payload["content"] = payload["name"]
        rest_client = RestClient()
        response = rest_client.request("post", url_clickup, body=payload)
        self.list_lists.append(response["body"]["id"])
        self.validate.validate_response(response, "post_create_lists_in_folder")

    @allure.feature("Lists")
    @allure.title("Test Get Folderless Lists")
    @allure.description("Test that the lists without folder are obtained in a space.")
    @allure.tag("acceptance", "lists")
    def test_get_folderless_lists(self):
        """
        Get Folderless Lists
        """
        list_id = create_list(self.space_id)
        self.list_lists.append(list_id)
        LOGGER.debug("List ID: %s", list_id)
        url_clickup = URL_CLICKUP + "space/" + self.space_id + "/list"
        response = self.rest_client.request("get", url_clickup)
        self.validate.validate_response(response, "post_get_folderless_list")

    @allure.feature("Lists")
    @allure.title("Test Create Folderless lists")
    @allure.description("Verify that a new list can be added to a space.")
    @allure.tag("acceptance", "lists")
    def test_create_folderless_lists(self):
        """
        Test Create Folder less lists
        """
        LOGGER.debug("Create list")
        url_clickup = URL_CLICKUP + "space/" + self.space_id + "/list"
        random_number = random.randint(1, 1000)
        payload = read_input_data_json("post_list")
        payload["name"] = f"New list API {random_number}"
        payload["content"] = payload["name"]
        rest_client = RestClient()
        response = rest_client.request("post", url_clickup, body=payload)
        id_list_created = response["body"]["id"]
        self.list_lists.append(id_list_created)
        self.validate.validate_response(response, "post_create_folderless_list")

    @allure.feature("Lists")
    @allure.title("Test Add Task To List")
    @allure.description("Verify that a task can be added to the list")
    @allure.tag("acceptance", "lists")
    def test_add_task_to_list(self):
        """
        Test Add Task To List
        """
        rest_client = RestClient()
        list_id_fist = create_list(self.space_id)
        list_id_second = create_list(self.space_id)
        task_id = create_task(list_id_fist)
        url_clickup = URL_CLICKUP + "list/" + list_id_second + "/task/" + task_id
        response = rest_client.request("post", url_clickup)
        self.validate.validate_response(response, "post_add_task_to_list")

    @allure.feature("Lists")
    @allure.title("Test Remove Task From List")
    @allure.description("Verify that a task can be deleted to the list")
    @allure.tag("acceptance", "lists")
    def test_delete_task_from_list(self):
        """
        Test Add Task To List
        """
        rest_client = RestClient()
        list_id_second, task_id = add_task_to_secondary_list(self.space_id)
        url_clickup = URL_CLICKUP + "list/" + list_id_second + "/task/" + task_id
        response = rest_client.request("delete", url_clickup)
        self.validate.validate_response(response, "delete_task_from_list")

    @allure.feature("Lists")
    @allure.title("Test get a list")
    @allure.description("Test that a list is obtained")
    @allure.tag("acceptance", "lists")
    def test_get_list(self):
        """
        Test Get list
        """
        list_id = create_list(self.space_id)
        self.list_lists.append(list_id)
        LOGGER.debug("List to get: %s", list_id)
        url_clickup = URL_CLICKUP + "list/" + list_id
        response = self.rest_client.request("get", url_clickup)
        self.validate.validate_response(response, "get_list")

    @allure.feature("Lists")
    @allure.title("Test update a list")
    @allure.description("Test that a list can be updated")
    @allure.tag("acceptance", "lists")
    def test_update_list(self):
        """
        Test Update list
        """
        list_id = create_list(self.space_id)
        self.list_lists.append(list_id)
        LOGGER.debug("List to update: %s", list_id)
        url_clickup = URL_CLICKUP + "list/" + list_id
        random_number = random.randint(1, 1000)
        payload = read_input_data_json("post_list")
        payload["name"] = f"Updated List Name {random_number}"
        payload["content"] = payload["name"]
        response = self.rest_client.request("put", url_clickup, body=payload)
        self.validate.validate_response(response, "put_update_list")

    @allure.feature("Lists")
    @allure.title("Test delete a list")
    @allure.description("Test that a list can be deleted from the workspace..")
    @allure.tag("acceptance", "Lists")
    def test_delete_list(self):
        """
        Test Delete list
        """
        list_id = create_list(self.space_id)
        LOGGER.debug("List to delete: %s", list_id)
        url_clickup = URL_CLICKUP + "list/" + list_id
        response = self.rest_client.request("delete", url_clickup)
        self.validate.validate_response(response, "delete_list")

    @allure.feature("Lists")
    @allure.title("Test empty json input returns 400 error")
    @allure.description("response : List Name Invalid with an invalid JSON input")
    @allure.tag("functional", "list")
    def test_empty_json_input_returns_400_error(self):
        """
        Test empty json input returns 400 error
        """
        rest_client = RestClient()
        LOGGER.debug("Create list")
        url_clickup = URL_CLICKUP + "space/" + self.space_id + "/list"
        payload = {}
        response = rest_client.request("post", url_clickup, body=payload)
        self.validate.validate_response(response, "error_List_name_Invalid")

    @classmethod
    def teardown_class(cls):
        """
        Delete all lists used in test
        """
        LOGGER.info('Cleanup space ...')
        for id_list in cls.list_lists:
            delete_list(id_list)
