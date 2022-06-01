from blockchain import Blockchain

block_one_transactions = {"sender":"Anakin", "receiver": "Kenobi", "amount":"50"}
block_two_transactions = {"sender": "Kenobi", "receiver":"Padme", "amount":"25"}
block_three_transactions = {"sender":"Anakin", "receiver":"Padme", "amount":"35"}
fake_transactions = {"sender": "Kenobi", "receiver":"Padme, Anakin", "amount":"25"}


local_blockchain = Blockchain()
print('-------------------------------------------')
local_blockchain.add_block(block_one_transactions) //adding blocks to the chain and then printing their contents 
local_blockchain.add_block(block_two_transactions)
local_blockchain.add_block(block_three_transactions)

local_blockchain.print_blocks()

local_blockchain.chain[2].transactions = fake_transactions
print(local_blockchain.validate_chain()) //prints False
