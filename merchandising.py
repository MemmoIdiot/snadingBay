from dependencies.dependenciesInstaller import *

if __name__ == '__main__':
    from ebaysdk.merchandising import Connection
    api = Connection(config_file='ebay.yaml')
    results = api.execute('getMostWatchedItems', {})

    for item in results.reply.itemRecommendations.item:
        print(
            f"The item {item.title} has been watched {item.watchCount} times")
