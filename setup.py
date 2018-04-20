from setuptools import setup, find_packages
import versioneer

with open('requirements.txt') as f:
    reqs = list(f.read().strip().split('\n'))

with open('README.rst') as f:
    long_desc = f.read()

setup(
    name='arrayish',
    description='A package to allow downstream inter-compatibility for Numpy-compatible array structures',
    long_description=long_desc,
    maintainer='Hameer Abbasi',
    maintainer_email='hameerabbasi@yahoo.com',
    packages=find_packages(
        include=['arrayish', 'arrayish.*'],
    ),
    install_requires=reqs,
    url='https://github.com/hameerabbasi/arrayish',
    zip_safe=False,
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    license='BSD',
)
