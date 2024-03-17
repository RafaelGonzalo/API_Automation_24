import random
import logging
import pytest

import requests

from config.config import URL_CLICKUP, space_id, HEADERS_CLICKUP_DATA
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


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
    response = requests.post(url_clickup, json=payload, headers=HEADERS_CLICKUP_DATA, \
                             timeout=10)
    assert response.status_code == 200, "wrong status code, expected 200"
    LOGGER.info("Response from create folder fixture %s", response.json())
    return response.json()
