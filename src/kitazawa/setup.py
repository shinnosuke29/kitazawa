from setuptools import setup

package_name = 'kitazawa'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kitazawa',
    maintainer_email='your_email@example.com',
    description='Example ROS2 package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'temperature_simulator = kitazawa.temperature_simulator:main',
            'temperature_publisher = kitazawa.temperature_publisher:main',
        ],
    },
)

