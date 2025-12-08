import json
import hashlib
import time
import os

BlockChainData = "blockchain.json"


def load_chain():

    if os.path.exists(BlockChainData):
        with open(BlockChainData, "r") as f:
            return json.load(f)
    else:
        return [create_block("Genesis Block", previous_hash="0")]


def save_chain(chain):

    with open(BlockChainData, "w") as f:
        json.dump(chain, f, indent=4)


def hash_block(block):

    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()


def create_block(data, previous_hash):

    block = {
        "index": 0,  # updated later
        "timestamp": time.time(),
        "data": data,
        "previous_hash": previous_hash,
    }

    block["hash"] = hash_block(block)
    return block


def add_data(chain, data):

    previous_hash = chain[-1]["hash"]
    block = create_block(data, previous_hash)
    block["index"] = len(chain) + 1
    chain.append(block)
    save_chain(chain)
    return block


def get_chain(chain):
    """Return blockchain as formatted JSON string."""
    return json.dumps(chain, indent=4)


# --------------------------
# Example Usage
# --------------------------

blockchain = load_chain()

add_data(blockchain, "Certificate issued to Alice")
add_data(blockchain, {"student": "Bob", "course": "Cyber Security", "grade": "A"})

print(get_chain(blockchain))
