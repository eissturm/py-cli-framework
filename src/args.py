import time
import argparse
import const
import sys
import os

startTime = time.strftime('%Y-%m-%dT%H-%M')
# Configure command-line arguments
parser = argparse.ArgumentParser(
        description="Capture and process logs into db format"
    )
parser.add_argument(
    '--log-output',
    default='{}.log'.format(const.NAME),
    type=str,
    help="File location to write the auditlogs to.  Default: {}.log".format(const.NAME)
)
parser.add_argument(
        '-v',
        '--verbose',
        default=False,
        action='store_true'
    )
parser.add_argument(
    '-V',
    '--version',
    action='version',
    version=const.VERSION
)
args = parser.parse_args()
