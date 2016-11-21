# -*- coding: utf-8 -*-
import os
from setuptools import setup


f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()

setup(
    name='wagtail-redactor',
    version='0.5.3',
    description='Imperavi Redactor for WagtailCMS',
    long_description=readme,
    author='Melfi Silver',
    author_email='diveru4i@gmail.com',
    url='https://github.com/diveru4i/wagtail-redactor',
    license='MIT',
    packages=['wagtail_redactor'],
    include_package_data=True,
    install_requires=['setuptools'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    keywords='django,admin,wysiwyg,editor,redactor,redactorjs,wagtail,wagtailcms',
)
