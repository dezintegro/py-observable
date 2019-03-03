import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-observable",
    version="0.0.1",
    description="Observable collections that supports change notification",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="dezintegro",
    author_email="dezintegro@gmail.com",
    license="MIT",
    download_url="https://github.com/dezintegro/py-observable",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
    ),
)
