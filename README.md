# Pythonista Stubs

[![PyPI](https://img.shields.io/pypi/v/pythonista-stubs.svg)](https://pypi.org/project/pythonista-stubs/)
[![GitHub issues](https://img.shields.io/github/issues-raw/hbmartin/pythonista-stubs.svg)](https://github.com/hbmartin/pythonista-stubs/issues)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Build Status](https://travis-ci.com/hbmartin/pythonista-stubs.svg?branch=master)](https://travis-ci.com/hbmartin/pythonista-stubs)


Stubs for the [Pythonista iOS API](http://omz-software.com/pythonista/docs/ios/). This allows for better error detection and IDE / editor autocomplete.

## Installation and Usage

```
pip install pythonista-stubs --upgrade
```
N.b. you may need to `pip3`, particularly if you installed python3 with homebrew

Type checking can then be performed with [mypy](https://mypy.readthedocs.io/en/latest/command_line.html)


* [PyCharm](https://www.jetbrains.com/help/pycharm/type-hinting-in-product.html#stub): Works immediately
* Vim: [vim-mypy](https://github.com/Integralist/vim-mypy)
* Emacs: using [Flycheck](https://github.com/flycheck/) and [Flycheck-mypy](https://github.com/lbolla/emacs-flycheck-mypy)
* Sublime Text: [SublimeLinter-contrib-mypy](https://github.com/fredcallaway/SublimeLinter-contrib-mypy)
* Atom: [linter-mypy](https://atom.io/packages/linter-mypy)
* VS Code: provides [basic integration](https://code.visualstudio.com/docs/python/linting#_mypy) with mypy.
* flake8: [flake8-mypy](https://github.com/ambv/flake8-mypy)

See also: [mypy integrations](https://github.com/python/mypy#ide--linter-integrations)

## API Coverage

| Module      | Status |
| ----------- |--------|
| appex       | ✔      |
| canvas      | ✘      |
| cb          | ✘      |
| clipboard   | ✔      |
| console     | ✔      |
| dialogs     | ✘      |
| contacts    | ✘      |
| editor      | ✘      |
| keychain    | ✘      |
| linguistictagger | ✘      |
| location    | ✘      |
| motion      | ✘      |
| notification   | ✘      |
| objc_util   | ✘      |
| photos      | ✘      |
| reminders   | ✔      |
| scene       | ✘      |
| sound       | ✔      |
| speech      | ✔      |
| twitter     | ✘      |
| ui          | ✘      |

## Built With

* [mypy](http://mypy-lang.org/)
* [Typing Extensions](https://github.com/python/typing/tree/master/typing_extensions)

## PEPs

* [PEP 484  -- Type Hints](https://www.python.org/dev/peps/pep-0484/)
* [PEP 561  -- Distributing and Packaging Type Information](https://www.python.org/dev/peps/pep-0561/)
* [PEP 3107 -- Function Annotations](https://www.python.org/dev/peps/pep-3107/)

## Contributing

Please [file a bug report](https://github.com/hbmartin/pythonista-stubs/issues) for any issues you find. Even more excellent than a good bug report is a fix for a bug, or the implementation of a much-needed stub. We'd love to have your contributions.

We use the usual GitHub pull-request flow, which may be familiar to
you if you've contributed to other projects on GitHub.  For the
mechanics, see [Mypy's git and GitHub workflow help page](https://github.com/python/mypy/wiki/Using-Git-And-GitHub),
or [GitHub's own documentation](https://help.github.com/articles/using-pull-requests/).

### Code Formatting

This project is linted with [pyflakes](https://github.com/PyCQA/pyflakes) and makes strict use of [Black](https://github.com/ambv/black) for code formatting.

### Conventions

* long functions and methods should be split up with one argument per line
* all function bodies should be empty
* prefer ``...`` over ``pass``
* prefer ``...`` on the same line as the class/function signature
* avoid vertical whitespace between consecutive module-level functions, names, or methods and fields within a single class
* use a single blank line between top-level class definitions
* do not use docstrings
* use variable annotations instead of type comments
* for arguments with a type and a default, use spaces around the `=`
* use `float` instead of `Union[int, float]`
* avoid Union return types: https://github.com/python/mypy/issues/1693
* imports in stubs are considered private unless they use the form ``from library import name as name``
* avoid using the `Any` type when possible
* type variables and aliases for legibility reasons should be prefixed with an underscore to make it obvious to the reader they are not part of the stubbed API.
* these conventions derived from [typeshed](https://github.com/python/typeshed/blob/master/CONTRIBUTING.md#conventions)

### Code of Conduct

Everyone participating in this community is expected to treat other people with respect and more generally to follow the guidelines articulated in the [Python Community Code of Conduct](https://www.python.org/psf/codeofconduct/).

## Authors

* [Harold Martin](https://www.linkedin.com/in/harold-martin-98526971/) - harold.martin at gmail


## Disclaimer

This is not an official project and is not associated with omz:software

## License

[Apache License 2.0](LICENSE.txt)
