Dưới đây là phần README cho công cụ **CSV Export** của bạn:

---

# CSV Export for Blender

## Overview

**CSV Export** is a Blender add-on that allows users to export summary data about 3D models in a specified folder to a CSV file. This tool helps you track important model details such as polygon count, texture properties, and other attributes. It is especially useful for asset management and optimization processes in Blender.

---

## Features

- **Exports model summary data** to CSV format, including:
  - Polygon/Face Count (output)
  - Texture name and size
  - Bit depth of the texture
  - Texture format (color space)
  - Model status based on specific criteria (e.g., texture format, texture size, poly count)

- **Batch processing**: The tool processes all `.gltf` files within a specified input folder and generates a comprehensive summary report.

- **Customizable folder selection**: Users can specify an input folder containing the 3D files and an output folder where the CSV report will be saved.

---

## Installation

1. Download or clone the repository.
2. Open Blender.
3. Go to `Edit > Preferences > Add-ons > Install`.
4. Choose the downloaded `.zip` file or `.py` script.
5. Enable the add-on by checking the box next to the **CSV Export** entry.

---

## Usage

### 1. Panel Setup

Once the add-on is installed, a new panel will appear in the **3D View**:

- Go to **3D View > Tools** (in the right sidebar).
- You will see the **Export CSV** panel under the **Tools** tab.

### 2. Select Folders

- **Input Folder**: Select the folder containing the `.gltf` files you want to process.
- **Output Folder**: Choose the folder where the generated CSV file will be saved.

### 3. Export CSV

- Click the **Export CSV** button to start the processing.
- The tool will process all `.gltf` files in the input folder and generate a CSV file containing the model summary data.
- Once completed, you will see a message confirming the successful export.

---

## Example Output

The generated CSV file will have the following structure for each model:

```
Model Code: example_model
Category, Information
Poly/face (output), 150000
Texture attached to material, example_texture.png
Texture size, 1024x1024
Bit Depth, 24
Texture Format (Color Space), sRGB
Status, True
```

If any issues are detected (e.g., non-standard texture formats, poly count too high), the "Status" will be marked as `False` and the conditions causing the issue will be listed.

---

## Requirements

- Blender 3.0 or later
- Python 3.7+ (typically bundled with Blender)
  
---

## License

This tool is released under the **MIT License**. You are free to use, modify, and distribute this tool, but please attribute the original author.

---

## Future Updates

- Support for more file formats (e.g., `.fbx`, `.obj`).
- Additional export options (e.g., exporting texture data as separate files).
- Enhanced filtering options for model validation.

---

## Contact

For any questions or contributions, feel free to reach out to me via:

- GitHub: [Bill Truong's GitHub](https://github.com/billtruong003)
- Email: truongbill003@gmail.com
