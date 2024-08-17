import pytest
import requests
from endpoints import Urls
import helpers
from data import Responses
import allure


class TestCreateOrder:

    @pytest.mark.parametrize(
        'payload',
        [
            helpers.create_data_for_order(['GREY']),
            helpers.create_data_for_order(['BLACK']),
            helpers.create_data_for_order(['GREY', 'BLACK']),
            helpers.create_data_for_order([''])
        ]
    )

    @allure.title('Проверка успешного создания заказа')
    def test_create_order_true(self, payload):
        response = requests.post(f'{Urls.URL}{Urls.CREATE_ORDER}',data=payload)
        assert response.status_code == 201 and Responses.ORDER_CREATE_TRUE in response.text