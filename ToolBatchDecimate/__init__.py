bl_info = {
    "name": "Batch Decimate",
    "author": "Akaverse",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Tools",
    "description": "Batch decimate meshes",
    "category": "Object",
}

import bpy
import os
from bpy.props import StringProperty

process_queue = []

def process_next_file():
    if not process_queue:
        return None

    input_folder, output_folder, dir_name = process_queue.pop(0)
    folder_path = os.path.join(input_folder, dir_name)
    output_path = os.path.join(output_folder, dir_name)
    os.makedirs(output_path, exist_ok=True)

    gltf_file = None
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if file_name.endswith('.gltf'):
            gltf_file = file_path

    if gltf_file:
        bpy.ops.import_scene.gltf(filepath=gltf_file)

    for obj in bpy.context.selected_objects:
        if obj.type == 'MESH':
            mod = obj.modifiers.new(name="Decimate", type='DECIMATE')
            mod.ratio = 0.5  # Cấu hình decimate tỷ lệ giảm
            bpy.ops.object.modifier_apply(modifier=mod.name)

    output_file = os.path.join(output_path, dir_name + ".gltf")
    bpy.ops.export_scene.gltf(filepath=output_file, export_format='GLTF_SEPARATE')

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

    return 0.1

def process_files_async(input_folder, output_folder):
    global process_queue
    process_queue = [(input_folder, output_folder, d) for d in os.listdir(input_folder) if os.path.isdir(os.path.join(input_folder, d))]
    bpy.app.timers.register(process_next_file)

class BatchDecimateOperator(bpy.types.Operator):
    bl_idname = "object.batch_decimate"
    bl_label = "Batch Decimate"
    
    def execute(self, context):
        input_folder = context.scene.input_folder
        output_folder = context.scene.output_folder
        if not input_folder or not output_folder:
            self.report({'ERROR'}, "Input/output folder not selected!")
            return {'CANCELLED'}
        process_files_async(input_folder, output_folder)
        self.report({'INFO'}, "Processing... check the console for progress!")
        return {'FINISHED'}

class BatchDecimatePanel(bpy.types.Panel):
    bl_label = "Batch Decimate"
    bl_idname = "PT_BatchDecimate"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tools'
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        layout.prop(scene, "input_folder")
        layout.prop(scene, "output_folder")
        layout.operator("object.batch_decimate")

def register():
    bpy.utils.register_class(BatchDecimateOperator)
    bpy.utils.register_class(BatchDecimatePanel)
    bpy.types.Scene.input_folder = StringProperty(name="Input Folder", description="Folder containing the files to process", subtype='DIR_PATH')
    bpy.types.Scene.output_folder = StringProperty(name="Output Folder", description="Folder to save processed files", subtype='DIR_PATH')

def unregister():
    bpy.utils.unregister_class(BatchDecimateOperator)
    bpy.utils.unregister_class(BatchDecimatePanel)
    del bpy.types.Scene.input_folder
    del bpy.types.Scene.output_folder

if __name__ == "__main__":
    register()
