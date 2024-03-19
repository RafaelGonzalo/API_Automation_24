import random
import logging
from logging import Logger

import pytest

import requests

from config.config import URL_CLICKUP, space_id
from utils.logger import get_logger
from helpers.rest_client import RestClient

LOGGER: Logger = get_logger(__name__, logging.DEBUG)


@pytest.fixture()
def create_folder(request):
    """
    Create a new folder fixture
    :param request:
    """
    LOGGER.debug("Create folder fixture")
    url_clickup = URL_CLICKUP + "space/" + space_id + "/folder"
    random_number = random.randint(1, 1000)
    folder_name = f"New Folder API {random_number}"
    payload = {
        "name": folder_name
    }
    rest_client = RestClient()
    response = rest_client.request("post", url_clickup, json_data=payload)
    assert response.status_code == 200, "wrong status code, expected 200"
    LOGGER.info("Response from create folder fixture %s", response.json())
    folder_id = response.json()["id"]
    yield folder_id
    delete_folder(folder_id)


def delete_folder(folder_id):
    """
    Delete a folder
    :param folder_id: folder's ID
    """
    LOGGER.info('Cleanup folder...')
    url_clickup = URL_CLICKUP + "folder/" + folder_id
    LOGGER.info('url: %s', url_clickup)
    rest_client = RestClient()
    response = rest_client.request("delete", url_clickup)
    if response.status_code == 200:
        LOGGER.info("Folder Id: %s deleted", folder_id)
