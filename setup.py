from setuptools import find_packages, setup

setup(
    name='k8s',
    version='0.1',
    description='Netbox plugin for Kubernetes objects and their teams',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)