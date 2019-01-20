import logging
import os
from logging.handlers import RotatingFileHandler
from MyScript.args import args, startTime
import MyScript.const as const
# Import your requirements here


# Configure Logging Settings
if args.log_output == "{}.log".format(const.NAME):
    # If no log-output variable specified, log to working directory
    logPath = os.path.join(args.working_directory, args.log_output)
else:
    # Otherwise, log at the specified path
    logPath = args.log_output
# Construct the Logger
handler = RotatingFileHandler(logPath, 'a', const.LOG_MAX_SIZE, const.LOG_MAX_NUM)
logging.basicConfig(
        format="%(asctime)s %(levelname)s %(threadName)s %(message)s",
        datefmt='%m/%d/%Y %I:%M:%S %p',
        level=logging.DEBUG,
        handlers=[handler]
    )
# logging can now be called

def main():
    logging.debug(args)
    print("Hello world!")

if __name__ == "__main__":
    main()
