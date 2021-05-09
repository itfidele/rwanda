import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rwanda",  # Replace with your own username
    version="0.2.1",
    author="Fidele Kirezi Cyisa",
    author_email="itfidele@gmail.com",
    description="Python Package to extract everything you can need in rwanda.",
    long_description='Python Package to extract everything you can need in rwanda. You can use',
    long_description_content_type="text/markdown",
    url="https://github.com/fidele000rwanda/",
    project_urls={
        "Bug Tracker": "https://github.com/fidele000/rwanda/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "rwanda"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
