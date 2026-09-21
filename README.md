# Powertrace Hooks
[![PyPI version](https://badge.fury.io/py/powertrace-hooks.svg)](https://badge.fury.io/py/powertrace-hooks)
![PyPI downloads](https://img.shields.io/pypi/dm/powertrace-hooks)
![Python version](https://img.shields.io/badge/python-3.11+-brightgreen)
![Operating system](https://img.shields.io/badge/os-linux%20%7c%20macOS%20%7c%20windows-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

Enables [powertrace](https://github.com/quintenroets/powertrace)'s improved rich tracebacks
in every Python process, without additional code. Interpreter startup overhead is less than
1%, since nothing is imported until an exception occurs.

![example](https://github.com/quintenroets/powertrace/blob/main/assets/examples/visualization.png?raw=true)

## Installation
```shell
pip install powertrace-hooks
```
