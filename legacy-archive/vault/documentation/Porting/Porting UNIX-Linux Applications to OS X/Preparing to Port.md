---
title: Porting UNIX/Linux Applications to OS X
apple_id: TP30001003
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2012-06-11'
source_url: https://developer.apple.com/library/archive/documentation/Porting/Conceptual/PortingUnix/preparing/preparing.html
archived_at: '2026-07-18T01:50:47.819464Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Porting UNIX/Linux Applications to OS X](Introduction%20to%20Porting%20UNIX-Linux%20Applications%20to%20OS%20X.md)


[Next](Compiling%20Your%20Code%20in%20OS%20X.md)[Previous](Overview%20of%20OS%20X.md)

# Preparing to Port

A seasoned UNIX developer recognizes that no matter how similar two UNIX-based operating systems may be, there are always details that set one apart from another.

This chapter highlights areas to be aware of when compiling your code base for OS X. It notes details about compiler flags that are important to you, and gives insight into how to link different parts of your code in OS X. Many of these topics are covered more extensively in other resources as noted.

With few exceptions, this chapter applies to all varieties of UNIX developers. However, there are a few things that are specific to a given audience. These are pointed out as they appear.

If you are porting an open source application, you should first check to see if any of the open source port collections have already ported the application to avoid duplicating effort. You should also consider including your port in one of these collections to make it easier for others to take advantage of it. Finally, you should always make your changes available upstream to the original open source project for inclusion in future releases.

Some of the Darwin-based open source port collections include:

