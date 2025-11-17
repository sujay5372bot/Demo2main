import json
import os
from typing import List

DB_PATH = os.path.join(os.path.dirname(__file__), "groups.json")

def _ensure_db():
    if not os.path.exists(DB_PATH):
        with open(DB_PATH, "w") as f:
            json.dump({"approved": [], "pending": []}, f)

def _read():
    _ensure_db()
    with open(DB_PATH, "r") as f:
        return json.load(f)

def _write(data):
    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=2)

# APPROVED GROUPS
async def add_approved(group_id: int):
    data = _read()
    if group_id not in data["approved"]:
        data["approved"].append(group_id)
        if group_id in data["pending"]:
            data["pending"].remove(group_id)
        _write(data)

async def remove_approved(group_id: int):
    data = _read()
    if group_id in data["approved"]:
        data["approved"].remove(group_id)
        _write(data)

async def get_approved() -> List[int]:
    return _read()["approved"]

# PENDING GROUPS
async def add_pending(group_id: int):
    data = _read()
    if group_id not in data["pending"] and group_id not in data["approved"]:
        data["pending"].append(group_id)
        _write(data)

async def remove_pending(group_id: int):
    data = _read()
    if group_id in data["pending"]:
        data["pending"].remove(group_id)
        _write(data)

async def get_pending() -> List[int]:
    return _read()["pending"]
