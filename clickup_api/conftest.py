"""
conftest.py - Global configuration file for pytest

This file defines global configurations and fixtures that apply to all tests in the project.

More information about pytest and how to use conftest.py can be found at:
- https://docs.pytest.org/en/stable/
"""

import json
import random
import logging
from logging import Logger

import pytest

from config.config import URL_CLICKUP, abs_path
from utils.logger import get_logger
from helpers.rest_client import RestClient

LOGGER: Logger = get_logger(__name__, logging.DEBUG)


def get_authorized_teams():
    """
    View the Workspaces available to the authenticated user.
    :return: authorized_teams: authorized teams's id
    """
    rest_client = RestClient()
    LOGGER.debug("Get Authorized Teams (Workspaces)")
    url_clickup = f"{URL_CLICKUP}team"
    response = rest_client.request("get", url_clickup)
    authorized_teams = response["body"]["teams"][0]["id"]
    return authorized_teams


@pytest.fixture(scope="class")
def create_space_fixture():
    """
    Create a new space fixture
    """
    id_space = create_space()
    yield id_space
    delete_space(id_space)


def create_space():
    """
    Create a new space
    :return: id_space: Space's id
    """
    rest_client = RestClient()
    LOGGER.debug("Create space fixture")
    team_id = get_authorized_teams()
    url_clickup = f"{URL_CLICKUP}team/{team_id}/space"
    random_number = random.randint(1, 1000)
    payload = read_input_data_json("put_space")
    payload["name"] = f"New Space Name API {random_number}"
    response = rest_client.request("post", url_clickup, body=payload)
    id_space = response["body"]["id"]
    return id_space


def delete_space(id_space):
    """
    Delete a folder
    :param id_space: space's ID
    """
    rest_client = RestClient()
    LOGGER.info('Cleanup spaces...')
    url_clickup = f"{URL_CLICKUP}space/{id_space}"
    response = rest_client.request("delete", url_clickup)
    if response["status_code"] == 200:
        LOGGER.info("Space Id: %s deleted", id_space)
    else:
        LOGGER.error("Error deleting space with ID: %s", id_space)


@pytest.fixture(scope="class")
def create_folder_in_space_fixture():
    """
    Create a new space fixture
    """
    id_space = create_space()
    id_folder = create_folder_in_space(id_space)
    yield id_space, id_folder
    delete_folder(id_folder)
    delete_space(id_space)


def create_folder_in_space(space_id):
    """
    Create a new folder fixture
    :param space_id: space's id
    :return: folder_id: folder's id
    """
    rest_client = RestClient()
    LOGGER.debug("Create folder on space_id: %s", space_id)
    url_clickup = f"{URL_CLICKUP}space/{space_id}/folder"
    random_number = random.randint(1, 1000)
    payload = read_input_data_json("post_folder")
    payload["name"] = f"New Folder API {random_number}"
    response = rest_client.request("post", url_clickup, body=payload)
    folder_id = response["body"]["id"]
    return folder_id


def delete_folder(folder_id):
    """
    Delete a folder
    :param folder_id: folder's ID
    """
    rest_client = RestClient()
    LOGGER.info('Cleanup folders...')
    url_clickup = f"{URL_CLICKUP}folder/{folder_id}"
    response = rest_client.request("delete", url_clickup)
    if response["status_code"] == 200:
        LOGGER.info("Folder Id: %s deleted", folder_id)
    else:
        LOGGER.error("Error deleting folder with ID: %s", folder_id)


def create_list(space_id):
    """
    Create a new list
    :param space_id: space's id
    :return: list's id
    """
    rest_client = RestClient()
    LOGGER.debug("Create list")
    url_clickup = f"{URL_CLICKUP}space/{space_id}/list"
    random_number = random.randint(1, 1000)
    payload = read_input_data_json("post_list")
    payload["name"] = f"New list API {random_number}"
    payload["content"] = payload["name"]
    response = rest_client.request("post", url_clickup, body=payload)
    list_id = response["body"]["id"]
    return list_id


def create_list_in_folder(folder_id):
    """
    Create a new list
    :param folder_id: folder's ID
    :return: list's id
    """
    LOGGER.debug("Create list in the folder %s", folder_id)
    url_clickup = f"{URL_CLICKUP}folder/{folder_id}/list"
    random_number = random.randint(1, 1000)
    payload = read_input_data_json("post_list")
    payload["name"] = f"New list API {random_number}"
    payload["content"] = payload["name"]
    rest_client = RestClient()
    response = rest_client.request("post", url_clickup, body=payload)
    list_id = response["body"]["id"]
    return list_id


def delete_list(list_id):
    """
    Test Delete list
    :param list_id: list's ID
    """
    url_clickup = URL_CLICKUP + "list/" + list_id
    rest_client = RestClient()
    response = rest_client.request("delete", url_clickup)
    if response["status_code"] == 200:
        LOGGER.info("List Id: %s deleted", list_id)
    else:
        LOGGER.error("Error deleting list with ID: %s", list_id)


def create_task(list_id):
    """
    Create a new task
    :param list_id: List's id
    :return: task's id
    """
    rest_client = RestClient()
    LOGGER.debug("Create Task")
    url_clickup = f"{URL_CLICKUP}list/{list_id}/task"
    random_number = random.randint(1, 1000)
    payload = read_input_data_json("post_task")
    payload["name"] = f"New Task Name API {random_number}"
    payload["description"] = payload["name"]
    response = rest_client.request("post", url_clickup, body=payload)
    task_id = response["body"]["id"]
    return task_id


def add_task_to_secondary_list(space_id):
    """
    Add the task to secondary list
    :param space_id: space's id
    :return: list_id_second, task_id: list's id , task's id
    """
    rest_client = RestClient()
    list_id_fist = create_list(space_id)
    list_id_second = create_list(space_id)
    task_id = create_task(list_id_fist)
    url_clickup = URL_CLICKUP + "list/" + list_id_second + "/task/" + task_id
    response = rest_client.request("post", url_clickup)
    LOGGER.debug("Response: %s", response)
    return list_id_second, task_id


def delete_task(task_id):
    """
    Delete list
    :param task_id: task's id
    """
    rest_client = RestClient()
    url_clickup = URL_CLICKUP + "task/" + task_id
    response = rest_client.request("delete", url_clickup)
    if response["status_code"] == 200:
        LOGGER.info("List Id: %s deleted", task_id)
    else:
        LOGGER.error("Error deleting list with ID: %s", task_id)


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
    return data
