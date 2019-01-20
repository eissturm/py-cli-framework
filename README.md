# Py-Cli-Framework

![pcf-version](https://img.shields.io/badge/PCF-v1.0.1-blue.svg)

A lightweight framework for friendly and functional Python scripting.

## Who is this For?

Py-Cli-Framework is for people looking for a quick place to start when creating simple Python scripts.  Frequently I found myself creating scripts to pull reports or automate tasks through various services and data sources.  This project grew out of the pieces I found myself reusing over and over again to make my scripts usable by humans.

Projects like [Cement](https://builtoncement.com/) are more sophisticated solutions, and seem to be for projects of a larger scale.  Py-Cli-Framework (PCF) is intended for small projects and scripts, while still providing a good foundation should your project grow.

## What's in the box?
- Your script is exposed as a command in your CLI once installed with `pip`
 - Check out [pyinstaller](http://www.pyinstaller.org/) if you want to include a Python runtime in your distribution package
- Pre-configured log handling and log rolling
- Pre-configured CLI argument handling
- Testing framework included.  Run from package root with `python setup.py test`
- Automated versioning with `bumpversion`

## Getting Started

1. Fork the git repository
1. Create your `virtualenv` (the `.gitignore` is looking for `/env/`)
1. Activate your virtual environment, and `pip install -r dev-requirements.txt`
1. Rename the folder, script, and values in `setup.py` and `MyScript/const.py`
1. Rename this file to something else, and name `YOUR_README.md` to `README.md`
1. Reset the version number to 0.0.0 with the command `bumpversion --current-verison 1.0.1 --new-version 0.0.0 major`
1. Run `pip install --editable .` then test if your command is available at your command prompt
1. Start scripting in `MyScript/myscript.py` (or whatever you decide to call it!)

### Adding CLI Arguments
It's pretty simple, just add  your argument declarations and validations in the `MyScript/args.py`.  This helps reduce clutter in your main script so you can focus on your work there.

### Working with Dependencies
In most cases, adding a dependency to your script will be pretty easy.  Add the package name, as you would `pip install` it to the 'requires' variable in `setup.py`, and `pip` will be able to locate it, and install it for you.

#### Example
`BigReport` relies on two common external libraries to get the job done, `requests` and `pandas`.  To include those in our tool:

```
In /setup.py
...
requires = [
  'requests',
  'pandas',
]
...
```
Then run `pip install --editable .` again.  `pip` will see the new dependencies, and retrieve them for us, or eventually our end-users.

#### Non-PIP Dependencies
For any dependencies not available from PyPI, include the module or package you need in your `/MyScript` directory to ensure it is included.  You may need to resolve any further dependencies on your own.

## Resources
- [Bumpversion](https://github.com/peritus/bumpversion)
- [Argparse](https://docs.python.org/3/library/argparse.html)
- [Logging](https://docs.python.org/3/library/logging.html)

Questions?  Comments?  Issues?  Contact the project maintainer on [Gitlab](https://gitlab.com/eissturm/py-cli-framework)

Last updated: 20 Jan 2019
