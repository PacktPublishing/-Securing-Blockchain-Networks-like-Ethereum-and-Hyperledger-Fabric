from bloxplorer import bitcoin_testnet_explorer

transaction_id = '6d0139c3d0f529dda57496f1eabf0b32c9296c93b49b7a4965fa5ad91be4f216'

transaction = bitcoin_testnet_explorer.tx.get(transaction_id)

print("Transaction output: ", transaction.data['vout'])

