---
title: 'A deployment script for a generic Cocoa Mac application | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/11/deployment-script-for-generic-cocoa-mac.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:b314c9ceb6fa46b9'
translated: false
---

> 原文：[A deployment script for a generic Cocoa Mac application | Cocoa with Love](https://www.cocoawithlove.com/2010/11/deployment-script-for-generic-cocoa-mac.html)　·　Cocoa with Love (Matt Gallagher)

Deployment for a Cocoa Mac application normally involves a few common steps: committing code into a repository, updating version numbers and packaging the application as a DMG disk image. In this post, I'll show you a combination bash/perl/Applescript to handle all these tasks in a single script.

## Deployment steps

Standard Xcode build templates will build your code but don't really offer any help beyond that point. Deploying your application normally requires a few extra steps beyond what the standard templates provide.

While you can simply make a ZIP archive out of the application in your Release directory and call it done, there's normally a few more steps that you should take when deploying an application.

### 1. Update your version number

Obviously, this isn't a hard step but it is easy to forget since the user-facing version number (build numbers not included) must be deliberately updated when you decide a build is ready.

### 2. Commit your code into a version control system

This step should be obvious: it protects your time investment by ensuring that your code doesn't disappear.

And yet I still visit small or single-programmer offices where all the code is just kept in a directory and the whole directory is duplicated from version to version or to play with features. Seriously, that is _not_ how you should manage things. You may have your disk backed up, you may keep copies of your builds but these things are only complimentary to maintaining your repository.

How did we implement this feature in version 1.2 (and where's the old code)? Why was this code changed and what did it do before? Do we have a copy of version 3.5 of the application anywhere?

These are the questions that are best answered by not only having a code repository but having it properly tagged for every build. I won't get into philosophies about how frequently you should commit _between_ releases or how you should tag bug fixes and feature changes but the absolute minimum for any system should be that you tag your releases. Your deployment script should make this mandatory.

Incidentally, newer distributed repository version control programs like git make creating a repository for your code so much simpler. Instead of needing to set up a centralized location, you can casually make any folder its own local repository (i.e. just run "git init" in the directory) and worry about whether and where to locate an official or shared repository later.

Frustrated at Xcode's horrible version control system support? Can't remember all the git commands? Don't like git's command-line interface? I certainly don't. Fortunately, Mac apps like [GitX](http://gitx.frim.nl/) are simple, pretty and work well.

### 3. Make certain you have a clean build

From time-to-time, you will encounter problems with builds that are only fixed by cleaning and rebuilding. One of the biggest examples of this are assets that you deliberately remove from the build — these never get removed from the build directory unless you clean first, then build. Without a step to clean the directory first, your build may not be exactly what you think it should be.

### 4. Package the application in a DMG file

Mostly for reasons of aesthetic presentation, Mac applications that don't require an installer are normally deployed as DMG disk images. These can be a little fiddly to create, adjust aesthetically and then create a compressed version for distribution.

Fortunately, with a little Applescripting, we can automate this process too.

## A big ole Bash script

Here then is a bash script to handle all of the above steps. It's an annoying diversion into another language for a C/Obj-C/C++ programmer but some things (especially setting folder view options) need to be done a specific way.

A script of this sort is the traditional way that this type of deployment is handled. However, it is actually _not_ how I handle my deployments (but I'm a little weird in this respect). Next week, I'll show you the code I use for deployment.

### Assumptions in this script

There's a few assumptions here. While they are normally valid assumptions if you create your project using default Cocoa Mac Application template, there are certainly cases where they won't apply and you'll need to tweak the script a little.

1. This script requires 1 parameter: the .xcodeproj file you want to build.
2. The target you want to build must have the same name as the project (minus the .xcodeproj extension).
3. The Info.plist for the application must have the same name as the project (minus the .xcodeproj extension) with the suffix "-Info.plist".
4. The application build has the same name as the project (minus the .xcodeproj extension).
5. The deployment build is the "Release" build and the build project directory is the build/Release directory.
6. You use git for your repository (although this script will continue if git is not installed).
7. The background image for your DMG folder is a 400x300px PNG named background.png in the same folder as the .xcodeproj file (although this script will skip background image steps if the background.png is missing).
8. The deployment DMG file will be saved to the Desktop with the same name as the project (minus the .xcodeproj extension) with the suffix ".dmg" (build will fail if there's already something at this location).

### The script

```objc
<span style="color:#793;">#!/bin/bash
</span>
if [ ! "${1}" ]; then
    echo "usage: $0 xcode_project_path"
    exit
fi

XCODE_PROJECT_PATH=$1
XCODE_DIRECTORY="`dirname "$1"`"
XCODE_PROJECT_NAME="`basename -s .xcodeproj "${XCODE_PROJECT_PATH}"`"

<span style="color:#793;"># xcodebuild needs to run from the project's directory so we'll move there
# and stay for the duration of this script
</span>cd "${XCODE_DIRECTORY}"

<span style="color:#793;"># Check if git is installed
</span>if [ `which git` ]; then
    echo "git is installed on this computer"

    <span style="color:#793;"># If git is installed, then require that the code be committed</span>
    if [ "`git status -s 2>&1 | egrep '^\?\?|^ M|^A |^ D|^fatal:'`" ] ; then
        echo "Code is not committed into git. Commit into git before deployment."
        exit
    fi
    echo "Repository up-to-date."
fi

<span style="color:#793;"># !! Update: Changed from using the Perl Cocoa bridge to using PlistBuddy !!
# Use the perl to Objective-C bridge to get the version from the Info.plist
# You could easily use the python or ruby bridges to do the same thing
#CURRENT_VERSION="`echo 'use Foundation;
#$file = "'"${XCODE_PROJECT_NAME}"'-Info.plist";
#$plist = NSDictionary->dictionaryWithContentsOfFile_($file);
#$value = $plist->objectForKey_("CFBundleVersion");
#print $value->description()->UTF8String() . "\n";' | perl`"
</span>
<span style="color:#793;"># Use PlistBuddy instead of the perl to Cocoa bridge
</span>CURRENT_VERSION="`/usr/libexec/PlistBuddy -c 'Print CFBundleVersion' \
    "${XCODE_PROJECT_NAME}-Info.plist"`"

<span style="color:#793;"># Report the current version
</span>echo "Current version is ${CURRENT_VERSION}"

<span style="color:#793;"># Prompt for a new version
</span>read -p "Please enter the new version:
" NEW_VERSION

<span style="color:#793;"># !! Update: Changed from using the Perl Cocoa bridge to using PlistBuddy !!
# Use the bridge again to write the updated version back to the Info.plist
#echo 'use Foundation;
#$version = "'$NEW_VERSION'";
#$file = "'"${XCODE_PROJECT_NAME}"'-Info.plist";
#$plist = NSDictionary->dictionaryWithContentsOfFile_($file);
#$plist->setObject_forKey_($version, "CFBundleVersion");
#$plist->writeToFile_atomically_($file, "YES");' | perl
</span>
<span style="color:#793;"># Use PlistBuddy instead of the perl to Cocoa bridge
</span>/usr/libexec/PlistBuddy -c "Set CFBundleVersion ${NEW_VERSION}" \
    "${XCODE_PROJECT_NAME}-Info.plist"

<span style="color:#793;"># Commit the updated Info.plist
</span>if [ `which git` ]; then
    git commit -m "Updated Info.plist to version ${NEW_VERSION}" \
        "${XCODE_PROJECT_NAME}-Info.plist"
fi

<span style="color:#793;"># Clean the Release build
</span>xcodebuild -configuration Release -target "${XCODE_PROJECT_NAME}" clean

<span style="color:#793;"># Build the Release build
</span>if [ "`xcodebuild -configuration Release -target "${XCODE_PROJECT_NAME}" build \
     | egrep ' error:'`" ] ; then
    echo "Build failed."
    exit
fi

<span style="color:#793;"># Tag the repository now that we have a successful build
</span>git tag "version-${NEW_VERSION}"

<span style="color:#793;">#########
# From this point onwards, the script is all about DMG packaging
#########
</span>
<span style="color:#793;"># Create a temporary directory to work in
</span>TEMP_DIR="`mktemp -d "${TMPDIR}${XCODE_PROJECT_NAME}.XXXXX"`"

<span style="color:#793;"># Create the folder from which we'll make the disk image
</span>DISK_IMAGE_SOURCE_PATH="${TEMP_DIR}/${XCODE_PROJECT_NAME}"
mkdir "${DISK_IMAGE_SOURCE_PATH}"

<span style="color:#793;"># Copy the application into the folder
</span>cp -R "build/Release/${XCODE_PROJECT_NAME}.app" \
    "${DISK_IMAGE_SOURCE_PATH}/${XCODE_PROJECT_NAME}.app"

<span style="color:#793;"># Make a symlink to the Applications folder
# (so we can prompt the user to install the application)
</span>ln -s "/Applications" "${DISK_IMAGE_SOURCE_PATH}/Applications"

<span style="color:#793;"># If a "background.png" file is present in the Xcode project directory,
# we'll use that for the background of the folder.
# An assumption is made in this script that the background image is 400x300px
# If you are using a different sized image, you'll need to adjust the
# placement and sizing parameters in the Applescript below
</span>if [ -e "background.png" ]; then
    cp "background.png" \
        "${DISK_IMAGE_SOURCE_PATH}/background.png"
fi

<span style="color:#793;"># Create the read-write version of the disk image from the folder
# Also note the path at which the disk is mounted so we can open the disk
# to adjust its attributes
</span>DISK_IMAGE_READWRITE_PATH="${DISK_IMAGE_SOURCE_PATH}-rw.dmg"
VOLUME_MOUNT_PATH="`hdiutil create -srcfolder "${DISK_IMAGE_SOURCE_PATH}" \
    -format UDRW -attach "${DISK_IMAGE_READWRITE_PATH}" | \
    sed -n 's/.*\(\/Volumes\/.*\)/\1/p'`"

<span style="color:#793;"># Now we use Applescript to tell the Finder to open the disk image,
# set the view options to a bare, icon arranged view
# set the background image (if present)
# and set the icon placements
</span>if [ -e "background.png" ]; then
    echo '
    tell application "Finder"
        open ("'"${VOLUME_MOUNT_PATH}"'" as POSIX file)
        set statusbar visible of front window to false
        set toolbar visible of front window to false
        set view_options to the icon view options of front window
        set icon size of view_options to 96
        set arrangement of view_options to not arranged
        set the bounds of front window to {100, 100, 500, 400}
        set app_icon to item "'"${XCODE_PROJECT_NAME}"'" of front window
        set app_folder to item "Applications" of front window
        set background_image to item "background.png" of front window
        set background picture of view_options to item "background.png" of front window
        set position of background_image to {200, 200}
        set position of app_icon to {120, 100}
        set position of app_folder to {280, 100}
        set current view of front window to icon view
    end tell' | osascript
else
    echo '
    tell application "Finder"
        open ("'"${VOLUME_MOUNT_PATH}"'" as POSIX file)
        set statusbar visible of front window to false
        set toolbar visible of front window to false
        set view_options to the icon view options of front window
        set icon size of view_options to 96
        set arrangement of view_options to not arranged
        set the bounds of front window to {100, 100, 500, 400}
        set app_icon to item "'"${XCODE_PROJECT_NAME}"'" of front window
        set app_folder to item "Applications" of front window
        set position of app_icon to {120, 100}
        set position of app_folder to {280, 100}
        set current view of front window to icon view
    end tell' | osascript
fi

<span style="color:#793;"># Make the background.png file invisible
</span>SetFile -a V "${VOLUME_MOUNT_PATH}/background.png"

<span style="color:#793;"># Eject the disk image so that we can convert it to a compressed format
</span>hdiutil eject "${VOLUME_MOUNT_PATH}"

<span style="color:#793;"># Create the final, compressed disk image
</span>hdiutil convert "${DISK_IMAGE_READWRITE_PATH}" -format UDBZ \
    -o "${HOME}/Desktop/${XCODE_PROJECT_NAME}.dmg"

<span style="color:#793;"># Remove the temp directory
</span>rm -Rf "${TEMP_DIR}"
```

## Conclusion

Ergh: a code-heavy post with neither C nor Objective-C.

Next week, I'll show you how to perform the same steps in a logging, reporting, error-handling Cocoa application.
