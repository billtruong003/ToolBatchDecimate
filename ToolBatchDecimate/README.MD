# README: Batch Decimate and Summary Export Addon for Blender

## Overview
The **Batch Decimate and Summary Export Addon** is a Blender tool designed to automate the process of decimating meshes and exporting a detailed summary report in CSV format. This is useful for optimizing 3D assets in bulk and tracking the results.

---

## Features
1. **Batch Decimation**: Applies a decimation modifier to all meshes in a folder of GLTF files, reducing polycount to 50%.
2. **Texture Analysis**: Extracts texture information, including file name, resolution, and color space.
3. **Validation and Reporting**: Outputs a CSV report summarizing polycount changes, texture details, and validation status.
4. **Export Results**: Outputs optimized models and the summary report to a designated folder.

---

## Requirements
- **Blender**: Version 3.0.0 or newer.
- Input files must be in **GLTF** format with textures properly linked.

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
- Create an **Input Folder** containing the GLTF files you want to process. Each model should be in its own folder, with its associated textures and `.bin` files if necessary.
- Create an **Output Folder** where optimized files and the CSV report will be saved.
- **Important**: Use separate folders for input and output to prevent overwriting or confusion during processing.

### Step 2: Using the Addon
1. In Blender, switch to the **3D Viewport**.
2. Open the **Tools** tab on the right-hand side (shortcut: `N` to toggle).
3. Locate the **Batch Decimate** panel.
4. Set the paths for:
   - **Input Folder**: Path to the folder containing your input models.
   - **Output Folder**: Path to the folder where the results will be saved.
5. Click **Batch Decimate** to start the process.

### Step 3: Review Results
- Decimated models will be saved in the Output Folder with the same folder structure as the Input Folder.
- A `summary_report.csv` file will be generated in the Output Folder. This file includes:
  - **Model Code**: Name of the processed folder.
  - **Poly/face (input/output)**: Polygon counts before and after decimation.
  - **Texture Information**: Name, size, and color space of attached textures.
  - **Status**: Indicates whether the model passed validation for texture format, size, and polycount.

---

## Notes
- The decimation ratio is set to 50%. You can modify this in the script if needed.
- Validation checks for:
  - Texture format (`.png`, `.jpg`, or `.jpeg`).
  - Texture size (less than 4000 pixels on any axis).
  - Texture color space (`sRGB`).
  - Polycount after decimation (less than 170,000).
- If a model fails validation, the `Status` column in the CSV will indicate the reasons.

---

## Recommendations
- Always use separate folders for **Input** and **Output**.
- Review the `summary_report.csv` file to check for any issues.
- Keep backups of the original files in case manual fixes are required.

---

## Troubleshooting
- **Textures Missing in Report**: Ensure textures are properly linked to the materials in the input models.
- **CSV Report Empty**: Verify that the Input Folder contains valid GLTF files and textures.
- **Output Folder Overwrites Input**: Always ensure Input and Output folders are different.

---

## Uninstallation
1. Open **Edit > Preferences > Add-ons**.
2. Search for "Batch Decimate and Summary Export."
3. Click **Remove**.