- MacPorts ([http://www.macports.org/](http://www.macports.org/))
- Fink ([http://fink.sourceforge.net/](http://fink.sourceforge.net/))
- GNU-Darwin ([http://www.gnu-darwin.org/](http://www.gnu-darwin.org/))

For more information on these port collections, visit their websites.

Before you bring the basic port of your code to OS X, make sure that you have the requisite tools for the task. It helps to know what is and isn’t available to you by default.

The most important thing to do before porting an application is to familiarize yourself with the OS X environment. In particular, you should familiarize yourself with the System Preferences application (and customize your computer to suit) and the Terminal application (to obtain a command-line interface).

The System Preferences application is located in the `Applications` folder at the root level of your hard drive. The `Terminal` application is located in the `Utilities` folder (which is within the `Applications` folder at the root level of your hard drive).

Once you have a Terminal window open, you can take advantage of a basic selection of common tools, assuming that they are installed. Before using OS X as a development platform, you should make sure that the BSD subsystem is installed. On OS X v10.4, this option is installed by default, but on previous versions, it was not.

You can check for this by looking for the BSD package receipt, `BSD.pkg`, in `/Library/Receipts`. If this receipt is not present on your system, you must reinstall OS X. When you do, you must customize the installation by checking the BSD Subsystem checkbox.

With the BSD subsystem installed, a look through `/bin` and `/usr/bin` should reveal a familiar environment. Welcome home.

Because OS X has a BSD core, you have access to the numerous open source tools that you are already familiar with (like the GNU tools, for example).

The OS X Xcode Tools package provides additional tools that you will need to install to round out your development environment. These are not part of the default installation, but are essential to you. They contain some of the most important tools, such as the compiler (gcc) and debugger (gdb).

Most (if not all) of the tools described in this document are part of the Xcode Tools installation, so if you don’t find `autoconf` or `make`, for example, that probably means you don’t have Xcode Tools installed.

You can find the Xcode Tools Installer on your OS X DVD (or as one of the CDs in the CD version). In addition, you can always obtain the very latest version online from the Apple Developer Connection (ADC) website, [http://connect.apple.com](http://connect.apple.com/) or the app store. You need an ADC account to download the Developer Tools. Free accounts are available for those who just need access to the tools.

After installing the OS X Developer Tools, you will have a selection of new tools to take advantage of:

- `/usr/bin` now contains more command-line tools than were supplied by the BSD package alone, most notably gcc and gdb. `/usr/bin/cc` defaults to gcc 3 in OS X version 10.2 and later, but gcc 2.95.2 is also available. See [Choosing a Compiler](Compiling%20Your%20Code%20in%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnjqfvbegskhi5cukqi) for more information.
- Xcode is a graphical integrated development environment for applications in multiple programming languages.
- Interface Builder provides a simple way to build complex user interfaces.
- FileMerge lets you graphically compare and merge files and directories.
- IORegistryExplorer helps you determine which devices are registered with the I/O KIT. See [Device Drivers](Additional%20Features.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnjwfvbecssiircugrq) for a discussion of the I/O Kit.
- MallocDebug analyzes all allocated memory in an application. It can measure the memory allocated since a given point in time and detect memory leaks
- PackageMaker builds easily distributable OS X packages.

Documentation for these tools is available from the Apple Technical Publications website.

OS X-native applications can be built in a number of environments. Most UNIX utilities are built using makefiles, though some are built using build scripts, imakefiles, or various other mechanisms.

If you are porting a UNIX command-line tool for personal use, you probably want to continue using the existing build environment, because keeping multiple build environments synchronized can be tricky at best. However if you are porting a more extensive tool and you plan to add an OS X GUI to the tool, you may find it more convenient to work with the project in a development environment such as Xcode.

Although Xcode keeps track of build settings in its own preferences files for information beyond what could normally be maintained in a makefile, it can also work closely with your project’s makefiles. If you want to use Xcode for development in OS X, you can include a makefile in a Xcode project as follows:

1. Launch Xcode.
2. Choose New Project from the File menu.
3. Select whatever project type you are targeting. If you ultimately want an application, select something like Cocoa Application. If you are just trying to build a command-line utility, select one of the tools—for example, Standard Tool.
4. Follow the prompts to name and save your project. A new default project of that type is opened.
5. Open the Targets disclosure triangle and delete any default targets that may exist.
6. From the Project menu, Choose New Target.
7. Select “External Target” from the list. If this is not shown in the “Special Targets” list, you are not running the latest version of Xcode. Upgrade first.
8. Follow the prompts to name that target. When you have done this, a target icon with the name you just gave it appears in the Targets pane of the open Xcode window.
9. Double-click that new target. You should now see a new window with the build information for this target. This is _not_ the same thing as clicking info. You _must_ double-click the target itself.
10. In the “Custom Build Command” section of the target inspector, change the field called “Directory” to point to the directory containing your makefile, and change any other settings as needed. For example, in the Custom Build Settings pane, you could change Build Tool from `/usr/bin/gnumake` to `/usr/bin/bsdmake`. More information on the fields is available in Xcode Help.
11. Change the active target to your new target by choosing "Set Active Target" from the Project menu.
12. Add the source files to the project. To do this, first open the disclosure triangle beside the “Source” folder in the left side of the project window. Next, drag the folder containing the sources from the Finder into that “Source” folder in Xcode. Tell Xcode not to copy files. Xcode will recursively find all of the files in that folder. Delete anything you don’t want listed.
13. When you are ready to build the project, click the Build and Run button in the toolbar, select Build from the Build menu, or just press Command-B.
14. Once the project is built, tell Xcode where to find the executable by choosing “New Custom Executable” from the Project menu. Choose the path where the executable is located, then add the name of the executable.
15. Run the resulting program by pressing Command-R.

This should get you started in bringing your application into the native build environment of OS X.

Before you compile an application in OS X, be aware that the OS X native windowing and display subsystem, Quartz, is based on the Portable Document Format (PDF). Quartz consists of a lightweight window server as well as a graphics rendering library for two-dimensional shapes. The window server features device-independent color and pixel depth, layered compositing, and buffered windows. The rendering model is PDF based.

Quartz is not an X Window System implementation. If you need an X11R6 implementation, you can easily install one. For more information, see [X11R6](Using%20Traditional%20UNIX%20Graphical%20Environments.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnjtfvkfawcsivddcmbz).

Information on the graphical environments available to you can be found in [Choosing a Graphical Environment for Your Application](Choosing%20a%20Graphical%20Environment%20for%20Your%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnjrfvkfawcsivddcmbr) along with some things to consider when choosing a graphical environment.

Beginning in version 10.4, OS X supports execution of 64-bit command-line tools. It is also possible to use a 32-bit OS X front-end application to provide a user interface through careful use of client-server communication.

This document primarily covers general porting issues. Issues specific to 64-bit computing are beyond the scope of this document. For additional information on porting 64-bit software to OS X, see the document _[64-Bit Transition Guide](../../Darwin/64-Bit%20Transition%20Guide/Introduction%20to%2064-Bit%20Transition%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanru)_.

[Next](Compiling%20Your%20Code%20in%20OS%20X.md)[Previous](Overview%20of%20OS%20X.md)

