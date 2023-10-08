from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.5.8'
DESCRIPTION = 'ASH-20 Einweg-Hashfunktion'

# Ausführliche Beschreibung
LONG_DESCRIPTION = (
    'Die ASH-20 Einweg-Hashfunktion ist eine kryptografisch sichere Hashfunktion, entwickelt von Joshua Dean Pond. '
    'Sie basiert auf komplexen mathematischen Operatoren, darunter Modulo, XOR, OR, AND, Integralrechnung, '
    'Bitverschiebung (Shift) und Zerlegung. Die Funktion ist als Einwegfunktion konzipiert, was bedeutet, dass '
    'es praktisch unmöglich ist, den ursprünglichen Eingabetext aus dem Hashwert wiederherzustellen. Die Verwendung '
    'von Avalanche sorgt dafür, dass kleine Änderungen im Eingabetext zu drastisch unterschiedlichen Hashwerten führen. '
    'Die ASH-20 Hashfunktion bietet ein hohes Maß an Sicherheit für kryptografische Anwendungen.'
)

# Setting up
setup(
    name="avalanchesumhash20",
    version=VERSION,
    author="Joshua Dean Pond",
    author_email="joshua.pond11@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['scipy'],
    keywords=['python', 'hash', 'cryptographic hash', 'security'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    package_data={'avalanchesumhash20': ['LICENSE', 'README.md', 'docs/script_documentation.pdf']},
    include_package_data=True,
)
