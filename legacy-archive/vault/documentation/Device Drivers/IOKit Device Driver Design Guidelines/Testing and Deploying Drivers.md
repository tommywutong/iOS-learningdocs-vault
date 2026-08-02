---
title: IOKit Device Driver Design Guidelines
apple_id: TP30000694
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2009-08-14'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/WritingDeviceDriver/DeployingDrivers/DeployingDrivers.html
archived_at: '2026-07-15T07:31:49.277650Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [IOKit Device Driver Design Guidelines](Introduction%20to%20I-O%20Kit%20Device%20Driver%20Design%20Guidelines.md)


[Next](Developing%20a%20Device%20Driver%20to%20Run%20on%20an%20Intel-Based%20Macintosh.md)[Previous](Debugging%20Drivers.md)

# Testing and Deploying Drivers

You’ve created your driver and thoroughly debugged it. Now you’re ready to test it and prepare it for installation on your customers’s computers. This chapter outlines testing strategies and describes how to use the OS X Package Maker application to create an installable package.

Now that you’ve debugged your driver and you know it’s working perfectly, you should test it on as many differently configured computers and as many different operating system releases as you plan to support (or expect your customers to have).

The first step in testing your driver is to perform a basic quality-control pass. Ideally, many of these checks should be part of your day-to-day development methodology:

- Are the permissions and ownership of the kernel extension correct? For security reasons, no component of a KEXT should be writable by any user other than the superuser. What this entails is that:

  - All files and folders in the KEXT, including the KEXT itself, must be owned by the root user (UID 0).
  - All files and folders in the KEXT, including the KEXT itself, must be owned by the wheel group (GID 0).
  - All folders in the KEXT, including the KEXT itself, must have permissions 0755 (octal) or `rwxr-xr-x` (as shown by `ls -l`).
  - All files in the KEXT must have permissions 0644 (octal) or `rw-r--r--` (as shown by `ls -l`). A KEXT is not the place to store a user-space executable.

  In your post-build and post-install scripts, you can set the correct ownership and permissions of kernel extensions using these shell script commands:

```
/usr/sbin/chown -R root:wheel MyDriver.kext
find MyDriver.kext -type d -exec /bin/chmod 0755 {} \;
find MyDriver.kext -type f -exec /bin/chmod 0644 {} \;
```

  You can also copy the driver as root to a temporary location to give the kernel extension the proper ownership and permissions.
- Have you tested the driver for memory leaks? Does it unload properly?

  - Load the driver and then try to unload it (using `kextunload`); if it does not successfully unload, then the driver has live objects that have not been released. You’ll need to track down the mismatched retain and release.
  - Load the driver and periodically run the `ioclasscount` and `ioalloccount` tools on it. If you see growth in the count of instances or in a type of allocated memory, then your driver is leaking memory.
  - Make a list of every class your driver directly defines and every class your driver directly manipulates (such as OSString). Create a command-line script that calls `ioclasscount` on all these classes (you don’t have to call `ioclasscount` for each class, you can list all the classes on one line), set your system on a short sleep-wake cycle, and run the script every time your system sleeps and wakes. If you detect a leak (an increase in the count for a class), unload and reload your driver and perform the test again to make sure it’s your driver that’s leaking. In this way, you can find leaks that might otherwise take thousands of normal sleep-wake cycles to detect.
- Have you recently performed validation checks using `kextload -nt`? (See [Debugging Drivers](Debugging%20Drivers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombrfvbeeq2gijfeusi) for details.) These checks may reveal undeclared dependencies and other errors.
- Have you correctly set or incremented the version number for the kernel extension? This is especially important if you want an improved version of your driver to be selected during the matching process.

When you are ready to deploy the driver, build it using the Development build style (in Project Builder) to get the full range of debugging symbols. Save a copy of the driver in case you or another developer might ever need a symboled version of it. Then, to get the final product, strip the symbols from the driver using the `strip` tool. Note that you use the Development build style instead of the Deployment build style for the final build of the driver. The Deployment style introduces additional optimizations that do little to enhance driver performance and yet make it harder to match up symbols in the stripped and non-stripped versions of the binary.

Configuration testing aims to test the operation of your driver within a range of factors that stress-test its performance under various conditions, possibly revealing a latent bug. These factors include the following:

- __Multiprocessor systems__. With multiprocessor systems becoming more and more common, it is important to test your driver on such systems. Your driver code could be running on any processor at any moment. Consequently, testing your driver on a multiprocessor system—where preemption and rescheduling occur simultaneously on each processor—might reveal a race condition or a locking bug.
- __Memory configurations__. You should test your driver on systems ranging from those with 128 megabyte installed (the current minimum) up to those with 1 gigabyte or more installed (typical, for example, in video-production systems).
- __Computer models__. You should test your drivers on a wide variety of Power PC computers: G3 and G4, desktop and portable.
- __Other hardware__. You should also test your driver with varied and even extreme assortments of hardware attached. For example, if you’re testing a driver for a USB device, you might test it with a dozen or so other USB devices attached.
- __OS X releases__. Obviously, you should also test your driver on a range of OS X versions that are currently in use.

