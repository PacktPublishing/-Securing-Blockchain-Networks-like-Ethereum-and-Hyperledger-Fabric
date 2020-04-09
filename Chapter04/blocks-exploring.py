from bloxplorer import bitcoin_testnet_explorer 

blk_id = "00000000000001bcfbd6242711752c6d8eb15701eb19e410a39a45fa363926e9"

block = bitcoin_testnet_explorer.blocks.get(blk_id)

print("Block ID: ", block.data['id'])

print("Merkle tree root: ", block.data['merkle_root'])

print("Previous block hash: ", block.data['previousblockhash'])

print("Block timestamp: ", block.data['timestamp'])

prev_block = bitcoin_testnet_explorer.blocks.get(block.data['previousblockhash'])

print(prev_block.data)


