from dependencies.dependenciesInstaller import *

if __name__ == '__main__':
    from ebaysdk.trading import Connection
    from xmltodict import parse as parseXml
    api: Connection = Connection(config_file="ebay.yaml",
                                 domain="api.sandbox.ebay.com",
                                 # debug=True
                                 )

    with open('book.xml', 'r', encoding='utf-8') as file:
        xml = file.read()
    item: dict = parseXml(xml)

    api.execute("AddItem", item)
