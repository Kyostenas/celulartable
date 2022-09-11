from distutils.core import setup
from setuptools import find_packages
import json
import os


def read_file(filename):
    with open(filename, 'r+') as file:
        data = file.read()
    file.close()
    return data


def read_json(file):
    with open(file) as json_file:
        data = json.load(json_file)
    json_file.close()
    return data


setup(
  name='celulartable',         
  packages=find_packages(),   
  version=read_json(f'.{os.sep}package.json')['version'],      
  description='Tables made of cells for console.',   
  long_description=read_file('README.md'),
  long_description_content_type='text/markdown',
  author='Kyostenas',                   
  author_email='kyostenas@gmail.com',      
  url='https://github.com/Kyostenas/celulartable',   
  license='MIT',        
  download_url='',    
  keywords=['console', 'table', 'cell'],   
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3.8',
  ],
  entry_points={
    'console_scripts': []
  },
  data_files=[('', ['LICENSE'])]
)