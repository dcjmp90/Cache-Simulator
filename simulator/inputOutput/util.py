import sys
import os
from .base import BufferReader

class Parser(BufferReader):
    '''
    '''
    def __init__(self, definitions):
        '''
        '''
        super(Parser, self).__init__(definitions)
        self.args = sys.argv
        self.argc = len(sys.argv)
        self.file = None
        assert (self.argc > 1), Exception(definitions.lowArgCount.format(args=' '.join(self.args)))
        try:
            self.file = open(self.args[-1].strip(), definitions.openFile)
        except:
            raise FileNotFoundError(definitions.fileNotFound.format(file_name=self.args[-1]))
        

    def __iter__(self):
        '''
        '''
        self.lines = self.file.readlines()
        self.length = len(self.lines) - 1
        self.idx = int()
        return self

    def __next__(self):
        '''
        '''
        if self.idx > self.length:
            raise StopIteration()
        split = self.lines[self.idx].split(' ')
        address = split[-1].strip()
        read_write = split[-2].strip()
        self.idx += 1
        return read_write, address

class translator:
    
    def __init__(self, definitions):
        '''
        '''
        self.definitions = definitions

    def __call__(self, address):
        '''
        '''
        address = address.replace('0x', '')
        binary = str()
        for base16 in address:
            binary += self.definitions[base16]
        if len(binary) < self.definitions.addressSize:
            for i in range(len(binary), self.definitions.addressSize):
                binary = '0' + binary
        return binary

