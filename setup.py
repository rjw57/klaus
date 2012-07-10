# encoding: utf-8

import glob
from distutils.core import setup

from klaus import KLAUS_VERSION


def install_data_files_hack():
    # This is a clever hack to circumvent distutil's data_files
    # policy "install once, find never". Definitely a TODO!
    # -- https://groups.google.com/group/comp.lang.python/msg/2105ee4d9e8042cb
    from distutils.command.install import INSTALL_SCHEMES
    for scheme in INSTALL_SCHEMES.values():
        scheme['data'] = scheme['purelib']


install_data_files_hack()


setup(
    name='klaus',
    version=KLAUS_VERSION,
    author='Jonas Haag',
    author_email='jonas@lophus.org',
    packages=['klaus'],
    scripts=['bin/klaus'],
    data_files=[
        ['klaus/templates', glob.glob('klaus/templates/*')],
        ['klaus/static',    glob.glob('klaus/static/*')],
    ],
    url='https://github.com/jonashaag/klaus',
    license='2-clause BSD',
    description='The first Git web viewer that Just Works™.',
    long_description=__doc__,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
    ],
    install_requires=[
        'werkzeug',
        'Jinja2',
        'Pygments',
        'dulwich>=0.7.1' # FIXME
    ],
)

