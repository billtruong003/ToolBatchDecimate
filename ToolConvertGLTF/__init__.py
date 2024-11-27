bl_info = {
    "name": "Batch Decimate and Summary Export",
    "author": "Akaverse",
    "version": (1, 1, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Tools",
    "description": "Batch decimate meshes and export a summary report",
    "category": "Object",
}

import bpy
import os
import csv
from bpy.props import StringProperty

process_queue = []
summary_data = []
output_folder_path = None

def write_summary_csv(output_folder):
    summary_csv_path = os.path.join(output_folder, "summary_report.csv")
    with open(summary_csv_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for entry in summary_data:
            writer.writerow([f"Model Code: {entry['folder_name']}"])
            writer.writerow(["Category", "Information"])
            writer.writerow(["Poly/face (input)", entry['tris_before']])
            writer.writerow(["Poly/face (output)", entry['tris_after']])
            writer.writerow(["Texture attached to material", entry['texture_name']])
            writer.writerow(["Texture size", entry['texture_size']])
            writer.writerow(["Bit Depth", entry['bit_depth']])  # Ghi thông tin bit depth
            writer.writerow(["Status", entry['status']])
            writer.writerow([])

def process_next_file():
    global output_folder_path

    if not process_queue:
        if output_folder_path:
            write_summary_csv(output_folder_path)
        return None

    input_folder, output_folder, dir_name = process_queue.pop(0)
    folder_path = os.path.join(input_folder, dir_name)
    output_path = os.path.join(output_folder, dir_name)
    os.makedirs(output_path, exist_ok=True)

    gltf_file = None
    bin_file = None
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if file_name.endswith('.gltf'):
            gltf_file = file_path
        elif file_name.endswith('.bin'):
            bin_file = file_path

    if gltf_file:
        bpy.ops.import_scene.gltf(filepath=gltf_file)

    tris_before = 0
    tris_after = 0
    texture_name = "None"
    texture_size = "None"
    bit_depth = "None"  # Biến để lưu thông tin bit depth
    status = "None"

    for obj in bpy.context.selected_objects:
        if obj.type == 'MESH':
            tris_before += len(obj.data.polygons)
            mod = obj.modifiers.new(name="Decimate", type='DECIMATE')
            mod.ratio = 0.5
            bpy.ops.object.modifier_apply(modifier=mod.name)
            tris_after += len(obj.data.polygons)

        for mat_slot in obj.material_slots:
            if mat_slot.material:
                for node in mat_slot.material.node_tree.nodes:
                    if node.type == 'TEX_IMAGE' and node.image:
                        texture_name = node.image.filepath_raw.split('/')[-1] if node.image.filepath_raw else node.image.name
                        texture_size = f"{node.image.size[0]}x{node.image.size[1]}"
                        
                        # Lấy thông tin bit depth
                        bit_depth = str(node.image.depth) if hasattr(node.image, 'depth') else "Unknown"

    conditions = []
    if not (texture_name.endswith('.jpeg') or texture_name.endswith('.jpg') or texture_name.endswith('.png')):
        conditions.append("Texture Format")
    if not (texture_size.split("x")[0].isdigit() and int(texture_size.split("x")[0]) < 4000):
        conditions.append("Texture Size")
    if bit_depth != "32":  # Kiểm tra bit depth
        conditions.append("Bit Depth")
    if tris_after >= 170001:
        conditions.append("Poly Count")

    status = f"False ({', '.join(conditions)})" if conditions else "True"

    output_file = os.path.join(output_path, dir_name + ".gltf")
    bpy.ops.export_scene.gltf(filepath=output_file, export_format='GLTF_SEPARATE')

    summary_data.append({
        "folder_name": dir_name,
        "tris_before": tris_before,
        "tris_after": tris_after,
        "texture_name": texture_name,
        "texture_size": texture_size,
        "bit_depth": bit_depth,  # Thêm bit depth vào báo cáo
        "status": status,
    })

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    
    return 0.1

def process_files_async(input_folder, output_folder):
    global process_queue, summary_data, output_folder_path
    process_queue = [(input_folder, output_folder, d) for d in os.listdir(input_folder) if os.path.isdir(os.path.join(input_folder, d))]
    summary_data = []
    output_folder_path = output_folder
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
