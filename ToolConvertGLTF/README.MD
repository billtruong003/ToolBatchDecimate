# Tool Overview

- **Main Functionality**: The tool converts `.glb` files to `.gltf` format in Blender, making it easier to work with 3D asset files in a more widely-used format.
- **User Interface**: The panel appears in the **GLB to GLTF** tab in Blender's UI, allowing users to easily choose input and output directories.
- **Batch Processing**: The tool can process all `.glb` files in a selected folder and convert them to separate `.gltf` files.

### Installation and Usage Steps

1. **Installation**: Once the add-on is installed in Blender, a new tab **GLB to GLTF** will appear in the **3D View** sidebar.
2. **Choose Input Folder**: Users can select a folder containing the `.glb` files they want to convert.
3. **Choose Output Folder**: Users can select a destination folder for the converted `.gltf` files.
4. **Convert**: Click the **Convert** button to automatically convert all `.glb` files in the input folder to `.gltf` files in the output folder.

### Key Features in the Code

- **Folder Selection**: Operators such as `ImportGLBOperator` and `ExportGLTFOperator` allow the user to select the input and output folders via file dialog boxes.
- **Conversion Process**: When the user presses the "Convert" button, the tool performs the following steps:
  1. Imports each `.glb` file into Blender.
  2. Exports the file as a `.gltf` in the specified format (`GLTF_SEPARATE`).
  3. Deletes all imported objects to prepare for the next conversion.
- **Logo Handling**: The `load_logo_image` function helps display a logo in the interface, enhancing the tool’s professionalism.

### Suggestions or Improvements

1. **Folder Management**:
   - Currently, an individual subfolder is created for each `.glb` file in the output folder, using the `.glb` file’s name as the subfolder name. This is useful, but could become cumbersome if you have a large number of files. Consider exporting all `.gltf` files into a single folder rather than creating separate subfolders for each.

2. **Error Reporting**:
   - It would be beneficial to improve error handling and reporting when `.glb` files are missing from the input folder or when the `.gltf` export fails. Clear error messages will help users troubleshoot more effectively.

3. **Additional Format Support**:
   - If you want the tool to support more input and output formats (e.g., `.fbx`, `.obj`), you could extend the functionality to handle other file types in the future.

4. **Performance Improvements**:
   - For folders with many `.glb` files, consider optimizing the import/export process to reduce latency. You could look into multi-threading or Blender's optimization techniques for handling large assets efficiently.

### Usage Instructions in Blender

1. **Installation**:
   - After installing and enabling the add-on, a new tab named **GLB to GLTF** will appear in the sidebar of the **3D View**.
   
2. **Choose Folders**:
   - Click the **Select Input Folder (.glb)** button to choose the folder that contains the `.glb` files you want to convert.
   - Then, click the **Select Output Folder (.gltf)** button to select the folder where the `.gltf` files will be saved.

3. **Conversion**:
   - Once both folders are selected, click the **Convert** button to begin the process. The tool will convert all `.glb` files in the input folder into `.gltf` format, saving them in the output folder.

---

### Example of how the conversion works:
1. A `.glb` file is imported into Blender.
2. The file is exported in `.gltf` format with all its assets (such as textures and meshes) saved separately.
3. The imported file is deleted, and the process continues with the next `.glb` file.

### Contact

For any questions or contributions, feel free to reach out to me via:

- GitHub: [Bill Truong's GitHub](https://github.com/billtruong003)
- Email: truongbill003@gmail.com