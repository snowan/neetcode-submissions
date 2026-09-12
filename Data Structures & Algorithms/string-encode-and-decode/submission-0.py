class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_res = []
        for s in strs:
            encoded_res.append(f"{len(s)}#{s}")

        return "".join(encoded_res)

    def decode(self, s: str) -> List[str]:
        decoded_res = []
        idx = 0
        while idx < len(s):
            j = idx
            while s[j] != '#':
                j += 1
            
            size = int(s[idx:j])
            start = j + 1
            end = start + size
            decoded_res.append(s[start:end])

            idx = end

        return decoded_res
