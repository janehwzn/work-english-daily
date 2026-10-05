#!/usr/bin/env python3
"""生成 scenarios/index.json：场景清单（id、标题、分类、weekday、tier）。"""
import json
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCEN_DIR = os.path.join(BASE, "scenarios")

index = []
for fname in sorted(os.listdir(SCEN_DIR)):
    if not fname.endswith(".json") or fname == "index.json":
        continue
    with open(os.path.join(SCEN_DIR, fname), encoding="utf-8") as f:
        d = json.load(f)
    index.append({
        "id": d["id"],
        "title": d["title"],
        "title_zh": d["title_zh"],
        "category": d["category"],
        "category_zh": d["category_zh"],
        "weekdays": d["weekdays"],
        "tier": d["tier"],
        "dialogue_turns": len(d["dialogue"]),
    })

with open(os.path.join(SCEN_DIR, "index.json"), "w", encoding="utf-8") as f:
    json.dump(index, f, ensure_ascii=False, indent=2)
print(f"wrote index.json with {len(index)} scenarios")
