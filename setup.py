from setuptools import setup, find_packages
import d2l

requirements = [
    # conda install jupyter
    'jupyter',
    'numpy<=1.23.5',
    'matplotlib',
    'matplotlib-inline',
    'requests',
    'pandas',
    # conda install -c conda-forge gym
    'gym',
    # conda install -c conda-forge gpytorch
    'gpytorch',
    'scipy',
    # pip install d2l or pip install d2l==1.0.0b0
    'd2l'
]

setup(
    name='d2l',
    version=d2l.__version__,
    python_requires='>=3.5',
    author='D2L Developers',
    author_email='d2l.devs@gmail.com',
    url='https://d2l.ai',
    description='Dive into Deep Learning',
    license='MIT-0',
    packages=find_packages(),
    zip_safe=True,
    install_requires=requirements,
)
