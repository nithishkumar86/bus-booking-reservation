import yaml
from app.common.logger import get_logger

logger = get_logger(__name__)

def config_loading(path :str="E:\\BUS_BOOKING\\Config\\config.yaml"):
    with open(path,'r') as file:
        config=yaml.safe_load(file)
    logger.info(f"the configuration file is successfully loaded from {path}")
    return config