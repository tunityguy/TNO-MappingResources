import geopandas as gpd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import os 
from lxml import etree

def create_map(lat, lon, highlighted_countries=None, puppet_states=None, alliance_to_show=None, output_svg='result.svg'):

    if highlighted_countries is None:
        highlighted_countries = []
    if puppet_states is None:
        puppet_states = []

    # Define alliance colors
    alliance_colors = {
        'OFN': '#0d1c3e',
        'Einheitspakt': '#465d63',
        'Sphere': '#3f1e1d',
        'Triumvate': '#4c6342'
    }

    # Map each country to its alliance (example data, adjust as needed)
    country_alliance = {
        'Germany': 'Einheitspakt',
        'Burgundy': 'Einheitspakt',
        'United Kingdom': 'Einheitspakt',
        'France': 'Einheitspakt',
        'Hungary': 'Einheitspakt',
        'Romania': 'Einheitspakt',
        'Transnistria': 'Einheitspakt',
        'Madagascar': 'Einheitspakt',
        'Denmark': 'Einheitspakt',
        'Slovakia': 'Einheitspakt',
        'Serbia': 'Einheitspakt',
        'Poland': 'Einheitspakt',
        'Ostland': 'Einheitspakt',
        'Netherlands': 'Einheitspakt',
        'Norway': 'Einheitspakt',
        'Kaukasien': 'Einheitspakt',
        'Ukraine': 'Einheitspakt',
        'Moskowien': 'Einheitspakt',
        'Central Africa': 'Einheitspakt',
        'Southwest Africa': 'Einheitspakt',
        'East Africa': 'Einheitspakt',
        'German Antarctica': 'Einheitspakt',
        'Pakistan': 'Einheitspakt',
        #
        'Japan': 'Sphere',
        'Manchuria': 'Sphere',
        'China': 'Sphere',
        'Sikkim': 'Sphere',
        'Guangdong': 'Sphere',
        'Azad Hind': 'Sphere',
        'Bhutan': 'Sphere',
        'Thailand': 'Sphere',
        'Burma': 'Sphere',
        'Indonesia': 'Sphere',
        'Vietnam': 'Sphere',
        'Laos': 'Sphere',
        'Cambodia': 'Sphere',
        'Malay': 'Sphere',
        'Second Philippine Republic': 'Sphere',
        '37th Army': 'Sphere',
        'Japanese Antarctica': 'Sphere',
        'Guangxi': 'Sphere',
        'Guizhou': 'Sphere',
        'Jinsui': 'Sphere',
        'Yunnan': 'Sphere',
        'Mongolia': 'Sphere',
        #
        'Italy': 'Triumvate',
        'Iberia': 'Triumvate',
        'Turkey': 'Triumvate',
        'Greece': 'Triumvate',
        'Iraq': 'Triumvate',
        'Yemen': 'Triumvate',
        'Egypt': 'Triumvate',
        'Italian Gulf': 'Triumvate',
        'Levant': 'Triumvate',
        'Montenegro': 'Triumvate',
        'Croatia': 'Triumvate',
        'Italian East Africa': 'Triumvate',
        'Algeria': 'Triumvate',
        'Iberian Algeria': 'Triumvate',
        'Syria': 'Triumvate',
        'Mosul': 'Triumvate',
        #
        'United States of America': 'OFN',
        'Canada': 'OFN',
        'Australia': 'OFN',
        'New Zealand': 'OFN',
        'Iceland': 'OFN',
        'Belize': 'OFN',
        'Guyana': 'OFN',
        'Suriname': 'OFN',
        'Haiti': 'OFN',
        'OFN Antarctica': 'OFN',
        'West Indies': 'OFN',
        'Faroes': 'OFN',
    }

    # Load the GeoJSON file
    world_map = gpd.read_file('TNO World Map.geojson')

    # Add a new column 'color' to the DataFrame
    world_map['color'] = '#0d2024'  # Default color for all countries

    # Update the color based on highlighted countries
    for country in highlighted_countries:
        world_map.loc[world_map['Name'] == country, 'color'] = '#6bf2b3'

    # Update the color for puppet states
    for country in puppet_states:
        world_map.loc[world_map['Name'] == country, 'color'] = '#91ccb1'

    # Update the color for alliance countries
    if alliance_to_show:
        for country, alliance in country_alliance.items():
            if country not in highlighted_countries and country not in puppet_states and alliance == alliance_to_show:
                world_map.loc[world_map['Name'] == country, 'color'] = alliance_colors.get(alliance, '#6bf2b3')

    # Set up the map projection
    ortho_proj = ccrs.Orthographic(central_longitude=lon, central_latitude=lat)

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': ortho_proj})

    # Plot the map using the colors from the DataFrame
    world_map.plot(ax=ax, color=world_map['color'], edgecolor='#50b4b0', linewidth=0.735, transform=ccrs.PlateCarree(), zorder=2)

    # Plot graticules (you need to have them loaded separately)
    graticules = gpd.read_file('Graticules/Graticules.shp')
    graticules.plot(ax=ax, color='#62b2c0', linewidth=0.735, transform=ccrs.PlateCarree(), zorder=1)

    ax.set_aspect('auto')
    ax.set_axis_off()

    # Save the map as a temporary SVG file
    temp_svg = 'temp_map.svg'
    plt.savefig(temp_svg, format='svg', bbox_inches='tight', pad_inches=0, transparent=True)
    plt.close()
    
    # Modify the SVG file to add the ocean ellipse
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(temp_svg, parser)
    root = tree.getroot()
    width, height = float(root.attrib["width"].replace("pt", "")), float(root.attrib["height"].replace("pt", ""))
    rx, ry = str(width / 2), str(height / 2)
    nsmap = root.nsmap

    ocean_ellipse = etree.Element(
        "ellipse",
        cx=rx,
        cy=ry,
        rx=rx,
        ry=ry,
        style="fill:#061115;fill-opacity:1;stroke:#62b2c0;stroke-width:0.4;stroke-opacity:1",
        nsmap=nsmap
    )
    root.insert(0, ocean_ellipse)

    tree.write(output_svg, pretty_print=True, xml_declaration=True, encoding="UTF-8")
    os.remove(temp_svg)
print("Thank you for using the Python script! Credits to Jankowek for making it.")

# CREATE MAPS BELOW THIS LINE
create_map(
    40, -101,
    highlighted_countries=['United States of America'],
    puppet_states=['West Indies'],
    alliance_to_show='OFN',
    output_svg='Maps/United States of America.svg'
)
