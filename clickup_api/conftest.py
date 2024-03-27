import json
import random
import logging
from logging import Logger

import pytest

from config.config import URL_CLICKUP, space_id, abs_path
from helpers.validate_response import ValidateResponse
from utils.logger import get_logger
from helpers.rest_client import RestClient

LOGGER: Logger = get_logger(__name__, logging.DEBUG)


def get_authorized_teams():
    """
    View the Workspaces available to the authenticated user.
    :return:
    """
    validate = ValidateResponse()
    LOGGER.debug("Get Authorized Teams (Workspaces)")
    url_clickup = URL_CLICKUP + "team"
    rest_client = RestClient()
    response = rest_client.request("get", url_clickup)
    validate.validate_response(response, "get_authorized_teams")
    authorized_teams = response["body"]["teams"][0]["id"]
    return authorized_teams


@pytest.fixture()
def create_list(request):
    """
    Create a new list
    :param request:
    :return:
    """
    validate = ValidateResponse()
    LOGGER.debug("Create list fixture")
    url_clickup = URL_CLICKUP + "space/" + space_id + "/list"
    random_number = random.randint(1, 1000)
    payload = read_input_data_json("post_list")
    payload["name"] = f"New list API {random_number}"
    payload["content"] = payload["name"]
    rest_client = RestClient()
    response = rest_client.request("post", url_clickup, body=payload)
    validate.validate_response(response, "post_create_folderless_list")
    list_id = response["body"]["id"]
    yield list_id
    delete_list(list_id)


def delete_list(list_id):
    """
    Delete a list
    :param list_id: list's ID
    """
    LOGGER.info('Cleanup list...')
    url_clickup = URL_CLICKUP + "list/" + list_id
    rest_client = RestClient()
    response = rest_client.request("delete", url_clickup)
    if response["status_code"] == 200:
        LOGGER.info("List Id: %s deleted", list_id)


@pytest.fixture()
def create_folder(request):
    """
    Create a new folder fixture
    :param request:
    """
    validate = ValidateResponse()
    LOGGER.debug("Create folder fixture")
    url_clickup = URL_CLICKUP + "space/" + space_id + "/folder"
    random_number = random.randint(1, 1000)
    payload = read_input_data_json("post_folder")
    payload["name"] = f"New Folder API {random_number}"
    rest_client = RestClient()
    response = rest_client.request("post", url_clickup, body=payload)
    validate.validate_response(response, "post_create_folder")
    folder_id = response["body"]["id"]
    yield folder_id
    delete_folder(folder_id)


def delete_folder(folder_id):
    """
    Delete a folder
    :param folder_id: folder's ID
    """
    LOGGER.info('Cleanup folder...')
    url_clickup = URL_CLICKUP + "folder/" + folder_id
    rest_client = RestClient()
    response = rest_client.request("delete", url_clickup)
    if response["status_code"] == 200:
        LOGGER.info("Folder Id: %s deleted", folder_id)


@pytest.fixture(scope="session")
def create_space(request):
    """
    Create a new space fixture
    :param request:
    """
    validate = ValidateResponse()
    LOGGER.debug("Create space fixture")
    team_id = get_authorized_teams()
    url_clickup = URL_CLICKUP + "team/" + team_id + "/space"
    random_number = random.randint(1, 1000)
    payload = read_input_data_json("put_space")
    payload["name"] = f"New Space Name API {random_number}"
    rest_client = RestClient()
    response = rest_client.request("post", url_clickup, body=payload)
    validate.validate_response(response, "post_create_space")
    id_space = response["body"]["id"]
    yield id_space
    delete_space(id_space)


def delete_space(id_space):
    """
    Delete a folder
    :param id_space: space's ID
    """
    LOGGER.info('Cleanup space...')
    url_clickup = URL_CLICKUP + "space/" + id_space
    rest_client = RestClient()
    response = rest_client.request("delete", url_clickup)
    if response["status_code"] == 200:
        LOGGER.info("Space Id: %s deleted", id_space)


def read_input_data_json(endpoint):
    """
    :param endpoint: File name
    :return: json
    """
    file_name = f"{abs_path}/clickup_api/payload/{endpoint}.json"
    LOGGER.debug("Reading file %s", file_name)
    with open(file_name, encoding="utf8") as json_file:
        data = json.load(json_file)
        LOGGER.debug("Content of '%s' : %s", file_name, data)
        json_file.close()
    return data
