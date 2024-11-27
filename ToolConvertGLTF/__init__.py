bl_info = {
    "name": "GLB to GLTF Converter",
    "blender": (4, 0, 0),
    "category": "Import-Export",
    "description": "Convert GLB to GLTF",
    "author": "Akaverse",
    "version": (1, 0, 0),
    "location": "View3D > UI > GLB to GLTF",
    "warning": "",
    "wiki_url": "https://github.com/Akaverse/GLBtoGLTF/wiki",
    "tracker_url": "https://github.com/Akaverse/GLBtoGLTF/issues",
    "support": "COMMUNITY",
}

import bpy
import os
from bpy.props import StringProperty
from bpy.types import Operator, Panel

# Global variable to store the Image
addon_image = None

def load_logo_image():
    """Loads the image if not already loaded, only executed when panel is drawn."""
    global addon_image
    if addon_image is None:
        addon_directory = os.path.dirname(__file__)
        image_path = os.path.join(addon_directory, "logo.png")

        if os.path.exists(image_path):
            try:
                # Load the image once
                addon_image = bpy.data.images.load(image_path)
                print("Logo loaded successfully.")
            except RuntimeError as e:
                print("Error loading logo:", e)
        else:
            print("Logo not found at:", image_path)

class ImportGLBOperator(Operator):
    """Select folder with .glb files to convert"""
    bl_idname = "import_scene.select_glb_input"
    bl_label = "Select Input Folder (.glb)"

    directory: StringProperty(subtype='DIR_PATH')

    def execute(self, context):
        context.scene.glb_input_folder = self.directory
        self.report({'INFO'}, f"Selected input folder: {self.directory}")
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

class ExportGLTFOperator(Operator):
    """Select output folder for .gltf files"""
    bl_idname = "export_scene.select_gltf_output"
    bl_label = "Select Output Folder (.gltf)"

    directory: StringProperty(subtype='DIR_PATH')

    def execute(self, context):
        context.scene.gltf_output_folder = self.directory
        self.report({'INFO'}, f"Selected output folder: {self.directory}")
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

class ConvertGLBToGLTFOperator(Operator):
    """Convert all .glb files in input folder to .gltf"""
    bl_idname = "convert.glb_to_gltf"
    bl_label = "Convert"

    def execute(self, context):
        input_folder = context.scene.glb_input_folder
        output_folder = context.scene.gltf_output_folder

        if not input_folder or not output_folder:
            self.report({'ERROR'}, "Please select both input and output folders.")
            return {'CANCELLED'}

        for filename in os.listdir(input_folder):
            if filename.endswith(".glb"):
                input_path = os.path.join(input_folder, filename)
                folder_name = os.path.splitext(filename)[0]
                output_subfolder = os.path.join(output_folder, folder_name)
                os.makedirs(output_subfolder, exist_ok=True)
                output_path = os.path.join(output_subfolder, folder_name + ".gltf")

                bpy.ops.import_scene.gltf(filepath=input_path)
                bpy.ops.export_scene.gltf(filepath=output_path, export_format='GLTF_SEPARATE')
                bpy.ops.object.select_all(action='SELECT')
                bpy.ops.object.delete(use_global=False)

                self.report({'INFO'}, f"Converted: {filename} -> {output_path}")

        self.report({'INFO'}, "Conversion completed for all .glb files.")
        return {'FINISHED'}

class GLBtoGLTFPanel(Panel):
    """Main panel for GLB to GLTF conversion"""
    bl_label = "GLB to GLTF Converter"
    bl_idname = "OBJECT_PT_glb_to_gltf"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "GLB to GLTF"

    def draw(self, context):
        global addon_image
        layout = self.layout
        scene = context.scene

        load_logo_image()  # Load the logo image if not already loaded

        if addon_image:
            # Directly display the image with layout.template_ID_preview
            layout.template_ID_preview(bpy.data.images, "logo.png", rows=1, cols=1)
        else:
            layout.label(text="Logo not loaded.")

        layout.prop(scene, "glb_input_folder", text="Input")
        layout.prop(scene, "gltf_output_folder", text="Output")
        layout.operator("convert.glb_to_gltf", text="Convert")

def register():
    bpy.utils.register_class(ImportGLBOperator)
    bpy.utils.register_class(ExportGLTFOperator)
    bpy.utils.register_class(ConvertGLBToGLTFOperator)
    bpy.utils.register_class(GLBtoGLTFPanel)
    bpy.types.Scene.glb_input_folder = StringProperty(name="Input Folder", subtype='DIR_PATH')
    bpy.types.Scene.gltf_output_folder = StringProperty(name="Output Folder", subtype='DIR_PATH')

def unregister():
    bpy.utils.unregister_class(ImportGLBOperator)
    bpy.utils.unregister_class(ExportGLTFOperator)
    bpy.utils.unregister_class(ConvertGLBToGLTFOperator)
    bpy.utils.unregister_class(GLBtoGLTFPanel)
    del bpy.types.Scene.glb_input_folder
    del bpy.types.Scene.gltf_output_folder

    global addon_image
    if addon_image and addon_image.name in bpy.data.images:
        bpy.data.images.remove(addon_image)
    addon_image = None

if __name__ == "__main__":
    register()
