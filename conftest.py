import pytest
import requests
from utils.urls import ApiUrls
from utils.helpers import Helpers

@pytest.fixture(scope='function')
def only_create_courier():
    courier_payload = Helpers.create_courier_data()
    yield courier_payload

@pytest.fixture(scope='function')
def create_and_delete_courier():
    courier_payload = Helpers.create_courier_data()
    yield courier_payload
    login_courier = requests.post(ApiUrls.MAIN_URL + ApiUrls.LOGIN_COURIER_API, data=courier_payload)
    id_courier = login_courier.json()['id']
    requests.delete(ApiUrls.MAIN_URL + ApiUrls.DELETE_COURIER_API + str(id_courier))


