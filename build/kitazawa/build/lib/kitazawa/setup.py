from setuptools import setup

package_name = 'kitazawa'

setup(
    name=package_name,
    version='0.0.0',
    packages=['kitazawa'],
    py_modules=['kitazawa.temperature_publisher'],
    install_requires=['setuptools'],
    zip_safe=True,
    author='kitazawa',
    author_email='shinnosuke.2511@icloud.com',
    maintainer='kitazawa',
    maintainer_email='shinnosuke.2511@icloud.com',
    description='Temperature Publisher',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'temperature_publisher = kitazawa.temperature_publisher:main',
        ],
    },
)
