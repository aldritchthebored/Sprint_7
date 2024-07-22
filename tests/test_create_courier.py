import allure
from utils.data import ApiResponses
from utils.methods import MethodsCourier


class TestCourierCreateAPI:
    @allure.title('Создание нового курьера')
    @allure.description('Генерируем данные курьера, отправляем запрос на создание и проверяем ответ ')
    def test_create_new_courier(self, create_and_delete_courier):
        test_courier = MethodsCourier.create_courier(create_and_delete_courier)
        assert test_courier.status_code == 201 and ApiResponses.COURIER_CREATE_SUCCESSFUL in test_courier.json()

    @allure.title('Создание курьера с повторными данными')
    @allure.description('Проверяем создание курьера с использованием уже существующих данных и получаем ошибку')
    def test_create_already_existing_courier_fail(self, only_create_courier):
        test_courier = MethodsCourier.create_courier(only_create_courier)
        test_courier_1 = MethodsCourier.create_courier(only_create_courier)
        test_courier = MethodsCourier.delete_courier(only_create_courier)
        assert test_courier_1.status_code == 409 and test_courier_1.json()['message'] == ApiResponses.TWIN_COURIER_CREATE_UNSUCCESSFUL

    @allure.title('Создание курьера не заполнив поле логина')
    @allure.description('Создаем курьера не заполнив обязательно поле и получаем ошибку')
    def test_create_courier_without_login(self):
        test_courier = MethodsCourier.create_courier_without_login()
        assert test_courier.status_code == 400 and test_courier.json()['message'] == ApiResponses.COURIER_WITHOUT_REQUIRED_PARAMS_NOT_CREATED

    @allure.title('Создание курьера не заполнив поле пароля')
    @allure.description('Создаем курьера не заполнив обязательно поле и получаем ошибку')
    def test_create_courier_without_password(self):
        test_courier = MethodsCourier.create_courier_without_password()
        assert test_courier.status_code == 400 and test_courier.json()['message'] == ApiResponses.COURIER_WITHOUT_REQUIRED_PARAMS_NOT_CREATED
