import allure
import pytest


@pytest.fixture
@allure.step('Подготовка данных')
def get_valid_credentials():
    return 'testatr0207251', '123456'

@pytest.fixture
@allure.step('Подготовка данных')
def get_invalid_credentials():
    return 'testatr0207251', '1234'

