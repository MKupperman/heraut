import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="heraut-mkupperman", # Replace with your own username
    version="0.0.1",
    author="Michael Kupperman",
    author_email="kupperma@uw.edu",
    description="The herald of python message passing between threads and processes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mkupperman/heraut",
    project_urls={
        "Bug Tracker": "https://github.com/mkupperman/heraut/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "heraut"},
    packages=setuptools.find_packages(where="heraut"),
    python_requires=">=3.6",
)
