import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="numberize",
    version="0.0.2",
    author="YemchenkoDS",
    author_email="emchenko@dlit.dp.ua",
    description="Replace numerals with numbers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DanATW/numberize.git",
    project_urls={
        "Bug Tracker": "https://github.com/DanATW/numberize/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(include=["numberize"]),
    python_requires=">=3.6",
    install_requires=['pymorphy2'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==6.2.4'],
    test_suite='test'
)
