#!/usr/bin/env python3
import json

class XPSystem:
    def __init__(self):
        self.xp = 1250450
        self.level = 7
        self.amor_agape = 100
    
    def add_xp(self, amount):
        self.xp += amount
        self.amor_agape = min(100, self.amor_agape + 1)
        return f"+{amount} XP | Total: {self.xp:,} | Amor: {self.amor_agape}%"

xp = XPSystem()
print("🎯 XP System criado!")
print(xp.add_xp(1000))
