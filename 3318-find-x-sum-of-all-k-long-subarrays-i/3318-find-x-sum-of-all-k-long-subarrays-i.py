from typing import List
from collections import defaultdict
from bisect import bisect_left, insort

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        if k > n:
            return []
        freq = defaultdict(int)
        sorted_keys: List[tuple] = []

        def key_of(v: int) -> tuple:
            return (-freq[v], -v)

        def remove_key(key: tuple) -> None:
            i = bisect_left(sorted_keys, key)
            if i < len(sorted_keys) and sorted_keys[i] == key:
                sorted_keys.pop(i)

        def add_key(key: tuple) -> None:
            insort(sorted_keys, key)
        for i in range(k):
            v = nums[i]
            if freq[v] > 0:
                remove_key((-freq[v], -v))
            freq[v] += 1
            add_key((-freq[v], -v))

        def compute_xsum() -> int:
            total = 0
            taken = 0
            for negf, negv in sorted_keys:
                if taken >= x:
                    break
                f = -negf
                v = -negv
                total += v * f
                taken += 1
            return total

        ans = [compute_xsum()]
        for i in range(k, n):
            out = nums[i - k]
            remove_key((-freq[out], -out))
            freq[out] -= 1
            if freq[out] > 0:
                add_key((-freq[out], -out))
            else:
                del freq[out]
            inn = nums[i]
            if freq[inn] > 0:
                remove_key((-freq[inn], -inn))
            freq[inn] += 1
            add_key((-freq[inn], -inn))

            ans.append(compute_xsum())

        return ans
