import requests
import allure
from utils.urls import ApiUrls
from utils.helpers import Helpers


class MethodsCourier:
    @staticmethod
    @allure.step("Создание нового курьера")
    def create_courier(payload):
        response = requests.post(ApiUrls.MAIN_URL + ApiUrls.CREATE_COURIER_API, data=payload)
        return response

    @staticmethod
    @allure.step("Удаление курьера из системы")
    def delete_courier(payload):
        login_courier = requests.post(ApiUrls.MAIN_URL + ApiUrls.LOGIN_COURIER_API, data=payload)
        id_courier = login_courier.json()['id']
        requests.delete(ApiUrls.MAIN_URL + ApiUrls.DELETE_COURIER_API + str(id_courier))

    @staticmethod
    @allure.step("Создание курьера без логина")
    def create_courier_without_login():
        only_password = Helpers.create_courier_data()["password"]
        payload = {
            "login": "",
            "password": only_password
        }
        response = requests.post(ApiUrls.MAIN_URL + ApiUrls.CREATE_COURIER_API, data=payload)
        return response

    @staticmethod
    @allure.step("Создание курьера без пароля")
    def create_courier_without_password():
        only_login = Helpers.create_courier_data()["login"]
        payload = {
            "login": only_login,
            "password": ""
        }
        response = requests.post(ApiUrls.MAIN_URL + ApiUrls.CREATE_COURIER_API, data=payload)
        return response

    @staticmethod
    @allure.step("Вход курьера в систему")
    def login_courier(payload):
        requests.post(ApiUrls.MAIN_URL + ApiUrls.CREATE_COURIER_API, data=payload)
        response = requests.post(ApiUrls.MAIN_URL + ApiUrls.LOGIN_COURIER_API, data=payload)
        return response

    @staticmethod
    @allure.step("Попытка войти в систему только с логином")
    def login_courier_with_login():
        only_login = Helpers.create_courier_data()["login"]
        payload = {
            "login": only_login,
            "password": ""
        }
        response = requests.post(ApiUrls.MAIN_URL + ApiUrls.LOGIN_COURIER_API, data=payload)
        return response

    @staticmethod
    @allure.step("Попытка войти в систему только с паролем")
    def login_courier_with_password():
        only_password = Helpers.create_courier_data()["password"]
        payload = {
            "login": "",
            "password": only_password
        }
        response = requests.post(ApiUrls.MAIN_URL + ApiUrls.LOGIN_COURIER_API, data=payload)
        return response

    @staticmethod
    @allure.step("Попытка залогиниться в систему с несуществующими логином и паролем")
    def login_no_such_username_and_password():
        payload = Helpers.create_courier_data()
        response = requests.post(ApiUrls.MAIN_URL + ApiUrls.LOGIN_COURIER_API, data=payload)
        return response


class MethodsOrder:
    @staticmethod
    @allure.step("Создание заказа")
    def create_order(payload):
        response = requests.post(ApiUrls.MAIN_URL + ApiUrls.ORDER_API, data=payload)
        return response

    @staticmethod
    @allure.step("Получение списка заказов")
    def get_list_order():
        response = requests.get(ApiUrls.MAIN_URL + ApiUrls.ORDER_API)
        return response