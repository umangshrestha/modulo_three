import modulo_three


def test_version():
    assert modulo_three.__version__ is not None
    assert isinstance(modulo_three.__version__, str)