# organizer.py - GGMON SoundCloud Manager
import json
from pathlib import Path

# Todas tus listas van aquí (pégalas como texto)
raw_links = """
https://soundcloud.com/ramoncerdaquiroz/...
# (pega aquí todas las URLs que me mandaste en las partes 2,3,5)
""".strip().splitlines()

def clean_links(links):
    cleaned = []
    seen = set()
    for line in links:
        line = line.strip()
        if line.startswith("http") and "soundcloud.com" in line and line not in seen:
            seen.add(line)
            cleaned.append(line)
    return cleaned

links = clean_links(raw_links)

# Guardar
data = {
    "pride_2024": [link for link in links if "pride" in link.lower() or "gay" in link.lower()],
    "circuit": [link for link in links if any(x in link.lower() for x in ["circuit", "ibiza", "mantamar"])],
    "rituales_2026": [link for link in links if "mantra" in link.lower() or "lakshmi" in link.lower()]
}

Path("soundcloud/playlists").mkdir(parents=True, exist_ok=True)

with open("soundcloud/playlists/all_playlists.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Se limpiaron {len(links)} links únicos")
print("Archivos guardados en soundcloud/playlists/")
