import hashlib as hasher
from collections import deque


class Block:
    def __init__(self, data: str, previous_hash: str):
        self.data = data
        self.previous_hash = previous_hash

    @property
    def hash(self) -> str:
        hashable = self.data + self.previous_hash
        sha = hasher.sha256()
        sha.update(hashable.encode('utf-8'))
        return sha.hexdigest()


def blockchain():
    block = Block("Genesis Block", "0")  # first block
    while True:
        data = yield block.hash
        block = Block(data, block.hash)


bc = blockchain()
bc.send(None)

data = ['msg1', 'msg2', 'msg3']
q = deque(data)
while q:
    data = q.popleft()
    bc_hash = bc.send(data)
    # Tell everyone about hash!
    print(f"Block is added to the chain: hash = {bc_hash}")
