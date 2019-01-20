import time
import argparse
import const
import sys
import os
from pathlib import Path

startTime = time.strftime('%Y-%m-%dT%H-%M')
# Configure command-line arguments
parser = argparse.ArgumentParser(
        description="Capture and process logs into db format"
    )
parser.add_argument(
    '--working-directory',
    default=os.path.join(str(Path.home()), '.' + const.NAME),
    help="Defaults to {}".format(os.path.join(str(Path.home()), '.' + const.NAME))
)
parser.add_argument(
    '--log-output',
    default='{}.log'.format(const.NAME),
    type=str,
    help="File location to write the auditlogs to.  Default: /working/directory/{}.log".format(const.NAME)
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
    version=const.__version__
)
args = parser.parse_args()

if not os.path.exists(args.working_directory):
    os.makedirs(args.working_directory)
