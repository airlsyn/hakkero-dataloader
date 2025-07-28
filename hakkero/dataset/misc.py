#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import re
from typing import List


def unpack_packed_string(packed: str):
    """
    [BOS]abc[EOS][BOS]123[BOS]456[EOS]789 => ['[BOS]abc[EOS]', '[BOS]123', '[BOS]456[EOS]', '789']
    """
    tokens = re.split(r"(\[BOS]|\[EOS])", packed)

    samples = []
    cur = ""

    for tok in tokens:
        if tok == "[BOS]":
            if cur:
                samples.append(cur)
            cur = tok
        elif tok == "[EOS]":
            cur += tok
            samples.append(cur)
            cur = ""
        else:
            cur += tok

    if cur:
        samples.append(cur)

    return samples


def unpack_packed_tokens(packed: List[int], bos_id: int, eos_id: int) -> List[List[int]]:
    samples: List[List[int]] = []
    cur: List[int] = []

    for tid in packed:
        if tid == bos_id:
            if cur:
                samples.append(cur)
            cur = [bos_id]
        elif tid == eos_id:
            cur.append(eos_id)
            samples.append(cur)
            cur = []
        else:
            cur.append(tid)

    if cur:
        samples.append(cur)

    return samples
