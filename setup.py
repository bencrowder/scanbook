from distutils.core import setup

setup(
    name='scanbook',
    version='0.1',
    description='Process page images for easier reading',
    long_description=open('README.md').read(),
    url='https://github.com/bencrowder/scanbook',
    author='Ben Crowder',
    author_email='ben.crowder@gmail.com',
    license='MIT',
    packages=['scanbook'],
    entry_points={
        'console_scripts': ['scanbook=scanbook.cli:main'],
    },
    install_requires=[
        'click',
        'opencv-python',
        'scikit-image',
    ],
    zip_safe=False,
)
