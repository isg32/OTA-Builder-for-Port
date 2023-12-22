# OTA Builder for Port ROMs 🛠️
```
==========================================
ota builder for port roms

[Place Build.prop & super.img inside input]
Note: Keep a Backup of super.img
==========================================
```

For issues contact [isg32 Telegram](https://t.me/isg32)

> __Overview__
This script automates the process of building an OTA package for ported ROMs. It gathers necessary information from the provided build.prop file and compresses the super.img. The resulting ROM package is stored in the Build folder.
### Demo: <a href="https://youtu.be/NVH47s3dIvs" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/youtube.svg" alt="https://www.youtube.com/@isg32" height="30" width="40" /></a>


>Prerequisites

__Input Requirements:__
* build.prop file with essential ROM information.
* super.img file (Backup recommended).
* Usage
* Clone the repository.
```bash
 git clone https://github.com/yourusername/otabuilder.git
 cd otabuilder

```
* Place the required files in the input directory.
* Add Your Firmware files in the output/BuildFiles/Firmware folder & edit the essentials in output/BuildFiles/META-INF/com/google/android - update-binary file.
* Run the script.

```bash
python main.py
```
Find the completed ROM package in the Build folder.
Script Details
The script performs the following tasks:

Retrieves variables from build.prop.
Compresses super.img.
Moves super.img to the output/BuildFiles/image directory.
Writes an installer script (update-binary) with ROM details.
Creates a payload zip file.
Stores the final ROM package in the build directory.
Script Execution
The script is executed using the L1() function. It is divided into several sections, each performing a specific task:

Retrieving variables from build.prop.
Compressing super.img.
Writing the installer script.
Creating the payload zip file.
Completing the ROM build.
Please ensure you have the necessary permissions and dependencies installed before running the script.

> __Notes:__
* Backup your super.img file before running the script.
* Add Your Firmware files in the output/BuildFiles/Firmware folder & edit the essentials in output/BuildFiles/META-INF/com/google/android - update-binary file.
* Contact isg32's Telegram for support.
