from urllib.parse import urlparse
from arq.connections import RedisSettings

from app.config import get_settings

settings = get_settings()


def get_redis_settings() -> RedisSettings:
    redis_url = str(settings.redis_url)
    parsed = urlparse(redis_url)
    
    host = parsed.hostname or "localhost"
    port = parsed.port or 6379
    database = int(parsed.path.lstrip("/")) if parsed.path else 0
    password = parsed.password
    
    return RedisSettings(
        host=host,
        port=port,
        database=database,
        password=password,
    )