import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")

    def add_block(self, data):
        last_block = self.chain[-1]
        new_block = Block(len(self.chain), data, last_block.hash)
        self.chain.append(new_block)

my_coin = Blockchain()
my_coin.add_block("Sent 1 BTC to Alice")
my_coin.add_block("Sent 5 BTC to Bob")

for block in my_coin.chain:
    print(f"Index: {block.index} | Hash: {block.hash[:20]}... | Data: {block.data}")