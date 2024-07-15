import allure
from utils.data import ApiResponses
from utils.methods import MethodsCourier


class TestLoginCourierAPI:
    @allure.title('Вход в систему курьером')
    @allure.description('Заходим в систему курьером и проверяем ответ')
    def test_login(self, create_and_delete_courier):
        test_courier = MethodsCourier.login_courier(create_and_delete_courier)
        assert test_courier.status_code == 200 and ApiResponses.COURIER_LOGIN_SUCCESSFUL in test_courier.json()

    @allure.title('Попытка входа в систему с отсутствием одного из полей')
    @allure.description('Вход в систему без логина и проверка ошибки')
    def test_login_missing_login(self):
        test_courier = MethodsCourier.login_courier_without_login()
        assert test_courier.status_code == 400 and test_courier.json()['message'] == ApiResponses.COURIER_LOGIN_MISSING_PARAM_UNSUCCESSFUL

    @allure.title('Попытка входа в систему с отсутствием одного из полей')
    @allure.description('Вход в систему без пароля и проверка ошибки')
    def test_login_missing_password(self):
        test_courier = MethodsCourier.login_courier_without_password()
        assert test_courier.status_code == 400 and test_courier.json()['message'] == ApiResponses.COURIER_LOGIN_MISSING_PARAM_UNSUCCESSFUL

    @allure.title('Попытка войти в систему с несуществующими данными')
    @allure.description('Входим в систему с невалидными данными и получаем ошибку')
    def test_login_invalid_data(self):
        test_courier = MethodsCourier.login_no_such_username_and_password()
        assert test_courier.status_code == 404 and test_courier.json()['message'] == ApiResponses.COURIER_LOGIN_WITH_INVALID_DATA_UNSUCCESSFUL
