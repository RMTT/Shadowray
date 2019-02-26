import setuptools
from shadowray.config.version import VERSION_ID

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="shadowray",
    version=VERSION_ID,
    author="RMT",
    author_email="d.rong@outlook.com",
    description="A useful client of v2ray for linux",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RMTT/Shadowray",
    packages=setuptools.find_packages(),
    keywords=("pip", "v2ray", "shadowsocks", "shadowray"),
    install_requires=["requests"],
    python_requires='>=3',
    license="MIT",
    platform=['any'],
    project_urls={
        'Tracker': 'https://github.com/RMTT/Shadowray/issues',
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    entry_points={
        'console_scripts': [
            'shadowray=shadowray:main',
        ],
    },
)
