from setuptools import setup



setup(
    name='code-katas',
    description='A package for tesing code wars katas.',
    package_dir={'':'src'},
    author='Mark Reynoso',
    author_email='mreynoso@spu.edu',
    py_modules=['code-katas'],
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'pytest-watch', 'tox'],
        'development': ['ipython']
    },
    entry_points={
        'console_scripts': [
            'code-katas=code-katas:code-katas'
        ]
    }
)