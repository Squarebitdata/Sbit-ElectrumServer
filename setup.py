from setuptools import setup

setup(
    name="electrum-sbit-server",
    version="0.9",
    scripts=['run_electrum_sbit_server','electrum-sbit-server'],
    install_requires=['plyvel','jsonrpclib', 'irc'],
    package_dir={
        'electrumsbitserver':'src'
        },
    py_modules=[
        'electrumsbitserver.__init__',
        'electrumsbitserver.utils',
        'electrumsbitserver.storage',
        'electrumsbitserver.deserialize',
        'electrumsbitserver.networks',
        'electrumsbitserver.blockchain_processor',
        'electrumsbitserver.server_processor',
        'electrumsbitserver.processor',
        'electrumsbitserver.version',
        'electrumsbitserver.ircthread',
        'electrumsbitserver.stratum_tcp',
        'electrumsbitserver.stratum_http'
    ],
    description="SquareBit Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.de",
    license="GNU Affero GPLv3",
    url="https://github.com/Squarebitdata/Sbit-ElectrumServer/",
    long_description="""Server for the Electrum Lightweight SquareBit Wallet"""
)


