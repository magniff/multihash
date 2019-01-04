import time
import setuptools


BUILD_NUMBER = str(int(time.time()))


setuptools.setup(
    name='cadena_multihash',
    version="0.1.%s" % BUILD_NUMBER,
    description="IPFS compatible multihash implementation",
    author="Julien Palard, Aleksandr Koshkin",
    url="https://github.com/magniff/multihash/",
    install_requires=[
        "pysha3", "pyblake2"
    ],
    modules=[
        "multihash"
    ],
)

