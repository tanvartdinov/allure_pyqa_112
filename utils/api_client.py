import allure
import requests

class APIClient:
    base_url = 'https://fe.rc.smotreshka.tv'

    @allure.step('Авторизация')
    def login(self, login, password):
        data = f'email={login}&password={password}'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post('https://fe.rc.smotreshka.tv/login',
                             headers=headers,
                             data=data)
        allure.attach('https://fe.rc.smotreshka.tv/login', name="URL", attachment_type=allure.attachment_type.TEXT)
        allure.attach(data, name="Payload", attachment_type=allure.attachment_type.TEXT)
        allure.attach(response.text, name="Response", attachment_type=allure.attachment_type.JSON)
        return response
