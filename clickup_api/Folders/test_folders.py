import logging
import requests

from config.config import space_id, URL_CLICKUP
from helpers.rest_client import RestClient
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


class TestFolder:
    @classmethod
    def setup_class(cls):
        """
        Setup class Method
        """
        LOGGER.debug("Setup Class Method")
        cls.rest_client = RestClient()
        cls.list_folders = []

    def test_get_all_folders(self):
        """
        Test get all folders
        """
        url_clickup = URL_CLICKUP + "space/" + space_id + "/folder"
        response = self.rest_client.request("get", url_clickup)
        assert response.status_code == 200, "wrong status code, expected 200"

    def test_create_folder(self):
        """
        Test create folder
        """
        url_clickup = URL_CLICKUP + "space/" + space_id + "/folder"
        payload = {
            "name": "New Folder Name API"
        }
        response = self.rest_client.request("post", url_clickup, json_data=payload)
        id_folder_created = response.json()["id"]
        self.list_folders.append(id_folder_created)
        assert response.status_code == 200, "wrong status code, expected 200"

    def test_get_folder(self, create_folder):
        """
        Test Get folder
        :param create_folder: folder's ID
        """
        LOGGER.debug("Folder to get: %s", create_folder)
        url_clickup_update = URL_CLICKUP + "folder/" + create_folder
        response = self.rest_client.request("get", url_clickup_update)
        self.list_folders.append(create_folder)
        assert response.status_code == 200, "wrong status code, expected 200"

    def test_update_folder(self, create_folder):
        """
        Test Update folder
        :param create_folder: folder's ID
        """
        LOGGER.debug("Folder to update: %s", create_folder)
        url_clickup_update = URL_CLICKUP + "folder/" + create_folder
        payload = {
            "name": "Updated Folder Name"
        }
        response = self.rest_client.request("put", url_clickup_update, json_data=payload)
        self.list_folders.append(create_folder)
        assert response.status_code == 200, "wrong status code, expected 200"

    def test_delete_folder(self, create_folder):
        """
        Test Delete folder
        :param create_folder: folder's ID
        """
        LOGGER.debug("Folder to delete: %s", create_folder)
        url_clickup = URL_CLICKUP + "folder/" + create_folder
        response = self.rest_client.request("delete", url_clickup)
        assert response.status_code == 200, "wrong status code, expected 200"

    @classmethod
    def teardown_class(cls):
        """
        Delete all folders used iin test
        """
        LOGGER.info('Cleanup space ...')
        for id_folder in cls.list_folders:
            url_clickup = URL_CLICKUP + "folder/" + id_folder
            response = cls.rest_client.request("delete", url_clickup)
            if response.status_code == 200:
                LOGGER.info("Folder Id: %s deleted", id_folder)
