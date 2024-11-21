# Powertrace Hooks
[![PyPI version](https://badge.fury.io/py/powertrace-hooks.svg)](https://badge.fury.io/py/powertrace-hooks)
![PyPI downloads](https://img.shields.io/pypi/dm/powertrace-hooks)
![Python version](https://img.shields.io/badge/python-3.10+-brightgreen)
![Operating system](https://img.shields.io/badge/os-linux%20%7c%20macOS%20%7c%20windows-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

Detailed stack trace logging and visualization:
* Rich traceback visualization
* Also works for headless scripts
* Stacktrace logging
* Easily reproducible visualization

![example](https://github.com/quintenroets/powertrace/blob/main/assets/examples/visualization.png?raw=true)

## Installation
Run
```shell
pip install powertrace-hooks
```
to enable automated detailed stack trace logging and visualization for all Python scripts.

## Usage
Run
```python
import powertrace

powertrace.visualize_traceback()
```
To explicitly visualize the current traceback.
