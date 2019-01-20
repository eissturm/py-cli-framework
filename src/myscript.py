import logging
from logging.handlers import RotatingFileHandler
from args import args, startTime
import const


# Configure Logging Settings
handler = RotatingFileHandler(args.log_output, 'a', const.LOG_MAX_SIZE, const.LOG_MAX_NUM)
logging.basicConfig(
        format="%(asctime)s %(levelname)s %(threadName)s %(message)s",
        datefmt='%m/%d/%Y %I:%M:%S %p',
        level=logging.DEBUG,
        handlers=[handler]
    )

if __name__ == "__main__":
    logging.debug(args)
