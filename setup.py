from setuptools import find_packages, setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='percentiles',
    use_scm_version=True,
    description="Get percentile of sequence without numpy",
    keywords=['percentile', 'statistics'],
    url="https://github.com/heaviss/percentiles",
    author="Vladimir Seregin",
    author_email="31631@rambler.ru",
    license="MIT",
    packages=find_packages(),
    install_requires=[],
    setup_requires=[
        'setuptools_scm',
    ],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
)
