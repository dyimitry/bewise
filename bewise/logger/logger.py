import logging.config
from pathlib import Path

log_conf = Path(__file__).parent.parent.parent.absolute() / "logging.ini"

logging.config.fileConfig(log_conf, disable_existing_loggers=True)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - [%(levelname)s] - %(name)s - "
    "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
)

logger = logging.getLogger(__name__)
