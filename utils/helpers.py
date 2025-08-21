import allure


@allure.step("Проверяем статус-код ответа")
def assert_status_code(response, expected_status=200):
    assert response.status_code == expected_status, (
        f"Ожидался статус {expected_status}, но получен {response.status_code}"
    )