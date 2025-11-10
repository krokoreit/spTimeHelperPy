# spTimeHelperPy

[![PyPI - Version](https://img.shields.io/pypi/v/spTimeHelperPy.svg)](https://pypi.org/project/spTimeHelperPy)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/spTimeHelperPy.svg)](https://pypi.org/project/spTimeHelperPy)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


This package provides the Python module TimeHelper for easy conversion and handling of time values.




Enjoy

&emsp;krokoreit  
&emsp;&emsp;&emsp;<img src="https://github.com/krokoreit/spTimeHelperPy/blob/main/assets/krokoreit-01.svg?raw=true" width="140"/>


## Installation

```console
pip install spTimeHelperPy
```


## Usage & API

### TimeHelper Class
Import module:
```py
  from spTimeHelperPy import TimeHelper
```
TimeHelper objects need to be initiated with a target timezone (target_tz) for converting time values between UTC and target_tz. Additionally you can provide a time format string, e.g. '%Y-%m-%d %H:%M:%S.%f', which will be used as a default format by various methods.

As in most programs such information will be user specific and defined in a configuration file, TimeHelper uses ConfigParser to extract the values from a file, which contains entries like this:
```py
[TimeHelper]
# target time zone and format for converting time strings
target_tz = Europe/Berlin
# mask % in format with a leading %, i.e. %Y -> %%Y
time_format = %%Y-%%m-%%d %%H:%%M:%%S.%%fZ
```

When using a configuration file, a TimeHelper object is created with the name of the configuration file and an optional section name (defaults to 'TimeHelper'):
```py
  obj = TimeHelper('config.ini')
  obj = TimeHelper('config.ini', 'My TimeHelper Setting')
```

Alternatively, a TimeHelper object can also be created by directly providing target_tz and optionally time_string_format as keyword arguments:
```py
  obj = TimeHelper(target_tz="Europe/Paris")
  obj = TimeHelper(target_tz="Europe/Paris", time_string_format='%Y-%m-%dT%H:%M:%S.%fZ')
```



</br>

### API

#### Methods<a id="methods"></a>
* [aaa()](#aaa-method)  
* [bbb()](#bbb-method)  


#### aaa() Method<a id="aaa-method"></a>
```py
  get_zoneinfo_utc()
```



<div style="text-align: right"><a href="#methods">&#8679; back up to list of methods</a></div>


</br>

## License
MIT license  
Copyright &copy; 2025 by krokoreit
