# Maya Test
[![Build Status](https://travis-ci.org/arubertoson/mayatest.svg?branch=master)](https://travis-ci.org/arubertoson/mayatest)
[![Coverage Status](https://coveralls.io/repos/github/arubertoson/mayatest/badge.svg?branch=master)](https://coveralls.io/github/arubertoson/mayatest?branch=master)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/arubertoson/mayatest/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/arubertoson/mayatest/?branch=master)
[![PyPI version](https://badge.fury.io/py/mayatest.svg)](https://badge.fury.io/py/mayatest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Wrapper to easily test maya scripts and modules with the powerful pytest framework.

## Getting Started

### Prerequisites

You'll need to install:
* Autodesk Maya (2014+)
* Python (2.7+)


### Installing

```bash
pip install mayatest
```

### Usage

Run mayatest in the folder of the script or module.

```bash
# To invoke pytest using mayapy from Maya 2017 do:
mayatest -m 2017

# Then the normal usage for pytest applies, e.g. to test specific  file:
mayatest -m 2017 --pytest="test_sometest.py"
# to only run test_func
mayatest -m 2017 --pytest="test_sometest.py::test_func"
# to get verbose results, you can include pytest flags
mayatest -m 2017 --pytest="-vvv test_sometest.py"
```

For more information using pytest go to their [docs](https://docs.pytest.org/en/latest/usage.html).


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
