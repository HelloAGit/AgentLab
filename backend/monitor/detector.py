import time
from typing import Dict, List
from collections import deque
import statistics

class SharpMovementDetector:
    def __init__(self, window=5, pct_threshold=0.05):
        self.window = window
        self.pct_threshold = pct_threshold
        self.history = {}  # fixture_id -> deque of odds

    def update(self, fixture_id: str, odds: float):
        dq = self.history.setdefault(fixture_id, deque(maxlen=self.window))
        dq.append(odds)
        return self.check_signal(fixture_id)

    def check_signal(self, fixture_id: str):
        dq = self.history.get(fixture_id)
        if not dq or len(dq) < 2:
            return None
        prev = dq[-2]
        curr = dq[-1]
        if prev == 0:
            return None
        pct_change = (curr - prev) / prev
        if abs(pct_change) >= self.pct_threshold:
            return {
                "fixture_id": fixture_id,
                "prev": prev,
                "curr": curr,
                "pct_change": pct_change,
                "timestamp": int(time.time())
            }
        return None
