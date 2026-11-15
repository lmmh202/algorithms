def solution(data, ext, val_ext, sort_by):
    idx = {"code":0, "date":1, "maximum":2, "remain":3}
    
    filtered = []
    for row in data:
        value = row[idx[ext]]
        if value < val_ext:
            filtered.append(row)
    
    return sorted(filtered, key=lambda row: row[idx[sort_by]])