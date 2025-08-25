import os
from dotenv import load_dotenv
from app.Config.configfile import config_loading
from langchain_openai import ChatOpenAI
from app.common.logger import get_logger
from app.common.custom_exception import BookingException
import sys
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI

logger = get_logger(__name__)


class ModelLoader:
    def __init__(self):
        self.config=config_loading()
        self._load_env()
        logger.debug("model get initialized")
        
    def _load_env(self):
        load_dotenv()
        GROQ_API_KEY = os.getenv('GROQ_API_KEY')
        if GROQ_API_KEY:
            os.environ['GROQ_API_KEY'] = GROQ_API_KEY
            logger.debug("environment loaded successfully")
    
    def model_loading(self):
        provider =self.config["llm"]["provider"]
        model = self.config["llm"]["model_name"]
        try:
            if provider == "groq":
                return ChatGroq(
                    model=model,
                )
            else:
                raise ValueError(f"❌ Unknown LLM provider: {provider}")
        except Exception as e:
            print({"error": "there is an error in model loading"})