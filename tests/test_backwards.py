import MyScript.args as args
import MyScript.const as const
import MyScript.myscript as myscript
from types import ModuleType, FunctionType

def test_args():
    assert isinstance(args, ModuleType)

def test_const():
    assert isinstance(const, ModuleType)

def test_myscrypt():
    assert isinstance(myscript, ModuleType)

def test_main():
    assert isinstance(myscript.main, FunctionType)
    assert myscript.main.__doc__
