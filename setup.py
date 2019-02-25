import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="shadowray",
    version="0.1",
    author="RMT",
    author_email="d.rong@outlook.com",
    description="A useful client of v2ray for linux",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RMTT/Shadowray",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
