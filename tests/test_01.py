from spTimeHelperPy import TimeHelper


def test_1():
    obj = TimeHelper()

    arg1 = "blabla"
    assert obj.for_test_only(arg1) == arg1

