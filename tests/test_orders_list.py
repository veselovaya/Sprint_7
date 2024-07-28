import requests
from endpoints import Urls
from data import Responses
import allure

class TestOrdersList:
    @allure.title('Проверка успешного получения списка заказов')
    def test_receive_order_list_true(self):
        response = requests.get(f'{Urls.URL}{Urls.ORDERS_LIST}')
        assert response.status_code == 200 and Responses.ORDER_LIST_TRUE in response.text



