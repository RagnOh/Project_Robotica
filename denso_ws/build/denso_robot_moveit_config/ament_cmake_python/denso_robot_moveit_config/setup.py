from setuptools import find_packages
from setuptools import setup

setup(
    name='denso_robot_moveit_config',
    version='0.3.0',
    packages=find_packages(
        include=('denso_robot_moveit_config', 'denso_robot_moveit_config.*')),
)
