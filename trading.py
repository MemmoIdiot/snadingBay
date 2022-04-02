from subprocess import call
from typing import Set

from ebaysdk.trading import Connection
from pkg_resources import working_set

required: Set[str] = {'xmltodict'}
installed: Set[str] = {pkg.key for pkg in working_set}
missing: Set[str] = required - installed
if missing:
    print('python -m pip install'.split(' ')+[*missing, '--user'])
    call('python -m pip install'.split(' ')+[*missing, '--user'])

from xmltodict import parse as parseXml  # noqa

if __name__ == '__main__':
    api: Connection = Connection(config_file="ebay.yaml",
                                 domain="api.sandbox.ebay.com",
                                 # debug=True
                                 )

    with open('book.xml', 'r', encoding='utf-8') as file:
        xml = file.read()

    d = parseXml(xml)

    api.execute("AddItem", d)
