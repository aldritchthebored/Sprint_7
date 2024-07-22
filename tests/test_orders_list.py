import allure
from utils.data import ApiResponses
from utils.methods import MethodsOrder


class TestGetListOfOrderAPI:
    @allure.title('Получение списка заказов')
    @allure.description('Проверяем, что отдаётся список заказов и проверяем код и содержание ответа')
    def test_get_list_of_order(self):
        orders = MethodsOrder.get_list_order()
        assert orders.status_code == 200 and ApiResponses.ORDER_LIST_SUCCESSFUL in orders.json()