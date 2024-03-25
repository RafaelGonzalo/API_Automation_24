import logging

from clickup_api.conftest import get_authorized_teams
from config.config import URL_CLICKUP
from helpers.rest_client import RestClient
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
        cls.list_spaces = []

    def test_get_all_spaces(self):
        """
        Test get all spaces
        """
        url_clickup = URL_CLICKUP + "team/" + self.team_id + "/space"
        response = self.rest_client.request("get", url_clickup)
        assert response.status_code == 200, "wrong status code, expected 200"

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

        response = self.rest_client.request("post", url_clickup, body=payload)
        id_space_created = response.json()["id"]
        self.list_spaces.append(id_space_created)
        assert response.status_code == 200, "wrong status code, expected 200"

    def test_get_space(self, create_space):
        """
        Test Get folder
        :param create_space: space's ID
        """
        LOGGER.debug("Folder to get: %s", create_space)
        url_clickup_update = URL_CLICKUP + "space/" + create_space
        response = self.rest_client.request("get", url_clickup_update)
        self.list_spaces.append(create_space)
        assert response.status_code == 200, "wrong status code, expected 200"

    def test_update_space(self, create_space):
        """
        Test Update space
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
        response = self.rest_client.request("put", url_clickup_update, body=payload)
        self.list_spaces.append(create_space)
        assert response.status_code == 200, "wrong status code, expected 200"

    def test_delete_space(self, create_space):
        """
        Test Delete space
        :param create_space: space's ID
        """
        LOGGER.debug("Space to delete: %s", create_space)
        url_clickup = URL_CLICKUP + "space/" + create_space
        response = self.rest_client.request("delete", url_clickup)
        assert response.status_code == 200, "wrong status code, expected 200"

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
            if response.status_code == 200:
                LOGGER.info("Folder Id: %s deleted", id_space)
