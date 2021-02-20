from collections import defaultdict

def read_rime_dict(file_path):
    '''Read a rime dictionary and get the pronunciations of words.'''
    d = defaultdict(list)

    with open(file_path, encoding='utf-8') as f:
        # skip header
        for line in f:
            if line == '...\n':
                break

        for line in f:
            line = line.rstrip('\n')
            if line and line[0] != '#': # skip empty lines and comments
                k, v, *_ = line.split('\t')
                d[k].append(v)

    return d
