from setuptools import setup, find_packages

setup(
    name='DataSpyre',
    version='0.2.8',
    description=(
        'Spyre makes it easy to build interactive web applications,'
        'and requires no knowledge of HTML, CSS, or Javascript.'
    ),
    url='https://github.com/adamhajari/spyre',
    author='Adam Hajari',
    author_email='adam@nextbigsound.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: CherryPy',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Environment :: Web Environment',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='web application template data visualization',
    include_package_data=True,
    packages=['spyre'],
    package_data={
        '': ['*.js', '*.css', '*.html'],
        'public': ['js/*.js', 'css/*.css'],
    },
    install_requires=[
        "six>=1.11.0",
        "numpy",
        "pandas",
        "cherrypy",
        "jinja2",
        "matplotlib",
    ]
)


