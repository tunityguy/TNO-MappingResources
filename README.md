Credits:

Map - Epentibi, TunityGuy

Python Script - Jankowek

Graticules by Natural Earth Data

Required software for editing maps:

Python - https://www.python.org/ftp/python/3.12.5/python-3.12.5-amd64.exe

QGIS - https://www.qgis.org/downloads/QGIS-OSGeo4W-3.34.10-1.msi

Inkspace - https://inkscape.org/release/inkscape-1.3.2/windows/64-bit/msi/dl/

Run this command to install python libraries: pip install -r requirements.txt

Python and PIP should be installed for this. If PIP isn't installed, run 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py' in CMD, followed by 'python get-pip.py'.

The map can be edited on geojson.io and with a text editor.

You can modify script.py to change around things if you wish to change how the output looks.

I reccomend using VSCode for this - https://code.visualstudio.com/docs/?dv=win64user, paired with the Python extension for it


New ultimate guide on TunityGuy's channel: https://www.youtube.com/channel/UCjr3tWIQUJKxqvFb5ZC88GQ


The highlighted_countries, puppet_states and alliance_to_show can be hashed out to not use their functionalities.

Countries and territories located near the edge of the image may have issues regarding their infill, solution is to edit them in Inkspace by moving path endpoints far out of the globe.

Example:

```create_map(
    52, 19,
    highlighted_countries=['Poland'],
    puppet_states=['Germany', 'Ukraine'], 
    alliance_to_show='Einheitspakt',
    output_svg='Polsha.svg'
)```