Many drivers implement some form of power management, responding to or initiating requests to sleep, power down, or power up. You should ensure this capability is thoroughly tested. One way to test power management is power cycling. Put a system with your driver installed on it asleep, then wake it up. Repeat this sequence many times (the more the better) to see if a bug in your power-management code surfaces.

If your driver is for a device that is “hot-swappable” (FireWire, USB, and PC Card), test the code in your driver that is responsible for handling device connection and (especially) device removal. You want to ensure that the driver stack is gracefully torn down when a device is disconnected. As with power-management testing, disconnect and reconnect the device many times to see if the sheer repetition of the event reveals a bug.

Here are a few more suggestions to help you test your driver:

- If your driver controls a Human Interface (HI) device or accepts input of any kind (such as an audio driver), be sure to exercise all possible types of input, including fringe cases. For example, for a keyboard driver you might want to test various combinations involving the Command, Control, Option, Escape, Function, and other keys. For audio drivers (that control audio input), you might want to test how the driver performs across a range of sound frequencies.
- Isolate and exercise layers of your driver. With a mass storage driver, for example, test how the driver performs at the file-system level with blocks of data that are above and below virtual-memory page size (4 kilobytes). Issue random sized read and write commands, and see how the driver behaves when a file-system check (`fsck`) is conducted.
- Last, but definitely not least, always consider your driver from the viewpoint of security. If your driver relies upon a user-space daemon that is `setuid`, make sure that the executable isn’t world-writable. Verify that the installation process does not present opportunities for security infringements and, generally, that there is no way for a non-administrative user to gain control of the device.

If possible, you can let your Apple developer technical support contact know you’re about to ship a driver. If you supply Apple with the `CFBundleIdentifier` and version that uniquely identifies your driver, Apple will know who to contact if a problem report appears that seems to point to your driver.

Before you send your driver out the door, you should package it so it’s easy for your customers to install. OS X provides the Package Maker application (available in `/Developer/Applications` and a command-line version available in `/Developer/Applications/Utilities/PackageMaker.app/Contents/MacOS/PackageMaker`) to create your package. The Package Maker application guides you through the creation of a package and creates the required files from information you enter in its editing windows, making the process almost automatic. The command-line tool requires you to supply the necessary files you’ve created yourself. For more detailed information on how to use Package Maker to create a package, see the Package Maker Help menu. For more information on using the command-line version, type `./PackageMaker -help` from the `/Developer/Applications/Utilities/PackageMaker.app/Contents/MacOS` directory.

The following sections provide an overview of the components of a Package Maker package, describe what comprises a valid package, and outline how your package gets installed. If you use another package-making tool to create your package, make sure the resulting package contains all the required elements discussed in these sections.

A Package Maker package is an `Info.plist`-based NSBundle object that contains the information the Installer requires to install software on an OS X system. Package contents are separated into required global resources and optional localizable resources. [Listing 8-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombsfvbussccijfemri) shows the format of a package named MyPackage.

__Listing 8-1__  PackageMaker format for MyPackage


```
MyPackage.pkg
    Contents
        Info.plist
        Archive.pax.gz
        Archive.bom
        Resources
            /* Optional, localizable package-description information */
            Description.plist

            /* Optional, localizable documents */
            License document
            ReadMe document
            Welcome document

            /* Optional scripts */
            preinstall script
            postinstall script
            preupgrade script
            postupgrade script
            preflight script
            postflight script

            /* Optional check tools */
            InstallationCheck tool
            VolumeCheck tool

            /* Optional, localizable background image */
            background

            /* Optional language project folders. If present, these */
            /* folders contain localized versions of Description.plist, */
            /* License, ReadMe, Welcome, and background files. */
            English.lproj
            Japanese.lproj
```

Package Maker creates the package’s `Info.plist` file using the information you enter in the Info window. Information such as the default installation location and level of user authorization required allow you to customize the installation of your package’s contents.

The `Archive.bom` and `Archive.pax.gz` files are required files Package Maker creates for you using information you enter in the Files window. The `Archive.bom` file is a bill-of-materials file that describes the contents of the package to the Installer. The `Archive.pax.gz` file is a compressed archive containing the contents of a package. (In earlier versions of Package Maker, these filenames incorporated the package name, as in `MyPackage.bom` and `MyPackage.pax.gz`.)

The Resources folder contains documents, scripts, and tools you provide for the Installer to use during installation. With the exception of the `Description.plist` file (which contains the information you enter in the Description window), Package Maker does not create these files for you. You have complete control over the contents of these files, but you do have to follow Package Maker’s naming conventions, or the Installer will not find and execute them.

You must name your localizable documents `License`_.extension_, `ReadMe`_.extension_, and `Welcome`_.extension_ where _extension_ is `html`, `rtf`, `rtfd`, `txt`, or no extension at all. In OS X version 10.2, you can customize the background image the Installer displays when it opens the package. You must name your background picture file `background.`_extension_, where _extension_ is `jpg`, `tif`, `tiff`, `gif`, `pict`, `eps`, or `pdf`.

