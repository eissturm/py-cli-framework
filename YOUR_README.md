Hello, welcome to my script!

![pcf-version](https://img.shields.io/badge/myscript-v0.0.0-blue.svg)
![build-status](https://img.shields.io/badge/build-passing-green.svg)
![coverage](https://img.shields.io/badge/coverage-100%25-orange.svg)

Includes:
- Log handling and rotation
- Command-line argument handling

## Usage

```
usage: my-script [-h] [--working-directory WORKING_DIRECTORY]
                 [--log-output LOG_OUTPUT] [-v] [-V]

Capture and process logs into db format

optional arguments:
  -h, --help            show this help message and exit
  --working-directory WORKING_DIRECTORY
                        Defaults to /home/andy/.MyScript
  --log-output LOG_OUTPUT
                        File location to write the auditlogs to. Default:
                        /working/directory/MyScript.log
  -v, --verbose
  -V, --version         show program's version number and exit
  ```
