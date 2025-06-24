# 🛠 UEBS Modded Unit Extractor

This is a simple Python script that collects all modded unit data from the **UEBS (Ultimate Epic Battle Simulator)** Steam Workshop folder and compiles it into a CSV file for easy use in Excel.  
Useful for unit comparison or tournament organisation.

---

## Setup

Run the python script with your desired workshop path
Default is set to C:\Program Files (x86)\Steam\steamapps\workshop\content\1468720
This is where it usually is stored

## Default Workshop Path


Update the `workshop_path` variable in the script if your install is elsewhere.

---

## What It Does

- Loops trough your Workshop folder for files named `MODDATA-*.bgmod`
- Extracts key-value stats from each `.bgmod` file
- Aggregates selected stats into a CSV file named `enemy_stats.csv`

---

## 🧾 Example `.bgmod` Content

animset=6
hp=350
dmg=50
attrange=120
splashdmg=0
splashdmgrng=0
impactforce=0
meleeblock=0
rangeblock=0
rangeblockforce=0
meleearmor=0
rangearmor=0
rangearmorforce=0
attacktime=1.5
attackbreak=0.7
projectile=1
projectilespeed=150
burstamount=5
burstrate=0.06
unitheight=1.9
unitwidth=0.5
soundpres=5
human=1


---

## ✅ Output

Generates `enemy_stats.csv`, ready to import into Excel for analysis or tournament management.

---

