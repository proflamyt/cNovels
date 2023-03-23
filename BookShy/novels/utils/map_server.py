from django.http import HttpResponse
from mapserver import mapObj, layerObj

def map_view(bbox, width, height, layers):
    # Create a MapServer map object and load the mapfile
    novel_map = mapObj('path/to/mmapapfile.map')
    novel_map.load()

    # Set the map extent to the requested bounding box
    minx, miny, maxx, maxy = bbox.split(',')
    novel_map.setExtent(float(minx), float(miny), float(maxx), float(maxy))

    # Create a layer object for the requested layer
    layer = layerObj(novel_map)
    layer.name = layers

    # Set the layer style
    layer.styles.append('default')

    # Set the image format to PNG
    novel_map.outputformat.format = 'png'

    # Set the image size to the requested dimensions
    novel_map.width = int(width)
    novel_map.height = int(height)

    # Render the map to a PNG image
    image = novel_map.draw()

   

    return image
