import bpy
from pathlib import Path
import os

current_directory = bpy.path.abspath("//") 
def has_material(obj):
    """Checks if the given object has any materials assigned."""
    return len(obj.material_slots) > 0

    
for ob in bpy.context.selected_objects:
    if has_material(ob):
        mat = ob.data.materials[0]
        matName = mat.name
        # Enable nodes for the material
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        
        for node in mat.node_tree.nodes:
            # Check if the node is an image node
            if node.type == 'TEX_IMAGE':
                # Remove the node
                mat.node_tree.nodes.remove(node)
        for node in mat.node_tree.nodes:
            if node.type == 'BSDF_PRINCIPLED':
                #set as primary node
                main_mat_node = node
            
        # Create an Image Texture node
        image_texture = nodes.new(type='ShaderNodeTexImage')
        image_texture.location = (-300, 0)

        # Set the image path
        image_path = (current_directory+matName+".bmp")
        if os.path.exists(image_path):
            image_texture.image = bpy.data.images.load(current_directory+matName+".bmp")

        print("Node inputs:", mat.node_tree)
        # Connect the Image Texture to the Base Color of the Principled BSDF
        mat.node_tree.links.new(image_texture.outputs["Color"], main_mat_node.inputs["Base Color"])

