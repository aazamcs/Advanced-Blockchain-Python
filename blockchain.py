""" Description of an abstract Blockchain. """
from tools import calculate_hash
from typing import Optional

GENESIS_HASH = '0' * 64


class Block:
    """ A block in a blockchain. Points to the previous block. """
    _number: int
    previous: Optional['Block']
    _data: Optional[dict]
    _nonce: int

    def __init__(self, previous=None, data=None, nonce=0) -> None:
        """ default _data for block defined in constructor.
            Minimum specified should be _number and _data. """
        if previous is None:
            self._number = 0
        else:
            self._number = 1  # TODO

        self._data = data
        self.previous = previous
        self._nonce = nonce

    def get_previous_hash(self) -> str:
        """ Return the hash of the previous block. """
        if self.previous is None:
            return GENESIS_HASH
        else:
            return self.previous.get_hash()

    def get_hash(self) -> str:
        """returns a sha256 hash for the block's _data.
        Function instead of variable in constructor to avoid corruption of the variable. """
        return calculate_hash(self._number, self.get_previous_hash(), self._data, self._nonce)

    def mine(self, num_zeroes: int) -> None:
        """ Mine the block by finding the correct _nonce. """
        while self.get_hash()[:num_zeroes] != '0' * num_zeroes:
            self._nonce += 1

    def copy(self) -> 'Block':
        """ Return a copy of self. """
        ...

    def get_number(self) -> int:
        """ Return the block number. """
        ...

    def get_data(self) -> dict:
        """ Return the block data. """
        return self._data

    def get_nonce(self) -> int:
        """ Return the block nonce. """
        return self._nonce

    def __str__(self) -> str:
        """ Returns a string of the block's _data. Useful for diagnostic print statements. """
        return str('\nBlock %s\nHash: %s\nPrevious Hash: %s\nData: %s\nNonce: %s' % (
            self._number,
            self.get_hash(),
            self.get_previous_hash(),
            str(self._data),
            self._nonce)
                   )

    def __len__(self) -> int:
        ...

    def __iter__(self) -> 'Block':
        ...

    def __next__(self) -> 'Block':
        ...


class Blockchain:
    """ Describe a blockchain class. """
    ...

    def __init__(self, last=None, difficulty=4) -> None:
        ...

    def get_difficulty(self) -> int:
        """ Return the blockchain difficulty. """
        ...

    def append(self, block: Block) -> None:
        """ Append new block to the chain. """
        ...

    def add_block(self, block: Block) -> None:
        """ Mine a new block"""
        ...

    def is_valid(self) -> bool:
        """ Verify a valid blockchain. """
        ...

    def get_signature(self) -> str:
        """ Hash signature of the blockchain. """
        ...

    def copy(self) -> object:
        """ Return a copy of self. """
        ...

    def __len__(self) -> int:
        ...

    def __getitem__(self, item: int) -> Block:
        ...

    def __str__(self) -> str:
        ...

    def __iter__(self) -> Block:
        ...

    def __next__(self) -> Block:
        ...


class CryptoBlockchain(Blockchain):
    """ A cryptocurrency blockchain. """

    def get_balance(self, address: str) -> float:
        """ Get the balance of an address. """
        ...


if __name__ == '__main__':
    DIFFICULTY = 4
    b0 = Block()
    b1 = Block(b0)
    b2 = Block(b1)
    b3 = Block(b2)
    b0.mine(DIFFICULTY)
    b1.mine(DIFFICULTY)
    b2.mine(DIFFICULTY)
    b3.mine(DIFFICULTY)
