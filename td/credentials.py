from datetime import date, datetime


class TdCredentials():

    def __init__(self) -> None:

        self._access_token = ''
        self._refresh_token = ''
        self._scope = []
        self._token_type = ''
        self._expires_in = 0
        self._refresh_token_expires_in = 0
        self._is_expired = True

        self._refresh_token_expiration_time = 0
        self._access_token_expiration_time = 0

    def from_token_dict(self, token_dict: dict) -> None:

        self._access_token = token_dict.get('access_token', '')
        self._refresh_token = token_dict.get('refresh_token', '')
        self._scope = token_dict.get('scope', [])
        self._token_type = token_dict.get('token_type', '')
        self._expires_in = token_dict.get('expires_in', 0)
        self._refresh_token_expires_in = token_dict.get(
            'refresh_token_expires_in',
            0
        )

        self._calculate_access_token_expiration(
            expiration_secs=self._expires_in,
        )

        self._calculate_refresh_token_expiration(
            expiration_secs=self._refresh_token_expires_in
        )

    def to_token_dict(self) -> dict:

        token_dict = {
            'access_token': self._access_token,
            'refresh_token': self._refresh_token,
            'scope': self._scope,
            'expires_in': self._expires_in,
            'refresh_token_expires_in': self._refresh_token_expires_in,
            'token_type': self._token_type
        }

        return token_dict

    @property
    def is_access_token_expired(self) -> bool:
        
        if (self._access_token_expiration_time - 20) < datetime.now().timestamp():
            return True
        else:
            return False

    @property
    def is_refresh_token_expired(self) -> bool:

        if (self._refresh_token_expiration_time - 20) < datetime.now().timestamp():
            return True
        else:
            return False
    
    @property
    def refresh_token_expiration_time(self) -> datetime:
        return datetime.fromtimestamp(self._refresh_token_expiration_time)

    @property
    def access_token_expiration_time(self) -> datetime:
        return datetime.fromtimestamp(self._access_token_expiration_time)

    def seconds_to_expiration(self, token: str = 'refresh_token') -> int:
        pass

    def _validate_tokens(self) -> None:
        pass

    def _calculate_refresh_token_expiration(self, expiration_secs: int) -> None:
        expiration_time = datetime.now().timestamp() + expiration_secs
        self._refresh_token_expiration_time = expiration_time

    def _calculate_access_token_expiration(self, expiration_secs: int) -> None:
        expiration_time = datetime.now().timestamp() + expiration_secs
        self._access_token_expiration_time = expiration_time
