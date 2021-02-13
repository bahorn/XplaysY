#!/usr/bin/env python3
import asyncio
import websockets
import logging
import redis
import config

from server import server
from health_check import health_check

logger = logging.getLogger()

if __name__ == "__main__":
    # Redis clients are thread safe, so this is fine to do.
    r = redis.Redis(
        config.REDIS_HOST,
        port=config.REDIS_PORT
    )
    logger.info('redis connected')
    start_server = websockets.serve(
        server(r),
        config.HOSTNAME,
        config.PORT,
        process_request=health_check
    )

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
