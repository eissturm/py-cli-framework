# Py-Cli-Framework

![pcf-version](https://img.shields.io/badge/PCF-v1.0.1-blue.svg)

A lightweight framework for friendly and functional Python scripting.

## Who is this For?

Py-Cli-Framework is for people looking for a quick place to start when creating simple Python scripts.  Frequently I found myself creating scripts to pull reports or automate tasks through REST APIs or from databases.  This project grew out of the pieces I found myself reusing over and over again to make my scripts usable by humans.

Projects like [Cement](https://builtoncement.com/) are a much more sophisticated solution, and seems to be for projects of a higher scale.  Py-Cli-Framework (PCF) is intended for small projects and scripts, while still providing a good foundation should your project grow.

## What's in the box?
- Your script is exposed as a command in your CLI once installed with `pip`
 - Check out [pyinstaller](http://www.pyinstaller.org/) if you want to include a Python runtime in your distribution package
- Pre-configured log handling and log rolling
- Pre-configured CLI argument handling
- Testing framework included.  Run from package root with `python setup.py test`
- Automated versioning with `bumpversion`

## Getting Started

1. Fork the git repository
1. Rename the folder, script, and values in `setup.py` and `MyScript/const.py`
1. Rename this file to something else, and name `YOUR_README.md` to `README.md`
1. Start scripting in `MyScript/myscript.py` (or whatever you decide to call it!)

## Resources
- [Bumpversion](https://github.com/peritus/bumpversion)
- [Argparse](https://docs.python.org/3/library/argparse.html)
- [Logging](https://docs.python.org/3/library/logging.html)


Last updated: 20 Jan 2019
