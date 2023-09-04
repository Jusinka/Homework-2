def combine_tuples_to_dict(keys, values):
    return dict(zip(keys, values))

coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')

result = combine_tuples_to_dict(coin, code)
print(result)