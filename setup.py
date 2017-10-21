from setuptools import setup



setup(
    name='code-katas',
    description='A package for tesing code wars katas.',
    package_dir={'':'src'},
    author='Mark Reynoso',
    author_email='mreynoso@spu.edu',
    py_modules=['multiples_of_3_and_5', 'changing_letters', 'exclamation_marks_series_6', 'find_the_odd_int', 'list_filtering', 'simple_pig_latin', 'sum_of_two_lowest_possible_integers', 'whats_the_real_floor'],
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'pytest-watch', 'tox'],
        'development': ['ipython']
    },
)