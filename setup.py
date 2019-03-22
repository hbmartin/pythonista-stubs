from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

packages = ["appex", "clipboard", "console", "reminders"]
packages_stubs = [p + "-stubs" for p in packages]
package_dir = {p + "-stubs": path.join("stubs", p) for p in packages}
package_data = {ps: ["__init__.pyi"] for ps in packages_stubs}

setup(
    name="pythonista-stubs",
    version="0.0.2",
    description="A collection of Pythonista stub files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hbmartin/pythonista-stubs",
    package_dir=package_dir,
    packages=packages_stubs,
    package_data=package_data,
    install_requires=["typing_extensions", "mypy", "Pillow"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: iOS",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Typing :: Typed",
    ],
    license="Apache License 2.0",
    keywords="pythonista stubs ios ide",
    project_urls={"Bug Reports": "https://github.com/hbmartin/pythonista-stubs/issues"},
)
