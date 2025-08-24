from os import getenv


def get_env_value(key: str) -> str:
    value: str | None = getenv(key)

    if not value:
        raise ValueError(f"Environment variable {key} was not found!")

    return value

