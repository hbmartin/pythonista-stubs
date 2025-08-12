# Pythonista Stubs

[![PyPI](https://img.shields.io/pypi/v/pythonista-stubs.svg)](https://pypi.org/project/pythonista-stubs/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![CI](https://github.com/hbmartin/pythonista-stubs/actions/workflows/ci.yml/badge.svg)](https://github.com/hbmartin/pythonista-stubs/actions/workflows/ci.yml)


Stubs for the [Pythonista iOS API](https://omz-software.com/pythonista/lab/). This allows for better error detection and IDE / editor autocomplete.

## Installation and Usage

Install using your preferred package manager:

```bash
# Using uv (recommended)
uv add pythonista-stubs

# Using pip
pip install pythonista-stubs
```

You can now develop from your computer editor with proper typing and completions.

## API Coverage

| Module      | Status | Documentation |
| ----------- |--------|---------------|
| appex       | ✔      | [API Docs](https://omz-software.com/pythonista/docs-3.4/py3/ios/appex.html) |
| canvas      | WIP   | [API Docs](https://omz-software.com/pythonista/docs-3.4/py3/ios/canvas.html) |
| cb          | [WIP](https://github.com/hbmartin/pythonista-stubs/issues/7) | [API Docs](https://omz-software.com/pythonista/docs-3.4/py3/ios/cb.html) |
| clipboard   | ✔      | [API Docs](https://omz-software.com/pythonista/docs-3.4/py3/ios/clipboard.html) |
| console     | ✔      | [API Docs](https://omz-software.com/pythonista/docs-3.4/py3/ios/console.html) |
| contacts | ✔     | [API Docs](https://omz-software.com/pythonista/docs-3.4/py3/ios/contacts.html) |
| dialogs | ✔     | [API Docs](https://omz-software.com/pythonista/docs-3.4/py3/ios/dialogs.html) |
| editor      | ✔      | [API Docs](https://omz-software.com/pythonista/docs-3.4/py3/ios/editor.html) |
| keychain    | ✔     | [API Docs](https://omz-software.com/pythonista/docs-3.4/py3/ios/keychain.html) |
| linguistictagger | ✔     | [API Docs](https://omz-software.com/pythonista/docs-3.4/py3/ios/linguistictagger.html) |
| location    | ✔     | [API Docs](https://omz-software.com/pythonista/docs-3.4/py3/ios/location.html) |
| motion      | ✔     | [API Docs](https://omz-software.com/pythonista/docs-3.4/py3/ios/motion.html) |
| notification   | ✔     | [API Docs](https://omz-software.com/pythonista/docs-3.4/py3/ios/notification.html) |
| objc_util   | [WIP](https://github.com/hbmartin/pythonista-stubs/issues/7) | [API Docs](https://omz-software.com/pythonista/docs-3.4/py3/ios/objc_util.html) |
| photos      | ✔     | [API Docs](https://omz-software.com/pythonista/docs-3.4/py3/ios/photos.html) |
| reminders   | ✔      | [API Docs](https://omz-software.com/pythonista/docs-3.4/py3/ios/reminders.html) |
| scene       | [✘](https://github.com/hbmartin/pythonista-stubs/issues/9) | [API Docs](https://omz-software.com/pythonista/docs-3.4/py3/ios/scene.html) |
| sound       | ✔      | [API Docs](https://omz-software.com/pythonista/docs-3.4/py3/ios/sound.html) |
| speech      | ✔      | [API Docs](https://omz-software.com/pythonista/docs-3.4/py3/ios/speech.html) |
| twitter     | ✘      | [API Docs](https://omz-software.com/pythonista/docs-3.4/py3/ios/twitter.html) |
| ui          | [WIP](https://github.com/hbmartin/pythonista-stubs/issues/6) | [API Docs](https://omz-software.com/pythonista/docs-3.4/py3/ios/ui.html) |

## Built With

* [mypy](http://mypy-lang.org/)
* [Typing Extensions](https://github.com/python/typing/tree/master/typing_extensions)

## PEPs

* [PEP 484  -- Type Hints](https://www.python.org/dev/peps/pep-0484/)
* [PEP 561  -- Distributing and Packaging Type Information](https://www.python.org/dev/peps/pep-0561/)
* [PEP 3107 -- Function Annotations](https://www.python.org/dev/peps/pep-3107/)

## Troubleshooting

### Type Checker Not Finding Stubs
- **VSCode**: Ensure the Python extension is using the correct interpreter where pythonista-stubs is installed
- **PyCharm**: Check that the stub package appears in your project's external libraries
- **mypy**: Make sure mypy can find the stubs in your Python path

### Import Errors in IDE
- Verify pythonista-stubs is installed in the same environment as your project
- Try restarting your IDE after installation
- Check that your IDE is using the correct Python interpreter

## Contributing

Please [file a bug report](https://github.com/hbmartin/pythonista-stubs/issues) for any issues you find. Even more excellent than a good bug report is a fix for a bug, or the implementation of a much-needed stub. We'd love to have your contributions.

### Code of Conduct

Everyone participating in this community is expected to treat other people with respect and more generally to follow the guidelines articulated in the [Python Community Code of Conduct](https://www.python.org/psf/codeofconduct/).

## Authors

* [Harold Martin](https://www.linkedin.com/in/harold-martin-98526971/) - harold.martin at gmail
* [Dmytro Yaroshenko](https://github.com/o-murphy)


## Disclaimer

This is not an official project and is not associated with omz:software

## License

[Apache License 2.0](LICENSE)
