class RC4:
    def __init__(self, key: bytes):
        self.key = key
        self.S = self._ksa(key)

    def _ksa(self, key: bytes):
        """Key-Scheduling Algorithm (KSA)"""
        key_length = len(key)
        S = list(range(256))
        j = 0
        for i in range(256):
            j = (j + S[i] + key[i % key_length]) % 256
            S[i], S[j] = S[j], S[i]
        return S

    def _prga(self, S):
        """Pseudo-Random Generation Algorithm (PRGA)"""
        i = 0
        j = 0
        while True:
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]
            K = S[(S[i] + S[j]) % 256]
            yield K

    def encrypt(self, plaintext: bytes) -> bytes:
        """Encrypt the plaintext"""
        S = self.S.copy()
        keystream = self._prga(S)
        return bytes([b ^ next(keystream) for b in plaintext])

    def decrypt(self, ciphertext: bytes) -> bytes:
        """Decrypt the ciphertext"""
        return self.encrypt(ciphertext)