import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rwanda", # Replace with your own username
    version="0.1.2",
    author="Fidele Kirezi Cyisa",
    author_email="itfidele@gmail.com",
    description="Python Package to extract everything you can need in rwanda",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fidele000/rwanda",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)