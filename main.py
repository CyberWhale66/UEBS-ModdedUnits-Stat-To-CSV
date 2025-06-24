import os
import csv

# Path to your workshop path usually C:\Program Files (x86)\Steam\steamapps\workshop\content\1468720

workshop_path = r"C:\Program Files (x86)\Steam\steamapps\workshop\content\1468720"
output_csv = "enemy_stats.csv"

# Values to store
ValuesToStore = [
    "animset", "hp", "dmg", "attrange", "splashdmg", "splashdmgrng",
    "impactforce", "meleeblock", "rangeblock", "rangeblockforce",
    "meleearmor", "rangearmor", "rangearmorforce", "attacktime",
    "attackbreak", "projectile", "projectilespeed", "burstamount",
    "burstrate", "unitheight", "unitwidth", "soundpres", "human"
]

rows = []

# Loop through each workshop item inside the games workshop directory
for mod_id in os.listdir(workshop_path):
    mod_folder = os.path.join(workshop_path, mod_id)

    # We only want folders to be taken into account (incase another hehe.dll spawns🤣)
    if os.path.isdir(mod_folder):

        for file in os.listdir(mod_folder):

            # We're only interested in files that start with "MODDATA-" and end with ".bgmod" as they hold the unit's data.
            # FOR FUTURE ME (there is an image it could be cool to also collect that as a base64 string)
            if file.startswith("MODDATA-") and file.endswith(".bgmod"):
                full_path = os.path.join(mod_folder, file)

                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        lines = f.readlines()
                        stats = {k: "" for k in ValuesToStore}
                        for line in lines:
                            if "=" in line:
                                key, val = line.strip().split("=", 1)
                                if key in stats:
                                    stats[key] = val
                        stats["name"] = os.path.splitext(file)[0]
                        rows.append([stats.get(k, "") for k in ["name"] + ValuesToStore])
                except Exception as e:
                    print(f"Failed to read the data from a unit. Failure at: {full_path}: {e}")

# Write to CSV
with open(output_csv, "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["name"] + ValuesToStore)
    writer.writerows(rows)

print("CSV successfully created")
