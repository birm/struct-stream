from distutils.core import setup

setup(
    name='StructStream',
    author_email='birm@rbirm.us',
    author='Ryan Birmingham',
    description='Save stream xml or json information for easy usage, keep size under control, use key constraints, and summarize your data.',
    url="http://rbirm.us/struct-stream",
    version='0.3',
    packages=['sstream'],
    license='none, to be added on alpha release',
    long_description=open('README.txt').read(),
    install_requires=[
        "xmltodict",
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Internet :: Log Analysis",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3",
    ],
)
