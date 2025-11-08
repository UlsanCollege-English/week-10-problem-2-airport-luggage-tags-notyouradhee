"""
HW02 — Airport Luggage Tags (Open Addressing with Delete)
Implement linear probing with EMPTY and DELETED markers.
"""
EMPTY = object()
DELETED = object()

def make_table_open(m):
    """Return a table of length m filled with EMPTY markers."""
    return [EMPTY] * m

def _find_slot_for_insert(t, key):
    """Return index to insert/overwrite (may return DELETED slot). Return None if full."""
    m = len(t)
    start = i = hash(key) % m
    first_deleted = None
    while True:
        slot = t[i]
        if slot is EMPTY:
            return first_deleted if first_deleted is not None else i
        elif slot is DELETED:
            if first_deleted is None:
                first_deleted = i
        elif slot[0] == key:
            return i
        i = (i + 1) % m
        if i == start:
            return None

def _find_slot_for_search(t, key):
    """Return index where key is found; else None. DELETED does not stop search."""
    m = len(t)
    start = i = hash(key) % m
    while True:
        slot = t[i]
        if slot is EMPTY:
            return None
        elif slot is DELETED:
            pass
        elif slot[0] == key:
            return i
        i = (i + 1) % m
        if i == start:
            return None

def put_open(t, key, value):
    """Insert or overwrite (key, value). Return True on success, False if table is full."""
    i = _find_slot_for_insert(t, key)
    if i is None:
        return False
    t[i] = (key, value)
    return True

def get_open(t, key):
    """Return value for key or None if not present."""
    i = _find_slot_for_search(t, key)
    if i is None:
        return None
    return t[i][1]

def delete_open(t, key):
    """Delete key if present. Return True if removed, else False."""
    i = _find_slot_for_search(t, key)
    if i is None:
        return False
    t[i] = DELETED
    return True

if __name__ == "__main__":
    pass
