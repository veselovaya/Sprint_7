import requests
from endpoints import Urls
from data import Responses
from helpers import create_new_courier as new_courier_data
import allure

class TestCreateCourier:
    data = new_courier_data()

    @allure.title('Проверка, что создается курьер с валидными данными')
    def test_create_courier_true(self):
        response = requests.post(f'{Urls.URL}{Urls.CREATE_COURIER}', TestCreateCourier.data)
        assert response.status_code == 201 and  Responses.CREATE_COURIER_TRUE in response.text

    @allure.title('Проверка, что нельзя создать двух одинаковых курьеров')
    def test_create_duplicate_courier_fail(self):
        response = requests.post(f'{Urls.URL}{Urls.CREATE_COURIER}', TestCreateCourier.data)
        assert response.status_code == 409 and Responses.DUBLICATE_COURIER_CREATION in response.text


    @allure.title('Проверка, что нельзя создать курьера без заполнения логина')
    def test_create_courier_without_login_false(self):
        new_password = new_courier_data()['password']
        payload = {
            "login": '',
            "password": new_password
        }
        response = requests.post(f'{Urls.URL}{Urls.CREATE_COURIER}', data=payload)
        assert response.status_code == 400 and Responses.COURIER_WITHOUT_PARAMS_FOR_CREATION in response.text


    @allure.title('Проверка, что нельзя создать курьера без указания пароля')
    def test_create_courier_without_password_false(self):
        new_login = new_courier_data()['login']
        payload = {
            "login": new_login,
            "password": ''
        }
        response = requests.post(f'{Urls.URL}{Urls.CREATE_COURIER}', data=payload)
        assert response.status_code == 400 and Responses.COURIER_WITHOUT_PARAMS_FOR_CREATION in response.text

