from spTimeHelperPy import TimeHelper

import os

f_path, f_ext = os.path.splitext(__file__)
f_head, f_tail = os.path.split(f_path)
file_path = f_head + os.sep

use_config_file_name = file_path + "config.ini"
use_section_name = "My TimeHelper Setting"
use_target_tz = "Europe/Paris"
use_time_string_format = '%Y-%m-%dT%H:%M:%S.%fZ'

bad_config_file_name = file_path + "bad_config.ini"
bad_section_name = "BadTimeHelper"
bad_target_tz = "Hamburg"
bad_time_string_format = '%A-%A-%dT%H:%M:%S.%fZ'


def test_01():
    # "with config and section
    try:
        th = TimeHelper(use_config_file_name, use_section_name)
    except Exception as e:
        assert False, "Got an exception " + str(e)

def test_01A():
    # "with config and no section
    try:
        th = TimeHelper(use_config_file_name)
    except Exception as e:
        assert False, "Got an exception " + str(e)

def test_02():
    # "with config and section
    try:
        th = TimeHelper(use_config_file_name, bad_section_name)
    except ValueError as e:
        assert True
    except Exception as e:
        assert False, "Got an exception " + str(e)

def test_03():
    # "with config and section
    try:
        th = TimeHelper(bad_config_file_name, use_section_name)
    except ValueError as e:
        assert True
    except Exception as e:
        assert False, "Got an exception " + str(e)

def test_04():
    # "with config and section
    try:
        th = TimeHelper(33, use_section_name)
    except TypeError as e:
        assert True
    except Exception as e:
        assert False, "Got an exception " + str(e)

def test_05():
    # "with target_tz
    try:
        th = TimeHelper(target_tz=use_target_tz)
    except TypeError as e:
        assert True
    except Exception as e:
        assert False, "Got an exception " + str(e)

def test_06():
    # "with target_tz
    try:
        th = TimeHelper(target_tz=bad_target_tz)
    except ValueError as e:
        assert True
    except Exception as e:
        assert False, "Got an exception " + str(e)

def test_07():
    # "with target_tz
    try:
        th = TimeHelper(target_tz=55)
    except TypeError as e:
        assert True
    except Exception as e:
        assert False, "Got an exception " + str(e)
