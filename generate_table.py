import json

# Load JSON
with open("all_metadata.json", "r") as f:
    data = json.load(f)

# Get all possible keys
all_keys = set()
for meta in data.values():
    all_keys.update(meta.keys())
all_keys = sorted(all_keys)

# Create table header
headers = ["Submodule"] + list(all_keys)
table_lines = ["| " + " | ".join(headers) + " |",
               "| " + " | ".join(["---"] * len(headers)) + " |"]

# Create one row per submodule
for submodule, metadata in data.items():
    row = [submodule]
    for key in all_keys:
        value = metadata.get(key, "")
        # Format lists/dicts as compact JSON strings
        if isinstance(value, (dict, list)):
            value = json.dumps(value, separators=(",", ": "))
        row.append(str(value))
    table_lines.append("| " + " | ".join(row) + " |")

# Save to markdown
with open("metadata_table.md", "w") as f:
    f.write("\n".join(table_lines))

print("✅ metadata_table.md has been generated in table (row-per-submodule) format.")
