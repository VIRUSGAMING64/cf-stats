import requests

from config.config import settings
from app.constant import Constant


class CFRequestHandler:
    """Provides services for requesting codeforces API."""

    user_info: dict = None
    user_submission: list = None
    rating_changes: list = None

    @classmethod
    def _make_api_request(cls, url: str):
        """Make a request to Codeforces API and return the result."""
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json().get('result')
        except Exception as e:
            raise SystemExit(f'Could not connect to the codeforces API: {e}')

    @classmethod
    def _get_user_info(cls):
        """Gets data from codeforces user.info api."""
        url = Constant.USER_INFO.format(settings.cf_handle)
        result = cls._make_api_request(url)
        cls.user_info = result[0] if isinstance(result, list) else result

    @classmethod
    def _get_user_sub(cls):
        """Gets data from codeforces user.status api."""
        url = Constant.USER_STATUS.format(settings.cf_handle)
        cls.user_submission = cls._make_api_request(url)

    @classmethod
    def _get_rating_changes(cls):
        """Gets all rating changes from codeforces api."""
        url = Constant.USER_RATING.format(settings.cf_handle)
        cls.rating_changes = cls._make_api_request(url)

    @staticmethod
    def make_request():
        """Makes all the necessary requests to cf API."""
        CFRequestHandler._get_user_info()
        CFRequestHandler._get_user_sub()
        CFRequestHandler._get_rating_changes()