The optional scripts must also follow Package Maker’s naming conventions. You can perform a wide range of tasks in these scripts but you should take care not to overburden them or the installation speed will suffer. For example, you could create folders in a preflight script, but it would be better to set up the necessary folders in the archive. As a general rule, you should try to create your package so that it provides everything your software needs, using the scripts sparingly to perform dynamic tasks during the install process. If you do include scripts to run during installation, be sure to make them executable.

If you need to examine a computer’s configuration prior to installation to determine, for example, if there is sufficient memory to run the Installer, or if some other software is present, you can provide an InstallationCheck tool. The Installer runs this tool (if it is present) when it first opens a package. As with the optional scripts, you must follow Package Maker’s naming convention and you must make the tool executable. In addition, the InstallationCheck tool must return an integer error code. The error code is used as a bitfield that encodes information about the installation status that the Installer can interpret. The Installer uses some of the bits as an index into files of error messages, either predefined by the Installer or custom. If you choose to define your own set of error messages, you create a localizable `InstallationCheck.strings` file and place it in your localized `.lproj` folder.

The Installer generally gives the user a choice of volumes on which to install your package. If you need to disable one or more volume choices, you can provide a VolumeCheck tool (you must name the tool VolumeCheck and make it executable). The Installer runs this tool (if it is present) before it displays the Target Select window. Like InstallationCheck, VolumeCheck returns an integer result code that is treated as a bitfield. The Installer uses some bits to identify several properties about the status of VolumeCheck and others as an index into either a predefined or a custom error message file named `VolumeCheck.strings`.

A metapackage is simply a package of prebuilt packages. If, for example, you offer a suite of drivers, you can create a metapackage to contain them all and allow your customers to install the ones they choose. To create a metapackage, select New Meta Package from Package Maker’s File menu.

A metapackage has the same components as a single package, with the addition of a list of subpackages (each of which must be a valid package). For specific differences in the `Info.plist` keys, see Package Maker’s Package Format Notes.

Package Maker provides a validation tool you can run on your package to flag potential problems (to run it, select Validate Package in the Tools menu). You can run the tool on packages built with any version of Package Maker. The tool checks for the presence of required files and that the scripts are executable. A valid package must contain

- a _.bom_ file
- a `.pax.gz` file unless the package is a receipt or has the Alternate Source Location key or the Proxy Package Location key set (these keys are defined in Package Maker’s Package Format Notes)
- an `Info.plist` file (for packages built with the newest version of Package Maker) or `.info` file (for packages built with older versions of Package Maker)
- a `.sizes` file, if the package is built with an older version of Package Maker
- executable scripts and tools, if scripts and tools are present

A valid metapackage must contain

- a `.list` file, if the metapackage is built with an older version of Package Maker
- a package list array in its `Info.plist` file, if the metapackage is built with the newer version of Package Maker
- the subpackages listed in the package list array, if the metapackage is built with the newer version of Package Maker

When the Installer installs a single package, it performs the following steps:

1. Run the InstallationCheck script (if present).
2. Display the Welcome screen.
3. Display the ReadMe screen.
4. Display the License screen.
5. Run the VolumeCheck script (if present) for each available volume.
6. Display the volume selection screen.
7. Wait for the user to select the target volume and click Install.
8. Run the preflight script, if present.
9. Run the preinstall script (or preupgrade script, if this is an upgrade), if present.
10. Copy the files to the target drive (if this is an upgrade, some files may be copied to an intermediate directory first).
11. Run the postinstall script (or postupgrade script, if this is an upgrade), if present.
12. If this is an upgrade, copy the files in the intermediate directory to their final destination.
13. Copy the receipt to the target drive’s Receipts folder.
14. Run the postflight script, if present.
15. Reboot or quit, depending on the package’s flags.

The Installer performs a similar set of steps when installing a metapackage:

1. Run the InstallationCheck script, if present.
2. Display the Welcome screen.
3. Display the ReadMe screen.
4. Display the License screen.
5. Run the VolumeCheck script (if present) for each available volume.
6. Display the volume selection screen.
7. Wait for the user to select the target volume and click Install.
8. Perform the following steps for each subpackage

   1. Run preflight script, if present.
   2. Run the preinstall script (or preupgrade script, if this is an upgrade), if present.
   3. Copy the files to the target drive (if this is an upgrade, some files may be copied to an intermediate directory first).
   4. Run the postinstall script (or postupgrade script, if this is an upgrade), if present.
   5. If this is an upgrade, copy the files in the intermediate directory to their final destination.
   6. Run the postflight script, if present.
9. Reboot or quit, depending on the metapackage’s flags.

If you’ve used another tool to create your package, you should examine the installed files carefully to make sure everything is where you want it to be.

[Next](Developing%20a%20Device%20Driver%20to%20Run%20on%20an%20Intel-Based%20Macintosh.md)[Previous](Debugging%20Drivers.md)

