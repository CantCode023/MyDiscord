import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup_info = {
    "name": "mydiscord",
    "version": "1.0.0",
    "author": "CantCode",
    "author_email": "cantcode023@gmail.com",
    "description": "MyDiscord, Control your Discord client with Python.",
    "long_description": long_description,
    "long_description_content_type": "text/markdown",
    "url": "https://github.com/CantCode023/MyDiscord",
    "packages": setuptools.find_packages(),
    "classifiers": [
        "Programming Language :: Python :: 3",
    ],
    "python_requires": '>=3.7',
    "install_requires": [
        "requests==2.26.0"
    ]
}


setuptools.setup(**setup_info)