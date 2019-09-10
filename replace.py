import bpy
import sys
from os.path import isfile

# Take image path as the last command line argument
imgPath = sys.argv[-1]

print('imgPath', imgPath)
print('Keys', bpy.data.images['Screen.jpg'].filepath)
bpy.data.images['Screen.jpg'].filepath = imgPath

# o  = bpy.data.objects['Cube'] # Replace with your actual object's name
# t = o.active_material.node_tree
# print('ttttttttt', t)
# im = t.nodes['Screen.jpg'].image

# For the world texture, use something like this:
# w  = bpy.data.worlds['World'] # Replace with your actual world's name
# w.use_nodes = True
# t  = w.node_tree
# im = t.nodes['Texture'].image

# If provided image exists set is as the image texture node's image
# if isfile( imgPath ): im.filepath = imgPath