Hello, welcome to my script!

## Example

```
$ my-script --version
1.0
$ my-script
Hello world!
```

## Usage

```
usage: my-script [-h] [--working-directory WORKING_DIRECTORY]
                 [--log-output LOG_OUTPUT] [-V]

Capture and process logs into db format

optional arguments:
  -h, --help            show this help message and exit
  --working-directory WORKING_DIRECTORY
                        Defaults to /home/andy/.MyScript
  --log-output LOG_OUTPUT
                        File location to write the audit logs to. Default:
                        /working/directory/MyScript.log
  -V, --version         show program's version number and exit
  ```
