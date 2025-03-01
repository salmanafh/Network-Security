import logging
import os
from datetime import datetime 

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d')}.log"

logs_part = os.path.join(os.getcwd(), 'logs', LOG_FILE)
os.makedirs(logs_part, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_part, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)