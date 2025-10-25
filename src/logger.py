import logging
import os
from datetime import datetime

# Create log file name based on current datetime
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create a "logs" folder if it doesn't exist
logs_folder = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_folder, exist_ok=True)

# Full path to the log file
LOG_FILE_PATH = os.path.join(logs_folder, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)