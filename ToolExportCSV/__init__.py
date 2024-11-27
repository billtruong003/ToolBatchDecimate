bl_info = {
    "name": "CSV Export",
    "author": "Akaverse",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Tools",
    "description": "Export summary data to CSV",
    "category": "Object",
}

import bpy
import os
import csv
from bpy.props import StringProperty

summary_data = []

def write_summary_csv(output_folder):
    summary_csv_path = os.path.join(output_folder, "summary_report.csv")
    with open(summary_csv_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for entry in summary_data:
            writer.writerow([f"Model Code: {entry['folder_name']}"])
            writer.writerow(["Category", "Information"])
            writer.writerow(["Poly/face (output)", entry['tris_after']])
            writer.writerow(["Texture attached to material", entry['texture_name']])
            writer.writerow(["Texture size", entry['texture_size']])
            writer.writerow(["Bit Depth", entry['bit_depth']])
            writer.writerow(["Texture Format (Color Space)", entry['color_space']])
            writer.writerow(["Status", entry['status']])
            writer.writerow([])

def process_files_for_export(input_folder):
    global summary_data
    summary_data = []
    for dir_name in os.listdir(input_folder):
        folder_path = os.path.join(input_folder, dir_name)
        if os.path.isdir(folder_path):
            gltf_file = None
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)
                if file_name.endswith('.gltf'):
                    gltf_file = file_path

            if gltf_file:
                bpy.ops.import_scene.gltf(filepath=gltf_file)

            tris_after = 0
            texture_name = "None"
            texture_size = "None"
            bit_depth = "None"
            color_space = "None"
            status = "None"

            # Quét và tính toán thông tin chỉ cho các đối tượng MESH hiện tại
            for obj in bpy.context.selected_objects:
                if obj.type == 'MESH':
                    tris_after += len(obj.data.polygons)

                for mat_slot in obj.material_slots:
                    if mat_slot.material:
                        for node in mat_slot.material.node_tree.nodes:
                            if node.type == 'TEX_IMAGE' and node.image:
                                texture_name = node.image.filepath_raw.split('/')[-1] if node.image.filepath_raw else node.image.name
                                texture_size = f"{node.image.size[0]}x{node.image.size[1]}"
                                bit_depth = str(node.image.depth) if hasattr(node.image, 'depth') else "Unknown"
                                color_space = node.image.colorspace_settings.name if hasattr(node.image, 'colorspace_settings') else "Unknown"

            conditions = []
            if not (texture_name.endswith('.jpg') or texture_name.endswith('.jpeg') or texture_name.endswith('.png')):
                conditions.append("Texture Format")
            if not (texture_size.split("x")[0].isdigit() and int(texture_size.split("x")[0]) < 4000):
                conditions.append("Texture Size")
            if bit_depth != "24":
                conditions.append("Bit Depth")
            if tris_after >= 170001:
                conditions.append("Poly Count")

            status = f"False ({', '.join(conditions)})" if conditions else "True"

            summary_data.append({
                "folder_name": dir_name,
                "tris_after": tris_after,
                "texture_name": texture_name,
                "texture_size": texture_size,
                "bit_depth": bit_depth,
                "color_space": color_space,
                "status": status,
            })

            bpy.ops.object.select_all(action='SELECT')
            bpy.ops.object.delete()

def export_csv(input_folder, output_folder):
    process_files_for_export(input_folder)
    write_summary_csv(output_folder)

class CSVExportOperator(bpy.types.Operator):
    bl_idname = "object.export_csv"
    bl_label = "Export CSV"
    
    def execute(self, context):
        input_folder = context.scene.input_folder
        output_folder = context.scene.output_folder
        if not input_folder or not output_folder:
            self.report({'ERROR'}, "Input/output folder not selected!")
            return {'CANCELLED'}
        export_csv(input_folder, output_folder)
        self.report({'INFO'}, "CSV Export Completed!")
        return {'FINISHED'}

class CSVExportPanel(bpy.types.Panel):
    bl_label = "Export CSV"
    bl_idname = "PT_CSVExport"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tools'
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        layout.prop(scene, "input_folder")
        layout.prop(scene, "output_folder")
        layout.operator("object.export_csv")

def register():
    bpy.utils.register_class(CSVExportOperator)
    bpy.utils.register_class(CSVExportPanel)
    bpy.types.Scene.input_folder = StringProperty(name="Input Folder", description="Folder containing the files to process", subtype='DIR_PATH')
    bpy.types.Scene.output_folder = StringProperty(name="Output Folder", description="Folder to save processed files", subtype='DIR_PATH')

def unregister():
    bpy.utils.unregister_class(CSVExportOperator)
    bpy.utils.unregister_class(CSVExportPanel)
    del bpy.types.Scene.input_folder
    del bpy.types.Scene.output_folder

if __name__ == "__main__":
    register()
