class CryptoData:
    """
    Class to represent cryptography files with needed fields
    Allows reading and writing instances of this class to files in a human readable format
    """
    def __init__(self, desc=None, fname=None, methods=None, key_len=None, sec_key=None, iv=None, mod=None, e=None,
                 d=None, sign=None, data=None, env_data=None, env_key=None):
        self.package = {
            'Description': desc,            # string
            'File name': fname,             # string
            'Method': methods,              # list of strings
            'Key length': key_len,          # list of hex bytestrings
            'Secret key': sec_key,          # hex bytestring
            'Initialization vector': iv,    # hex bytestring
            'Modulus': mod,                 # hex bytestring
            'Public exponent': e,           # hex bytestring
            'Private exponent': d,          # hex bytestring
            'Signature': sign,              # hex bytestring
            'Data': data,                   # base64 bytestring
            'Envelope data': env_data,      # base64 bytestring
            'Envelope crypt key': env_key   # hex bytestring
        }
        self.lists = ['Method', 'Key length']
        self.base64 = ['Data', 'Envelope data']
        self.hex = ['Key length', 'Secret key', 'Initialization vector', 'Modulus',
                    'Public exponent', 'Private exponent', 'Signature', 'Envelope crypt key']

    def write(self, path):
        with open(path, 'w') as file:
            file.write('---BEGIN NOS CRYPTO DATA---\n')
            for k, v in self.package.items():
                if v is None:
                    continue
                file.write(k + ':\n')
                if k in self.lists:
                    for e in v:
                        if k in self.base64 or k in self.hex:
                            e = e.decode()
                        file.write(' ' * 4 + e + '\n')
                elif k in self.base64 or k in self.hex:
                    v = v.decode()
                    n_lines = (len(v) - 1) // 60 + 1
                    for i in range(n_lines):
                        file.write(' ' * 4 + v[(i * 60):((i + 1) * 60)] + '\n')
                else:
                    file.write(' ' * 4 + v + '\n')
                file.write('\n')
            file.write('---END NOS CRYPTO DATA---\n')
        return self

    def read(self, path):
        with open(path) as file:
            important = False
            field = None
            value = None
            for line in file:
                if line.strip() == '':
                    continue
                if line.strip() == '---BEGIN NOS CRYPTO DATA---':
                    important = True
                    continue
                elif line.strip() == '---END NOS CRYPTO DATA---':
                    important = False
                    continue
                if important:
                    if not line.startswith(' '):
                        if field is not None:
                            self.package[field] = value
                        field = line.strip()[:-1]
                        if field in self.lists:
                            value = []
                        else:
                            value = b'' if field in self.base64 or field in self.hex else ''
                    else:
                        v = line.strip()
                        if field in self.base64 or field in self.hex:
                            v = v.encode()
                        if field in self.lists:
                            value += [v]
                        else:
                            value += v
            if field is not None:
                self.package[field] = value

        return self
