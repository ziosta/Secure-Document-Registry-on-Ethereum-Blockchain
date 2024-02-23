from setuptools import setup, find_packages

setup(
    name='Ziosta-Secure-Document-Registry-on-Ethereum-Blockchain',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'web3==5.24.0'  # Eğer projenizde başka bağımlılıklar varsa buraya ekleyin
    ],
)
