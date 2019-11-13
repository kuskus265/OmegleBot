try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='Kubí Industries Omegle Spammer',
      version='1337',
      description='Simple Omegle bot based on pyomegle library',
      author='Jacko Froggyfingers',
      author_email='kuskus265@gmail.com',
      url='https://github.com/elias94/pyomegle',
      license='MIT',
      packages=[ 'pyomegle' ],
      install_requires=[ 'mechanize' ],
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Topic :: Communications :: Chat',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Browsers'
      ],
      zip_safe=False)
