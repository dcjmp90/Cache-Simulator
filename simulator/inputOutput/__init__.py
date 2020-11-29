from .util import Parser
from .base import dotnoted
from .util import translator


definitions = {  'notImplemented'     : 'This method {method_name:s} should be implemented and has not been!'
                ,'fileNotFound'       : 'The file specified: {file_name:s} cannot be found'
                ,'missRate'           : 'Miss Rate: {miss_rate:2d}%'
                ,'addressTranslation' : 'Actual address is {address:s}\n\nThe offset is {offset:s}\nThe tag is {tag:s}\nThe index is {index:s}'
                ,'openFile'           : 'r'
                ,'lowArgCount'        : 'The command line didnt not have enough arguments, only received: \'{args:s}\'.'
                ,'0'                  : '0000'
                ,'1'                  : '0001'
                ,'2'                  : '0010'
                ,'3'                  : '0011'
                ,'4'                  : '0100'
                ,'5'                  : '0101'
                ,'6'                  : '0110'
                ,'7'                  : '0111'
                ,'8'                  : '1000'
                ,'9'                  : '1001'
                ,'a'                  : '1010'
                ,'b'                  : '1011'
                ,'c'                  : '1100'
                ,'d'                  : '1101'
                ,'e'                  : '1110'
                ,'f'                  : '1111'
                ,'addressSize'        : 32
              }
definitions = dotnoted(definitions)

reader = Parser(definitions)

hex2binary = translator(definitions)