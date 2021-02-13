import logging
import json
import config

logger = logging.getLogger()


def validate(message):
    """
    Check if the message is in the correct format.
    """
    if not ('x' in message and 'y' in message):
        return False

    if not(isinstance(message['x'], float)) or not(isinstance(message['y'], float)):
        return False

    return True    

def message_handler(redis_client, client, path, message):
    """
    Handles each message
    """
    value = ''
    error = False
    try:
        data = json.loads(message)
        if validate(data):
            x = data['x']
            y = data['y']
            key = '{}:{}'.format(path, client)
            pipe = redis_client.pipeline()
            pipe.hset(
                key,
                mapping={
                    'x': x,
                    'y': y
                }
            )
            pipe.expire(key, config.CMD_EXPIRE)
            pipe.execute()
        else:
            error = True

    except Exception as exp:
        logger.error(exp)
        error = True

    return (error, value)


def server(redis_client):
    """
    Wrapper for the update function, so it has a redis instance passed in.
    """
    async def update(websocket, path):
        cleaned_path = path.split('?')[0].split('/')[-1]
        if cleaned_path not in config.PATH:
            logger.warning("Request for unknown path: %s Expected: %s", cleaned_path, config.PATH)
            return

        exception_count = 0
        remote_ip = websocket.remote_address[0]
        logger.info('connection from %s', remote_ip)

        async for message in websocket:
            (error, _value) = message_handler(redis_client, remote_ip, cleaned_path, message)
            if error:
                exception_count += 1

            if exception_count > 3:
                logger.warning(
                    'killing client %s for too many exceptions', remote_ip
                )
                return

    return update
