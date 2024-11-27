# README - Blender Tools

This repository contains three Blender tools designed for different tasks, including exporting CSV reports, batch decimating meshes, and converting GLB files to GLTF format. These tools are designed to streamline and automate various processes in Blender, making it easier to manage assets and work with 3D models.

---

### 1. CSV Export Tool

**Name:** CSV Export  
**Author:** Akaverse  
**Version:** 1.0.0  
**Blender Version:** 3.0.0 or higher  
**Category:** Object  
**Description:** Export summary data of 3D models to a CSV file for analysis.

**Features:**
- Processes `.gltf` files within a specified input folder.
- Gathers information such as poly count, textures, bit depth, and more.
- Exports the gathered information to a CSV file in a user-specified output folder.

**Usage:**
1. Select the input folder containing the `.gltf` files to process.
2. Choose an output folder where the summary CSV report will be saved.
3. Click "Export CSV" to generate the report.

**Exported Data Includes:**
- Model Code
- Poly/Face Count (output)
- Texture attached to material
- Texture size
- Bit depth
- Texture format (color space)
- Status of model (if it meets certain conditions like texture format or poly count)

---

### 2. Batch Decimate Tool

**Name:** Batch Decimate  
**Author:** Akaverse  
**Version:** 1.0.0  
**Blender Version:** 3.0.0 or higher  
**Category:** Object  
**Description:** Batch decimate meshes in `.gltf` files to reduce polygon count.

**Features:**
- Processes `.gltf` files in the selected input folder.
- Applies a decimation modifier with a configurable ratio to reduce polygon count.
- Exports the decimated models to a user-specified output folder in the `.gltf` format.

**Usage:**
1. Select the input folder containing the `.gltf` files to process.
2. Choose an output folder where the processed `.gltf` files will be saved.
3. Click "Batch Decimate" to process all files in the input folder.

**Decimation Settings:**
- Decimate Ratio: 50% (can be adjusted in the code).

---

### 3. GLB to GLTF Converter Tool

**Name:** Batch Decimate and Summary Export  
**Author:** Akaverse  
**Version:** 1.1.0  
**Blender Version:** 3.0.0 or higher  
**Category:** Object  
**Description:** Converts `.glb` files to `.gltf` format and generates a summary CSV report.

**Features:**
- Converts `.glb` files to `.gltf` format, exporting each file separately.

**Usage:**
1. Select the input folder containing `.glb` files to convert.
2. Choose an output folder where the `.gltf` files and the summary CSV will be saved.
3. Click "Batch Decimate" to process and export files.

**Exported Data Includes:**
- Model Code
- Poly/Face Count (before and after decimation)
- Texture information (name, size, bit depth)
- Export status (if model meets certain conditions)

---

## Installation Instructions

1. Download or clone this repository.
2. In Blender, go to `Edit > Preferences > Add-ons > Install...`.
3. Select the zip file for the desired tool (e.g., `ToolExportCSV.zip`).
4. Enable the addon by checking the box next to its name in the preferences window.
5. Access the tools via the `View3D > Tools` panel in the 3D viewport.

---

## Future Enhancements

- Support for additional file formats (e.g., `.obj`, `.fbx`).
- Customizable decimation ratios and texture handling options.
- More detailed export reports with additional data points.
- Support for asynchronous processing for large batches.

---

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

For any questions, issues, or contributions, feel free to open an issue or submit a pull request.

