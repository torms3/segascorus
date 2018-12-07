from Cython.Build import cythonize
from distutils.sysconfig import get_python_inc
from setuptools import setup, Extension

import numpy
import os


include_dirs = [
    './segascorus',
    os.path.dirname(get_python_inc()),
    numpy.get_include(),
]


extensions = [
    Extension( "segascorus.global_vars",
              ["segascorus/global_vars.pyx"]),
    Extension( "segascorus.data_prep_u",
              ["segascorus/data_prep_u.pyx"]),
    Extension( "segascorus.metrics_u",
              ["segascorus/metrics_u.pyx"]),
    Extension( "segascorus.repres_u",
              ["segascorus/repres_u.pyx"],
              language="c++",
              extra_compile_args=["-std=c++11"]),
]


setup(
    name='segascorus',
    version='0.0.1',
    packages=['segascorus'],
    package_data={
        '': [
            'segascorus/*.c',
            'segascorus/*.cpp',
            'segascorus/*.pyx',
        ]
    },
    include_package_data=True,
    ext_modules = cythonize(extensions),
    include_dirs=include_dirs
)
