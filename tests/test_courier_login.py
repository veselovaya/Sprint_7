import requests
from endpoints import Urls
from helpers import create_new_courier as new_courier_data
from data import Couriers
from data import Responses
import allure

class TestCourierLogin:

    @allure.title('Проверка, что при успешной авторизации под УЗ курьера возвращается id')
    def test_courier_login_true(self):
        data = Couriers.valid_user
        response = requests.post(f'{Urls.URL}{Urls.LOGIN_COURIER}', data)
        assert response.status_code == 200 and Responses.COURIER_LOGIN_SUCCESSFUL in response.text

    @allure.title('проверка, что невозможно авторизоваться под УЗ курьера без логина')
    def test_courier_login_without_login_false(self):
        data = Couriers.user_no_login
        response = requests.post(f'{Urls.URL}{Urls.LOGIN_COURIER}', data)
        assert response.status_code == 400 and Responses.COURIER_LOGIN_WITHOUT_PARAMS in response.text

    @allure.title('Проверка, что невозможно авторизоваться под УЗ курьера без пароля')
    def test_courier_login_without_password_false(self):
        data = Couriers.user_no_password
        response = requests.post(f'{Urls.URL}{Urls.LOGIN_COURIER}', data)
        assert response.status_code == 400 and Responses.COURIER_LOGIN_WITHOUT_PARAMS in response.text

    @allure.title('Проверка, что невозможно авторизоваться под УЗ курьера с невалидным логином и паролем')
    def test_courier_login_with_invalid_data_false(self):
        data = new_courier_data()
        response = requests.post(f'{Urls.URL}{Urls.LOGIN_COURIER}', data)
        assert response.status_code == 404 and Responses.COURIER_LOGIN_INVALID_DATA in response.text




