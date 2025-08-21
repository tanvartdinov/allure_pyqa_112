import allure
import requests

from utils.api_client import APIClient
from utils.helpers import assert_status_code


@allure.epic('Authorization')
@allure.feature('Authentication via password')
@allure.title('Успешная авторизация с валидными данными (устаревший метод)')
@allure.description('Авторизация через /login')
def test_login_success():
    with allure.step('Подготовка данных'):
        data = 'email=testatr0207251&password=123456'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        allure.attach(data, 'Body', attachment_type=allure.attachment_type.TEXT)
        allure.attach(str(headers), 'headers', attachment_type=allure.attachment_type.TEXT)

    with allure.step('Логин'):
        response = requests.post('https://fe.rc.smotreshka.tv/login',
                                 headers=headers,
                                 data=data)
    with allure.step('Валидация статус-кода'):
        assert response.status_code == 200

@allure.epic('Authorization')
@allure.feature('Authentication via password')
@allure.title('Неуспешная авторизация с невалидным паролем')
@allure.description('Авторизация через /login')
def test_login_failed_invalid_password(get_invalid_credentials):
    client = APIClient()
    login, password = get_invalid_credentials
    response = client.login(login, password)
    assert_status_code(response, 403)


@allure.epic('Authorization')
@allure.feature('Authentication via password v2')
@allure.title('Успешная авторизация с валидными данными v2')
@allure.description('Авторизация через /v2/login')
def test_login_v2_success():
    data = 'email=testatr0207251&password=123456'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post('https://fe.rc.smotreshka.tv/v2/login',
                             headers=headers,
                             data=data)
    assert response.status_code == 200

@allure.epic('Authorization')
@allure.feature('Authentication via password v2')
@allure.title('Неуспешная авторизация с невалидным паролем v2')
@allure.description('Авторизация через /v2/login')
def test_login_v2_failed_invalid_password():
    data = 'email=testatr0207251&password=1234'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post('https://fe.rc.smotreshka.tv/v2/login',
                             headers=headers,
                             data=data)
    assert response.status_code == 403


# Ключ Назначение
# -v Подробный вывод (verbose) — показывает названия тестов
# --tb=short/line/long Формат вывода traceback при падении
# --maxfail=N Прервать выполнение после N падений
# --durations=N Показать N самых медленных тестов