from distutils.core import setup

setup(
    name="Slowloris",
    py_modules=["slowloris"],
    entry_points={"console_scripts": ["slowloris=slowloris:main"]},
    version="0.3.1",
    description="Ferramenta DoS de baixa largura de banda.  Slowloris reescrito em Python.",
    author="Mister ",
    author_email="procurandouqfdp@gmail.com",
    url="https://github.com/MisterIot/DDOSBYMISTER",
    keywords=["dos", "http", "slowloris"],
    license="MIT",
