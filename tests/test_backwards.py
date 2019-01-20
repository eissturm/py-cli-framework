from argparse import Namespace

import MyScript.args as args
import MyScript.const as const
import MyScript.myscript as myscript
from types import ModuleType, FunctionType

def test_args():
    assert isinstance(args, ModuleType)

def test_args_are_args():
    assert isinstance(args.args, Namespace)

def test_startTime():
    assert isinstance(args.startTime, str)

def test_const():
    assert isinstance(const, ModuleType)
    assert const.LOG_MAX_SIZE
    assert const.LOG_MAX_NUM
    assert const.NAME
    assert const.COMMAND_NAME
    assert const.__version__

def test_myscrypt():
    assert isinstance(myscript, ModuleType)

def test_main():
    assert isinstance(myscript.main, FunctionType)
    assert myscript.main.__doc__
