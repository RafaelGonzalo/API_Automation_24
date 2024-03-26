import json
import logging

import allure

from clickup_api.conftest import get_authorized_teams
from config.config import URL_CLICKUP
from helpers.rest_client import RestClient
from helpers.validate_response import ValidateResponse
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


class TestSpace:
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
    def test_get_all_spaces(self, create_space):
        """
        Test get all spaces
        """
        self.list_spaces.append(create_space)
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
        payload = {
            "name": "New Space Name API",
            "multiple_assignees": True,
            "features": {
                "due_dates": {
                    "enabled": True,
                    "start_date": False,
                    "remap_due_dates": True,
                    "remap_closed_due_date": False
                },
                "time_tracking": {
                    "enabled": False
                },
                "tags": {
                    "enabled": True
                },
                "time_estimates": {
                    "enabled": True
                },
                "checklists": {
                    "enabled": True
                },
                "custom_fields": {
                    "enabled": True
                },
                "remap_dependencies": {
                    "enabled": True
                },
                "dependency_warning": {
                    "enabled": True
                },
                "portfolios": {
                    "enabled": True
                }
            }
        }

        response = self.rest_client.request("post", url_clickup, body=json.dumps(payload))
        id_space_created = response["body"]["id"]
        self.list_spaces.append(id_space_created)
        self.validate.validate_response(response, "post_create_space")

    @allure.feature("Spaces")
    @allure.title("Test Get Space")
    @allure.description("Test that space is obtained")
    @allure.tag("acceptance", "Spaces")
    def test_get_space(self, create_space):
        """
        Test Get folder
        :param create_space: space's ID
        """
        LOGGER.debug("Folder to get: %s", create_space)
        url_clickup_update = URL_CLICKUP + "space/" + create_space
        response = self.rest_client.request("get", url_clickup_update)
        self.list_spaces.append(create_space)
        self.validate.validate_response(response, "get_space")

    @allure.feature("Spaces")
    @allure.title("Test Update space")
    @allure.description("Test that Update the space")
    @allure.tag("functional", "Spaces")
    def test_update_space_admin_can_manage(self, create_space):
        """
        admin_can_manage: boolean
        Note: Allowing or restricting admins from managing private Spaces using "admin_can_manage" is an Enterprise Plan feature.
        :param create_space: space's ID
        """
        LOGGER.debug("Space to update: %s", create_space)
        url_clickup_update = URL_CLICKUP + "space/" + create_space
        LOGGER.debug("URL: %s", url_clickup_update)
        payload = {
            "name": "Updated Space Name",
            "color": "#7B68EE",
            "private": False,
            "admin_can_manage": False,
            "multiple_assignees": False,
            "features": {
                "due_dates": {
                    "enabled": False,
                    "start_date": False,
                    "remap_due_dates": False,
                    "remap_closed_due_date": False
                },
                "time_tracking": {
                    "enabled": False
                },
                "tags": {
                    "enabled": False
                },
                "time_estimates": {
                    "enabled": False
                },
                "checklists": {
                    "enabled": False
                },
                "custom_fields": {
                    "enabled": False
                },
                "remap_dependencies": {
                    "enabled": False
                },
                "dependency_warning": {
                    "enabled": False
                },
                "portfolios": {
                    "enabled": False
                }
            }
        }
        response = self.rest_client.request("put", url_clickup_update, body=json.dumps(payload))
        self.validate.validate_response(response, "update_space")

    @allure.feature("Spaces")
    @allure.title("Test Delete Space")
    @allure.description("Test that space is deleted")
    @allure.tag("acceptance", "Spaces")
    def test_delete_space(self, create_space):
        """
        Test Delete space
        :param create_space: space's ID
        """
        LOGGER.debug("Space to delete: %s", create_space)
        url_clickup = URL_CLICKUP + "space/" + create_space
        response = self.rest_client.request("delete", url_clickup)
        self.validate.validate_response(response, "delete_space")

    @classmethod
    def teardown_class(cls):
        """
         Delete all spaces used iin test
        """
        LOGGER.info('Cleanup space ...')
        for id_space in cls.list_spaces:
            url_clickup = URL_CLICKUP + "space/" + id_space
            LOGGER.info("URL: %s", url_clickup)
            response = cls.rest_client.request("delete", url_clickup)
            if response["status_code"] == 200:
                LOGGER.info("Folder Id: %s deleted", id_space)
