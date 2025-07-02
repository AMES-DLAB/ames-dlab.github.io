import json

# Load the JSON
with open("all_metadata.json", "r") as f:
    data = json.load(f)

# Prepare markdown table
headers = ["Submodule", "Key", "Value"]
table_lines = ["| " + " | ".join(headers) + " |",
               "| " + " | ".join(["---"] * len(headers)) + " |"]

for submodule, metadata in data.items():
    for key, value in metadata.items():
        table_lines.append(f"| {submodule} | {key} | {value} |")

# Write to markdown file
with open("metadata_table.md", "w") as f:
    f.write("\n".join(table_lines))
