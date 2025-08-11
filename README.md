# Pythonista Stubs

[![PyPI](https://img.shields.io/pypi/v/pythonista-stubs.svg)](https://pypi.org/project/pythonista-stubs/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![CI](https://github.com/hbmartin/pythonista-stubs/actions/workflows/ci.yml/badge.svg)](https://github.com/hbmartin/pythonista-stubs/actions/workflows/ci.yml)



Stubs for the [Pythonista iOS API](http://omz-software.com/pythonista/docs/ios/). This allows for better error detection and IDE / editor autocomplete.

## Installation and Usage

```
uv add pythonista-stubs
```
You can now develop from your computer editor with proper typing and completinos.

## API Coverage

| Module      | Status |
| ----------- |--------|
| appex       | ✔      |
| canvas      | WIP   |
| cb          | [WIP](https://github.com/hbmartin/pythonista-stubs/issues/7) |
| clipboard   | ✔      |
| console     | ✔      |
| contacts | ✔     |
| dialogs | ✔     |
| editor      | ✔      |
| keychain    | ✔     |
| linguistictagger | ✔     |
| location    | ✔     |
| motion      | ✔     |
| notification   | ✔     |
| objc_util   | [WIP](https://github.com/hbmartin/pythonista-stubs/issues/7) |
| photos      | ✔     |
| reminders   | ✔      |
| scene       | [✘](https://github.com/hbmartin/pythonista-stubs/issues/9) |
| sound       | ✔      |
| speech      | ✔      |
| twitter     | ✘      |
| ui          | [WIP](https://github.com/hbmartin/pythonista-stubs/issues/6) |

## Built With

* [mypy](http://mypy-lang.org/)
* [Typing Extensions](https://github.com/python/typing/tree/master/typing_extensions)

## PEPs

* [PEP 484  -- Type Hints](https://www.python.org/dev/peps/pep-0484/)
* [PEP 561  -- Distributing and Packaging Type Information](https://www.python.org/dev/peps/pep-0561/)
* [PEP 3107 -- Function Annotations](https://www.python.org/dev/peps/pep-3107/)

## Contributing

Please [file a bug report](https://github.com/hbmartin/pythonista-stubs/issues) for any issues you find. Even more excellent than a good bug report is a fix for a bug, or the implementation of a much-needed stub. We'd love to have your contributions.

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
* [Dmytro Yaroshenko](https://github.com/o-murphy)


## Disclaimer

This is not an official project and is not associated with omz:software

## License

[Apache License 2.0](LICENSE.txt)
