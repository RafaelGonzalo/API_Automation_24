import json
import logging
import random

import allure

from clickup_api.conftest import get_authorized_teams
from config.config import space_id, URL_CLICKUP
from helpers.rest_client import RestClient
from helpers.validate_response import ValidateResponse
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


class TestList:
    @classmethod
    def setup_class(cls):
        """
        Setup class Method
        """
        LOGGER.debug("Setup Class Method")
        authorized_teams = get_authorized_teams()
        LOGGER.info("Authorized Teams: %s", authorized_teams)
        cls.rest_client = RestClient()
        cls.validate = ValidateResponse()
        cls.list_lists = []

    @allure.feature("Lists")
    @allure.title("Test Get Folderless Lists")
    @allure.description("Test that the lists without folder are obtained in a space.")
    @allure.tag("acceptance", "lists")
    def test_get_folderless_lists(self, create_list):
        """
        Get Folderless Lists
        """
        url_clickup = URL_CLICKUP + "space/" + space_id + "/list"
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
        url_clickup = URL_CLICKUP + "space/" + space_id + "/list"
        payload = {
            "name": "New list API",
            "content": f"New list API",
            "due_date_time": False,
            "priority": 1,
            "status": "red"
        }
        rest_client = RestClient()
        response = rest_client.request("post", url_clickup, body=json.dumps(payload))
        id_list_created = response["body"]["id"]
        self.list_lists.append(id_list_created)
        self.validate.validate_response(response, "post_create_folderless_list")

    @allure.feature("Lists")
    @allure.title("Test get a list")
    @allure.description("Test that a list is obtained")
    @allure.tag("acceptance", "lists")
    def test_get_list(self, create_list):
        """
        Test Get list
        :param create_list: folder's ID
        """
        LOGGER.debug("List to get: %s", create_list)
        url_clickup = URL_CLICKUP + "list/" + create_list
        response = self.rest_client.request("get", url_clickup)
        self.list_lists.append(create_list)
        self.validate.validate_response(response, "get_list")

    @allure.feature("Lists")
    @allure.title("Test update a list")
    @allure.description("Test that a list can be updated")
    @allure.tag("acceptance", "lists")
    def test_update_list(self, create_list):
        """
        Test Update list
        :param create_list: folder's ID
        """
        LOGGER.debug("Folder to update: %s", create_list)
        url_clickup = URL_CLICKUP + "list/" + create_list
        payload = {
            "name": "Updated List Name",
            "content": "Updated List Content",
            "due_date": 1567780450202,
            "due_date_time": True,
            "priority": 2,
            "assignee": "none",
            "status": "red",
            "unset_status": True
        }
        response = self.rest_client.request("put", url_clickup, body=json.dumps(payload))
        self.list_lists.append(create_list)
        self.validate.validate_response(response, "put_update_list")

    @allure.feature("Lists")
    @allure.title("Test delete a list")
    @allure.description("Test that a list can be deleted from the workspace..")
    @allure.tag("acceptance", "Lists")
    def test_delete_list(self, create_list):
        """
        Test Delete list
        :param create_list: list's ID
        """
        LOGGER.debug("List to delete: %s", create_list)
        url_clickup = URL_CLICKUP + "list/" + create_list
        response = self.rest_client.request("delete", url_clickup)
        self.validate.validate_response(response, "delete_list")

    @classmethod
    def teardown_class(cls):
        """
        Delete all lists used in test
        """
        LOGGER.info('Cleanup space ...')
        for id_list in cls.list_lists:
            url_clickup = URL_CLICKUP + "list/" + id_list
            response = cls.rest_client.request("delete", url_clickup)
            if response["status_code"] == 200:
                LOGGER.info("List Id: %s deleted", id_list)
