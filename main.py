import os

def L1():
    print("""
 ==========================================
|       ota builder for port roms          |
 ==========================================
|   For issues contact https://t.me/isg32  |
|                                          |
|[Place Build.prop & super.img inside input]
|    Note: Keep a Backup of super.img      | 
 ==========================================\n""")
    os.system("""
sleep 1
clear
sleep 1
cd input

echo "retrieving vars from build.prop"
sleep 0.5
build=$(cat build.prop | grep ro.system.build.id | cut -d "=" -f 2)
sysname=$(cat build.prop | grep ro.product.system.name | cut -d "=" -f 2)
androidver=$(cat build.prop | grep ro.build.version.release | cut -d "=" -f 2)
buildfp=$(cat build.prop | grep ro.system.build.fingerprint | cut -d "=" -f 2)
securitypatch=$(cat build.prop | grep ro.build.version.security_patch | cut -d "=" -f 2)
androidversion=$(cat build.prop | grep ro.build.version.release_or_codename | cut -d "=" -f 2)

echo " "
echo "===="
echo "TARGET_NAME = $build"
echo "BUILD_FINGP = $buildfp"
echo "===="
sleep 0.5
              
echo "Compressing Super..."
#gzip -f super.img
echo "Done! "
sleep 0.5
echo "Compressing Complete! "
echo "Moving Super to package..." 
#mv super.img.gz ../output/BuildFiles/image
sleep 0.5
echo "Done!"

sleep 0.5
cd ..
outrom="$build $build"
buildfp_text="Fingerprint: $buildfp"
build_text="Build: $build"
patch="Security Patch: $securitypatch"
android="Android: $androidversion"
cd metadata

sleep 0.5
echo " "
echo "Writiing Installer Script..."
# Create a temporary file with the updated content
sed -e '21s|.*|ui_print "'"$outrom"'"|' -e '22s|.*|ui_print "'"$buildfp_text"'"|' -e '23s|.*|ui_print "'"$build_text"'"|' -e '25s|.*|ui_print "'"$patch"'"|'  -e '24s|.*|ui_print "'"$android"'"|' update-binary > update-binary.tmp

# Overwrite the original file with the temporary file
mv update-binary.tmp update-binary
cp update-binary ../output/BuildFiles/META-INF/com/google/android
cd ..
cd output/BuildFiles
echo "Done!"
sleep 0.5
              
clear
echo "Creating Payload..."
echo " "
zip -r $sysname-$build-$androidversion.0-Hanoip.zip *
mv $sysname-$build-$androidversion.0-Hanoip.zip ../../build

clear
echo "  Complete you can find the rom in Build folder"

rm -fr Post.txt

echo \"\" \" **$(date)**\" >> Post.txt
echo \"\" \" \" >> Post.txt
echo \"📱\" \" **$sysname-$build**\" >> Post.txt
echo \"\" \" \" >> Post.txt
echo \"⚡ **Android**\":\" $androidversion\" >> Post.txt
echo \"🔒 **Security Patch**\":\" $securitypatch\" >> Post.txt
echo \"⬇️ **Download**\":\" 'https://sourceforge.net/projects/oemports-hanoip/files/'\" >> Post.txt
echo \"\" \" \" >> Post.txt
echo \"👤 **By**\":\" @semisapeol 'https://t.me/semisapeol/'\" >> Post.txt
echo \"🚶🏻 **Follow**\":\" @hanoipprojects\" >> Post.txt

echo " "
echo "  Data for Post has been dumped to Post.txt"
""")

L1()
