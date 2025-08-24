import subprocess
import threading
import time
from app.common.custom_exception import BookingException
from app.common.logger import get_logger
import sys

logger = get_logger(__name__)

def run_backround():
    try:
        subprocess.run(["uvicorn","app.backend.fastapi_backend:app","--host","127.0.0.1","--port","8000"],check=True)
    except BookingException as e:  # check = True => makes Python throw an exception if the command fails.
        logger.error(f"an error occured {str(e)}")
        raise BookingException(e,sys)
    
def run_frontend():
    try:
        subprocess.run(["streamlit","run","frontend/streamlit_frontend.py"],check=True)
    except BookingException as e:
        logger.error(f"an error occured {str(e)}")
        raise BookingException(e,sys)
    
if __name__ == "__main__":
    threading.Thread(target=run_backround).start()
    time.sleep(2)
    run_frontend()




