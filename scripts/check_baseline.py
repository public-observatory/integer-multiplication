#!/usr/bin/env python3
"""Check the agenda's elementary deductions, not the multiplication theorem."""
import json
from fractions import Fraction as Q
from pathlib import Path

root = Path(__file__).resolve().parents[1]
data = json.loads((root / 'evidence/baseline.json').read_text())
a, k = Q(data['bit_saving']), Q(data['kappa'])
assert data['m'] * data['W'] - data['weighted_child_sum'] == data['deficit']
assert 0 < data['max_child'] < data['m']
assert Q(1, 2**15) < k < Q(1, 2**14)
ceiling = a / (1 + a)
gap = ceiling - k
assert 0 < gap < Q(135, 10**22)
required = Q(1, 16383)
increase = required / a - 1
assert Q(1963, 10000) < increase < Q(1964, 10000)
h = Q(data['backoff'])
q = a * (1 - 2*h)
epsilon = (1-h) / (1+q)
assert 0 < h < Q(1, 2)
assert k < epsilon*q < ceiling
# Same deficit for both abstract examples; moment comparisons follow by squaring.
assert 2*1 + 2*2 == 2*3 == 6
assert Q(1, 2) > Q(1, 2)**2  # 1/sqrt(2) > 1/2
assert Q(3, 4) < 1           # sqrt(3)/2 < 1
print('PASS: baseline ledger, rational comparisons and assembly bound')
print(f'Assembly ceiling minus selected kappa: {float(gap):.12g}')
print(f'Necessary bit-saving increase for target: {float(increase*100):.9f}%')
