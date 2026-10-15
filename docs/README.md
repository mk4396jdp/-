# ESP32-CAM Breakout (esp32cam-pcb)

This branch contains:

- KiCad placeholders (kicad/) — replace with full KiCad project if needed
- Gerber ZIP placeholder (gerber/esp32cam-pcb_gerber.zip) — not included in this commit; generate from KiCad before ordering
- docs/ with README, BOM, and image placeholders
- firmware/ with ESP32-CAM Arduino example
- web/ with Flask-based OMR server (Python)

Manufacturing notes (for JLCPCB):
- Board size: 60 x 40 mm
- 2 layers, FR-4, 1.6mm
- Surface finish: HASL
- Solder mask: green, silkscreen: white
- Keepout: leave 8mm keepout area around ESP32-CAM module antenna (no copper on top/bottom)
- Lens hole: 8 mm diameter at module camera location (check footprint alignment)
- Mounting holes: 2 x M2.5 (3.0 mm drill)

How to produce Gerbers:
1. Open the KiCad project in KiCad 6 (place the real .kicad_sch and .kicad_pcb files in kicad/)
2. In Pcbnew, run File -> Plot to generate Gerber RS-274X and Export Drill Files
3. Zip the Gerber files and upload to JLCPCB

Burning firmware (with on-board CH340):
- Plug micro-USB cable to board, select COM port in Arduino IDE, choose AI-Thinker ESP32-CAM board settings, and upload.
- To enter bootloader manually: hold IO0 LOW and press RESET, then release RESET, then release IO0 after programming.

