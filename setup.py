import setuptools

setuptools.setup(
    name='scanbook-bencrowder',
    version='0.1.0',
    description='Tool that processes page images for easier reading',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/bencrowder/scanbook',
    author='Ben Crowder',
    author_email='ben.crowder@gmail.com',
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': ['scanbook=scanbook.cli:main'],
    },
    install_requires=[
        'click',
        'opencv-python',
        'scikit-image',
    ],
    zip_safe=False,
    python_requires='>=3.6',
)
