import datetime
from typing import List, Optional

from jinja2 import Environment, FileSystemLoader

from src.core.config import settings


class EmailManager:
    REGISTRATION_TEMPLATE = 'welcome.html'
    PERSONAL_TEMPLATE = 'personal_email.html'
    MAILING_LIST_TEMPLATE = 'mailing_list_email.html'

    def __init__(self, template_directory: str = 'email/templates'):
        self._env = Environment(loader=FileSystemLoader(template_directory))

    def send_registration_email(
            self,
            receiver_email: str,
            trial_days: int,
            login: str,
            action_url: str,
            login_url: str,
            user_name: str = 'Уважаемый Гость',
    ):
        context = self._get_email_context()
        context.update({
            'trial_days': trial_days,
            'user_name': user_name,
            'login': login,
            'password': 'adminmyparol',
        })
        _template = self._env.get_template(self.REGISTRATION_TEMPLATE)
        output_html = _template.render(context)
        self._send(message=output_html, to=[receiver_email])

    def send_personal_email(
            self,
            receiver_email: str,
            title_message: str,
            message: str,
            message_dict: Optional[dict] = None,
    ):
        context = self._get_email_context()
        context.update({
            'title_message': title_message,
            'message': message,
            'message_dict': message_dict,
        })
        _template = self._env.get_template(self.PERSONAL_TEMPLATE)
        output_html = _template.render(context)
        self._send(message=output_html, to=[receiver_email])

    def send_mailing_list_email(
            self,
            receiver_email: List[str],
            title_message: str,
            message: str,
            message_dict: Optional[dict] = None,
    ):
        context = self._get_email_context()
        context.update({
            'title_message': title_message,
            'message': message,
            'message_dict': message_dict,
        })
        _template = self._env.get_template(self.MAILING_LIST_TEMPLATE)
        output_html = _template.render(context)
        self._send(message=output_html, to=receiver_email)

    @staticmethod
    def _get_email_context():
        return {
            'company_name': settings.COMPANY_NAME,
            'company_city': settings.COMPANY_CITY,
            'company_address': settings.COMPANY_ADDRESS,
            'company_email': settings.COMPANY_EMAIL,
        }

    @staticmethod
    def _send(message: str, to: list):
        with open('test.html', 'w') as f:
            f.write(message)


# EmailManager().send_registration_email(
#     receiver_email='poluchatel228@mail.ru',
#     trial_days=3,
#     login='vasya_pupkov',
#     action_url='https://google.com/',
#     login_url='https://accounts.google.com/',
#     user_name='Василий',
# )


# EmailManager().send_personal_email(
#     receiver_email='poluchatel228@mail.ru',
#     title_message='Добро пожаловать Эльдияр!',
#     message='Кто-то ввёл правильный пароль от вашего аккаунта, который Вы используете в Почте '
#             'и других сервисах Онлайн-Кинотеатра. Вот что нам известно:',
#     message_dict={
#         'Логин': 'vasya_pupkov',
#         'Пароль': 'neverniyparol5'
#     },
# )


EmailManager().send_mailing_list_email(
    receiver_email=['poluchatel228@mail.ru'],
    title_message='Уважаемые клиенты!',
    message='Пришло время отпраздновать день рождения нашего Онлайн-Кинотеатра! '
            'В рамках нашего особого дня мы предлагаем эксклюзивную скидку 30% на любой годовой план, '
            'и она не продлится долго!',
    message_dict={
        'Промокод': 'CINEMAPLAN',
    },
)