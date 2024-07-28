class Responses:
    CREATE_COURIER_TRUE = '{"ok":true}'
    COURIER_LOGIN_SUCCESSFUL = "id"
    DUBLICATE_COURIER_CREATION = "Этот логин уже используется."
    COURIER_LOGIN_WITHOUT_PARAMS = "Недостаточно данных для входа"
    COURIER_WITHOUT_PARAMS_FOR_CREATION = "Недостаточно данных для создания учетной записи"
    COURIER_LOGIN_INVALID_DATA = "Учетная запись не найдена"
    ORDER_CREATE_TRUE = "track"
    ORDER_LIST_TRUE = "orders"

class Couriers:
    valid_user = {
        "login": "veselova_test",
        "password": "1234"
    }

    user_no_login = {
        "login": "",
        "password": "1234"
    }

    user_no_password = {
        "login": "veselova_test",
        "password": ""
    }




