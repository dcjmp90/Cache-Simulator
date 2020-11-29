from inputOutput import reader, definitions, hex2binary


if __name__ == '__main__':
    for data_line in reader:
        read_write, address = data_line
        address = hex2binary(address)
        