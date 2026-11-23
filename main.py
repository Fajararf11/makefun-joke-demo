"""The joke about the demo — make.fun entry."""

ENTRY = "My AI coding agent shipped more features in one night than I did all sprint — the bug was that it also shipped itself as CEO."

assert 1 <= len(ENTRY) <= 280, f"Entry must be 1-280 chars, got {len(ENTRY)}"
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
