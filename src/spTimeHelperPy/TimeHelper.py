# ================================================================================
#
#   TimeHelper class
#
#   object for .....
#
#   MIT License
#
#   Copyright (c) 2024 krokoreit (krokoreit@gmail.com)
#
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#   of this software and associated documentation files (the "Software"), to deal
#   in the Software without restriction, including without limitation the rights
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#   copies of the Software, and to permit persons to whom the Software is
#   furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in all
#   copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#   SOFTWARE.
#
# ================================================================================

import os
from datetime import datetime
from zoneinfo import ZoneInfo
import configparser


class TimeHelper:
    #def __init__(self):
    #    pass

    def __init__(self, config_file_name=None, section_name=None, *, target_tz=None, time_string_format=None):

        err_class_prefix = self.__class__.__name__ + '():'
        err_bad_argument = err_class_prefix + " invalid %s argument."
        err_empty_string = err_class_prefix + " argument %s is an empty string."
        
        # default section_name
        if section_name is None:
            section_name = "TimeHelper"
        # default timezone
        if target_tz is None:
            #target_tz = 'Europe/Berlin'
            target_tz = 'Europe/Paris'
        # defaults time string format
        if time_string_format is None:
            time_string_format = "%Y-%m-%dT%H:%M:%S.%fZ"

        if config_file_name is not None and section_name is not None:
            if not isinstance(config_file_name, str):
                raise TypeError (err_bad_argument % "config_file_name")
            if len(config_file_name) == 0:
                raise ValueError (err_empty_string % "config_file_name")
            if not os.path.isfile(config_file_name):
                raise ValueError (err_class_prefix + " config file '" + config_file_name + "' does not exist.")
            
            if not isinstance(section_name, str):
                raise TypeError (err_bad_argument % "section_name")
            if len(section_name) == 0:
                raise ValueError (err_empty_string % "section_name")

            config = configparser.ConfigParser(inline_comment_prefixes='#', empty_lines_in_values=False)
            config.read(config_file_name)
            if config.has_section(section_name):
                target_tz = config[section_name].get('target_tz', target_tz)
                time_string_format = config[section_name].get('time_format', time_string_format)
            else:
                raise ValueError (err_class_prefix + " section '" + section_name + "' does not exist in '" + config_file_name + "'.")
        else:
            # non-config-file setup must give needed keyword-only parameters
            if not isinstance(target_tz, str):
                raise TypeError (err_bad_argument % "target_tz")
            if len(target_tz) == 0:
                raise ValueError (err_empty_string % "target_tz")
            if not isinstance(time_string_format, str):
                raise TypeError (err_bad_argument % "time_string_format")
            if len(time_string_format) == 0:
                raise ValueError (err_empty_string % "time_string_format")
        
        print(config_file_name, section_name, target_tz, time_string_format)

        try:
            self._target_tz = ZoneInfo(target_tz)
        except Exception as e:
            raise ValueError(err_bad_argument % "target_tz" + " " + str(e))
        
        self._utc = ZoneInfo("UTC")
        self._time_string_format = time_string_format

    def _get_time_string_format(self, fmt=None):
        """Internal method to use fallback time string format (default or '%Y-%m-%d %H:%M:%S.%f')"""
        if fmt == None or not isinstance(fmt, str):
            fmt = self._time_string_format
            if fmt == None:
                fmt = '%Y-%m-%d %H:%M:%S.%f'
        return fmt


    # -----------------------------------------------------------------------------
    # target timezone
    # -----------------------------------------------------------------------------

    def get_dtTZ(self):
        """Returns the current timezone datetime, aka now."""

        return datetime.now(self._target_tz)

    def get_dtTZ_from_strTZ(self, strTZ, time_string_format=None, second_hour=False):
        """Returns a timezone datetime from a timezone time string. For an ambigious case when switching 
        back to normal time in autumn (times for one hour occuring twice), use second_hour to 
        convert into datetime for the second occurance."""

        if not isinstance(strTZ, str):
            raise TypeError("get_dtTZ_from_strTZ() called with strTZ not being a string.)")
        if len(strTZ) == 0:
            raise ValueError("get_dtTZ_from_strTZ() called with empty strTZ.)")
        # get format
        fmt = self._get_time_string_format(time_string_format)
        # create naive datetime, i.e. based on time string without 'local'
        dt = datetime.strptime(strTZ, fmt)
        # make tz aware datetime for timezone and second_hour
        if second_hour:
            return dt.replace(tzinfo=self._target_tz, fold=1)
        else:
            return dt.replace(tzinfo=self._target_tz, fold=0)


    def get_dtTZ_from_strUTC(self, strUTC, time_string_format=None):
        """Returns a timezone datetime from an UTC time string."""

        if not isinstance(strUTC, str):
            raise TypeError("get_dtTZ_from_strUTC() called with strUTC not being a string.)")
        if len(strTZ) == 0:
            raise ValueError("get_dtTZ_from_strUTC() called with empty strUTC.)")
        # make tz aware datetime for UTC
        dt = self.get_dtUTC_from_strUTC(strUTC, time_string_format)
        # convert to local
        return dt.astimezone(self._target_tz)
    
    
    def get_dtTZ_from_ts(self, timestamp):
        if not isinstance(timestamp, int):
            raise TypeError("get_dtTZ_from_ts() called with timestamp not being an integer.)")
        return datetime.fromtimestamp(timestamp, self._target_tz)

    def get_dtTZ_from_SSE(self, sse):
        pass

    def get_dtTZ_from_NSSE(self, nsse):
        pass



    # -----------------------------------------------------------------------------
    # nano seconds since epoch
    # -----------------------------------------------------------------------------

    def get_nsse_from_strUTC(self, strUTC, time_string_format=None):
        """Returns nano seconds since epoch from an UTC time string."""
        
        if not isinstance(strUTC, str):
            raise TypeError("get_nsse_from_strUTC() called with strUTC not being a string.)")
        if len(strTZ) == 0:
            raise ValueError("get_nsse_from_strUTC() called with empty strUTC.)")
        dt = self.get_dtUTC_from_strUTC(strUTC, time_string_format)
        return int(dt.timestamp() * 1000000000)



    # -----------------------------------------------------------------------------
    # UTC
    # -----------------------------------------------------------------------------

    def get_dtUTC(self):
        """Returns the current UTC datetime, aka now."""

        return datetime.now(self._utc)
    

    def get_dtUTC_from_strTZ(self, strTZ, time_string_format=None, second_hour=False):
        """Returns an UTC datetime from a timezone time string. For an ambigious case when switching 
        back to normal time in autumn (times for one hour occuring twice), use second_hour to 
        convert into datetime for the second occurance."""
        
        if not isinstance(strTZ, str):
            raise TypeError("get_dtUTC_from_strTZ() called with strTZ not being a string.)")
        if len(strTZ) == 0:
            raise ValueError("get_dtUTC_from_strTZ() called with empty strTZ.)")
        dt = self.get_dtTZ_from_strTZ(strTZ, time_string_format, second_hour)
        return dt.astimezone(self._utc)


    def get_dtUTC_from_strUTC(self, strUTC, time_string_format=None):
        """Returns an UTC datetime from an UTC time string."""

        if not isinstance(strUTC, str):
            raise TypeError("get_dtUTC_from_strUTC() called with strUTC not being a string.)")
        if len(strTZ) == 0:
            raise ValueError("get_dtUTC_from_strUTC() called with empty strUTC.)")
        # get format
        fmt = self._get_time_string_format(time_string_format)
        # create naive datetime, i.e. based on time string without 'local'
        dt = datetime.strptime(strUTC, fmt)
        # make tz aware datetime for UTC
        return dt.replace(tzinfo=self._utc)

    # -----------------------------------------------------------------------------
    # zoneinfo
    # -----------------------------------------------------------------------------

    def get_zoneinfo_utc(self):
        """Return TzInfo for UTC."""
        return self._utc

    def get_zoneinfo_tz(self):
        """Return TzInfo for target timezone"""
        return self._target_tz


    # -----------------------------------------------------------------------------
    # to sort out:
    # -----------------------------------------------------------------------------

    # make sse
    def dt_2_rounded_ts(self, dt):
        """Return rounded timestamp from datetime."""
        f_ts = dt.timestamp()
        i_ts = int(f_ts)
        if f_ts - i_ts > 0.5:
            i_ts += 1
        return i_ts

    # make nsse
    def time_ns_2_utc_dt(self, time_ns=0):
        """Return UTC datetime from nano seconds since epoch."""
        ts = time_ns / 1000000000
        dt = datetime.fromtimestamp(ts)
        return dt.astimezone(self._utc)

    def time_ns_2_tz_dt(self, time_ns=0):
        """Return timezone datetime from nano seconds since epoch."""
        ts = time_ns / 1000000000
        dt = datetime.fromtimestamp(ts)
        return dt.astimezone(self._target_tz)


    def datetime_from_time_ns(self, time_ns = 0):
        """Create datetime from time_ns"""
        return datetime.fromtimestamp(float(time_ns / 1000000000))

    def get_time_ns(self, from_text, time_string_format=None):
        """Tries to return a time_ns integer from text given as either a UTC datetime string or
        a text with nano seconds since epoch. Raises error if both conversions fail."""
        try:
            dt = self.utc_str_2_utc_dt(from_text, time_string_format)
            return int(dt.timestamp() * 1000000000)
        except Exception as e:
            pass
        try:
            vInt = int(from_text)
            if str(vInt) == from_text:
                return vInt
        except Exception as e:
            pass
        raise Exception("Error getting time_ns from '" + from_text + "'")
