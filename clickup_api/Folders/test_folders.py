import logging
import requests

from config.config import space_id, token_clickup, URL_CLICKUP, \
    HEADERS_CLICKUP_DATA, HEADERS_CLICKUP
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


class TestFolder:
    @classmethod
    def setup_class(cls):
        """
        Setup class Method
        """
        LOGGER.debug("Setup Class Method")
        cls.list_folders = []

    def test_get_all_folders(self):
        """
        Test get all folders
        """
        url_clickup = URL_CLICKUP + "space/" + space_id + "/folder"
        query = {"archived": "false"}

        headers_clickup = {"Authorization": f"{token_clickup}"}
        response = requests.get(url=url_clickup, headers=headers_clickup, params=query, timeout=10)
        LOGGER.info("Response from get all folders %s", response.json())
        LOGGER.info("Status Code %s", response.status_code)
        assert response.status_code == 200, "wrong status code, expected 200"

    def test_create_folder(self):
        """
        Test create folder
        """
        url_clickup = URL_CLICKUP + "space/" + space_id + "/folder"
        payload = {
            "name": "New Folder Name API"
        }
        response = requests.post(url_clickup, json=payload, headers=HEADERS_CLICKUP_DATA, \
                                 timeout=10)
        LOGGER.info("Response from create folder %s", response.json())
        LOGGER.info("Status Code %s", response.status_code)
        id_folder_created = response.json()["id"]
        self.list_folders.append(id_folder_created)
        assert response.status_code == 200, "wrong status code, expected 200"

    def test_get_folder(self, create_folder):
        """
        Test Get folder
        :param create_folder:
        """
        id_folder_create = create_folder["id"]
        LOGGER.debug("Folder to get: %s", id_folder_create)
        url_clickup_update = URL_CLICKUP + "folder/" + id_folder_create
        response = requests.put(url_clickup_update, headers=HEADERS_CLICKUP, timeout=10)
        LOGGER.info("Status Code %s", response.status_code)
        self.list_folders.append(id_folder_create)
        assert response.status_code == 200, "wrong status code, expected 200"

    def test_update_folder(self, create_folder):
        """
        Test Update folder
        :param create_folder:
        """
        id_folder_update = create_folder["id"]
        LOGGER.debug("Folder to update: %s", id_folder_update)
        url_clickup_update = URL_CLICKUP + "folder/" + id_folder_update
        payload = {
            "name": "Updated Folder Name"
        }
        response = requests.put(url_clickup_update, json=payload, headers=HEADERS_CLICKUP_DATA, \
                                timeout=10)
        LOGGER.info("Status Code %s", response.status_code)
        self.list_folders.append(id_folder_update)
        assert response.status_code == 200, "wrong status code, expected 200"

    def test_delete_folder(self, create_folder):
        """
        Test Delete folder
        :param create_folder:
        """
        id_folder_delete = create_folder["id"]
        LOGGER.debug("Folder to delete: %s", id_folder_delete)
        url_clickup = URL_CLICKUP + "folder/" + id_folder_delete
        response = requests.delete(url_clickup, headers=HEADERS_CLICKUP, timeout=10)
        LOGGER.info("Status Code %s", response.status_code)
        assert response.status_code == 200, "wrong status code, expected 200"

    @classmethod
    def teardown_class(cls):
        """
        Delete all folders used iin test
        """
        for id_folder in cls.list_folders:
            url_clickup = URL_CLICKUP + "folder/" + id_folder
            response = requests.delete(url_clickup, headers=HEADERS_CLICKUP, timeout=10)
            if response.status_code == 200:
                LOGGER.info("Folder Id: %s deleted", id_folder)
