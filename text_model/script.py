import bpy
import sys

myText = sys.argv[-1]

bpy.data.objects['Text'].select_set(state=True)
bpy.ops.object.editmode_toggle
bpy.ops.font.select_all()
bpy.ops.font.delete(type='SELECTION')
bpy.ops.font.text_insert(text=myText)