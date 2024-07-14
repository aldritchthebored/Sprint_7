class ApiResponses:
    COURIER_CREATE_SUCCESSFUL = "ok"
    TWIN_COURIER_CREATE_UNSUCCESSFUL = "Этот логин уже используется. Попробуйте другой."
    COURIER_WITHOUT_REQUIRED_PARAMS_NOT_CREATED = "Недостаточно данных для создания учетной записи"
    COURIER_LOGIN_SUCCESSFUL = "id"
    COURIER_LOGIN_MISSING_PARAM_UNSUCCESSFUL = "Недостаточно данных для входа"
    COURIER_LOGIN_WITH_INVALID_DATA_UNSUCCESSFUL = "Учетная запись не найдена"
    ORDER_CREATE_SUCCESSFUL = "track"
    ORDER_LIST_SUCCESSFUL = "orders"
