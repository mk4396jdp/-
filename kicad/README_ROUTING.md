# KiCad routing and export instructions

This folder contains guidance and a simple netlist to help a person with KiCad install open, place components, route the board, and export production Gerbers.

Files added:
- esp32cam_netlist.txt — a plain-text netlist / connection map for the main signals (USB, power, CH340, ESP32-CAM breakout pins)
- README_ROUTING.md — step-by-step instructions for opening KiCad, importing netlist, placing components, design rules, routing, and exporting Gerbers.

What you should do next (recommended):
1. Download this repo and open KiCad 6+.
2. Open the schematic file kicad/esp32cam-pcb.kicad_sch (if present) or create a new schematic and add the components listed in esp32cam_netlist.txt.
3. Generate netlist (or use the provided netlist) and import into PCBNew, place parts and route.
4. Run DRC and ERC, fix warnings, and use Pcbnew -> Plot to export Gerber RS-274X and the drill file.

If you want, after the routing is complete you can upload the generated Gerber ZIP here and I will review the Gerber Viewer screenshots for final checks.
