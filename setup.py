import os
from setuptools import find_packages, setup
from distutils.util import convert_path

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

main_ns = {}
ver_path = convert_path('django_polymer_template/version.py')
with open(ver_path) as ver_file:
    exec (ver_file.read(), main_ns)

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-polymer-template',
    version=main_ns['__version__'],
    packages=find_packages(),
    include_package_data=True,
    license='Apache 2.0 License',  # example license
    description='Django template for Polymer applications.',
    long_description=README,
    url='https://github.com/lordoftheflies/django-polymer-template/',
    author='lordoftheflies',
    author_email='laszlo.hegedus@cherubits.hu',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.10',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Database',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: System :: Monitoring',
        'Development Status :: 2 - Pre-Alpha'
    ],
    install_requires=[
        'django',
        'dj-database-url',
        'django-material',
        'uwsgi',
        'django-configurations',
        'django-debug-toolbar',
        'django-dotenv',
        'django-extensions',

    ],
    # tests_require=[
    #     "Werkzeug"
    # ]
)
