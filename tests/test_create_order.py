import allure
import pytest
from utils.helpers import Helpers
from utils.methods import MethodsOrder
from utils.data import ApiResponses


class TestCreateOrderAPI:
    @allure.title('Cоздание заказа')
    @allure.description('Создание заказа с разными входными данными самоката')
    @pytest.mark.parametrize(
        'payload',
        [
            Helpers.create_data_for_order(["BLACK"]),
            Helpers.create_data_for_order(["BLACK", "GREY"]),
            Helpers.create_data_for_order([""])
        ]
    )
    def test_create_order(self, payload):
        test_order = MethodsOrder.create_order(payload)
        assert test_order.status_code == 201 and ApiResponses.ORDER_CREATE_SUCCESSFUL in test_order.json()