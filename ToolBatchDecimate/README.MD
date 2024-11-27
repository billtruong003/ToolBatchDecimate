# README: Batch Decimate Addon for Blender

## Overview
The **Batch Decimate Addon** is a Blender tool designed to automate the process of decimating meshes in multiple GLTF files. It allows you to batch process models by applying a decimate modifier to reduce the polycount, making the models more optimized for use in real-time applications. The addon also exports the processed models into a designated output folder.

---

## Features
1. **Batch Decimation**: Automatically applies a decimation modifier to all meshes in a folder of GLTF files, reducing their polycount by 50%.
2. **Efficient Processing**: Processes models one by one asynchronously, so you can continue working in Blender while the addon processes your models in the background.
3. **File Management**: Keeps the same folder structure for output files as the input folder.
4. **Model Export**: Outputs optimized models in GLTF format to a specified output folder.

---

## Requirements
- **Blender**: Version 3.0.0 or newer.
- Input files must be in **GLTF** format with associated textures properly linked.

---

## Installation
1. Open Blender.
2. Go to **Edit > Preferences > Add-ons**.
3. Click **Install...**.
4. Select the ZIP file containing the `batch_decimate.py` script.
5. Click **Install Add-on** and ensure the checkbox next to the add-on is enabled.

---

## Usage Instructions

### Step 1: Prepare Input and Output Folders
- **Input Folder**: This folder should contain the GLTF files you want to decimate. Each model should be in its own folder, with its associated textures and `.bin` files if necessary.
- **Output Folder**: Create a folder where the processed GLTF files will be saved.
- **Important**: Ensure that the **Input** and **Output** folders are separate to avoid overwriting files.

### Step 2: Using the Addon
1. Open Blender and switch to the **3D Viewport**.
2. Press `N` to open the **Tools** tab on the right-hand side.
3. Find the **Batch Decimate** panel.
4. Set the paths for:
   - **Input Folder**: The path to the folder containing your input GLTF models.
   - **Output Folder**: The path where the decimated models will be saved.
5. Click **Batch Decimate** to begin the decimation process.

### Step 3: Review Results
- The processed models will be saved in the **Output Folder**, maintaining the original folder structure from the **Input Folder**.
- Decimated models will be saved in `.gltf` format in the output folder.

---

## Notes
- **Decimation Ratio**: The decimation modifier is set to reduce the polycount by 50%. You can change this ratio in the script if necessary by modifying `mod.ratio = 0.5`.
- The addon will create separate subfolders within the output folder corresponding to each model in the input folder.
- You can monitor the decimation progress via the console, as the addon runs asynchronously in the background.

---

## Recommendations
- **Organize your folders**: Always use separate folders for **Input** and **Output** to avoid overwriting.
- **Check the Output Folder**: After processing, review the output folder to ensure that the models have been properly decimated and exported.
- **Backup Originals**: Keep backups of the original models in case manual adjustments are needed.

---

## Troubleshooting
- **Textures Missing in Processed Models**: Ensure that all textures are properly linked to the models in the input GLTF files.
- **No Processed Files in Output Folder**: Double-check that the **Input Folder** contains valid GLTF files and that the **Output Folder** is properly set.
- **No Progress Feedback**: Make sure the console is open to view progress updates, as the addon runs asynchronously.

---

## Uninstallation
1. Open **Edit > Preferences > Add-ons**.
2. Search for "Batch Decimate".
3. Click **Remove** to uninstall the addon.

---

### Additional Information

The addon processes files asynchronously using Blender’s `bpy.app.timers.register()` to avoid blocking the user interface while the models are being processed in the background. This makes it possible to decimate multiple models without interrupting other tasks in Blender.

### Contact

For any questions or contributions, feel free to reach out to me via:

- GitHub: [Bill Truong's GitHub](https://github.com/billtruong003)
- Email: truongbill003@gmail.com