import jwt
from datetime import datetime, timedelta
from src.config.environment import env


def create_access_token(data: dict, expires_delta: timedelta = timedelta(seconds=env.JWT_ACCESS_TOKEN_EXPIRES)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, env.JWT_SECRET_KEY,
                             algorithm=env.JWT_ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str):
    try:
        decoded_token = jwt.decode(
            token, env.JWT_SECRET_KEY, algorithms=[env.JWT_ALGORITHM])
        return decoded_token if decoded_token["exp"] >= datetime.utcnow().timestamp() else None
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
