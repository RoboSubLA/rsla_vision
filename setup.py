from setuptools import find_packages, setup

package_name = 'rsla_vision'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pererry',
    maintainer_email='pererry@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'rsla_vision = rsla_vision.rsla_vision:main',
            'rsla_vision_record = rsla_vision.rsla_vision_record:main'
        ],
    },
)
