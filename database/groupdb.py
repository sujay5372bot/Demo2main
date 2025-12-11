import json
import os

DB_PATH = "database/groups.json"

# Ensure DB File Exists
def init_db():
    if not os.path.exists(DB_PATH):
        with open(DB_PATH, "w") as f:
            json.dump({"approved": [], "pending": []}, f)

def read_db():
    init_db()
    with open(DB_PATH, "r") as f:
        return json.load(f)

def write_db(data):
    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=2)

# -------------------------
#   DATABASE MAIN FUNCTIONS
# -------------------------

async def add_pending(group_id):
    data = read_db()
    if group_id not in data["pending"]:
        data["pending"].append(group_id)
    write_db(data)

async def add_approved(group_id):
    data = read_db()
    if group_id not in data["approved"]:
        data["approved"].append(group_id)
    write_db(data)

async def remove_pending(group_id):
    data = read_db()
    if group_id in data["pending"]:
        data["pending"].remove(group_id)
    write_db(data)

async def remove_approved(group_id):
    data = read_db()
    if group_id in data["approved"]:
        data["approved"].remove(group_id)
    write_db(data)

async def get_pending():
    return read_db()["pending"]

async def get_approved():
    return read_db()["approved"]

async def is_approved(group_id):
    data = read_db()
    return group_id in data["approved"]
