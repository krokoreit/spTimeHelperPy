#   example01.py
#
#   file to demonstrate the use of spTimeHelperPy
#
#
import sys
import os
import time

from spTimeHelperPy import TimeHelper

from datetime import datetime

print("running Python executable from path", sys.executable)


f_path, f_ext = os.path.splitext(__file__)
f_head, f_tail = os.path.split(f_path)
file_path = f_head + os.sep

print('file_path', file_path)

use_config_file_name = file_path + "config.ini"
use_section_name = "TimeHelper"
use_target_tz = "Europe/Paris"
#use_time_string_format = "%Y-%m-%dT%H:%M:%S.%f%Z"
#use_time_string_format = '%Y-%m-%dT%H:%M:%S %Z'
use_time_string_format = "%Y-%m-%dT%H:%M:%S.%f"


th = TimeHelper(use_config_file_name)

# make methods for now()
#   - dt, ts and nsse for TZ and UTC


#print("TZ ", th.get_dtTZ())
#print("UTC", th.get_dtUTC())

print(time.tzname)


#dtTZ = th.get_dtTZ()
#dtTZ = datetime.fromtimestamp(4 * 60 * 60, th.get_zoneinfo_tz())
dtTZ = th.get_dtTZ_from_ts(4 * 60 * 60)
strTZ = dtTZ.strftime(use_time_string_format)
tsTZ = dtTZ.timestamp()

#dtTZ_u = th.get_dtUTC_from_strTZ(strTZ, use_time_string_format)
dtTZ_u = th.get_dtUTC_from_strTZ("", use_time_string_format)

tsTZ_u = dtTZ_u.timestamp()
print("TZ: ", dtTZ, strTZ, tsTZ, tsTZ_u)

dtUTC = th.get_dtUTC_from_strTZ(strTZ, use_time_string_format)
strUTC = dtUTC.strftime(use_time_string_format)
tsUTC = dtUTC.timestamp()
print("UTC:", dtUTC, strUTC, tsUTC)


