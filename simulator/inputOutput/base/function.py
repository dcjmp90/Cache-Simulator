
class BufferReader:
    '''
    '''
    def __init__(self, definitions):
        '''
        '''
        self.report = definitions

    def __len__(self):
        '''
        '''
        return int()

    def __iter__(self):
        '''
        '''
        raise NotImplementedError(self.report.notImplemented.format(method_name = '__iter__')) 

    def __next__(self):
        '''
        '''
        raise NotImplementedError(self.report.notImplemented.format(method_name = '__name__')) 

class dotnoted(dict):
    '''
    '''
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__