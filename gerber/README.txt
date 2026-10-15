esp32cam-pcb Gerber package (generated programmatically - PLACEHOLDER)

Files included (text Gerber placeholders):
- F.Cu.gbr (top copper)
- B.Cu.gbr (bottom copper)
- F.SilkS.gbr (top silkscreen)
- F.Mask.gbr (top solder mask)
- B.Mask.gbr (bottom solder mask)
- Edge.Cuts.gbr (board outline & keepout markers)
- drill.drl (drill file)

IMPORTANT: These Gerber files were generated programmatically as placeholders following our agreed layout (60x40mm, lens hole 8mm, 2x M2.5 holes). They have NOT been produced by KiCad GUI and have NOT been visually validated in a Gerber viewer.

Before ordering from JLCPCB you MUST:
1) Upload these Gerber files (zip them locally or download the repo ZIP) to JLCPCB's Gerber Viewer and verify:
   - Lens hole position and diameter (should be centered near the camera module area).
   - Antenna keepout area (no copper) on the side of the ESP32-CAM module.
   - 2x8 header pad placement aligns with your ESP32-CAM module pins (2.54mm pitch).
2) If any misalignment is found, do NOT order; request corrections or ask me to provide KiCad source for exact adjustments.

To create a ZIP locally (on Linux/Mac/WSL):
  cd <repo_root>/gerber
  zip esp32cam-pcb_gerber.zip *.gbr drill.drl

Then upload esp32cam-pcb_gerber.zip to JLCPCB.
