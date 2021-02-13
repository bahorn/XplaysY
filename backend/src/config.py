import os
from dotenv import load_dotenv
load_dotenv()

HOSTNAME = os.getenv('HOSTNAME') or '127.0.0.1'
PORT = os.getenv('PORT') or 8080
PATH = ['devpath']

REDIS_HOST = os.getenv('REDIS_HOST') or '127.0.0.1'
REDIS_PORT = os.getenv('REDIS_PORT') or 6379

CMD_EXPIRE = 2
