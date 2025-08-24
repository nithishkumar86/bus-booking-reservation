import os
from dotenv import load_dotenv
from app.Config.configfile import config_loading
from langchain_openai import ChatOpenAI
from app.common.logger import get_logger
from app.common.custom_exception import BookingException
import sys
from langchain_groq import ChatGroq

logger = get_logger(__name__)


class ModelLoader:
    def __init__(self):
        self.config=config_loading()
        self._load_env()
        logger.debug("model get initialized")
        
    def _load_env(self):
        load_dotenv()
        GROQ_API_KEY= os.getenv('GROQ_API_KEY')
        if GROQ_API_KEY:
            os.environ['GROQ_API_KEY'] = GROQ_API_KEY
            logger.debug("environment loaded successfully")
    
    def model_loading(self):
        try:
            name = self.config["llm"]["model_name"]
            llm = ChatGroq(model=name)
            logger.info(f"{llm} model is ready to execute")
            return llm
        except Exception as e:
            logger.error(f"there is as error in model loading {str(e)}")
            raise BookingException(e,sys)