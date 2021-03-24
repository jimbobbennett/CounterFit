from setuptools import find_packages, setup

setup(
    name='virtualiot_shims_grove',
    packages=find_packages(include=['virtualiot_shims_grove']),
    version='0.1.0',
    description='Shims for the Seeed Grove sensors for the VirtualIoT device app',
    author='Jim Bennett',
    license='MIT',
    install_requires=['requests'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)