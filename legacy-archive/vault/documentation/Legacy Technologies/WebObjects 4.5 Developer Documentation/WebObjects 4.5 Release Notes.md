---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/ReleaseNotes/ReleaseNotes.html
archived_at: '2026-07-15T08:09:53.608410Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Release Notes

WebObjects Release Notes  Copyright 1998-2000 by Apple Computer, Inc. All Rights Reserved.

# WebObjects 4.5 Release Notes

_Last Updated March 24, 2000_

This document lists those problems known to exist in WebObjects 4.5. Release notes for Enterprise Objects Framework are listed separately, and can be found [here](Enterprise%20Objects%20Framework%204.5%20Release%20Notes.md).

Among the documention supplied with this release is ["What's New in WebObjects 4.5"](What%27s%20New%20in%20WebObjects%204.5.md), which details those features that are new or have substantially changed since the last release of WebObjects. As well, ["WebObjects Post-Installation Instructions"](WebObjects%20Release%204.5%20Post-Installation%20Instructions.md) details a number of important steps you may need to take--depending on your particular configuration--after installing WebObjects.

## Known Problems in This Release

---

### Installation

|  |  |  |
| --- | --- | --- |
| Reference | 2425526 | 2425526 |
| Problem | System paths longer than 255 characters can cause problems during installation on Windows NT. | System paths longer than 255 characters can cause problems during installation on Windows NT. |
| Description | During installation to an NT machine with long system paths (greater than 255 characters) there may be some problems. The installer will be unable to include necessary additions to the PATH environment variable, which means that some of the post-install scripts will fail because they can't locate needed commands. It also means that installed applications and services won't work following the installation. | During installation to an NT machine with long system paths (greater than 255 characters) there may be some problems. The installer will be unable to include necessary additions to the PATH environment variable, which means that some of the post-install scripts will fail because they can't locate needed commands. It also means that installed applications and services won't work following the installation. |
| Workaround | When installing try choosing an install path that isn't very long. For example, the default "C:\Apple" is a good choice. If you have a number of items in your system path you might try moving those items to a user PATH environment variable. To do this, create a user environment variable called PATH, add the values from the system path environment variable to it, and include %PATH% in the value (for instance, "%PATH%;C:\MyStuff"). Do not, however, move any of the Windows system path settings to the user path variable. | When installing try choosing an install path that isn't very long. For example, the default "C:\Apple" is a good choice. If you have a number of items in your system path you might try moving those items to a user PATH environment variable. To do this, create a user environment variable called PATH, add the values from the system path environment variable to it, and include %PATH% in the value (for instance, "%PATH%;C:\MyStuff"). Do not, however, move any of the Windows system path settings to the user path variable. |
|  |  |  |
|  |  |  |
| Reference | 2424664 | 2424664 |
| Problem | Selecting a cgi-bin (scripts) or document root directory with spaces in the path name during installation of WebObjects on Windows NT may result in files not being copied over or updated. | Selecting a cgi-bin (scripts) or document root directory with spaces in the path name during installation of WebObjects on Windows NT may result in files not being copied over or updated. |
| Description | On Windows NT if you choose a cgi-bin or document root directory with one or more spaces in the path name, some of the installation scripts won't function properly. The result is that the adaptors will not be copied into the selected cgi-bin directory, the document root files won't be copied into the selected document root directory, and the WebServerConfig.plist file won't be updated. | On Windows NT if you choose a cgi-bin or document root directory with one or more spaces in the path name, some of the installation scripts won't function properly. The result is that the adaptors will not be copied into the selected cgi-bin directory, the document root files won't be copied into the selected document root directory, and the WebServerConfig.plist file won't be updated. |
| Workaround | The best solution is to install your web server into a directory without spaces in the path. You may also manually copy the appropriate WebObjects adaptor from the $NEXT_ROOT/Library/WebObjects/Adaptors directory to your cgi-bin directory, and the document root directory from $NEXT_ROOT/Library/WebObjects/WODocumentRoot to your web server's document root directory. If you choose to manually copy these files you'll also need to edit the WebServerConfig.plist file so that the DocumentRoot value is set to your web server's document root and the WOAdaptorURL value includes the path to your cgi-bin directory. | The best solution is to install your web server into a directory without spaces in the path. You may also manually copy the appropriate WebObjects adaptor from the $NEXT_ROOT/Library/WebObjects/Adaptors directory to your cgi-bin directory, and the document root directory from $NEXT_ROOT/Library/WebObjects/WODocumentRoot to your web server's document root directory. If you choose to manually copy these files you'll also need to edit the WebServerConfig.plist file so that the DocumentRoot value is set to your web server's document root and the WOAdaptorURL value includes the path to your cgi-bin directory. |
|  |  |  |
|  |  |  |
| Reference | 2253233 | 2253233 |
| Problem | machd and nmserver aren't always installed as NT services. | machd and nmserver aren't always installed as NT services. |
| Description | On some platforms, the Mach emulation Daemon and the Netname Server sometimes don't properly install themselves as NT services. Among other things, this will cause YellowBox apps (such as EOModeler, ProjectBuilder, and WebObjectsBuilder) to fail to launch; they will hang at the splash screen and complain that they cannot contact the window server.    Symptoms are as follows:    0) Install WebObjects.  1) Open the "Services" control panel. Check whether two services exist therein:    "Apple Mach Daemon"  "Apple NetName Server" | On some platforms, the Mach emulation Daemon and the Netname Server sometimes don't properly install themselves as NT services. Among other things, this will cause YellowBox apps (such as EOModeler, ProjectBuilder, and WebObjectsBuilder) to fail to launch; they will hang at the splash screen and complain that they cannot contact the window server.    Symptoms are as follows:    0) Install WebObjects.  1) Open the "Services" control panel. Check whether two services exist therein:    "Apple Mach Daemon"  "Apple NetName Server" |
| Workaround | In order to fix this, open up a Bourne shell and type the following:    1) cd $NEXT_ROOT/Library/System  2) ./machd.exe -install  3) ./nmserver.exe -install | In order to fix this, open up a Bourne shell and type the following:    1) cd $NEXT_ROOT/Library/System  2) ./machd.exe -install  3) ./nmserver.exe -install |
|  |  |  |
|  |  |  |
| Reference | 2252905 | 2252905 |
| Problem | Uninstalling from an account other than Administrator can result in some items not being removed | Uninstalling from an account other than Administrator can result in some items not being removed |
| Description | If you happen to uninstall WebObjects or Yellow Box from an account that doesn't have Administrator privileges, some items--such as the Start Menu items--will not be removed. | If you happen to uninstall WebObjects or Yellow Box from an account that doesn't have Administrator privileges, some items--such as the Start Menu items--will not be removed. |
| Workaround | Uninstall from the Administrator account, or from the account with administrator privileges that was used to install the product. | Uninstall from the Administrator account, or from the account with administrator privileges that was used to install the product. |
|  |  |  |
|  |  |  |
| Reference | 2252815 | 2252815 |
| Problem | Existing Sybase environment variable is removed during installation of Sybase Client Libraries | Existing Sybase environment variable is removed during installation of Sybase Client Libraries |
| Description | If you choose to install the Sybase Client Libraries in the Yellow Box or WebObjects Installer, any existing Sybase environment variable will be replaced by a value that points to the newly-installed client libraries. After uninstalling Yellow Box or WebObjects, the Sybase variable is completely removed. | If you choose to install the Sybase Client Libraries in the Yellow Box or WebObjects Installer, any existing Sybase environment variable will be replaced by a value that points to the newly-installed client libraries. After uninstalling Yellow Box or WebObjects, the Sybase variable is completely removed. |
| Workaround | Save your existing Sybase environment variable into another variable, such as Sybase_bak. After you uninstall set your Sybase environment variable back to the value saved in the Sybase_bak variable. | Save your existing Sybase environment variable into another variable, such as Sybase_bak. After you uninstall set your Sybase environment variable back to the value saved in the Sybase_bak variable. |
|  |  |  |
|  |  |  |
| Reference | 2250013 | 2250013 |
| Problem | Incomplete uninstalls cause subsequent uninstalls to fail | Incomplete uninstalls cause subsequent uninstalls to fail |
| Description | If the NT uninstaller application is aborted or fails during the uninstall process it will cause subsequent uninstalls to fail. | If the NT uninstaller application is aborted or fails during the uninstall process it will cause subsequent uninstalls to fail. |
| Workaround | If uninstallation is aborted or fails, follow the steps outlined in the Readme.txt file in the Uninstall/UninstallWO4.0 directory on your CD. | If uninstallation is aborted or fails, follow the steps outlined in the Readme.txt file in the Uninstall/UninstallWO4.0 directory on your CD. |
|  |  |  |
|  |  |  |
| Reference | 2235477 | 2235477 |
| Problem | Attempting to uninstall while WebObjects or Yellow Box applications are running can cause the uninstaller to hang | Attempting to uninstall while WebObjects or Yellow Box applications are running can cause the uninstaller to hang |
| Description | If you launch the uninstaller while WebObjects or Yellow Box applications are running in the background, the uninstaller is likely to hang. | If you launch the uninstaller while WebObjects or Yellow Box applications are running in the background, the uninstaller is likely to hang. |
| Workaround | Close all WebObjects and Yellow Box applications before starting the uninstaller. | Close all WebObjects and Yellow Box applications before starting the uninstaller. |
|  |  |  |
|  |  |  |
| Reference | 2173328 | 2173328 |
| Problem | Installing WebObjects onto a machine that already has Yellow Box, OpenStep, or WebObjects installed can cause subsequent uninstalls to fail. | Installing WebObjects onto a machine that already has Yellow Box, OpenStep, or WebObjects installed can cause subsequent uninstalls to fail. |
| Description | If you install WebObjects onto a machine with an existing version of WebObjects, Yellow Box, or OpenStep, it is possible that the uninstaller will be disabled. Some files shared by these releases will be removed by the uninstall, causing problems with the originally installed product. | If you install WebObjects onto a machine with an existing version of WebObjects, Yellow Box, or OpenStep, it is possible that the uninstaller will be disabled. Some files shared by these releases will be removed by the uninstall, causing problems with the originally installed product. |
| Workaround | Uninstall any previous version of WebObjects, Yellow Box, or OpenStep before installing new versions of WebObjects or Yellow Box. | Uninstall any previous version of WebObjects, Yellow Box, or OpenStep before installing new versions of WebObjects or Yellow Box. |
|  |  |  |
|  |  |  |
| Reference | 2172707 | 2172707 |
| Problem | Installing into a deep directory structure may prevent the uninstaller from working. | Installing into a deep directory structure may prevent the uninstaller from working. |
| Description | If you install into a deep directory structure you may find that the uninstaller doesn't work. This is due to limitations in the file system path length. | If you install into a deep directory structure you may find that the uninstaller doesn't work. This is due to limitations in the file system path length. |
| Workaround | Don't install into directories that are more than two or three levels deep, and use short directory names. | Don't install into directories that are more than two or three levels deep, and use short directory names. |
|  |  |  |
|  |  |  |
| Reference | 1685375 | 1685375 |
| Problem | Installing WebObjects into the "Program Files" directory--or any directory with spaces in the directory name--causes problems in the installer | Installing WebObjects into the "Program Files" directory--or any directory with spaces in the directory name--causes problems in the installer |
| Description | If you try to install WebObjects into a directory with spaces in the directory name, some of the installation scripts won't function properly. The result is that some of the services will not be started, documentation will not be indexed, and other necessary tasks will not be completed. | If you try to install WebObjects into a directory with spaces in the directory name, some of the installation scripts won't function properly. The result is that some of the services will not be started, documentation will not be indexed, and other necessary tasks will not be completed. |
| Workaround | Choose the default installation location, or install into a directory that doesn't have spaces in its name. | Choose the default installation location, or install into a directory that doesn't have spaces in its name. |
|  |  |  |
|  |  |  |
| Reference | 2410313 | 2410313 |
| Problem | Uninstall not clean if using NSAPI from default location. | Uninstall not clean if using NSAPI from default location. |
| Description | If you uninstall WebObjects 4.5 while running Netscape server the NSAPI adaptor most likely won't be removed because it resides in the $NEXT_ROOT directory and is in use by the server. | If you uninstall WebObjects 4.5 while running Netscape server the NSAPI adaptor most likely won't be removed because it resides in the $NEXT_ROOT directory and is in use by the server. |
| Workaround | We recommend that you copy the Netscape adaptor (NSAPI.dll) to another location, preferably under the Netscape root directory (/Netscape/Suitespot/WebObjects/WebObjects/dll, for example), and configure your server to use that dll. | We recommend that you copy the Netscape adaptor (NSAPI.dll) to another location, preferably under the Netscape root directory (/Netscape/Suitespot/WebObjects/WebObjects/dll, for example), and configure your server to use that dll. |
|  |  |  |
|  |  |  |
| Reference | 2428687 | 2428687 |
| Problem | Uninstallation on Solaris or HP-UX can leave files behind. | Uninstallation on Solaris or HP-UX can leave files behind. |
| Description | On HP-UX and Solaris, if the WebObjects adaptors are running when you attempt to uninstall WebObjects, wotaskd won't be killed and and subsequently a number of files and directories aren't removed during uninstallation. | On HP-UX and Solaris, if the WebObjects adaptors are running when you attempt to uninstall WebObjects, wotaskd won't be killed and and subsequently a number of files and directories aren't removed during uninstallation. |
| Workaround | Prior to uninstalling:  - Make sure that no WebObjects applications are running.   - Manually stop wotaskd.   - If any WebObjects adaptors are active, turn off your webserver (after WebObjects has been uninstalled, you can restart your webserver). | Prior to uninstalling:  - Make sure that no WebObjects applications are running.   - Manually stop wotaskd.   - If any WebObjects adaptors are active, turn off your webserver (after WebObjects has been uninstalled, you can restart your webserver). |
|  |  |  |
|  |  |  |
| Reference | 2410314 | 2410314 |
| Problem | The WebObjects cleanup script doesn't work when copied to the desktop of a Windows 2000 machine. | The WebObjects cleanup script doesn't work when copied to the desktop of a Windows 2000 machine. |
| Description | If you copy the WebObjects cleanup kit to the desktop of a Windows 2000 machine and follow the instructions in the ReadMe.txt file, you'll find that the cleanup script doesn't work. The reason is that the bourne shell (sh.exe) doesn't work from the desktop of a Windows 2000 machine. | If you copy the WebObjects cleanup kit to the desktop of a Windows 2000 machine and follow the instructions in the ReadMe.txt file, you'll find that the cleanup script doesn't work. The reason is that the bourne shell (sh.exe) doesn't work from the desktop of a Windows 2000 machine. |
| Workaround | Use the cleanup kit directly from the CD or copy it to a location other than the desktop. | Use the cleanup kit directly from the CD or copy it to a location other than the desktop. |
|  |  |  |
|  |  |  |
| Reference | 2410309 | 2410309 |
| Problem | Uninstalling WebObjects 4.5 on Windows NT produces an error indicating that the uninstaller cannot find foundation.dll in the path. | Uninstalling WebObjects 4.5 on Windows NT produces an error indicating that the uninstaller cannot find foundation.dll in the path. |
| Description | During uninstallation of WebObjects 4.5 for Windows you may see an error to the effect that the uninstaller is unable to find foundation.dll in the specified path. This usually prevents WOService and the WebObjects Task Daemon services from being stopped and removed. When you restart your computer you may get a message that it is trying to start woservice or wotaskd but cannot because they no longer exist. | During uninstallation of WebObjects 4.5 for Windows you may see an error to the effect that the uninstaller is unable to find foundation.dll in the specified path. This usually prevents WOService and the WebObjects Task Daemon services from being stopped and removed. When you restart your computer you may get a message that it is trying to start woservice or wotaskd but cannot because they no longer exist. |
| Workaround | Be sure that you quit all other tasks while uninstalling. Otherwise, these tasks may prevent services from terminating before files are removed, resulting in this error.    If you happen to have this error during uninstallation; continue with the uninstall. When it has completed run the cleanup script in the Uninstall/UninstallWO4.5 directory, in the directory that contains your WebObjects 4.5 installation for Windows. Then restart your machine. | Be sure that you quit all other tasks while uninstalling. Otherwise, these tasks may prevent services from terminating before files are removed, resulting in this error.    If you happen to have this error during uninstallation; continue with the uninstall. When it has completed run the cleanup script in the Uninstall/UninstallWO4.5 directory, in the directory that contains your WebObjects 4.5 installation for Windows. Then restart your machine. |
|  |  |  |
|  |  |  |
| Reference | 2409092 | 2409092 |
| Problem | During installation of WebObjects on Solaris or HP-UX, typing "q" to quit at the C string character encoding prompt does not quit the install. | During installation of WebObjects on Solaris or HP-UX, typing "q" to quit at the C string character encoding prompt does not quit the install. |
| Description | During the installation of WebObjects on Solaris and HP-UX you are asked to choose which C string character encoding you are going to use. If you type "q" to quit the install at that prompt, the installer will try to continue and will display a number of errors. | During the installation of WebObjects on Solaris and HP-UX you are asked to choose which C string character encoding you are going to use. If you type "q" to quit the install at that prompt, the installer will try to continue and will display a number of errors. |
| Workaround | If you need to quit out of the installation, type "q" at any of the previous prompts which allow it, or type "ctrl-C". | If you need to quit out of the installation, type "q" at any of the previous prompts which allow it, or type "ctrl-C". |
|  |  |  |
|  |  |  |
| Reference | 2327908 | 2327908 |
| Problem | Java Client applications need the Java Plugin from Sun. | Java Client applications need the Java Plugin from Sun. |
| Description | We recommend running Java Client applets with Sun's Java Plugin. Java Client applications usually can't run in Netscape's VM, and they can experience some problems when running in Microsoft's Internet Explorer. | We recommend running Java Client applets with Sun's Java Plugin. Java Client applications usually can't run in Netscape's VM, and they can experience some problems when running in Microsoft's Internet Explorer. |
| Workaround | Get the Java plugin from http://www.javasoft.com/products/plugin/index.html | Get the Java plugin from http://www.javasoft.com/products/plugin/index.html |
|  |  |  |
|  |  |  |

---

### WebObjects Framework

|  |  |  |
| --- | --- | --- |
| Reference | 2424464 | 2424464 |
| Problem | Auto-sizing with PNG images does not work on Solaris or HPUX | Auto-sizing with PNG images does not work on Solaris or HPUX |
| Description | When a PNG image is used in a WebObjects component and auto-sizing enabled, a crash in the code calculating the size of the image can occur on Solaris or HPUX. | When a PNG image is used in a WebObjects component and auto-sizing enabled, a crash in the code calculating the size of the image can occur on Solaris or HPUX. |
| Workaround | Set the size manually or disable auto-sizing for that PNG image. | Set the size manually or disable auto-sizing for that PNG image. |
|  |  |  |
|  |  |  |
| Reference | 2406152 | 2406152 |
| Problem | NSString's writeToFile:atomically: fails if the path is not an absolute path. | NSString's writeToFile:atomically: fails if the path is not an absolute path. |
| Description | NSString's writeToFile:atomically: method fails and returns NO if the path is not an absolute path. This method only works when the filename starts with a "/" or is an absolute path. | NSString's writeToFile:atomically: method fails and returns NO if the path is not an absolute path. This method only works when the filename starts with a "/" or is an absolute path. |
| Workaround | Only supply absolute pathnames to writeToFile:. | Only supply absolute pathnames to writeToFile:. |
|  |  |  |
|  |  |  |
| Reference | 2394210 | 2394210 |
| Problem | "+n" is needed when linking frameworks or shared libraries with static libraries on HP-UX 11.0. | "+n" is needed when linking frameworks or shared libraries with static libraries on HP-UX 11.0. |
| Description | If you attempt to link a framework (or any shared library) with a static library (libXXX.a) using the standard WebObjects makefiles, the linker will not necessarily include all a of the symbols required by the shared library. This can result in a runtime crash when the runtime dynamic loader can't find some required symbols. | If you attempt to link a framework (or any shared library) with a static library (libXXX.a) using the standard WebObjects makefiles, the linker will not necessarily include all a of the symbols required by the shared library. This can result in a runtime crash when the runtime dynamic loader can't find some required symbols. |
| Workaround | Add the following to the top-level Makefile.preamble of the framework or shared library:    ifeq "$(PLATFORM_OS)" "hpux"  + # Ensure we load all library code on HP-UX. The linker seems a bit too good at deciding some symbol is unreferenced.  + OTHER_LDFLAGS += +n   endif    If you still see problems, try adding +vshlibunsats as well. This will detail which symbols aren't being located. Details can be found in the HP-UX ld man page. | Add the following to the top-level Makefile.preamble of the framework or shared library:    ifeq "$(PLATFORM_OS)" "hpux"  + # Ensure we load all library code on HP-UX. The linker seems a bit too good at deciding some symbol is unreferenced.  + OTHER_LDFLAGS += +n   endif    If you still see problems, try adding +vshlibunsats as well. This will detail which symbols aren't being located. Details can be found in the HP-UX ld man page. |
|  |  |  |
|  |  |  |
| Reference | 2275589 | 2275589 |
| Problem | When linking a database application on Solaris and HP-UX, the make process complains that it can't find the database client libraries. | When linking a database application on Solaris and HP-UX, the make process complains that it can't find the database client libraries. |
| Description | The database-client linking logic in the makefiles for Solaris and HP-UX does not check whether the environment variables have been properly set, so there's no more explanation provided by make beyond the fact that the client libraries can't be found. The linking step cannot succeed without one or more of the variables being set. | The database-client linking logic in the makefiles for Solaris and HP-UX does not check whether the environment variables have been properly set, so there's no more explanation provided by make beyond the fact that the client libraries can't be found. The linking step cannot succeed without one or more of the variables being set. |
| Workaround | You need to have one or more of the following environment variables set (and exported, if in the Bourne shell) in the environment that the make process is launched in:    1) ORACLE_HOME  2) SYBASE_HOME (can be set to the value of SYBASE)  3) NFORMIX_HOME (can be set to the value of INFORMIXDIR) | You need to have one or more of the following environment variables set (and exported, if in the Bourne shell) in the environment that the make process is launched in:    1) ORACLE_HOME  2) SYBASE_HOME (can be set to the value of SYBASE)  3) NFORMIX_HOME (can be set to the value of INFORMIXDIR) |
|  |  |  |
|  |  |  |
| Reference | 2424669 | 2424669 |
| Problem | setPageRefreshOnBacktrackEnabled doesn't work on Macintosh computers running Internet Explorer 4.01 or 4.5. | setPageRefreshOnBacktrackEnabled doesn't work on Macintosh computers running Internet Explorer 4.01 or 4.5. |
| Description | Macintosh clients running Microsoft Internet Explorer versions 4.01 and 4.5 appear to ignore the setting of WOApplication's setPageRefreshOnBacktrackEnabled method. | Macintosh clients running Microsoft Internet Explorer versions 4.01 and 4.5 appear to ignore the setting of WOApplication's setPageRefreshOnBacktrackEnabled method. |
| Workaround | If possible, use a different version of Internet Explorer, or use another browser such as Netscape. | If possible, use a different version of Internet Explorer, or use another browser such as Netscape. |
|  |  |  |
|  |  |  |
| Reference | 2418323 | 2418323 |
| Problem | Subprojects deeper than two levels do not render html in rapid turnaround mode | Subprojects deeper than two levels do not render html in rapid turnaround mode |
| Description | In development mode, rapid turnaround only works for the resource files in your top level project directory and in the first level of subprojects. | In development mode, rapid turnaround only works for the resource files in your top level project directory and in the first level of subprojects. |
| Workaround | Add to the NSProjectSearchPath user default each of the subprojects' subprojects directory paths. See the documentation on user defaults to learn how to modify them. | Add to the NSProjectSearchPath user default each of the subprojects' subprojects directory paths. See the documentation on user defaults to learn how to modify them. |
|  |  |  |
|  |  |  |
| Reference | 2417211 | 2417211 |
| Problem | Projects using the Plot.framework and importing Plot.h fail to compile | Projects using the Plot.framework and importing Plot.h fail to compile |
| Description | Applications using the Plot.framework with WebObjects 4.5 won't compile because Plot.h imports a missing header file: PFLabel.h. | Applications using the Plot.framework with WebObjects 4.5 won't compile because Plot.h imports a missing header file: PFLabel.h. |
| Workaround | There are two ways to work around this problem:  \* As root, edit the Library/Frameworks/Plot.framework/Headers/Plot.h header file and remove the "#import PFLabel.h" line.  \* Include the contents of Plot.h--except for the PFLabel.h import--in your code. | There are two ways to work around this problem:  \* As root, edit the Library/Frameworks/Plot.framework/Headers/Plot.h header file and remove the "#import PFLabel.h" line.  \* Include the contents of Plot.h--except for the PFLabel.h import--in your code. |
|  |  |  |
|  |  |  |
| Reference | 2408559 | 2408559 |
| Problem | Applications fail to launch under wotaskd but launch from a terminal shell | Applications fail to launch under wotaskd but launch from a terminal shell |
| Description | This situation can occur because the application needs environment settings not available from wotaskd (as root). An example is an application that uses Oracle - you might see "libclntsh.so.1.0: open failed" from the application if you run the wotaskd process manually.    If you su to root, the shell gets your environment variables, so you won't see this problem unless you explicitly reset LD_LIBRARY_PATH to what root gets by default. It occurs because the wotaskd startup script needs to include the Oracle shared library directory. | This situation can occur because the application needs environment settings not available from wotaskd (as root). An example is an application that uses Oracle - you might see "libclntsh.so.1.0: open failed" from the application if you run the wotaskd process manually.    If you su to root, the shell gets your environment variables, so you won't see this problem unless you explicitly reset LD_LIBRARY_PATH to what root gets by default. It occurs because the wotaskd startup script needs to include the Oracle shared library directory. |
| Workaround | Modify the wotaskd startup script to include the Oracle shared library directory in LD_LIBRARY_PATH when the Oracle adaptor is used by the program. | Modify the wotaskd startup script to include the Oracle shared library directory in LD_LIBRARY_PATH when the Oracle adaptor is used by the program. |
|  |  |  |
|  |  |  |
| Reference | 2290990 | 2290990 |
| Problem | Standard error and warning messages aren't localized. | Standard error and warning messages aren't localized. |
| Description | When running a WebObjects application, some standard error and warning messages--such as "You have backtracked too far"--can be sent directly to the user. These messages aren't localized and can confuse a non-English user. | When running a WebObjects application, some standard error and warning messages--such as "You have backtracked too far"--can be sent directly to the user. These messages aren't localized and can confuse a non-English user. |
| Workaround | Provide your own implementation for the different handle...Error methods in WOApplication:    - handlePageRestorationError (handlePageRestorationErrorInContext: in Objective-C) for localizing the "backtracked too far" messages  - handleSessionCreationError (handleSessionCreationErrorInContext: in Objective-C) when the application is unable to create a new Session  - handleSessionRestorationError (handleSessionRestorationErrorInContext: in Objective-C) when the WOApplication is unable to find the Session    Its always a good idea to implement the above methods, providing your own logic and user interface to handle exceptional conditions. | Provide your own implementation for the different handle...Error methods in WOApplication:    - handlePageRestorationError (handlePageRestorationErrorInContext: in Objective-C) for localizing the "backtracked too far" messages  - handleSessionCreationError (handleSessionCreationErrorInContext: in Objective-C) when the application is unable to create a new Session  - handleSessionRestorationError (handleSessionRestorationErrorInContext: in Objective-C) when the WOApplication is unable to find the Session    Its always a good idea to implement the above methods, providing your own logic and user interface to handle exceptional conditions. |
|  |  |  |
|  |  |  |
| Reference | 2273821 | 2273821 |
| Problem | The session size numbers on the WOStats page appear to be too large. | The session size numbers on the WOStats page appear to be too large. |
| Description | The session size numbers are only an indication of the actual size of the session. When an application has finished initializing, its memory size is noted. The session size that is reported is based on the memory increase since startup, and is divided by the current number of active sessions. The memory increase includes any cached data and/or data initialized after startup, skewing the size computation. | The session size numbers are only an indication of the actual size of the session. When an application has finished initializing, its memory size is noted. The session size that is reported is based on the memory increase since startup, and is divided by the current number of active sessions. The memory increase includes any cached data and/or data initialized after startup, skewing the size computation. |
| Workaround | None. | None. |
|  |  |  |
|  |  |  |
| Reference | 2265729 | 2265729 |
| Problem | .woo file entries from 3.5.1 cause weird initial values in WebObjects 4 | .woo file entries from 3.5.1 cause weird initial values in WebObjects 4 |
| Description | Old .woo files from a 3.5.1 project have lists of known page instance variables. These .woo files typically have key/value pairs where each key is an instance variable name and the corresponding value is a dictionary:    someIvar = {AutoInitialized = 1; TypeName = Object;};    At runtime this causes undesirable behavior: those instance variables are populated with "AutoInitialized = 1" in the WO4 user interface. | Old .woo files from a 3.5.1 project have lists of known page instance variables. These .woo files typically have key/value pairs where each key is an instance variable name and the corresponding value is a dictionary:    someIvar = {AutoInitialized = 1; TypeName = Object;};    At runtime this causes undesirable behavior: those instance variables are populated with "AutoInitialized = 1" in the WO4 user interface. |
| Workaround | Manually edit all .woo files to remove all instance definitions of the form "someIvar =". | Manually edit all .woo files to remove all instance definitions of the form "someIvar =". |
|  |  |  |
|  |  |  |
| Reference | 2260519 | 2260519 |
| Problem | [WOApplication port] returns a nonsensical result | [WOApplication port] returns a nonsensical result |
| Description | If your user defaults have WOPort=-1, then [[WOApplication application] port] will return -1. | If your user defaults have WOPort=-1, then [[WOApplication application] port] will return -1. |
| Workaround | Access the port number directly from the adaptor via:    WOApplication.application().adaptors().objectAtIndex(0).port(); | Access the port number directly from the adaptor via:    WOApplication.application().adaptors().objectAtIndex(0).port(); |
|  |  |  |
|  |  |  |
| Reference | 2418073 | 2418073 |
| Problem | Applications shouldn't listen on port 1085 | Applications shouldn't listen on port 1085 |
| Description | Port 1085 is reserved for the exclusive use of wotaskd. Any application that tries to listen on this port will fail. | Port 1085 is reserved for the exclusive use of wotaskd. Any application that tries to listen on this port will fail. |
| Workaround | Choose another port (note that ports above 1024 are quite commonly used - see iana.org for info). | Choose another port (note that ports above 1024 are quite commonly used - see iana.org for info). |
|  |  |  |
|  |  |  |
| Reference | 2343325 | 2343325 |
| Problem | \*\*\* Negative Session lifes corrupt stats page. | \*\*\* Negative Session lifes corrupt stats page. |
| Description | The statistics page will record inaccurate session life values for applications that programmatically shorten or extend their session life--by terminating sessions early, for example. Session life is computed by subtracting the session timeout period from the actual "age" of the session. If the session was terminated programmatically, the session's age is smaller than the session timeout, and the resulting "life" value is negative. | The statistics page will record inaccurate session life values for applications that programmatically shorten or extend their session life--by terminating sessions early, for example. Session life is computed by subtracting the session timeout period from the actual "age" of the session. If the session was terminated programmatically, the session's age is smaller than the session timeout, and the resulting "life" value is negative. |
| Workaround | None really. It's theoretically possible, by modifying the WOStatsPage in WOExtensions, to add the session timeout value to all sessions. Or you can subclass the WOStatisticsStore and change the values it gathers. | None really. It's theoretically possible, by modifying the WOStatsPage in WOExtensions, to add the session timeout value to all sessions. Or you can subclass the WOStatisticsStore and change the values it gathers. |
|  |  |  |
|  |  |  |
| Reference | 2276414 | 2276414 |
| Problem | Sessions are not dealloced with WOAditionalAdaptors | Sessions are not dealloced with WOAditionalAdaptors |
| Description | If you attempt to use the WOAdditionalAdaptors feature, sessions may not timeout. | If you attempt to use the WOAdditionalAdaptors feature, sessions may not timeout. |
| Workaround | None. | None. |
|  |  |  |
|  |  |  |
| Reference | 2181730 | 2181730 |
| Problem | WOStats memory statistics are missing on HP-UX | WOStats memory statistics are missing on HP-UX |
| Description | There is no memory information available in the WOStats component or the WOStatisticsStore object on HP-UX. | There is no memory information available in the WOStats component or the WOStatisticsStore object on HP-UX. |
| Workaround | None. | None. |
|  |  |  |
|  |  |  |
| Reference | 2181204 | 2181204 |
| Problem | terminateAfterTimeInterval: doesn't work if app is not "touched". | terminateAfterTimeInterval: doesn't work if app is not "touched". |
| Description | The WOApplication method terminateAfterTimeInterval: requires at least one request to be handled within the specified time interval for the application to shut down. | The WOApplication method terminateAfterTimeInterval: requires at least one request to be handled within the specified time interval for the application to shut down. |
| Workaround | None | None |
|  |  |  |
|  |  |  |
| Reference | 2219521 | 2219521 |
| Problem | My DirectAction raises when I trigger it | My DirectAction raises when I trigger it |
| Description | I added a DirectAction to my project and trying to access it from the browser causes a:  Oct 21 14:29:58 TestD2W2L2[2539] <WODirectActionRequestHandler>: NSInvalidArgumentException exception occurred while handling request:  _BRIDGEUnmappedInitMethodImp: the java class da does not implement any constructor that maps to the Objective C method initWithRequest: | I added a DirectAction to my project and trying to access it from the browser causes a:  Oct 21 14:29:58 TestD2W2L2[2539] <WODirectActionRequestHandler>: NSInvalidArgumentException exception occurred while handling request:  _BRIDGEUnmappedInitMethodImp: the java class da does not implement any constructor that maps to the Objective C method initWithRequest: |
| Workaround | Your DirectAction has to implement a constructor which takes a WORequest as an argument:    public class MyDirectAction extends WODirectAction {  public MyDirectAction(WORequest r) {  super(r);  ...  }    this is the constructor used by WOF during request handling | Your DirectAction has to implement a constructor which takes a WORequest as an argument:    public class MyDirectAction extends WODirectAction {  public MyDirectAction(WORequest r) {  super(r);  ...  }    this is the constructor used by WOF during request handling |
|  |  |  |
|  |  |  |
| Reference | 2418118 | 2418118 |
| Problem | Garbage collection never seems to be triggered in my application | Garbage collection never seems to be triggered in my application |
| Description | When concurrent request handling is enabled, garbage collection is forced every second. When concurrent request handling is disabled, however, garbage collection is triggered only if your application is Java based. | When concurrent request handling is enabled, garbage collection is forced every second. When concurrent request handling is disabled, however, garbage collection is triggered only if your application is Java based. |
| Workaround | Add an application.java to your project. | Add an application.java to your project. |
|  |  |  |
|  |  |  |
| Reference | 2282368 | 2282368 |
| Problem | Java Inner classes can create retain cycles resulting in leaked sessions and pages. | Java Inner classes can create retain cycles resulting in leaked sessions and pages. |
| Description | If you are using inner classes in your session and/or pages, be aware that non-static inner classes have a hidden pointer to their owning class. This make it easy to get into situation where a mixed objC-Java retain cycle is created, preventing the deallocation of all objects on that cycle. For example, if you pass an instance of an inner class of a page to one of its subcomponents, you get the following cycle:    yourSubcomponent > theInnerClassInstance > (through the hidden ivar) theTopLevelPage > (through normal objC containment) > yourSubComponent | If you are using inner classes in your session and/or pages, be aware that non-static inner classes have a hidden pointer to their owning class. This make it easy to get into situation where a mixed objC-Java retain cycle is created, preventing the deallocation of all objects on that cycle. For example, if you pass an instance of an inner class of a page to one of its subcomponents, you get the following cycle:    yourSubcomponent > theInnerClassInstance > (through the hidden ivar) theTopLevelPage > (through normal objC containment) > yourSubComponent |
| Workaround | One possible way to break the cycle is to use a \*static\* inner class, which does not have this hidden ivar. | One possible way to break the cycle is to use a \*static\* inner class, which does not have this hidden ivar. |
|  |  |  |
|  |  |  |
| Reference | 2275083 | 2275083 |
| Problem | Calls to setGarbageCollectionPeriod(n) seem to be ignored | Calls to setGarbageCollectionPeriod(n) seem to be ignored |
| Description | Calling setGarbageCollectionPeriod(n) in the constructor of an app doesn't seem to do anything. In fact, the garbage collection period is indeed set: the log displayed at startup, however, is incorrect and erroneously indicates that the call was ignored. | Calling setGarbageCollectionPeriod(n) in the constructor of an app doesn't seem to do anything. In fact, the garbage collection period is indeed set: the log displayed at startup, however, is incorrect and erroneously indicates that the call was ignored. |
| Workaround | None needed (ignore the garbage collection period displayed in the startup log). | None needed (ignore the garbage collection period displayed in the startup log). |
|  |  |  |
|  |  |  |
| Reference | 2265298 | 2265298 |
| Problem | tops conversion tool fails with "Unterminated character constant" message. | tops conversion tool fails with "Unterminated character constant" message. |
| Description | The tops conversion tool expects character constants in code to be one character long, (e.g., 'a'). Constants like '\u0048' causes tops to report an error like    \*\*\*Unterminated character constant at line X  \*\*\*Lexing error at line X | The tops conversion tool expects character constants in code to be one character long, (e.g., 'a'). Constants like '\u0048' causes tops to report an error like    \*\*\*Unterminated character constant at line X  \*\*\*Lexing error at line X |
| Workaround | Comment out the line with the long character constant, run tops, uncomment the line, and do the necessary conversion(s) on the line by hand | Comment out the line with the long character constant, run tops, uncomment the line, and do the necessary conversion(s) on the line by hand |
|  |  |  |
|  |  |  |
| Reference | 2305692 | 2305692 |
| Problem | WebObjects apps won't link against the Oracle 8.0.4 client libraries | WebObjects apps won't link against the Oracle 8.0.4 client libraries |
| Description | Oracle moved some symbols into different libraries in the 8.0.4 release, so the existing WebObjects makefiles don't get all the symbols you need. | Oracle moved some symbols into different libraries in the 8.0.4 release, so the existing WebObjects makefiles don't get all the symbols you need. |
| Workaround | Edit the makefile rule in /System/Developer/Makefiles/pb_makefiles/pdo-solaris-oracle.make to include the libclient.a library. Line 20 should read as follows:  OTHER_LIBS += -lclntsh -lclient -lcommon -lcore4 -lnlsrtl3 | Edit the makefile rule in /System/Developer/Makefiles/pb_makefiles/pdo-solaris-oracle.make to include the libclient.a library. Line 20 should read as follows:  OTHER_LIBS += -lclntsh -lclient -lcommon -lcore4 -lnlsrtl3 |
|  |  |  |
|  |  |  |
| Reference | 2182177 | 2182177 |
| Problem | On Solaris and HP-UX, RebuildWODefaultApp assumes 7.3 static linking for the Oracle adaptor. | On Solaris and HP-UX, RebuildWODefaultApp assumes 7.3 static linking for the Oracle adaptor. |
| Description | The RebuildWODefaultApp script contains no setting for the ORACLE_REL makefile variable. The default value for ORACLE_REL is 7.3-static. This causes the rebuild of WODefaultApp to fail if you don't have those client libraries installed. | The RebuildWODefaultApp script contains no setting for the ORACLE_REL makefile variable. The default value for ORACLE_REL is 7.3-static. This causes the rebuild of WODefaultApp to fail if you don't have those client libraries installed. |
| Workaround | Set an environment variable named ORACLE_REL to one of the following values:    "8.0-static", for Oracle 8.0.3 static client library linking  "7.3-dynamic", for Oracle 7.3.2 dynamic client library linking | Set an environment variable named ORACLE_REL to one of the following values:    "8.0-static", for Oracle 8.0.3 static client library linking  "7.3-dynamic", for Oracle 7.3.2 dynamic client library linking |
|  |  |  |
|  |  |  |
| Reference | 2235052 | 2235052 |
| Problem | Distributed Object connections don't work when a WebObjects app is multithreaded | Distributed Object connections don't work when a WebObjects app is multithreaded |
| Description | If a D.O. connection is made in either the main thread or a worker thread of an application and enableMultipleThreads isn't invoked on the NSConnection, an error will occur when the connection is accessed by a worker thread. | If a D.O. connection is made in either the main thread or a worker thread of an application and enableMultipleThreads isn't invoked on the NSConnection, an error will occur when the connection is accessed by a worker thread. |
| Workaround | When the connection is created, invoke enableMultipleThreads on the NSConnection. | When the connection is created, invoke enableMultipleThreads on the NSConnection. |
|  |  |  |
|  |  |  |
| Reference | 2282569 | 2282569 |
| Problem | Applications with dynamic images may leak them. | Applications with dynamic images may leak them. |
| Description | If you are testing such an application with the playback tool, the tool will not do the necessary callbacks to retrieve dynamic images. Therefore, these images will stay in the data cache of the app and never be released. Same can happen once deployed, as clients disable image loading from their browser. You will see your application leaking when it is not really, it is just waiting indefinitely for someone to come ask for an image. | If you are testing such an application with the playback tool, the tool will not do the necessary callbacks to retrieve dynamic images. Therefore, these images will stay in the data cache of the app and never be released. Same can happen once deployed, as clients disable image loading from their browser. You will see your application leaking when it is not really, it is just waiting indefinitely for someone to come ask for an image. |
| Workaround | When using the data, mimeType bindings for dynamic images, try to use the key binding as well. With the key binding set to employee.picture, only once will the picture be saved in memory and stay there, limiting the amount of data leaked. Otherwise, you can always use the -flushCache call on WOResourceManager regularly. This clears out everything from the data cache, so this may impact currently connected users. | When using the data, mimeType bindings for dynamic images, try to use the key binding as well. With the key binding set to employee.picture, only once will the picture be saved in memory and stay there, limiting the amount of data leaked. Otherwise, you can always use the -flushCache call on WOResourceManager regularly. This clears out everything from the data cache, so this may impact currently connected users. |
|  |  |  |
|  |  |  |
| Reference | 2408143 | 2408143 |
| Problem | WOMessage's setUserInfo method makes a copy of its dictionary argument. | WOMessage's setUserInfo method makes a copy of its dictionary argument. |
| Description | WOMessage's setUserInfo method unconditionally makes an immutable copy of the dictionary passed as an argument to the method. This can be a problem if changes made elsewhere to the dictionary's contents need to be reflected in the userInfo dictionary. | WOMessage's setUserInfo method unconditionally makes an immutable copy of the dictionary passed as an argument to the method. This can be a problem if changes made elsewhere to the dictionary's contents need to be reflected in the userInfo dictionary. |
| Workaround | If you need to pass in a mutable dictionary that can be changed by others down the chain, wrap the mutable dictionary in a read-only (immutable) dictionary and pass the immutable dictionary to setUserInfo. Be extremely careful doing this if your application is multi-threaded and the userinfo data may be accessed by more than one thread. | If you need to pass in a mutable dictionary that can be changed by others down the chain, wrap the mutable dictionary in a read-only (immutable) dictionary and pass the immutable dictionary to setUserInfo. Be extremely careful doing this if your application is multi-threaded and the userinfo data may be accessed by more than one thread. |
|  |  |  |
|  |  |  |
| Reference | 2396118 | 2396118 |
| Problem | WOMessage string encoding constants seem to be missing in Java. | WOMessage string encoding constants seem to be missing in Java. |
| Description | The Content Encodings section of the WOMessage class reference lists a number of string encodings. While the documentation is accurate for Objective-C applications, Java developers should note that these constants are declared in the Java-only class NSStringReference (and they no longer have the "NS" prefix). | The Content Encodings section of the WOMessage class reference lists a number of string encodings. While the documentation is accurate for Objective-C applications, Java developers should note that these constants are declared in the Java-only class NSStringReference (and they no longer have the "NS" prefix). |
| Workaround | Reference the constants from within NSStringReference. For instance, rather than NSASCIIStringEncoding, use NSStringReference.ASCIIStringEncoding. | Reference the constants from within NSStringReference. For instance, rather than NSASCIIStringEncoding, use NSStringReference.ASCIIStringEncoding. |
|  |  |  |
|  |  |  |
| Reference | 2387835 | 2387835 |
| Problem | WOApplication now returns a final status. | WOApplication now returns a final status. |
| Description | The WOApplicationMain function used to return a zero value even if your WebObjects application terminated abnormally. In WebObjects 4.5, it returns a non-zero value if an exception was raised during application execution. | The WOApplicationMain function used to return a zero value even if your WebObjects application terminated abnormally. In WebObjects 4.5, it returns a non-zero value if an exception was raised during application execution. |
| Workaround | None needed. | None needed. |
|  |  |  |
|  |  |  |
| Reference | 2378754 | 2378754 |
| Problem | WOHyperlink documentation incorrectly indicates that the actionClass binding must be specified. | WOHyperlink documentation incorrectly indicates that the actionClass binding must be specified. |
| Description | The actionClass binding only needs to be specified if the directActionName binding is specified. | The actionClass binding only needs to be specified if the directActionName binding is specified. |
| Workaround | None needed. | None needed. |
|  |  |  |
|  |  |  |
| Reference | 2375462 | 2375462 |
| Problem | Display group queryOperator string queries behave differently in 4.5. | Display group queryOperator string queries behave differently in 4.5. |
| Description | In previous versions, when you performed a string query with the query operator set to =, the result matched 'caseInsensitiveLike value\*' instead of '= value'. This behavior has been fixed for 4.5. | In previous versions, when you performed a string query with the query operator set to =, the result matched 'caseInsensitiveLike value\*' instead of '= value'. This behavior has been fixed for 4.5. |
| Workaround | Use the "starts with" string qualifier operator. See the stringQualifierOperators method in the WODisplayGroup class specification for more information. | Use the "starts with" string qualifier operator. See the stringQualifierOperators method in the WODisplayGroup class specification for more information. |
|  |  |  |
|  |  |  |
| Reference | 2372492 | 2372492 |
| Problem | Cookie expire header date format change | Cookie expire header date format change |
| Description | In order to comply with RFC 2109 and the Netscape informal specification, the date format used with the cookie expire header has been changed to "%a, %d-%b-%Y, %H:%M:%S GMT". Previously %A was used rather than %a. %a formats weekdays as Mon, Tue, Wed, etc. rather than the full weekday name. | In order to comply with RFC 2109 and the Netscape informal specification, the date format used with the cookie expire header has been changed to "%a, %d-%b-%Y, %H:%M:%S GMT". Previously %A was used rather than %a. %a formats weekdays as Mon, Tue, Wed, etc. rather than the full weekday name. |
| Workaround | None | None |
|  |  |  |
|  |  |  |
| Reference | 2364124 | 2364124 |
| Problem | Inner classes require special naming convention in the mapping coder | Inner classes require special naming convention in the mapping coder |
| Description | Specifying the name of an inner class in a mapping model (such as MappingHelper.RelatedLinks) produces a 'NOClassDef' exception. | Specifying the name of an inner class in a mapping model (such as MappingHelper.RelatedLinks) produces a 'NOClassDef' exception. |
| Workaround | The Sun VM expects the inner classes to be specified with their internal names. In the above example, use MappingHelper$RelatedLinks instead | The Sun VM expects the inner classes to be specified with their internal names. In the above example, use MappingHelper$RelatedLinks instead |
|  |  |  |
|  |  |  |
| Reference | 2296030 | 2296030 |
| Problem | Random raises with -[Session ???]: selector not recognized | Random raises with -[Session ???]: selector not recognized |
| Description | Java subclasses of Objective-C classes (that is, subclasses of com.apple.yellow.foundation.NSObject) must take two precautions if the finalize() method is implemented on the class:    1. You absolutely must call super.finalize() before returning. Failure to do so will leak memory and create an inconsistancy in the bridge's map tables.    2. You must not reconstitute the object out of the finalize() method. ("Reconsitituting" an object means creating a new global reference to the object in the finalize() method.) This is generally a bad idea, but it is permitted by the Java language. The semantics of the virtual machine are such that the object will \*not\* be finalized a second time, however. When no more references to the object exist, it will be collected but the finalize() method will not be invoked. As with the first precaution, this will leak memory and create an inconsistancy in the bridge's map tables. | Java subclasses of Objective-C classes (that is, subclasses of com.apple.yellow.foundation.NSObject) must take two precautions if the finalize() method is implemented on the class:    1. You absolutely must call super.finalize() before returning. Failure to do so will leak memory and create an inconsistancy in the bridge's map tables.    2. You must not reconstitute the object out of the finalize() method. ("Reconsitituting" an object means creating a new global reference to the object in the finalize() method.) This is generally a bad idea, but it is permitted by the Java language. The semantics of the virtual machine are such that the object will \*not\* be finalized a second time, however. When no more references to the object exist, it will be collected but the finalize() method will not be invoked. As with the first precaution, this will leak memory and create an inconsistancy in the bridge's map tables. |
| Workaround | None needed. | None needed. |
|  |  |  |
|  |  |  |
| Reference | 2277580 | 2277580 |
| Problem | WOApplicationWillFinishLaunchingNotification has been relocated | WOApplicationWillFinishLaunchingNotification has been relocated |
| Description | If your application depends on receiving WOApplicationWillFinishLaunchingNotification, be aware that it now comes after app init, before the adaptors are registered.  WOApplicationDidFinishLaunchingNotification comes after the adaptors are registered, just prior to receiving requests. | If your application depends on receiving WOApplicationWillFinishLaunchingNotification, be aware that it now comes after app init, before the adaptors are registered.  WOApplicationDidFinishLaunchingNotification comes after the adaptors are registered, just prior to receiving requests. |
| Workaround | None. | None. |
|  |  |  |
|  |  |  |
| Reference | 2276012 | 2276012 |
| Problem | Using alloc/init with WOComponent crashes without good feedback | Using alloc/init with WOComponent crashes without good feedback |
| Description | If you mistakenly use [[MyComponent alloc] init] to create a component, your application will crash without any indication of what happened. | If you mistakenly use [[MyComponent alloc] init] to create a component, your application will crash without any indication of what happened. |
| Workaround | Always use -[WOComponent pageWithName:] | Always use -[WOComponent pageWithName:] |
|  |  |  |
|  |  |  |
| Reference | 2256925 | 2256925 |
| Problem | NSDate's distantPast method shouldn't be used to set cookie expiration dates | NSDate's distantPast method shouldn't be used to set cookie expiration dates |
| Description | If you want to set a past date on the expires attribute of WOCookie, do not use [NSDate distantPast]. distantPast returns a date from the year 1 AD, and some browsers interpret this incorrectly as the year 2001. | If you want to set a past date on the expires attribute of WOCookie, do not use [NSDate distantPast]. distantPast returns a date from the year 1 AD, and some browsers interpret this incorrectly as the year 2001. |
| Workaround | Use a recent date in the past. | Use a recent date in the past. |
|  |  |  |
|  |  |  |
| Reference | 2429734 | 2429734 |
| Problem | WOMailDelivery forces current context to generate complete URLs for the returned page after mailing a component. | WOMailDelivery forces current context to generate complete URLs for the returned page after mailing a component. |
| Description | URLs in a mailed page need to be complete. Otherwise, the hyperlinks and buttons wouldn't work when clicked on by the recipeient. WOMailDelivery ensures this by forcing the context to complete all URLs in the page. However, once the context is set to complete all URLs, it will do it for the subsequent returned page as well. | URLs in a mailed page need to be complete. Otherwise, the hyperlinks and buttons wouldn't work when clicked on by the recipeient. WOMailDelivery ensures this by forcing the context to complete all URLs in the page. However, once the context is set to complete all URLs, it will do it for the subsequent returned page as well. |
| Workaround | In Objective-C, after using WOMailDelivery to email a component, do the following:  aRequest = [aContext request];  [aContext _setRequest:nil];  [aContext _setRequest:aRequest];    In Java, after using WOMailDelivery to email a component, do the following:  aContext.takeValueForKey("request", null);  aContext.takeValueForKey("request", aRequest);    Note that the above code uses key-value coding to invoke a private set method (_setRequest) which would otherwise be impossible in Java. | In Objective-C, after using WOMailDelivery to email a component, do the following:  aRequest = [aContext request];  [aContext _setRequest:nil];  [aContext _setRequest:aRequest];    In Java, after using WOMailDelivery to email a component, do the following:  aContext.takeValueForKey("request", null);  aContext.takeValueForKey("request", aRequest);    Note that the above code uses key-value coding to invoke a private set method (_setRequest) which would otherwise be impossible in Java. |
|  |  |  |
|  |  |  |
| Reference | 2282001 | 2282001 |
| Problem | The current context and the current request aren't accessible from within a WOSession initializer | The current context and the current request aren't accessible from within a WOSession initializer |
| Description | WOSession's initializer doesn't set its context instance variable, so it isn't possible to access either the current context or the current request for use in your WOSession subclass initializer. | WOSession's initializer doesn't set its context instance variable, so it isn't possible to access either the current context or the current request for use in your WOSession subclass initializer. |
| Workaround | There are two ways to work around this problem. The simplest is to implement awake() on your session. At this point, the context instance variable is set. Since awake() is invoked for every request, though, you'll have to protect your code so it is executed only once in awake() (if it is initialization code, it most likely needs to happen only once). A better solution, assuming you only need the request object, is to implement createSessionForRequest() in your subclass of WOApplication:    public WOSession createSessionForRequest(WORequest aRequest) {  Session session = (Session)super.createSessionForRequest(aRequest);  // put your custom initialization that needs the request object here.  return session;  } | There are two ways to work around this problem. The simplest is to implement awake() on your session. At this point, the context instance variable is set. Since awake() is invoked for every request, though, you'll have to protect your code so it is executed only once in awake() (if it is initialization code, it most likely needs to happen only once). A better solution, assuming you only need the request object, is to implement createSessionForRequest() in your subclass of WOApplication:    public WOSession createSessionForRequest(WORequest aRequest) {  Session session = (Session)super.createSessionForRequest(aRequest);  // put your custom initialization that needs the request object here.  return session;  } |
|  |  |  |
|  |  |  |
| Reference | 2279328 | 2279328 |
| Problem | WOResourceManager may leak for dynamic resources if 'key' attribute is not used. | WOResourceManager may leak for dynamic resources if 'key' attribute is not used. |
| Description | If you use WOImage like  MyImage : WOImage {  data = someData;  mimeType = "image/gif";  }  This can potentially leak as the data will be kept in memory under a random key. Some browsers don't ever load the resource. Playback clients will not load the resource either. In such cases, WOResourceManager will cache copies of it indefinitely. | If you use WOImage like  MyImage : WOImage {  data = someData;  mimeType = "image/gif";  }  This can potentially leak as the data will be kept in memory under a random key. Some browsers don't ever load the resource. Playback clients will not load the resource either. In such cases, WOResourceManager will cache copies of it indefinitely. |
| Workaround | Use the 'key' attribute to cache the same image over and over and save memory. Or call 'flushDataCache' on WOResourceManager. | Use the 'key' attribute to cache the same image over and over and save memory. Or call 'flushDataCache' on WOResourceManager. |
|  |  |  |
|  |  |  |
| Reference | 2279933 | 2279933 |
| Problem | WOF is not thread safe when WOCachingEnabled == NO | WOF is not thread safe when WOCachingEnabled == NO |
| Description | If you attempt to stress test your multi-threaded WOF app (i.e., where allowsConcurrentRequestHandling returns YES) without setting WOCachingEnabled to YES, you will probably experience unstable behavior. WOF is not designed to be thread safe with caching disabled. | If you attempt to stress test your multi-threaded WOF app (i.e., where allowsConcurrentRequestHandling returns YES) without setting WOCachingEnabled to YES, you will probably experience unstable behavior. WOF is not designed to be thread safe with caching disabled. |
| Workaround | set WOCachingEnabled YES before performing stress testing. | set WOCachingEnabled YES before performing stress testing. |
|  |  |  |
|  |  |  |
| Reference | 2270322 | 2270322 |
| Problem | Localization doesn't work smoothly with dialects. | Localization doesn't work smoothly with dialects. |
| Description | The built in support for localization is limited to the standard language definitions (i.e., the 2-char symbols from the ISO 639 spec). | The built in support for localization is limited to the standard language definitions (i.e., the 2-char symbols from the ISO 639 spec). |
| Workaround | Extend the Languages.plist in:    <NEXT_ROOT>/Library/Frameworks/WebObjects.framework/Resources    and add any language string you want. The left side is what will be sent by the browser and the right side is the name of your .lproj directory. You can also extend ProjectBuilder's languages plist so you can more easily add resources to the lproj of your choosing. See:    <NEXT_ROOT>/Library/Frameworks/ProjectBuilder.framework/Resources/MainInfo.table    and add your language to the HumanLanguages entry. | Extend the Languages.plist in:    <NEXT_ROOT>/Library/Frameworks/WebObjects.framework/Resources    and add any language string you want. The left side is what will be sent by the browser and the right side is the name of your .lproj directory. You can also extend ProjectBuilder's languages plist so you can more easily add resources to the lproj of your choosing. See:    <NEXT_ROOT>/Library/Frameworks/ProjectBuilder.framework/Resources/MainInfo.table    and add your language to the HumanLanguages entry. |
|  |  |  |
|  |  |  |
| Reference | 2269517 | 2269517 |
| Problem | Rapid turnaround doesn't seem to work for aggregates | Rapid turnaround doesn't seem to work for aggregates |
| Description | The default NSProjectSearchPath '(../..)' doesn't work for aggregates because the .woa is built into the top level of the aggregate. | The default NSProjectSearchPath '(../..)' doesn't work for aggregates because the .woa is built into the top level of the aggregate. |
| Workaround | Change the user default for your application to point either to the aggregate itself or to "..". For example:    defaults write MyApplication NSProjectSearchPath '("~/projects/MyAggregate")'    or    defaults write MyApplication NSProjectSearchPath '("..")' | Change the user default for your application to point either to the aggregate itself or to "..". For example:    defaults write MyApplication NSProjectSearchPath '("~/projects/MyAggregate")'    or    defaults write MyApplication NSProjectSearchPath '("..")' |
|  |  |  |
|  |  |  |
| Reference | 2181995 | 2181995 |
| Problem | Java ResourceManager method pathForResourceNamedInFramework returns empty string instead of null | Java ResourceManager method pathForResourceNamedInFramework returns empty string instead of null |
| Description | In some rare circumstances, the Java version of the ResourceManager method pathForResourceNamedInFramework returns an empty string when it should be returning null. | In some rare circumstances, the Java version of the ResourceManager method pathForResourceNamedInFramework returns an empty string when it should be returning null. |
| Workaround | Test for both null and "" to know if a resource has been found. | Test for both null and "" to know if a resource has been found. |
|  |  |  |
|  |  |  |
| Reference | 2425742 | 2425742 |
| Problem | Monitor's Path Wizard can be confused by the back button | Monitor's Path Wizard can be confused by the back button |
| Description | If you use the browser's back button in Monitor's Path Wizard, you may see an exception. Monitor is still running, however. The wizard is not correctly keeping track of the current page. | If you use the browser's back button in Monitor's Path Wizard, you may see an exception. Monitor is still running, however. The wizard is not correctly keeping track of the current page. |
| Workaround | Avoid using the browser back button when in the Path Wizard. | Avoid using the browser back button when in the Path Wizard. |
|  |  |  |
|  |  |  |
| Reference | 2425256 | 2425256 |
| Problem | On Windows 2000, some of the fonts used by tools such as ProjectBuilder, FileMerge, WebObjectsBuilder are hard to read | On Windows 2000, some of the fonts used by tools such as ProjectBuilder, FileMerge, WebObjectsBuilder are hard to read |
| Description | Windows 2000 introduced a new "message" font, Tahoma. This font is fairly unreadable at point sizes larger than 9. | Windows 2000 introduced a new "message" font, Tahoma. This font is fairly unreadable at point sizes larger than 9. |
| Workaround | Open the Display control panel, click on the Appearance tab, select Message Box from the Item pulldown menu, and then select another font (such as MS Sans Serif) instead of Tahoma. | Open the Display control panel, click on the Appearance tab, select Message Box from the Item pulldown menu, and then select another font (such as MS Sans Serif) instead of Tahoma. |
|  |  |  |
|  |  |  |
| Reference | 2425213 | 2425213 |
| Problem | Custom project types that mix Java and native code on HP-UX need to set a makefile variable. | Custom project types that mix Java and native code on HP-UX need to set a makefile variable. |
| Description | Due to the manner in which the Java VM is implemented by HP coupled with limitations in the 32-bit dynamic loader for HP-UX 11.0, some special linking behavior is required when making any project that produces an executable and that mixes native and Java code. This behavior is handled by the set of makefiles provided by WebObjects. WebObjectsApplication and Tool projects already make use of this behavior by default if they incorporate Java code. WebObjectsFramework, Framework and Library projects do not need to use this behavior, because these projects produce libraries, not executables. | Due to the manner in which the Java VM is implemented by HP coupled with limitations in the 32-bit dynamic loader for HP-UX 11.0, some special linking behavior is required when making any project that produces an executable and that mixes native and Java code. This behavior is handled by the set of makefiles provided by WebObjects. WebObjectsApplication and Tool projects already make use of this behavior by default if they incorporate Java code. WebObjectsFramework, Framework and Library projects do not need to use this behavior, because these projects produce libraries, not executables. |
| Workaround | If you have a custom project type that produces an executable that mixes native and Java code, add the following line to your project's Makefile.preamble:    HPUX_SPECIAL_LINKING = YES | If you have a custom project type that produces an executable that mixes native and Java code, add the following line to your project's Makefile.preamble:    HPUX_SPECIAL_LINKING = YES |
|  |  |  |
|  |  |  |
| Reference | 2425106 | 2425106 |
| Problem | WebObjects applications launched by wotaskd have logging redirected to /dev/null | WebObjects applications launched by wotaskd have logging redirected to /dev/null |
| Description | When wotaskd launches WebObjects applications, it redirects logging to /dev/null. | When wotaskd launches WebObjects applications, it redirects logging to /dev/null. |
| Workaround | Launch a shell script instead. The name of the shell script (minus the extension) must be the same as the name of the executable. So, for instance, if you have a script to launch HelloWorldCompiled, the script should be named HelloWorldCompiled.sh (on Windows, the executable would be HelloWorldCompiled.exe and the script would be HelloWorldCompiled.bat). | Launch a shell script instead. The name of the shell script (minus the extension) must be the same as the name of the executable. So, for instance, if you have a script to launch HelloWorldCompiled, the script should be named HelloWorldCompiled.sh (on Windows, the executable would be HelloWorldCompiled.exe and the script would be HelloWorldCompiled.bat). |
|  |  |  |
|  |  |  |
| Reference | 2424573 | 2424573 |
| Problem | A POST request to a WebObjects application via Apache 1.3 or later using the CGI adaptor results in null form values. | A POST request to a WebObjects application via Apache 1.3 or later using the CGI adaptor results in null form values. |
| Description | The latest version of Apache passes certain environment variables to the CGI adaptor that contain newline characters. The WebObjects CGI adaptor converts all of these environment variables to headers - which can confuse the application when parsing HTTP headers - resulting in the loss of form values. | The latest version of Apache passes certain environment variables to the CGI adaptor that contain newline characters. The WebObjects CGI adaptor converts all of these environment variables to headers - which can confuse the application when parsing HTTP headers - resulting in the loss of form values. |
| Workaround | Use a CGI utility such as printenv (it may be installed by default in your cgi-bin directory but you may need to add execute permission) to determine if you have any environment variables being passed to CGI programs that contain newline characters. A common one is SERVER_SIGNATURE. Modify Apache's configuration file ServerSignature entry to be Off. It may also be possible to use the new SetEnvIf Directive, although this workaround has not been tested. | Use a CGI utility such as printenv (it may be installed by default in your cgi-bin directory but you may need to add execute permission) to determine if you have any environment variables being passed to CGI programs that contain newline characters. A common one is SERVER_SIGNATURE. Modify Apache's configuration file ServerSignature entry to be Off. It may also be possible to use the new SetEnvIf Directive, although this workaround has not been tested. |
|  |  |  |
|  |  |  |
| Reference | 2418131 | 2418131 |
| Problem | It isn't always clear which port you need to connect to for Monitor and the WOInfoCenter. | It isn't always clear which port you need to connect to for Monitor and the WOInfoCenter. |
| Description | Much of the debugging information for Monitor and WOInfoCenter has been turned off. Because of that, it may not be clear which port you're supposed to connect to. | Much of the debugging information for Monitor and WOInfoCenter has been turned off. Because of that, it may not be clear which port you're supposed to connect to. |
| Workaround | Create a default so that you always get the same port. For instance:  defaults write Monitor WOPort 9999 | Create a default so that you always get the same port. For instance:  defaults write Monitor WOPort 9999 |
|  |  |  |
|  |  |  |
| Reference | 2418129 | 2418129 |
| Problem | Make rule for .lm files broken. | Make rule for .lm files broken. |
| Description | If you add a .lm (Lex + Objective-C) file to a project, the only way to get it to   compile properly is to do a "make clean", followed by a "make". Alternatively, you can add -ObjC to OTHER_C_FLAG. | If you add a .lm (Lex + Objective-C) file to a project, the only way to get it to   compile properly is to do a "make clean", followed by a "make". Alternatively, you can add -ObjC to OTHER_C_FLAG. |
| Workaround | See the description, above. | See the description, above. |
|  |  |  |
|  |  |  |
| Reference | 2418127 | 2418127 |
| Problem | Key-value coding crash when a WOComponent refers to a static Java string declared in the application class. | Key-value coding crash when a WOComponent refers to a static Java string declared in the application class. |
| Description | If you build a WebObjects application that has a static Java string declared in the application class, and then build a WOComponent that refers to that string in its .wod file, on Windows NT the compiled application will crash ("_JAVAKVCGetClassFromIvar()") instead of working or throwing an exception. On Mac OS X Server this doesn't crash, but neither does it report a missing binding as it should. | If you build a WebObjects application that has a static Java string declared in the application class, and then build a WOComponent that refers to that string in its .wod file, on Windows NT the compiled application will crash ("_JAVAKVCGetClassFromIvar()") instead of working or throwing an exception. On Mac OS X Server this doesn't crash, but neither does it report a missing binding as it should. |
| Workaround | None. | None. |
|  |  |  |
|  |  |  |
| Reference | 2417392 | 2417392 |
| Problem | WebObjects fills up the Windows NT Event Viewer log. | WebObjects fills up the Windows NT Event Viewer log. |
| Description | Invocations of NSLog, logWithFormat:, debugWithFormat: fill up the Windows NT Event Viewer log. | Invocations of NSLog, logWithFormat:, debugWithFormat: fill up the Windows NT Event Viewer log. |
| Workaround | If recording the entire history using the Event Viewer log is not necessary, set the Event Viewer to overwrite events when the log fills up. Open 'Event Viewer' and select 'Log Settings...' from the 'Log' menu. Select the 'Overwrite Events as Needed' option. The number of generated messages can also be reduced by using the -WODebuggingEnabled NO command line option, when debugging info is not required. | If recording the entire history using the Event Viewer log is not necessary, set the Event Viewer to overwrite events when the log fills up. Open 'Event Viewer' and select 'Log Settings...' from the 'Log' menu. Select the 'Overwrite Events as Needed' option. The number of generated messages can also be reduced by using the -WODebuggingEnabled NO command line option, when debugging info is not required. |
|  |  |  |
|  |  |  |
| Reference | 2404574 | 2404574 |
| Problem | Windows NT: wotaskd crashed and will not restart | Windows NT: wotaskd crashed and will not restart |
| Description | On Windows NT, if wotaskd crashes for some reason it should be restarted automatically by the woservice process. However, if the machine is set to have Dr Watson visual alerts appear in the event of a crash, the process will hang and wotaskd won't restart until the Dr Watson panel is dismissed. | On Windows NT, if wotaskd crashes for some reason it should be restarted automatically by the woservice process. However, if the machine is set to have Dr Watson visual alerts appear in the event of a crash, the process will hang and wotaskd won't restart until the Dr Watson panel is dismissed. |
| Workaround | Turn off Dr Watson visual alerts. This is usually required for any server machine. | Turn off Dr Watson visual alerts. This is usually required for any server machine. |
|  |  |  |
|  |  |  |
| Reference | 2404022 | 2404022 |
| Problem | Apps intermittently fail to connect via the webserver using multicast with a large number of hosts. | Apps intermittently fail to connect via the webserver using multicast with a large number of hosts. |
| Description | The multicast code accumulates the responses to a multicast message in a single 4096-byte buffer. This limits the number of hosts that can reply to a single multicast message. Each reply is of the form "http://hostname:port", so for a given set of hosts and port numbers you should be able to calculate whether the responses will fit within the buffer. For instance, if each hostname was no more than 8 characters long, and each port number was no more than 4 digits long, each reply would be no more than 20 characters; about 200 hosts could respond in this instance. | The multicast code accumulates the responses to a multicast message in a single 4096-byte buffer. This limits the number of hosts that can reply to a single multicast message. Each reply is of the form "http://hostname:port", so for a given set of hosts and port numbers you should be able to calculate whether the responses will fit within the buffer. For instance, if each hostname was no more than 8 characters long, and each port number was no more than 4 digits long, each reply would be no more than 20 characters; about 200 hosts could respond in this instance. |
| Workaround | Disable multicast mode (see "What's New in WebObjects 4.5" for more information), reduce the number of hosts, or shorten their hostnames. | Disable multicast mode (see "What's New in WebObjects 4.5" for more information), reduce the number of hosts, or shorten their hostnames. |
|  |  |  |
|  |  |  |
| Reference | 2396728 | 2396728 |
| Problem | Web server adaptors by default retrieve configuration information using multicast. | Web server adaptors by default retrieve configuration information using multicast. |
| Description | As described in "What's New in WebObjects 4.5," by default web server adaptors build up a list of WebObjects application servers from responses received after sending a multicast message. In some situations--particularly in deployment--you may wish to limit which application servers can be accessed from a given web server. | As described in "What's New in WebObjects 4.5," by default web server adaptors build up a list of WebObjects application servers from responses received after sending a multicast message. In some situations--particularly in deployment--you may wish to limit which application servers can be accessed from a given web server. |
| Workaround | Alter your web server's configuration file as described in "What's New in WebObjects 4.5" so that it obtains WebObjects configuration information from a file (either on the local web server or on a different web server). | Alter your web server's configuration file as described in "What's New in WebObjects 4.5" so that it obtains WebObjects configuration information from a file (either on the local web server or on a different web server). |
|  |  |  |
|  |  |  |
| Reference | 2396721 | 2396721 |
| Problem | Unable to set breakpoints on symbols in shared libraries on Solaris and HP-UX. | Unable to set breakpoints on symbols in shared libraries on Solaris and HP-UX. |
| Description | When you start gdb, the shared libraries used by your program have yet to be loaded. Therefore, gdb is unaware of the symbols in the shared library until the beginning of main(). | When you start gdb, the shared libraries used by your program have yet to be loaded. Therefore, gdb is unaware of the symbols in the shared library until the beginning of main(). |
| Workaround | Set a breakpoint on main (for example, "b main") in gdb before starting your program (for example, "run"). When gdb breaks at main(), if you haven't seen log messages indicating that gdb is trying to load symbols for each shared library, you may also need to execute the shared library symbol loading command ("sharedlibrary") before continuing on from the breakpoint. | Set a breakpoint on main (for example, "b main") in gdb before starting your program (for example, "run"). When gdb breaks at main(), if you haven't seen log messages indicating that gdb is trying to load symbols for each shared library, you may also need to execute the shared library symbol loading command ("sharedlibrary") before continuing on from the breakpoint. |
|  |  |  |
|  |  |  |
| Reference | 2394732 | 2394732 |
| Problem | The WODirectActionHandler now allows direct-connect requests when the application is refusing new session. | The WODirectActionHandler now allows direct-connect requests when the application is refusing new session. |
| Description | In previous versions of WebObjects, if an application is refusing new sessions and a request with no session id comes in, a redirect is returned to the sender. In WebObjects 4.5, if an application is refusing new sessions and a request with no session id comes in through the adaptor, a redirect is returned to the sender. If the request is made using direct connect, it is processed normally. | In previous versions of WebObjects, if an application is refusing new sessions and a request with no session id comes in, a redirect is returned to the sender. In WebObjects 4.5, if an application is refusing new sessions and a request with no session id comes in through the adaptor, a redirect is returned to the sender. If the request is made using direct connect, it is processed normally. |
| Workaround | None needed. | None needed. |
|  |  |  |
|  |  |  |
| Reference | 2393227 | 2393227 |
| Problem | c++ headers wind up in the wrong location on Solaris, and so are unusable. | c++ headers wind up in the wrong location on Solaris, and so are unusable. |
| Description | On Solaris, the c++ headers wind up in $NEXT_ROOT/Library/Frameworks/System.framework/Versions/Versions/B/g++, rather than in $NEXT_ROOT/Library/Frameworks/System.framework/Versions/A/g++. | On Solaris, the c++ headers wind up in $NEXT_ROOT/Library/Frameworks/System.framework/Versions/Versions/B/g++, rather than in $NEXT_ROOT/Library/Frameworks/System.framework/Versions/A/g++. |
| Workaround | Copy the g++ directory to the correct location (.../System.framework/Versions/A). | Copy the g++ directory to the correct location (.../System.framework/Versions/A). |
|  |  |  |
|  |  |  |
| Reference | 2321336 | 2321336 |
| Problem | On HP-UX, user and group id's for 'nobody' need to be positive numbers | On HP-UX, user and group id's for 'nobody' need to be positive numbers |
| Description | By default on HP-UX, user and group id's for 'nobody' are set to negative numbers. This introduces some problems: for instance, the apache web server fails to start. | By default on HP-UX, user and group id's for 'nobody' are set to negative numbers. This introduces some problems: for instance, the apache web server fails to start. |
| Workaround | Reset nobody's user and group id's in /etc/passwd files to positive values. | Reset nobody's user and group id's in /etc/passwd files to positive values. |
|  |  |  |
|  |  |  |
| Reference | 2304924 | 2304924 |
| Problem | WebObjects is not thread safe with component caching disabled | WebObjects is not thread safe with component caching disabled |
| Description | WebObjects isn't thread safe when AllowsConcurrentHandling is set to YES and CachingEnabled is set to NO. This problem can manifest in different ways. For example, you might experience a deadlock after a message like this:    Component Named <A_COMPONENT_NAME> was improperly initialized. It appears that the -init method of this component did not call [super init] | WebObjects isn't thread safe when AllowsConcurrentHandling is set to YES and CachingEnabled is set to NO. This problem can manifest in different ways. For example, you might experience a deadlock after a message like this:    Component Named <A_COMPONENT_NAME> was improperly initialized. It appears that the -init method of this component did not call [super init] |
| Workaround | When deploying WebObjects applications, be sure to set -WOCachingEnabled YES. | When deploying WebObjects applications, be sure to set -WOCachingEnabled YES. |
|  |  |  |
|  |  |  |
| Reference | 2294891 | 2294891 |
| Problem | Some makefiles on HP-UX may not point properly to lex and yacc. | Some makefiles on HP-UX may not point properly to lex and yacc. |
| Description | This should only affect those using lex and yacc directly within their projects. The makefiles in question expect lex and yacc to be installed in /usr/ccs/bin, but these executables may be in /usr/bin or elsewhere. Since WebObjects does not include either lex or yacc, the makefiles don't have any sure way of finding them. | This should only affect those using lex and yacc directly within their projects. The makefiles in question expect lex and yacc to be installed in /usr/ccs/bin, but these executables may be in /usr/bin or elsewhere. Since WebObjects does not include either lex or yacc, the makefiles don't have any sure way of finding them. |
| Workaround | If you want to use lex and yacc, include symbolic links to those executables in /usr/ccs/bin with the names "lex" and "yacc", respectively. | If you want to use lex and yacc, include symbolic links to those executables in /usr/ccs/bin with the names "lex" and "yacc", respectively. |
|  |  |  |
|  |  |  |
| Reference | 2285467 | 2285467 |
| Problem | nil and null can be used in .wod files. | nil and null can be used in .wod files. |
| Description | In previous releases, the .wod file format forced you to use the keyword "NO" in lieu of "nil" or "null". All of these keywords are now acceptable. | In previous releases, the .wod file format forced you to use the keyword "NO" in lieu of "nil" or "null". All of these keywords are now acceptable. |
| Workaround | None needed. | None needed. |
|  |  |  |
|  |  |  |
| Reference | 2279655 | 2279655 |
| Problem | ObjectAlloc doesn't work "out of the box" for WebObjects apps | ObjectAlloc doesn't work "out of the box" for WebObjects apps |
| Description | ObjectAlloc doesn't work for WebObjects apps without some prior configuration. See the Workaround, below, for the needed user default setting. | ObjectAlloc doesn't work for WebObjects apps without some prior configuration. See the Workaround, below, for the needed user default setting. |
| Workaround | Set the ImagePaths user default as follows:  defaults write NSGlobalDomain ImagePaths = "(/System/Library/Frameworks/System.framework/System, /System/Library/Frameworks/Foundation.framework/Foundation, /System/Library/Frameworks/WebObjects.framework/WebObjects,   /System/Library/Frameworks/EOControl.framework/EOControl);" | Set the ImagePaths user default as follows:  defaults write NSGlobalDomain ImagePaths = "(/System/Library/Frameworks/System.framework/System, /System/Library/Frameworks/Foundation.framework/Foundation, /System/Library/Frameworks/WebObjects.framework/WebObjects,   /System/Library/Frameworks/EOControl.framework/EOControl);" |
|  |  |  |
|  |  |  |
| Reference | 2275286 | 2275286 |
| Problem | Java programs on Solaris that don't use WOApplicationMain() may malfunction due to garbage collection problems | Java programs on Solaris that don't use WOApplicationMain() may malfunction due to garbage collection problems |
| Description | All NSThreads and cthreads need to make their stack base addresses available to the bridge so that the Java garbage collector can execute successfully. This issue is dealt with transparently in the bridge for all the cthreads and NSThreads created. However, in the case of the main thread, the cthreads layer does not detect a new thread being created. As a result, it cannot, on its own, supply an accurate stack base address to the Java VM. You need to write code in the main function of your program to supply this address. Note that WebObjects applications come with their own main function (WOApplicationMain) which takes the necessary steps. For other types of applications (EOF applications, for example) that do not supply a "main" function, see the Workaround, below. | All NSThreads and cthreads need to make their stack base addresses available to the bridge so that the Java garbage collector can execute successfully. This issue is dealt with transparently in the bridge for all the cthreads and NSThreads created. However, in the case of the main thread, the cthreads layer does not detect a new thread being created. As a result, it cannot, on its own, supply an accurate stack base address to the Java VM. You need to write code in the main function of your program to supply this address. Note that WebObjects applications come with their own main function (WOApplicationMain) which takes the necessary steps. For other types of applications (EOF applications, for example) that do not supply a "main" function, see the Workaround, below. |
| Workaround | Add these lines in your main function, immediately following the variable declaration block:    #if defined(__svr4__)  unsigned long java_reserved[16];  void cthread_set_java_vm_stack_base(void \*);  cthread_set_java_vm_stack_base(java_reserved);  #endif | Add these lines in your main function, immediately following the variable declaration block:    #if defined(__svr4__)  unsigned long java_reserved[16];  void cthread_set_java_vm_stack_base(void \*);  cthread_set_java_vm_stack_base(java_reserved);  #endif |
|  |  |  |
|  |  |  |
| Reference | 2261627 | 2261627 |
| Problem | finalize() must call super on hybrid objects | finalize() must call super on hybrid objects |
| Description | Very strange, difficult to debug problems can occur if your Java subclasses of Objective-C classes implement finalize() and fail to call super.finalize(). The most common manifestations of this problem are 1) objects of this class will not be deallocated, 2) these objects may be swapped in for other (unrelated) objects that cross the bridge. | Very strange, difficult to debug problems can occur if your Java subclasses of Objective-C classes implement finalize() and fail to call super.finalize(). The most common manifestations of this problem are 1) objects of this class will not be deallocated, 2) these objects may be swapped in for other (unrelated) objects that cross the bridge. |
| Workaround | If you implement finalize() you absolutely MUST (1) be sure to call super.finalize() and (2) never "reconstitute" the Java object from the finalize() method (by assigning a reference to it from another object). | If you implement finalize() you absolutely MUST (1) be sure to call super.finalize() and (2) never "reconstitute" the Java object from the finalize() method (by assigning a reference to it from another object). |
|  |  |  |
|  |  |  |
| Reference | 2181630 | 2181630 |
| Problem | refuseNewSessions:YES may cause endless redirects if only one instance is running | refuseNewSessions:YES may cause endless redirects if only one instance is running |
| Description | If an application has programmatically been set to refuse new sessions, the application is run without using Monitor, and only a single instance of the application is running, it causes endless redirects. The application redirects the request back to the WOAdaptor, which tries to pick another instance, but since there is only one instance running, it will pick that instance again. | If an application has programmatically been set to refuse new sessions, the application is run without using Monitor, and only a single instance of the application is running, it causes endless redirects. The application redirects the request back to the WOAdaptor, which tries to pick another instance, but since there is only one instance running, it will pick that instance again. |
| Workaround | Use the Monitor application to deploy the application. Monitor will detect that there are no non-refusing instances running and return an error page. | Use the Monitor application to deploy the application. Monitor will detect that there are no non-refusing instances running and return an error page. |
|  |  |  |
|  |  |  |
| Reference | 2303670 | 2303670 |
| Problem | No static documentation entry point web page appears to be available. | No static documentation entry point web page appears to be available. |
| Description | A web page called the WebObjects Documentation Page is in the install and functions as an alternative to the WOInfoCenter. However, the WOInfoCenter does not display it. | A web page called the WebObjects Documentation Page is in the install and functions as an alternative to the WOInfoCenter. However, the WOInfoCenter does not display it. |
| Workaround | Go to the WebObjects Documentation Page directly.  The file is named WOHomePage.html and is located in /System/Documentation/Developer/WebObjects/ on MacOS X Server and $(NEXT_ROOT)\Documentation\Developer\WebObjects\ on Windows NT. | Go to the WebObjects Documentation Page directly.  The file is named WOHomePage.html and is located in /System/Documentation/Developer/WebObjects/ on MacOS X Server and $(NEXT_ROOT)\Documentation\Developer\WebObjects\ on Windows NT. |
|  |  |  |
|  |  |  |
| Reference | 2279737 | 2279737 |
| Problem | WOInfoCenter occasionally exits after handling the first request | WOInfoCenter occasionally exits after handling the first request |
| Description | Occasionally the WOInfoCenter crashes after handling the first request from the web browser. This usually indicates corrupt or out-of-date indexes. | Occasionally the WOInfoCenter crashes after handling the first request from the web browser. This usually indicates corrupt or out-of-date indexes. |
| Workaround | Run the WOInfoIndexer program in /System/Library/WebObjects/Executables ($NEXT_ROOT\Library\WebObjects\Executables on Windows NT) to recreate the indexes. | Run the WOInfoIndexer program in /System/Library/WebObjects/Executables ($NEXT_ROOT\Library\WebObjects\Executables on Windows NT) to recreate the indexes. |
|  |  |  |
|  |  |  |
| Reference | 2421581 | 2421581 |
| Problem | The "cache-control: no-cache" http header causes Internet Explorer 5 to hang when using a proxy server. | The "cache-control: no-cache" http header causes Internet Explorer 5 to hang when using a proxy server. |
| Description | By default WebObjects adds the "cache-control" header with a value of "no-cache" (among others) to responses. This particular header causes Microsoft's Internet Explorer 5 to hang if a proxy server is being used. | By default WebObjects adds the "cache-control" header with a value of "no-cache" (among others) to responses. This particular header causes Microsoft's Internet Explorer 5 to hang if a proxy server is being used. |
| Workaround | Set the WOAllowsCacheControlHeader user default to NO. This will cause the "cache-control" header (and all associated values) to be omitted from WebObjects responses. | Set the WOAllowsCacheControlHeader user default to NO. This will cause the "cache-control" header (and all associated values) to be omitted from WebObjects responses. |
|  |  |  |
|  |  |  |
| Reference | 2418051 | 2418051 |
| Problem | WebScript cannot talk to NSProxies. | WebScript cannot talk to NSProxies. |
| Description | If you obtain a proxy in WebScript, and try to send messages to the proxy, an "Unknown type 16" error message will be generated. | If you obtain a proxy in WebScript, and try to send messages to the proxy, an "Unknown type 16" error message will be generated. |
| Workaround | Use Objective-C rather than WebScript to communicate with NSProxies. | Use Objective-C rather than WebScript to communicate with NSProxies. |
|  |  |  |
|  |  |  |
| Reference | 2417397 | 2417397 |
| Problem | WebObjects compiler doesn't support -nopdolib on Windows NT. | WebObjects compiler doesn't support -nopdolib on Windows NT. |
| Description | Building any application using the compiler supplied with WebObjects will forcibly link nextpdo.dll into any .dll or executable. One of the implications is that the WebServer adaptors shipped with WebObjects require nextpdo.dll to be installed on any machine they need to execute on. | Building any application using the compiler supplied with WebObjects will forcibly link nextpdo.dll into any .dll or executable. One of the implications is that the WebServer adaptors shipped with WebObjects require nextpdo.dll to be installed on any machine they need to execute on. |
| Workaround | Copy nextpdo.dll to the machine where you want to run the adaptor. | Copy nextpdo.dll to the machine where you want to run the adaptor. |
|  |  |  |
|  |  |  |
| Reference | 2282578 | 2282578 |
| Problem | Messaging Java objects from within some threads can cause a crash. | Messaging Java objects from within some threads can cause a crash. |
| Description | Any threads spawned before the Java virtual machine is created, and any threads created using the cthread/pthread or other non-NSThread API, must be explicitly attached to the Java virtual machine before you message any Java object from within that thread. Once you've created the virtual machine, any NSThreads spawned will automatically be attached (as will the thread that created the Java virtual machine). | Any threads spawned before the Java virtual machine is created, and any threads created using the cthread/pthread or other non-NSThread API, must be explicitly attached to the Java virtual machine before you message any Java object from within that thread. Once you've created the virtual machine, any NSThreads spawned will automatically be attached (as will the thread that created the Java virtual machine). |
| Workaround | Attach threads created before the Java virtual machine and non-NSThread threads to the Java virtual machine using the NSJavaVirtualMachine class's -attachCurrentThread method (NSJavaVirtualMachine is part of the JavaVM framework). | Attach threads created before the Java virtual machine and non-NSThread threads to the Java virtual machine using the NSJavaVirtualMachine class's -attachCurrentThread method (NSJavaVirtualMachine is part of the JavaVM framework). |
|  |  |  |
|  |  |  |

---

### Webserver Adaptors

|  |  |  |
| --- | --- | --- |
| Reference | 2425919 | 2425919 |
| Problem | CGI performance too slow | CGI performance too slow |
| Description | On subnets with a large number of application servers, the response times when running the CGI adaptor in multicast mode may become unnacceptably slow. | On subnets with a large number of application servers, the response times when running the CGI adaptor in multicast mode may become unnacceptably slow. |
| Workaround | Use a non-multicast method for obtaining application configuration information when using the CGI adaptor. For example, with Apache activate mod_env by uncommenting the appropriate lines in apache.conf and add the directive PassEnv WO_CONFIG_URL. Then set the WO_CONFIG_URL environement variable to http://someHost:1085. Alternatively, set CONFIG_URL in config.h and recompile the adaptor. | Use a non-multicast method for obtaining application configuration information when using the CGI adaptor. For example, with Apache activate mod_env by uncommenting the appropriate lines in apache.conf and add the directive PassEnv WO_CONFIG_URL. Then set the WO_CONFIG_URL environement variable to http://someHost:1085. Alternatively, set CONFIG_URL in config.h and recompile the adaptor. |
|  |  |  |
|  |  |  |
| Reference | 2424576 | 2424576 |
| Problem | NSAPI adaptor fails to build on NT | NSAPI adaptor fails to build on NT |
| Description | On Windows NT the NSAPI adaptor doesn't compile, complaining about not being able to find header files. | On Windows NT the NSAPI adaptor doesn't compile, complaining about not being able to find header files. |
| Workaround | Install the Netscape server 3.6, locate the header files in their source or examples directory, and follow the build instructions in c:/Apple/Developer/Examples/WebObjects/Source/Adaptors/BuildingInstructions.html | Install the Netscape server 3.6, locate the header files in their source or examples directory, and follow the build instructions in c:/Apple/Developer/Examples/WebObjects/Source/Adaptors/BuildingInstructions.html |
|  |  |  |
|  |  |  |
| Reference | 2423333 | 2423333 |
| Problem | WebObjects 4.5 adaptors don't work reliably with WebObjects 3.5 apps running on Windows NT. | WebObjects 4.5 adaptors don't work reliably with WebObjects 3.5 apps running on Windows NT. |
| Description | When contacting WebObjects 3.5 apps running on Windows NT, the error message "Invalid response received from application." may be returned. In some cases a page may be returned containing partial data. | When contacting WebObjects 3.5 apps running on Windows NT, the error message "Invalid response received from application." may be returned. In some cases a page may be returned containing partial data. |
| Workaround | None. | None. |
|  |  |  |
|  |  |  |
| Reference | 2420040 | 2420040 |
| Problem | Security warning: asking Apache for a non-existent application can generate an application listing | Security warning: asking Apache for a non-existent application can generate an application listing |
| Description | When you specify an invalid application name to the WebObjects Apache plug-in, the plug-in invokes the CGI is adaptor which then produces a list (including hyperlinks) of all available applications (on the subnet if you're running in multicast mode). Giving your end users access to all running WebObjects applications is often undesireable, especially in deployment situations. | When you specify an invalid application name to the WebObjects Apache plug-in, the plug-in invokes the CGI is adaptor which then produces a list (including hyperlinks) of all available applications (on the subnet if you're running in multicast mode). Giving your end users access to all running WebObjects applications is often undesireable, especially in deployment situations. |
| Workaround | Either remove the CGI adaptor or install the Apache module as /Apps/WebObjects instead of cgi-bin. | Either remove the CGI adaptor or install the Apache module as /Apps/WebObjects instead of cgi-bin. |
|  |  |  |
|  |  |  |
| Reference | 2389605 | 2389605 |
| Problem | Why does WebObjects use an HTTP success status code when a WebObjects app returns an error? | Why does WebObjects use an HTTP success status code when a WebObjects app returns an error? |
| Description | When the webserver adaptor detects an error, it returns a simple HTML page describing the problem, but not an error status. This is done so that the user will see the returned HTML, and not the message the browser thinks should be substituted. | When the webserver adaptor detects an error, it returns a simple HTML page describing the problem, but not an error status. This is done so that the user will see the returned HTML, and not the message the browser thinks should be substituted. |
| Workaround | None, aside from modifying the adaptor source and rebuilding. | None, aside from modifying the adaptor source and rebuilding. |
|  |  |  |
|  |  |  |
| Reference | 2362493 | 2362493 |
| Problem | WOHTTPConnections cannot be shared between worker threads. | WOHTTPConnections cannot be shared between worker threads. |
| Description | Due to the fact that WOHTTPConnection currently has one input buffer per instance, and no locking thereof, WOHTTPConnection objects cannot easily be shared between threads, as unpredictable results will occur. | Due to the fact that WOHTTPConnection currently has one input buffer per instance, and no locking thereof, WOHTTPConnection objects cannot easily be shared between threads, as unpredictable results will occur. |
| Workaround | Either avoid sharing WOHTTPConnection objects between threads, or add additional locking logic in your own code. | Either avoid sharing WOHTTPConnection objects between threads, or add additional locking logic in your own code. |
|  |  |  |
|  |  |  |
| Reference | 2340057 | 2340057 |
| Problem | Requests to a WebObjects application cause stat calls in Netscape servers | Requests to a WebObjects application cause stat calls in Netscape servers |
| Description | When observing a Netscape server using a tool such as "truss" with the NSAPI or CGI adaptor accepting requests for a WebObjects application, several stat calls are visible. This is indicative of the machine perfoming system calls to look up directories, which can have a detrimental impact on performance. | When observing a Netscape server using a tool such as "truss" with the NSAPI or CGI adaptor accepting requests for a WebObjects application, several stat calls are visible. This is indicative of the machine perfoming system calls to look up directories, which can have a detrimental impact on performance. |
| Workaround | The stat calls are primarily caused by the presence of a PathCheck directive in Netscape's obj.conf:  PathCheck fn=find-pathinfo  If you are not using CGI programs (that is, the NSAPI adaptor with WebObjects and no other CGI programs), this directive can be removed to reduce the number of stat calls. | The stat calls are primarily caused by the presence of a PathCheck directive in Netscape's obj.conf:  PathCheck fn=find-pathinfo  If you are not using CGI programs (that is, the NSAPI adaptor with WebObjects and no other CGI programs), this directive can be removed to reduce the number of stat calls. |
|  |  |  |
|  |  |  |
| Reference | 2268619 | 2268619 |
| Problem | Application instance numbers must be greater than zero, and unique per application name | Application instance numbers must be greater than zero, and unique per application name |
| Description | Zero was a legal application instance number in previous versions of WebObjects. In WebObjects 4, application instance numbers must be both greater than zero and unique for each application name. Although Monitor follows this rule, if you hand-enter an instance number of zero in your public WebObjects.conf file, strange behavior will result. The adaptor will load balance to the application with instance number zero, but won't insert the instance number into the request. This will cause the application to respond with a page containing URLs without instance numbers. If you then click on a link in this page, you'll most likely load balance to another application instance, and get a session timeout error. | Zero was a legal application instance number in previous versions of WebObjects. In WebObjects 4, application instance numbers must be both greater than zero and unique for each application name. Although Monitor follows this rule, if you hand-enter an instance number of zero in your public WebObjects.conf file, strange behavior will result. The adaptor will load balance to the application with instance number zero, but won't insert the instance number into the request. This will cause the application to respond with a page containing URLs without instance numbers. If you then click on a link in this page, you'll most likely load balance to another application instance, and get a session timeout error. |
| Workaround | Start your applications with instance numbers greater than zero. | Start your applications with instance numbers greater than zero. |
|  |  |  |
|  |  |  |
| Reference | 2174404 | 2174404 |
| Problem | WebObjects log file is not updated. | WebObjects log file is not updated. |
| Description | This bug occurs for NSAPI adaptors on all platforms and the ISAPI adaptor on Windows NT.   For performance reasons, when the adaptor receives its first log function call, it sets a global "attempted logging flag" to YES and checks to see if there is a logWebObjects file in the temporary directory (usually /tmp on UNIX platforms and c:\temp on Windows NT). If the file exists, it sets a global "log flag" to YES. If the file doesn't exist, it sets the "log flag" to NO. On subsequent log function calls, the adaptor will only log a message if both the "attempted logging flag" and the "log flag" are YES.     The problem arises from the fact that these flags are global variables. In threaded API servers, if one thread has set the "log flag" to NO, there is no way it will be turned back to YES. | This bug occurs for NSAPI adaptors on all platforms and the ISAPI adaptor on Windows NT.   For performance reasons, when the adaptor receives its first log function call, it sets a global "attempted logging flag" to YES and checks to see if there is a logWebObjects file in the temporary directory (usually /tmp on UNIX platforms and c:\temp on Windows NT). If the file exists, it sets a global "log flag" to YES. If the file doesn't exist, it sets the "log flag" to NO. On subsequent log function calls, the adaptor will only log a message if both the "attempted logging flag" and the "log flag" are YES.     The problem arises from the fact that these flags are global variables. In threaded API servers, if one thread has set the "log flag" to NO, there is no way it will be turned back to YES. |
| Workaround | Do the following:    - Create the logWebObjects file in the temporary directory.  - Restart your server.   - If you remove the logWebObjects file, you should restart your server afterward.     This workaround will work as long as the server keeps using the current thread for the API adaptor. | Do the following:    - Create the logWebObjects file in the temporary directory.  - Restart your server.   - If you remove the logWebObjects file, you should restart your server afterward.     This workaround will work as long as the server keeps using the current thread for the API adaptor. |
|  |  |  |
|  |  |  |
| Reference | 2173679 | 2173679 |
| Problem | Can't run two WebObjects adaptors on the same machine with two different web servers. | Can't run two WebObjects adaptors on the same machine with two different web servers. |
| Description | If you attempt to run two WebObjects adaptors on the same machine with two different web servers, the adaptors share the public WebObjects.conf file, allowing applications to be visible on both web servers. | If you attempt to run two WebObjects adaptors on the same machine with two different web servers, the adaptors share the public WebObjects.conf file, allowing applications to be visible on both web servers. |
| Workaround | There is a #define that sets the location of the configuration directory in Apple/Developer/Examples/WebObjects/Source/Adaptors/Adaptor/woconfig.h. Change this #define and recompile the adaptor. Now you can have several web servers running adaptors that do not share the same applications. | There is a #define that sets the location of the configuration directory in Apple/Developer/Examples/WebObjects/Source/Adaptors/Adaptor/woconfig.h. Change this #define and recompile the adaptor. Now you can have several web servers running adaptors that do not share the same applications. |
|  |  |  |
|  |  |  |

---

### Dynamic Elements

|  |  |  |
| --- | --- | --- |
| Reference | 2425444 | 2425444 |
| Problem | When binding a date object to a WOTextField, you must also bind a formatter. | When binding a date object to a WOTextField, you must also bind a formatter. |
| Description | If you bind an NSGregorianDate object to a WOTextField's value attribute but do not bind either a date format string to dateFormat or a formatter object to formatter, after submission the date object will be invalid. For example, entering '10/10/20' will store an NSGregorianDate with a yearOfCommonEra: 1. | If you bind an NSGregorianDate object to a WOTextField's value attribute but do not bind either a date format string to dateFormat or a formatter object to formatter, after submission the date object will be invalid. For example, entering '10/10/20' will store an NSGregorianDate with a yearOfCommonEra: 1. |
| Workaround | Bind either the dateFormat or formatter attributes as well. | Bind either the dateFormat or formatter attributes as well. |
|  |  |  |
|  |  |  |
| Reference | 2421645 | 2421645 |
| Problem | WOFrame doesn't allow a file URL to be bound to its 'src' attribute | WOFrame doesn't allow a file URL to be bound to its 'src' attribute |
| Description | If you bind a URL which begins with "file:" to a WOFrame's 'src' binding, the WOFrame will try to send -isRelativeURL to an NSAbsoluteURL and will raise an exception. | If you bind a URL which begins with "file:" to a WOFrame's 'src' binding, the WOFrame will try to send -isRelativeURL to an NSAbsoluteURL and will raise an exception. |
| Workaround | Use a WOGenericElement as follows:    MyFrame: WOGenericElement {  elementName = "frame";  src = "file:/path/to/my/file";  } | Use a WOGenericElement as follows:    MyFrame: WOGenericElement {  elementName = "frame";  src = "file:/path/to/my/file";  } |
|  |  |  |
|  |  |  |
| Reference | 2410285 | 2410285 |
| Problem | WOConditional's 'condition' attribute shouldn't be bound to an object | WOConditional's 'condition' attribute shouldn't be bound to an object |
| Description | Although you're allowed to bind the 'condition' attribute of a WOConditional to an object (as opposed to a true/false value), in bridged Java WebObjects sometimes determines the truth-value of the object by sending it an 'intValue' message and evaluating the result of that method. In the particular case of a Java String object, for instance, this will result in the object sometimes being true and sometimes being false. This clearly can lead to unpredictable behavior. | Although you're allowed to bind the 'condition' attribute of a WOConditional to an object (as opposed to a true/false value), in bridged Java WebObjects sometimes determines the truth-value of the object by sending it an 'intValue' message and evaluating the result of that method. In the particular case of a Java String object, for instance, this will result in the object sometimes being true and sometimes being false. This clearly can lead to unpredictable behavior. |
| Workaround | Never bind the condition attribute to an object. Instead, always make sure that the condition evaluates to true/false (the 'boolean' primitive in Java, for instance). | Never bind the condition attribute to an object. Instead, always make sure that the condition evaluates to true/false (the 'boolean' primitive in Java, for instance). |
|  |  |  |
|  |  |  |
| Reference | 2343393 | 2343393 |
| Problem | A WebObjects component, which worked in 4.0.1, reports an error with WebObjects 4.5 | A WebObjects component, which worked in 4.0.1, reports an error with WebObjects 4.5 |
| Description | The WebObjects 4.5 .wod format does not support attribute names containing hyphens unless they are enclosed in double-quotes. For example:    Foo: WOMetaRefresh {  http-equiv = "goop";  }    should read    Foo: WOMetaRefresh {  "http-equiv" = "goop";  } | The WebObjects 4.5 .wod format does not support attribute names containing hyphens unless they are enclosed in double-quotes. For example:    Foo: WOMetaRefresh {  http-equiv = "goop";  }    should read    Foo: WOMetaRefresh {  "http-equiv" = "goop";  } |
| Workaround | Add quotes to attribute containing hyphens. | Add quotes to attribute containing hyphens. |
|  |  |  |
|  |  |  |
| Reference | 2377692 | 2377692 |
| Problem | WODynamicElement's initWithName:associations:template: method now allows the template parameter to be nil. | WODynamicElement's initWithName:associations:template: method now allows the template parameter to be nil. |
| Description | In WebObjects 4.5 WODynamicElement's initWithName:associations:template: method--which corresponds to the Java constructor WODynamicElement(String, NSDictionary, WOElement)--has changed slightly in that it now allows the template parameter to be nil. This change should only affect developers who have created their own dynamic elements. | In WebObjects 4.5 WODynamicElement's initWithName:associations:template: method--which corresponds to the Java constructor WODynamicElement(String, NSDictionary, WOElement)--has changed slightly in that it now allows the template parameter to be nil. This change should only affect developers who have created their own dynamic elements. |
| Workaround | Update your custom dynamic elements so that they handle a nil template parameter. | Update your custom dynamic elements so that they handle a nil template parameter. |
|  |  |  |
|  |  |  |
| Reference | 2164906 | 2164906 |
| Problem | WOCheckbox checked attribute doesn't work as expected | WOCheckbox checked attribute doesn't work as expected |
| Description | WOCheckBox's checked attribute should return YES or NO as specified in the API, but it actually returns self or nil. | WOCheckBox's checked attribute should return YES or NO as specified in the API, but it actually returns self or nil. |
| Workaround | Test the checked attribute for nil or non-nil values instead of NO or YES. You may also want to write your own checkbox component that returns YES or NO instead of self or nil. | Test the checked attribute for nil or non-nil values instead of NO or YES. You may also want to write your own checkbox component that returns YES or NO instead of self or nil. |
|  |  |  |
|  |  |  |
| Reference | 2178762 | 2178762 |
| Problem | WOActiveImage should have a name attribute even when not in a form | WOActiveImage should have a name attribute even when not in a form |
| Description | WOActiveImage's name attribute is useful for doing JavaScript tricks, but doesn't appear if the WOActiveImage isn't in a form. | WOActiveImage's name attribute is useful for doing JavaScript tricks, but doesn't appear if the WOActiveImage isn't in a form. |
| Workaround | Use a generic element as a hyperlink around a WOImage instead of a WOActiveImage. For example:    JSActiveButton.wod:  JSActiveButton: WOHyperlink {  action = action;  alt = message;  onMouseOver = activateImageScript;  onMouseOut = deactivateImageScript;  };    ButtonImage: WOImage {  src = imagePath;  name = imageName;  width = width;  height = height;  border = 0;  };    JSActiveButton.wos:    id imageName;  id message;  id toPage;  id width;  id height;    // Private vars  id activateImage;  id deactivateImage;  id includeScript;    - script {  // It's just too trivial to warrant another file !  return @"function setButtonImage(imageName, imagePath) { document.images[imageName].src = imagePath; }";  }    - activateImageScript {  if (! activateImage) {  activateImage = [NSString stringWithFormat:@"setButtonImage('%@', '%@'); window.status='%@';return true;", imageName, [self highlightedImagePath], message];  }  return activateImage;  }    - deactivateImageScript {  if (! deactivateImage) {  deactivateImage = [NSString stringWithFormat:@"setButtonImage('%@', '%@'); window.status='';", imageName, [self imagePath]];  }  return deactivateImage;  } | Use a generic element as a hyperlink around a WOImage instead of a WOActiveImage. For example:    JSActiveButton.wod:  JSActiveButton: WOHyperlink {  action = action;  alt = message;  onMouseOver = activateImageScript;  onMouseOut = deactivateImageScript;  };    ButtonImage: WOImage {  src = imagePath;  name = imageName;  width = width;  height = height;  border = 0;  };    JSActiveButton.wos:    id imageName;  id message;  id toPage;  id width;  id height;    // Private vars  id activateImage;  id deactivateImage;  id includeScript;    - script {  // It's just too trivial to warrant another file !  return @"function setButtonImage(imageName, imagePath) { document.images[imageName].src = imagePath; }";  }    - activateImageScript {  if (! activateImage) {  activateImage = [NSString stringWithFormat:@"setButtonImage('%@', '%@'); window.status='%@';return true;", imageName, [self highlightedImagePath], message];  }  return activateImage;  }    - deactivateImageScript {  if (! deactivateImage) {  deactivateImage = [NSString stringWithFormat:@"setButtonImage('%@', '%@'); window.status='';", imageName, [self imagePath]];  }  return deactivateImage;  } |
|  |  |  |
|  |  |  |

---

### WOExtensions

|  |  |  |
| --- | --- | --- |
| Reference | 2395684 | 2395684 |
| Problem | JSValidatedField WOExtensions component fails to check the validity of fields if the user does not tab through them. | JSValidatedField WOExtensions component fails to check the validity of fields if the user does not tab through them. |
| Description | The Java Script code for JSValidatedField is only invoked when the user tabs through the field. If the user submits the form without tabbing through the fields, the fields will not be validated. | The Java Script code for JSValidatedField is only invoked when the user tabs through the field. If the user submits the form without tabbing through the fields, the fields will not be validated. |
| Workaround | None. | None. |
|  |  |  |
|  |  |  |
| Reference | 2383290 | 2383290 |
| Problem | My browser complains that there are syntax errors in the JSModalWindow JavaScript code. | My browser complains that there are syntax errors in the JSModalWindow JavaScript code. |
| Description | Spaces in the window name (specified by the windowName binding) can prevent the modal window from appearing and trigger a Java Script syntax error message from the browser. | Spaces in the window name (specified by the windowName binding) can prevent the modal window from appearing and trigger a Java Script syntax error message from the browser. |
| Workaround | Remove the spaces from your window names. | Remove the spaces from your window names. |
|  |  |  |
|  |  |  |
| Reference | 2369994 | 2369994 |
| Problem | WOTable WebObjects Extension specification is missing the cellWidth and tableWidth bindings. | WOTable WebObjects Extension specification is missing the cellWidth and tableWidth bindings. |
| Description | The documentation should have the following bindings:    tableWidth  The width of the table. This attribute is passed to the HTML TABLE tag.    cellWidth  The width of the cells in the table. This attribute is passed to each HTML TD tag in the table. | The documentation should have the following bindings:    tableWidth  The width of the table. This attribute is passed to the HTML TABLE tag.    cellWidth  The width of the cells in the table. This attribute is passed to each HTML TD tag in the table. |
| Workaround | None needed. | None needed. |
|  |  |  |
|  |  |  |

---

### EO Java Client

|  |  |  |
| --- | --- | --- |
| Reference | 2275826 | 2275826 |
| Problem | EOPalette won't parse keys from the source code of client-side Java classes | EOPalette won't parse keys from the source code of client-side Java classes |
| Description | If you drop a display group into a client-side nib, EOPalette won't recognize keys from the client-side class associated with the entity. Instead, it parses keys from the server side class. | If you drop a display group into a client-side nib, EOPalette won't recognize keys from the client-side class associated with the entity. Instead, it parses keys from the server side class. |
| Workaround | Add any keys you need manually, using the EODisplayGroup inspector. | Add any keys you need manually, using the EODisplayGroup inspector. |
|  |  |  |
|  |  |  |
| Reference | 2261908 | 2261908 |
| Problem | Can't use custom value classes on the client when using Java Client Distribution | Can't use custom value classes on the client when using Java Client Distribution |
| Description | In order to use a custom value class in your enterprise objects, you must use the same coding/decoding scheme that we use in the framework. This coder is not documented because it's likely to change for the next revision of our software. | In order to use a custom value class in your enterprise objects, you must use the same coding/decoding scheme that we use in the framework. This coder is not documented because it's likely to change for the next revision of our software. |
| Workaround | None. | None. |
|  |  |  |
|  |  |  |
| Reference | 2377934 | 2377934 |
| Problem | When you add instance variables to EO's that are subclasses of EOGenericRecord and change your accessors to match, fetched EO's look like they're empty. | When you add instance variables to EO's that are subclasses of EOGenericRecord and change your accessors to match, fetched EO's look like they're empty. |
| Description | The logic to create the binder objects used by the client version of EOContol incorrectly creates a binder that stores the value from the database in the EOGenericRecord dictionary rather then in the instance variable. If your logic looks for data in the instance variable, it always finds it empty. | The logic to create the binder objects used by the client version of EOContol incorrectly creates a binder that stores the value from the database in the EOGenericRecord dictionary rather then in the instance variable. If your logic looks for data in the instance variable, it always finds it empty. |
| Workaround | Don't add instance variables to your subclasses of EOGenericRecord, or reparent them to use EOCustomClass. | Don't add instance variables to your subclasses of EOGenericRecord, or reparent them to use EOCustomClass. |
|  |  |  |
|  |  |  |
| Reference | 2281716 | 2281716 |
| Problem | Java Client applets can use the wrong session on the application server | Java Client applets can use the wrong session on the application server |
| Description | Web browsers don't usually start a new Java VM when a new applet is started. The Java Client applet stores some information about the session in static variables--these variables may be reused if a second Java Client applet is started in the same VM. If the original session has already timed out by the time you display the second applet, you'll get a "your session timed out" error message. Otherwise, the second applet will use the original applet's session on the server, instead of the current one. | Web browsers don't usually start a new Java VM when a new applet is started. The Java Client applet stores some information about the session in static variables--these variables may be reused if a second Java Client applet is started in the same VM. If the original session has already timed out by the time you display the second applet, you'll get a "your session timed out" error message. Otherwise, the second applet will use the original applet's session on the server, instead of the current one. |
| Workaround | Run the client as an application, or restart the Web browser between uses of a Java Client applet. | Run the client as an application, or restart the Web browser between uses of a Java Client applet. |
|  |  |  |
|  |  |  |
| Reference | 2275922 | 2275922 |
| Problem | Browser (Internet Explorer and Netscape) implementations of AWT are not sufficient. | Browser (Internet Explorer and Netscape) implementations of AWT are not sufficient. |
| Description | On Windows, if you run Java Client applets in browsers, they might not work correctly without Sun's Java Plug-in. In Netscape, Java Client applications do not work at all without the plug-in. In Internet Explorer, combo boxes do not work properly, and modal "Save" dialogs that appear when closing a window often let the application hang.    Under MacOS, running Java Client (Swing) applets requires MRJ 2.1 or a later version. | On Windows, if you run Java Client applets in browsers, they might not work correctly without Sun's Java Plug-in. In Netscape, Java Client applications do not work at all without the plug-in. In Internet Explorer, combo boxes do not work properly, and modal "Save" dialogs that appear when closing a window often let the application hang.    Under MacOS, running Java Client (Swing) applets requires MRJ 2.1 or a later version. |
| Workaround | Run the client as an application (in the java interpreter) or use the Java Plug-in. | Run the client as an application (in the java interpreter) or use the Java Plug-in. |
|  |  |  |
|  |  |  |
| Reference | 2367086 | 2367086 |
| Problem | Java Client Windows do not become visible on Windows NT. | Java Client Windows do not become visible on Windows NT. |
| Description | There appears to be a bug in the Windows AWT which results in windows not becoming visible. The Windows task bar actually shows the window. | There appears to be a bug in the Windows AWT which results in windows not becoming visible. The Windows task bar actually shows the window. |
| Workaround | Right-click on the window's button in the task bar and use the context menu to maximize the window. | Right-click on the window's button in the task bar and use the context menu to maximize the window. |
|  |  |  |
|  |  |  |
| Reference | 2254297 | 2254297 |
| Problem | The column-based sort ordering of tables seen in InterfaceBuilder does not occur at runtime. | The column-based sort ordering of tables seen in InterfaceBuilder does not occur at runtime. |
| Description | Table rows appear in fetch order no matter which column is left-most. | Table rows appear in fetch order no matter which column is left-most. |
| Workaround | Connect the EODisplayGroup acting as the table's dataSource to an EOInterfaceController outlet and invoke setSortOrderings within the controller's constructor. | Connect the EODisplayGroup acting as the table's dataSource to an EOInterfaceController outlet and invoke setSortOrderings within the controller's constructor. |
|  |  |  |
|  |  |  |
| Reference | 2269932 | 2269932 |
| Problem | Adding a subproject of type EOJavaClientSubproject does not add the EOJavaClient.framework to the project's frameworks. | Adding a subproject of type EOJavaClientSubproject does not add the EOJavaClient.framework to the project's frameworks. |
| Description | If you create Java Client interface controllers and interface files (nib files) in a Java Client subproject, you have to add the EOJavaClient.framework to the root project's frameworks. Otherwise you can't compile the client-side classes and you can't run the application. | If you create Java Client interface controllers and interface files (nib files) in a Java Client subproject, you have to add the EOJavaClient.framework to the root project's frameworks. Otherwise you can't compile the client-side classes and you can't run the application. |
| Workaround | Add the EOJavaClient.framework by hand. | Add the EOJavaClient.framework by hand. |
|  |  |  |
|  |  |  |
| Reference | 2261318 | 2261318 |
| Problem | WebObjects Java Client wizards always use the package name "<application name>.client". | WebObjects Java Client wizards always use the package name "<application name>.client". |
| Description | The Java Client wizards create interface controllers and interface files for the client side. The Java classes are always placed in a package named "<application name>.client". | The Java Client wizards create interface controllers and interface files for the client side. The Java classes are always placed in a package named "<application name>.client". |
| Workaround | The first time a Java Client wizard is used, it inserts a special key named EOJAVACLIENT_WIZARD_PACKAGE into the PB.project of the topmost non-aggregate project (usually the application project). By editing the value of this key by hand you can change the package name used by the wizard. To edit the value, close the project in ProjectBuilder, open the PB.project file in a text editor (for example TextEdit), change the value, save the PB.project file and reopen it in ProjectBuilder. | The first time a Java Client wizard is used, it inserts a special key named EOJAVACLIENT_WIZARD_PACKAGE into the PB.project of the topmost non-aggregate project (usually the application project). By editing the value of this key by hand you can change the package name used by the wizard. To edit the value, close the project in ProjectBuilder, open the PB.project file in a text editor (for example TextEdit), change the value, save the PB.project file and reopen it in ProjectBuilder. |
|  |  |  |
|  |  |  |

---

### Direct to Web

|  |  |  |
| --- | --- | --- |
| Reference | 2282046 | 2282046 |
| Problem | The Live Assistant won't launch under Netscape 4 | The Live Assistant won't launch under Netscape 4 |
| Description | Attempting use the Live Assistant under Netscape 4.0x on NT or MacOS using the customize button produces a java security exception. This is caused by the fact that Netscape 4.0x does not implement the complete 1.1 Java specification | Attempting use the Live Assistant under Netscape 4.0x on NT or MacOS using the customize button produces a java security exception. This is caused by the fact that Netscape 4.0x does not implement the complete 1.1 Java specification |
| Workaround | Use Netscape 4.5, Internet Explorer 4.0 or 3.0, or appletviewer to connect to the Live Assistant. | Use Netscape 4.5, Internet Explorer 4.0 or 3.0, or appletviewer to connect to the Live Assistant. |
|  |  |  |
|  |  |  |
| Reference | 2429855 | 2429855 |
| Problem | D2WCustomComponent settings are ignored when they affect all entities | D2WCustomComponent settings are ignored when they affect all entities |
| Description | DirectToWeb generates the wrong rule when setting a custom component to be used for a specific type on all entities. For example, if you set a component called EditDatePopup to be used in list pages for all NSDates, your d2wmodel file will include the incorrect rule  ((task = 'list') and (propertyKey = 'NSDate')) ====>> customComponentName = EditDatePopup | DirectToWeb generates the wrong rule when setting a custom component to be used for a specific type on all entities. For example, if you set a component called EditDatePopup to be used in list pages for all NSDates, your d2wmodel file will include the incorrect rule  ((task = 'list') and (propertyKey = 'NSDate')) ====>> customComponentName = EditDatePopup |
| Workaround | Edit the d2wmodel file by hand (or with RuleEditor) to say "attribute.valueClassName" instead of "propertyKey". For example:    ((task = 'list') and (attribute.valueClassName = 'NSDate')) ====>> customComponentName = EditDatePopup | Edit the d2wmodel file by hand (or with RuleEditor) to say "attribute.valueClassName" instead of "propertyKey". For example:    ((task = 'list') and (attribute.valueClassName = 'NSDate')) ====>> customComponentName = EditDatePopup |
|  |  |  |
|  |  |  |
| Reference | 2427535 | 2427535 |
| Problem | The DirectToWeb Assistant in Netscape 4.7/NT throws up an alert panel when I click on update. | The DirectToWeb Assistant in Netscape 4.7/NT throws up an alert panel when I click on update. |
| Description | After making modification in the DirectToWeb live assistant, when I click on update to send my changes to the server, I get an alert panel with a message similar to: "Socket is not a file descriptor". This problem only happens after resizing either the window or the browser frame which contains the small Assistant Applet (whose visible part is the 'Show Assistant' button). | After making modification in the DirectToWeb live assistant, when I click on update to send my changes to the server, I get an alert panel with a message similar to: "Socket is not a file descriptor". This problem only happens after resizing either the window or the browser frame which contains the small Assistant Applet (whose visible part is the 'Show Assistant' button). |
| Workaround | Either use Microsoft Internet Explorer, appletViewer, or an earlier version of Netscape, or simply avoid resizing your browser windows after launching the assistant. | Either use Microsoft Internet Explorer, appletViewer, or an earlier version of Netscape, or simply avoid resizing your browser windows after launching the assistant. |
|  |  |  |
|  |  |  |
| Reference | 2425118 | 2425118 |
| Problem | RuleEditor does not allow, or ignores, some rule edits | RuleEditor does not allow, or ignores, some rule edits |
| Description | There are two known problems with editing rules in the RuleEditor:    1) Changes made in the text field below the qualifier browser aren't always registered.    2) The Custom field in the right-hand area becomes disabled when you first change the Class PopUp to use a CUSTOM class. | There are two known problems with editing rules in the RuleEditor:    1) Changes made in the text field below the qualifier browser aren't always registered.    2) The Custom field in the right-hand area becomes disabled when you first change the Class PopUp to use a CUSTOM class. |
| Workaround | Both of these problems have workarounds:    1) Edit rule values directly in the qualifier browser areas.    2) When changing the right-hand Class PopUp to use a Custom class, fill all of the other fields (Key, Priority, Value) first. Then, select any other rule and then reselect the rule you're trying to edit. When the rule is selected for the second time, the Custom text field will be editable and you'll be able to enter the name of your custom class. | Both of these problems have workarounds:    1) Edit rule values directly in the qualifier browser areas.    2) When changing the right-hand Class PopUp to use a Custom class, fill all of the other fields (Key, Priority, Value) first. Then, select any other rule and then reselect the rule you're trying to edit. When the rule is selected for the second time, the Custom text field will be editable and you'll be able to enter the name of your custom class. |
|  |  |  |
|  |  |  |
| Reference | 2424172 | 2424172 |
| Problem | Direct to Web applications hang in multithreaded mode. | Direct to Web applications hang in multithreaded mode. |
| Description | An editing context in your application may be locked and not properly unlocked. Due to the details of how Direct to Web locks editing contexts, an editing context isn't unlocked when you create a new Direct to Web page without rendering it.    In WebObjects, the locking and unlocking of session.defaultEditingContext is performed transparently. However, if your application uses other editing contexts, you need to lock them yourself.    Direct to Web helps you manage the locking of such editing contexts:    - The edit and inspect pages lock the editing context when the setObject method is invoked.    - The edit-relationship page locks the editing context when the setObjectAndMasterRelationshipKey method is invoked.    - The inspect, edit, and edit-relationship pages lock the editing context of the object they manipulate when the awake method is invoked    - The inspect, edit and edit-relationship pages unlock the editing context of the object they manipulate when the sleep method is invoked.    Therefore the following code:    myPage=D2W.factory().inspectPageForEntityNamed("FOO",session());  myPage.setObject(myEO);  return myPage;    requires no extra lock/unlock statements on your part, even when myEO is not in session.defaultEditingContext.    However if you do not render the page right away but store it instead, the editing context remains locked unless you unlock it yourself. | An editing context in your application may be locked and not properly unlocked. Due to the details of how Direct to Web locks editing contexts, an editing context isn't unlocked when you create a new Direct to Web page without rendering it.    In WebObjects, the locking and unlocking of session.defaultEditingContext is performed transparently. However, if your application uses other editing contexts, you need to lock them yourself.    Direct to Web helps you manage the locking of such editing contexts:    - The edit and inspect pages lock the editing context when the setObject method is invoked.    - The edit-relationship page locks the editing context when the setObjectAndMasterRelationshipKey method is invoked.    - The inspect, edit, and edit-relationship pages lock the editing context of the object they manipulate when the awake method is invoked    - The inspect, edit and edit-relationship pages unlock the editing context of the object they manipulate when the sleep method is invoked.    Therefore the following code:    myPage=D2W.factory().inspectPageForEntityNamed("FOO",session());  myPage.setObject(myEO);  return myPage;    requires no extra lock/unlock statements on your part, even when myEO is not in session.defaultEditingContext.    However if you do not render the page right away but store it instead, the editing context remains locked unless you unlock it yourself. |
| Workaround | Unlock the editing context explicitly by calling sleep():    myPage=D2W.factory().inspectPageForEntityNamed("FOO",session());  myPage.setObject(myEO);  myPage.sleep();  thisOtherPage.setNextPage(myPage); | Unlock the editing context explicitly by calling sleep():    myPage=D2W.factory().inspectPageForEntityNamed("FOO",session());  myPage.setObject(myEO);  myPage.sleep();  thisOtherPage.setNextPage(myPage); |
|  |  |  |
|  |  |  |
| Reference | 2365760 | 2365760 |
| Problem | String query behavior on Direct to Web query pages does not match documentation. | String query behavior on Direct to Web query pages does not match documentation. |
| Description | The default property-level component used for string queries has been changed from D2WQueryStringComponent to D2WQueryStringOperator. The new component provides more powerful string matching operators: starts with, contains, ends with, is, and like. It also provides the standard =, <>, <, <=, >, and >= operators. | The default property-level component used for string queries has been changed from D2WQueryStringComponent to D2WQueryStringOperator. The new component provides more powerful string matching operators: starts with, contains, ends with, is, and like. It also provides the standard =, <>, <, <=, >, and >= operators. |
| Workaround | If you want the D2WQueryStringComponent (the default component in previous releases), use the property tab in the Web Assistant to change the component. You can do this on a property by property basis in standard mode. In expert mode, you can change the component used to query for NSStrings on a global basis, by selecting task='query' and entity='\*all\*'. | If you want the D2WQueryStringComponent (the default component in previous releases), use the property tab in the Web Assistant to change the component. You can do this on a property by property basis in standard mode. In expert mode, you can change the component used to query for NSStrings on a global basis, by selecting task='query' and entity='\*all\*'. |
|  |  |  |
|  |  |  |
| Reference | 2363291 | 2363291 |
| Problem | Direct to Web classes do not appear in the Java Browser by default. | Direct to Web classes do not appear in the Java Browser by default. |
| Description | When you start up the Java Browser application, the Direct to Web classes are not included in the list of classes that appears. | When you start up the Java Browser application, the Direct to Web classes are not included in the list of classes that appears. |
| Workaround | Add the framework by hand.  1. Select File -> Add Classes.  2. Navigate to /System/Library/Frameworks/DirectToWeb.framework/Resources/Java ($NEXT_ROOT\Library\Frameworks\DirectToWeb.framework\Resources\Java on Windows NT)  3. Select directtoweb.zip. | Add the framework by hand.  1. Select File -> Add Classes.  2. Navigate to /System/Library/Frameworks/DirectToWeb.framework/Resources/Java ($NEXT_ROOT\Library\Frameworks\DirectToWeb.framework\Resources\Java on Windows NT)  3. Select directtoweb.zip. |
|  |  |  |
|  |  |  |
| Reference | 2274611 | 2274611 |
| Problem | DirectToWeb raises on custom or non-existent keys | DirectToWeb raises on custom or non-existent keys |
| Description | Either due to a mistyped key in the Live Assistant or the removal or renaming of an attribute or relationship in EOModeler, an EOUnknownKey exception can be raised when you run a DirectToWeb application. | Either due to a mistyped key in the Live Assistant or the removal or renaming of an attribute or relationship in EOModeler, an EOUnknownKey exception can be raised when you run a DirectToWeb application. |
| Workaround | Using the Live Assistant's expert mode, select the task/entity couple for which you're getting an exception and hide the key that is causing the problem. | Using the Live Assistant's expert mode, select the task/entity couple for which you're getting an exception and hide the key that is causing the problem. |
|  |  |  |
|  |  |  |
| Reference | 2274181 | 2274181 |
| Problem | DisplayHyperlink does not work properly with incomplete URL's. | DisplayHyperlink does not work properly with incomplete URL's. |
| Description | When using the DisplayHyperlink component, the properties are incomplete URL's missing the "http://", and the generated HTML is incorrect. | When using the DisplayHyperlink component, the properties are incomplete URL's missing the "http://", and the generated HTML is incorrect. |
| Workaround | Generate the page and modify the WOString in the HREF so that "http://" is added if needed. This is the quick and dirty solution.    A cleaner solution is to generate a custom class for your EO that contains the hyperlink. In that custom class, add a custom method (e.g., 'absoluteURL') that returns the proper value (i.e., adding "http://" if needed). From the live assistant, hide the property key is generating the   incorrect url, click on the add button, and enter 'absoluteURL' in the dialog box. Then select 'absoluteURL' in the property key list and DisplayHyperlink for its component. | Generate the page and modify the WOString in the HREF so that "http://" is added if needed. This is the quick and dirty solution.    A cleaner solution is to generate a custom class for your EO that contains the hyperlink. In that custom class, add a custom method (e.g., 'absoluteURL') that returns the proper value (i.e., adding "http://" if needed). From the live assistant, hide the property key is generating the   incorrect url, click on the add button, and enter 'absoluteURL' in the dialog box. Then select 'absoluteURL' in the property key list and DisplayHyperlink for its component. |
|  |  |  |
|  |  |  |
| Reference | 2258117 | 2258117 |
| Problem | Page not refreshed automatically after update | Page not refreshed automatically after update |
| Description | Launch the live assistant in applet viewer and use a separate browser to see a DirectToWeb application. After clicking on update in the Live Assistant, the page is not always refreshed with the new settings. | Launch the live assistant in applet viewer and use a separate browser to see a DirectToWeb application. After clicking on update in the Live Assistant, the page is not always refreshed with the new settings. |
| Workaround | If Java was disabled in your browser, enable it. If your browser doesn't support Java, hitting refresh, or in some cases re-navigating to a new instance of the same page, will display the new settings. | If Java was disabled in your browser, enable it. If your browser doesn't support Java, hitting refresh, or in some cases re-navigating to a new instance of the same page, will display the new settings. |
|  |  |  |
|  |  |  |
| Reference | 2253962 | 2253962 |
| Problem | Newly-created DirectToWeb projects sometimes come up empty | Newly-created DirectToWeb projects sometimes come up empty |
| Description | If you create a new DirectToWeb project in ProjectBuilder and point the wizard at an existing model, the project may come up empty. This can happen if you don't have read permission in the file system for the .eomodeld directory or for the files inside. | If you create a new DirectToWeb project in ProjectBuilder and point the wizard at an existing model, the project may come up empty. This can happen if you don't have read permission in the file system for the .eomodeld directory or for the files inside. |
| Workaround | Use a model for which you have read access. | Use a model for which you have read access. |
|  |  |  |
|  |  |  |
| Reference | 2201189 | 2201189 |
| Problem | DirectToWeb does not handle queries custom data types | DirectToWeb does not handle queries custom data types |
| Description | If one of your attributes has a custom data types (i.e. not one of the built-in types such as NSNumber, NSDecimalNumber, NSDate, NSCalendateDate..) can can get an exception when DirectToWeb is trying to display it. | If one of your attributes has a custom data types (i.e. not one of the built-in types such as NSNumber, NSDecimalNumber, NSDate, NSCalendateDate..) can can get an exception when DirectToWeb is trying to display it. |
| Workaround | Using the Live Assistant, navigate to the faulty query page in expert mode and hide the property that has a custom type. | Using the Live Assistant, navigate to the faulty query page in expert mode and hide the property that has a custom type. |
|  |  |  |
|  |  |  |
| Reference | 2182327 | 2182327 |
| Problem | Creating a D2W project with the rentals model raises | Creating a D2W project with the rentals model raises |
| Description | The rentals models has cross-model relationships with the movies model. The wizard does not not notice this and fails to pull both models in the project by default. This results in runtime errors when the destination of the cross-model relationships cannot be resolved. | The rentals models has cross-model relationships with the movies model. The wizard does not not notice this and fails to pull both models in the project by default. This results in runtime errors when the destination of the cross-model relationships cannot be resolved. |
| Workaround | Everything works fine if you drag a copy of both models in the newly created project. | Everything works fine if you drag a copy of both models in the newly created project. |
|  |  |  |
|  |  |  |
| Reference | 2181971 | 2181971 |
| Problem | Cannot start the Web Assistant on Solaris. | Cannot start the Web Assistant on Solaris. |
| Description | If you try to start the Web Assistant for a Direct to Web application on Solaris, you receive a log similar to the following:    Oct 16 02:31:45 d2walpha[4181] waiting for requests...  ld.so.1: ./d2walpha: fatal: libnet.so: can't open file: errno=2 (libnet.so)  java.lang.UnsatisfiedLinkError: no net in shared library path  at java.lang.Runtime.loadLibrary(Runtime.java)  at java.lang.System.loadLibrary(System.java)  at   at java.net.ServerSocket.<init>(ServerSocket.java:57)  ... | If you try to start the Web Assistant for a Direct to Web application on Solaris, you receive a log similar to the following:    Oct 16 02:31:45 d2walpha[4181] waiting for requests...  ld.so.1: ./d2walpha: fatal: libnet.so: can't open file: errno=2 (libnet.so)  java.lang.UnsatisfiedLinkError: no net in shared library path  at java.lang.Runtime.loadLibrary(Runtime.java)  at java.lang.System.loadLibrary(System.java)  at   at java.net.ServerSocket.<init>(ServerSocket.java:57)  ... |
| Workaround | Make sure libnet.so is in your path | Make sure libnet.so is in your path |
|  |  |  |
|  |  |  |

---

### XML Framework

|  |  |  |
| --- | --- | --- |
| Reference | 2430661 | 2430661 |
| Problem | XML Mappings needn't be unique for decoding, contrary to what the documentation says | XML Mappings needn't be unique for decoding, contrary to what the documentation says |
| Description | The XML Framework reference documentation states that mappings must be unique for a given property when decoding. This isn't true: they don't have to be unique for decoding (although they must be unique for encoding). The RelatedLinks example illustrates one situation where you can take advantage of multiple tags mapped to a single property. | The XML Framework reference documentation states that mappings must be unique for a given property when decoding. This isn't true: they don't have to be unique for decoding (although they must be unique for encoding). The RelatedLinks example illustrates one situation where you can take advantage of multiple tags mapped to a single property. |
| Workaround |  |  |
|  |  |  |
|  |  |  |
| Reference | 2424816 | 2424816 |
| Problem | java.io.FileNotFoundException: /usr/local/java/lib/content-types.properties when trying to read an XML file | java.io.FileNotFoundException: /usr/local/java/lib/content-types.properties when trying to read an XML file |
| Description | Either IBM's XML parser or sun.net.www.MimeTable seems to assume that /usr/local/java/lib/content-types.properties exists. This file is actually located in /usr/java/lib. | Either IBM's XML parser or sun.net.www.MimeTable seems to assume that /usr/local/java/lib/content-types.properties exists. This file is actually located in /usr/java/lib. |
| Workaround | Make a link from /usr/java to /usr/local/java, or copy the content-types.properties file to /usr/local/java/lib. | Make a link from /usr/java to /usr/local/java, or copy the content-types.properties file to /usr/local/java/lib. |
|  |  |  |
|  |  |  |
| Reference | 2399206 | 2399206 |
| Problem | The XML decoder cannot decode NSData that contains characters outside of the range of XML-allowed characters (those less than \u0020). | The XML decoder cannot decode NSData that contains characters outside of the range of XML-allowed characters (those less than \u0020). |
| Description | These characters will occur frequently when encoding or decoding NSData objects that represent images. | These characters will occur frequently when encoding or decoding NSData objects that represent images. |
| Workaround | None at this time. Avoid encoding or decoding images. | None at this time. Avoid encoding or decoding images. |
|  |  |  |
|  |  |  |
| Reference | 2394606 | 2394606 |
| Problem | In the introduction to the XML Framework Reference, the example under "contentsKey" isn't complete. | In the introduction to the XML Framework Reference, the example under "contentsKey" isn't complete. |
| Description | The example illustrating the use of the contentsKey attribute (in the XML Framework Reference introduction, under the section titled "The 'entity' Tag") will raise when the sample XML data is parsed if the <b> tag is not mapped. | The example illustrating the use of the contentsKey attribute (in the XML Framework Reference introduction, under the section titled "The 'entity' Tag") will raise when the sample XML data is parsed if the <b> tag is not mapped. |
| Workaround | Include a mapping for the <b> tag. | Include a mapping for the <b> tag. |
|  |  |  |
|  |  |  |
| Reference | 2393373 | 2393373 |
| Problem | The XML Framework reference doesn't specify the behavior to expect when you use the unmappedTagsKey attribute in a mapping model entity. | The XML Framework reference doesn't specify the behavior to expect when you use the unmappedTagsKey attribute in a mapping model entity. |
| Description | If your entity has the attribute unmappedTagsKey=myKey, any tags for which there is no specified mapping will be saved as key/value pairs in an NSMutableDictionary named myKey. | If your entity has the attribute unmappedTagsKey=myKey, any tags for which there is no specified mapping will be saved as key/value pairs in an NSMutableDictionary named myKey. |
| Workaround | None. | None. |
|  |  |  |
|  |  |  |

---

### Foundation Framework

|  |  |  |
| --- | --- | --- |
| Reference | 2425246 | 2425246 |
| Problem | Adding or removing certain Java classes to wrapped collection classes does not work | Adding or removing certain Java classes to wrapped collection classes does not work |
| Description | Trying to add or remove NSRect, NSSize or NSPoint or similar objects that correspond to structs in the Objective-C world to NSMutableArray can cause a crash. | Trying to add or remove NSRect, NSSize or NSPoint or similar objects that correspond to structs in the Objective-C world to NSMutableArray can cause a crash. |
| Workaround | Avoid this practice, perhaps by using your own wrapped classes or different Java classes to contain the information. | Avoid this practice, perhaps by using your own wrapped classes or different Java classes to contain the information. |
|  |  |  |
|  |  |  |
| Reference | 2425242 | 2425242 |
| Problem | -[NSCalendarDate dateByAddingYears:months:days:hours:minutes:seconds:] leaks on MacOS X Server. | -[NSCalendarDate dateByAddingYears:months:days:hours:minutes:seconds:] leaks on MacOS X Server. |
| Description | The object returned by this method should be autoreleased but it is not. The leak occurs when this method is invoked in Java or Objective-C. This problem has been fixed on Windows, HP-UX and Solaris. | The object returned by this method should be autoreleased but it is not. The leak occurs when this method is invoked in Java or Objective-C. This problem has been fixed on Windows, HP-UX and Solaris. |
| Workaround | A Tech Info Library article is available that explains how to work around this bug. See http://til.info.apple.com. | A Tech Info Library article is available that explains how to work around this bug. See http://til.info.apple.com. |
|  |  |  |
|  |  |  |
| Reference | 2424870 | 2424870 |
| Problem | Using distantFuture and distantPast methods on NSDate in Java causes UnsatisfiedLinkError on MacOS X Server. | Using distantFuture and distantPast methods on NSDate in Java causes UnsatisfiedLinkError on MacOS X Server. |
| Description | These methods are wrapped properly on Windows NT, Solaris, and HP-UX. | These methods are wrapped properly on Windows NT, Solaris, and HP-UX. |
| Workaround | A Tech Info Library article is available that explains how to work around this bug. See http://til.info.apple.com. | A Tech Info Library article is available that explains how to work around this bug. See http://til.info.apple.com. |
|  |  |  |
|  |  |  |
| Reference | 2424827 | 2424827 |
| Problem | NSCalendarDate dateByAddingGregorianUnits gives incorrect results on MacOS X Server. | NSCalendarDate dateByAddingGregorianUnits gives incorrect results on MacOS X Server. |
| Description | Adding a number of months, days, hours, or minutes outside the range of -128 to 127 causes an overflow and results in an incorrect date. This bug is fixed on Windows NT, Solaris, and HP-UX. | Adding a number of months, days, hours, or minutes outside the range of -128 to 127 causes an overflow and results in an incorrect date. This bug is fixed on Windows NT, Solaris, and HP-UX. |
| Workaround | A Tech Info Library article is available that explains how to work around this bug. See http://til.info.apple.com. | A Tech Info Library article is available that explains how to work around this bug. See http://til.info.apple.com. |
|  |  |  |
|  |  |  |
| Reference | 2424740 | 2424740 |
| Problem | Serialization (archiving) fails for Java subclasses of Objective-C classes that don't directly implement -encodeWithCoder: and -initWithCoder: | Serialization (archiving) fails for Java subclasses of Objective-C classes that don't directly implement -encodeWithCoder: and -initWithCoder: |
| Description | If you subclass an Objective-C class in Java and try to serialize (or archive) it, serialization will fail if the Objective-C superclass does not directly implement -encodeWithCoder: and -initWithCoder:. Serialization will fail even if the Objective-C class inherits an implementation of these two NSCoding methods.    For example you can subclass EOAndQualifier (which directly implements these methods) but not EOQualifier (which does not implement them itself; it relies on NSObject's implementation). | If you subclass an Objective-C class in Java and try to serialize (or archive) it, serialization will fail if the Objective-C superclass does not directly implement -encodeWithCoder: and -initWithCoder:. Serialization will fail even if the Objective-C class inherits an implementation of these two NSCoding methods.    For example you can subclass EOAndQualifier (which directly implements these methods) but not EOQualifier (which does not implement them itself; it relies on NSObject's implementation). |
| Workaround | Implement these methods in your Objective-C classes, if only to invoke super's implementation. | Implement these methods in your Objective-C classes, if only to invoke super's implementation. |
|  |  |  |
|  |  |  |
| Reference | 2423817 | 2423817 |
| Problem | Foundation's archiving methods aren't exposed in Java | Foundation's archiving methods aren't exposed in Java |
| Description | Because Java serialization does not support two-pass archiving (which is what +archiveRootObject:toFile: does), the following Objective-C methods are not exposed in the Java version of Foundation (these methods are marked as "deprecated" but should not be used because they'll cause a crash):    -encodeRootObject  +archivedDataWithRootObject  +archiveRootObject:toFile: | Because Java serialization does not support two-pass archiving (which is what +archiveRootObject:toFile: does), the following Objective-C methods are not exposed in the Java version of Foundation (these methods are marked as "deprecated" but should not be used because they'll cause a crash):    -encodeRootObject  +archivedDataWithRootObject  +archiveRootObject:toFile: |
| Workaround | None. | None. |
|  |  |  |
|  |  |  |
| Reference | 2414797 | 2414797 |
| Problem | Some Objective-C objects cannot be subclassed in Java. | Some Objective-C objects cannot be subclassed in Java. |
| Description | NSArray, NSNotification, NSDictionary--and possibly other Objective-C classes--cannot be subclassed in Java due to the fact that they don't implement any init... methods. | NSArray, NSNotification, NSDictionary--and possibly other Objective-C classes--cannot be subclassed in Java due to the fact that they don't implement any init... methods. |
| Workaround | None. | None. |
|  |  |  |
|  |  |  |
| Reference | 2405827 | 2405827 |
| Problem | valueForKeyPath and takeValueForKeyPath do not work with partial keys returning an NSArray and NSDictionary. | valueForKeyPath and takeValueForKeyPath do not work with partial keys returning an NSArray and NSDictionary. |
| Description | Key paths passed to valueForKeyPath and takeValueForKeyPath cannot contain a key that returns an NSArray or a NSDictionary, for example valueForKeyPath("roles.talent") on a Movie enterprise object (with the standard Movies.eomodeld example) does not work. | Key paths passed to valueForKeyPath and takeValueForKeyPath cannot contain a key that returns an NSArray or a NSDictionary, for example valueForKeyPath("roles.talent") on a Movie enterprise object (with the standard Movies.eomodeld example) does not work. |
| Workaround | Invoke valueForKey and takeValueForKey directly on the NSArray or NSDictionary, do not use helper methods on EOKeyValueCodingAdditions or so. | Invoke valueForKey and takeValueForKey directly on the NSArray or NSDictionary, do not use helper methods on EOKeyValueCodingAdditions or so. |
|  |  |  |
|  |  |  |
| Reference | 2397081 | 2397081 |
| Problem | BigInteger isn't supported in bridged Objective-C collection classes. | BigInteger isn't supported in bridged Objective-C collection classes. |
| Description | java.math.BigInteger objects can't be contained by the bridged Objective-C collection classes (NSDictionary, NSMutableDictionary, NSArray, and so on). This is due to the fact that the bridge doesn't know how to re-map BigInteger objects in Objective-C. An attempt to add a BigInteger object to such a collection will cause an Objective-C exception to be thrown indicating that a nil value cannot be added to the collection. | java.math.BigInteger objects can't be contained by the bridged Objective-C collection classes (NSDictionary, NSMutableDictionary, NSArray, and so on). This is due to the fact that the bridge doesn't know how to re-map BigInteger objects in Objective-C. An attempt to add a BigInteger object to such a collection will cause an Objective-C exception to be thrown indicating that a nil value cannot be added to the collection. |
| Workaround | None. | None. |
|  |  |  |
|  |  |  |
| Reference | 2396723 | 2396723 |
| Problem | +load methods cannot message Foundation. | +load methods cannot message Foundation. |
| Description | +load methods cannot contain references to argc, argv, or environ (or NX... equivalents). Within a +load method, you also cannot message any classes or objects in Foundation (or any subclasses of them, either). | +load methods cannot contain references to argc, argv, or environ (or NX... equivalents). Within a +load method, you also cannot message any classes or objects in Foundation (or any subclasses of them, either). |
| Workaround | Perform the needed operations at a later point in your application. | Perform the needed operations at a later point in your application. |
|  |  |  |
|  |  |  |
| Reference | 2372305 | 2372305 |
| Problem | NSAttributedString has Java constructors that are unimplemented. | NSAttributedString has Java constructors that are unimplemented. |
| Description | Certain Foundation methods for NSAttributed string are unimplemented on on HP-UX and Solaris platforms as they are in the AppKit framework (which is only available on Windows NT and Mac OS X Server).    The NSAttributedString documentation does not highlight this issue. If you attempt to use the unimplemented constructors, you will see an error such as:    NSAttributedString as = new NSAttributedString(data, new Object(), dict);  [NSAttributedString initWithHTML:baseURL:documentAttributes:]: selector not recognized | Certain Foundation methods for NSAttributed string are unimplemented on on HP-UX and Solaris platforms as they are in the AppKit framework (which is only available on Windows NT and Mac OS X Server).    The NSAttributedString documentation does not highlight this issue. If you attempt to use the unimplemented constructors, you will see an error such as:    NSAttributedString as = new NSAttributedString(data, new Object(), dict);  [NSAttributedString initWithHTML:baseURL:documentAttributes:]: selector not recognized |
| Workaround | In your WebObjects applications do not use methods that aren't implemented in Foundation. Check the Objective-C header file for NSAttributedString to determine which are available. | In your WebObjects applications do not use methods that aren't implemented in Foundation. Check the Objective-C header file for NSAttributedString to determine which are available. |
|  |  |  |
|  |  |  |
| Reference | 2364260 | 2364260 |
| Problem | NSMutableArray removeIdenticalObject method fails to remove the same string instance in Java. | NSMutableArray removeIdenticalObject method fails to remove the same string instance in Java. |
| Description | If you invoke removeIdenticalObject to remove a string instance you previously added to an NSMutable array, the method fails to remove the instance. In the example code:    String aString = "abc";  NSMutableArray anArray = new NSMutableArray();  anArray.addObject(aString);  anArray.removeIdenticalObject(aString);    the string "abc" is not deleted from the array. This problem occurs because the Java Bridge   creates new Objective-C strings whenever it converts Java Strings. The identical object methods use pointer comparisons instead of isEqual to determine if objects are the same. | If you invoke removeIdenticalObject to remove a string instance you previously added to an NSMutable array, the method fails to remove the instance. In the example code:    String aString = "abc";  NSMutableArray anArray = new NSMutableArray();  anArray.addObject(aString);  anArray.removeIdenticalObject(aString);    the string "abc" is not deleted from the array. This problem occurs because the Java Bridge   creates new Objective-C strings whenever it converts Java Strings. The identical object methods use pointer comparisons instead of isEqual to determine if objects are the same. |
| Workaround | Use removeObject instead. | Use removeObject instead. |
|  |  |  |
|  |  |  |
| Reference | 2339405 | 2339405 |
| Problem | NSNotFound is mentioned in the Java reference docs but isn't defined | NSNotFound is mentioned in the Java reference docs but isn't defined |
| Description | The documentation for NSArray in Java references the NSNotFound Foundation   constant. However it doesn't define this constant. | The documentation for NSArray in Java references the NSNotFound Foundation   constant. However it doesn't define this constant. |
| Workaround | See the Objective-C reference docs for the corresponding class when looking for information missing in the Java reference documentation for both Foundation and AppKit. | See the Objective-C reference docs for the corresponding class when looking for information missing in the Java reference documentation for both Foundation and AppKit. |
|  |  |  |
|  |  |  |
| Reference | 2308421 | 2308421 |
| Problem | NSObjects appear in Java components instead of the expected Foundation class (NSDecimalNumber, NSArray...) | NSObjects appear in Java components instead of the expected Foundation class (NSDecimalNumber, NSArray...) |
| Description | Java components or EOs that have methods which expect instances of a class in the com.apple.yellow.foundation package (such as NSArray, NSDecimalNumber) coming from Objective-C get NSObjects from the Java bridge, resulting, for example, in a ClassCastException. | Java components or EOs that have methods which expect instances of a class in the com.apple.yellow.foundation package (such as NSArray, NSDecimalNumber) coming from Objective-C get NSObjects from the Java bridge, resulting, for example, in a ClassCastException. |
| Workaround | Insert the following code into the constructor of your application:    public Application () {  new NSArray();  }    This will force FoundationJava to be initialized properly. | Insert the following code into the constructor of your application:    public Application () {  new NSArray();  }    This will force FoundationJava to be initialized properly. |
|  |  |  |
|  |  |  |

---

### WebObjects Builder

|  |  |  |
| --- | --- | --- |
| Reference | 2281669 | 2281669 |
| Problem | The Java parser used by WebObjectsBuilder does not recognize international characters. | The Java parser used by WebObjectsBuilder does not recognize international characters. |
| Description | Java variables and methods containing international characters do not appear in the WebObjectsBuilder browser. | Java variables and methods containing international characters do not appear in the WebObjectsBuilder browser. |
| Workaround | Don't use international characters when naming Java methods or variables. | Don't use international characters when naming Java methods or variables. |
|  |  |  |
|  |  |  |
| Reference | 2275047 | 2275047 |
| Problem | WebObjectsBuilder can't parse fully declared WebScript files | WebObjectsBuilder can't parse fully declared WebScript files |
| Description | If you have a wos file which uses @interface/@implementation to declare its class, the builder will not parse it correctly. You won't see the proper keys in the object browser and code generation will fail. | If you have a wos file which uses @interface/@implementation to declare its class, the builder will not parse it correctly. You won't see the proper keys in the object browser and code generation will fail. |
| Workaround | If you need to use @interface/@implementation (for example, if you need to subclass an existing component), convert your wos file to compiled Objective-C. | If you need to use @interface/@implementation (for example, if you need to subclass an existing component), convert your wos file to compiled Objective-C. |
|  |  |  |
|  |  |  |
| Reference | 2174247 | 2174247 |
| Problem | WebObjects Builder and Project Builder don't notify each other when application files are edited. | WebObjects Builder and Project Builder don't notify each other when application files are edited. |
| Description | WebObjects Builder does not notice any changes made in Project Builder to source code files, HTML files, or .wod files until you save. Likewise, Project Builder does not notice files that you edit in WebObjects Builder until you save. | WebObjects Builder does not notice any changes made in Project Builder to source code files, HTML files, or .wod files until you save. Likewise, Project Builder does not notice files that you edit in WebObjects Builder until you save. |
| Workaround | Save the edited files before switching applications. | Save the edited files before switching applications. |
|  |  |  |
|  |  |  |
| Reference | 2270740 | 2270740 |
| Problem | Localizing components in Project Builder removes them from the Global suitcase. | Localizing components in Project Builder removes them from the Global suitcase. |
| Description | If you choose the language for a component, the component will be removed from the top-level suitcase and will only appear in the chosen language suitcase(s). | If you choose the language for a component, the component will be removed from the top-level suitcase and will only appear in the chosen language suitcase(s). |
| Workaround | Open the PB.project file with a text editor, and add the component to the WO_COMPONENTS list. | Open the PB.project file with a text editor, and add the component to the WO_COMPONENTS list. |
|  |  |  |
|  |  |  |
| Reference | 2370222 | 2370222 |
| Problem | Opening a WebObjects 4.0 component can generate errors in WebObjects Builder. | Opening a WebObjects 4.0 component can generate errors in WebObjects Builder. |
| Description | For 4.5, WebObjects Builder now detects errors in components. One particular error occurs when previous versions of WebObjects Builder inserted the text "Custom" between the <WEBOBJECT> and </WEBOBJECT> tags for a custom component. If the component does not contain a WOComponentContent dynamic element, such component content is illegal and the current WebObjects Builder flags the content as an error. | For 4.5, WebObjects Builder now detects errors in components. One particular error occurs when previous versions of WebObjects Builder inserted the text "Custom" between the <WEBOBJECT> and </WEBOBJECT> tags for a custom component. If the component does not contain a WOComponentContent dynamic element, such component content is illegal and the current WebObjects Builder flags the content as an error. |
| Workaround | Remove the "Custom" text between the <WEBOBJECT> and </WEBOBJECT> tags for custom components without WOComponentContent. | Remove the "Custom" text between the <WEBOBJECT> and </WEBOBJECT> tags for custom components without WOComponentContent. |
|  |  |  |
|  |  |  |
| Reference | 2308405 | 2308405 |
| Problem | WebObjects Builder hangs or crashes when opening certain components. | WebObjects Builder hangs or crashes when opening certain components. |
| Description | When opening a WebObjects component that contains hardcoded references to sites that are both not HTTP 1.0 compliant and not responding, WebObjects Builder sometimes hangs or crashes. | When opening a WebObjects component that contains hardcoded references to sites that are both not HTTP 1.0 compliant and not responding, WebObjects Builder sometimes hangs or crashes. |
| Workaround | You can disable host lookup using a preferences panel. This will disable fetching all URLs (but not resources in your projects) and you will be able to open and manipulate your component. | You can disable host lookup using a preferences panel. This will disable fetching all URLs (but not resources in your projects) and you will be able to open and manipulate your component. |
|  |  |  |
|  |  |  |
| Reference | 2280939 | 2280939 |
| Problem | Unsynchronized files servers may cause WebObjects Builder to display a spurious revert panel | Unsynchronized files servers may cause WebObjects Builder to display a spurious revert panel |
| Description | If you create a web component on a file server whose clock is out of sync with your system, WebObjects Builder may think that the file has been modified when it hasn't. This will cause WebObjects Builder to display a revert panel when none is needed. | If you create a web component on a file server whose clock is out of sync with your system, WebObjects Builder may think that the file has been modified when it hasn't. This will cause WebObjects Builder to display a revert panel when none is needed. |
| Workaround | Running a network time protocol on your local machine will prevent this problem. Otherwise, saving the file will reset WebObjects Builder's internal modification times. | Running a network time protocol on your local machine will prevent this problem. Otherwise, saving the file will reset WebObjects Builder's internal modification times. |
|  |  |  |
|  |  |  |
| Reference | 2274651 | 2274651 |
| Problem | In WebObjects Builder, opening a file for which you do not have read permission presents a blank document; no warning is generated | In WebObjects Builder, opening a file for which you do not have read permission presents a blank document; no warning is generated |
| Description | Attempting to open a file for which you do not have read permission will result in a new blank document. This could result in the false perception that the component is actually blank, which may not be the case. | Attempting to open a file for which you do not have read permission will result in a new blank document. This could result in the false perception that the component is actually blank, which may not be the case. |
| Workaround | Make sure permissions are set correctly for projects you are working on and copy any read-only examples to your own directory. | Make sure permissions are set correctly for projects you are working on and copy any read-only examples to your own directory. |
|  |  |  |
|  |  |  |
| Reference | 2256367 | 2256367 |
| Problem | Configuration of WODisplayGroups in WebObjects Builder is not undoable. | Configuration of WODisplayGroups in WebObjects Builder is not undoable. |
| Description | WebObjects Builder won't undo any changes made to a WODisplayGroup via the configuration panel. | WebObjects Builder won't undo any changes made to a WODisplayGroup via the configuration panel. |
| Workaround | Changes can be reverted before dismissing the panel. Otherwise, you must restore the desired settings by hand. | Changes can be reverted before dismissing the panel. Otherwise, you must restore the desired settings by hand. |
|  |  |  |
|  |  |  |
| Reference | 2279837 | 2279837 |
| Problem | Deleting the name underneath one of the items in a custom palette causes the palette to become corrupted. | Deleting the name underneath one of the items in a custom palette causes the palette to become corrupted. |
| Description | Custom palette items must have either a name or an associated image. WebObjects Builder allows you to associate an image with a custom palette item by dragging an image file onto the item, automatically deleting the item's name. WebObjects Builder should not allow you to delete the name without associating an image with the item. | Custom palette items must have either a name or an associated image. WebObjects Builder allows you to associate an image with a custom palette item by dragging an image file onto the item, automatically deleting the item's name. WebObjects Builder should not allow you to delete the name without associating an image with the item. |
| Workaround | Once your palette has become corrupted, you will need to remake it from scratch. To create a palette item without a name, give it an image. | Once your palette has become corrupted, you will need to remake it from scratch. To create a palette item without a name, give it an image. |
|  |  |  |
|  |  |  |
| Reference | 2180253 | 2180253 |
| Problem | WebObjects Builder does not validate keys and values in the bindings inspector | WebObjects Builder does not validate keys and values in the bindings inspector |
| Description | WebObjects Builder lets you write illegal values (such as values with unrecognized characters) for binding attributes and values. These values are written to your .wod file without validation, so your .wod file will not be correct. | WebObjects Builder lets you write illegal values (such as values with unrecognized characters) for binding attributes and values. These values are written to your .wod file without validation, so your .wod file will not be correct. |
| Workaround | Don't set your bindings to such values. If you do, close the component and reopen it. WebObjects Builder displays a parse error and puts you in source editing mode, where you can fix the corrupted bindings. | Don't set your bindings to such values. If you do, close the component and reopen it. WebObjects Builder displays a parse error and puts you in source editing mode, where you can fix the corrupted bindings. |
|  |  |  |
|  |  |  |
| Reference | 2264154 | 2264154 |
| Problem | WebObjects Builder uses a common namespace for all of the classes | WebObjects Builder uses a common namespace for all of the classes |
| Description | WebObjects Builder uses a common namespace for all of the classes it encounters. It will simply use the last one it sees, and it will change whenever you edit the component or the eomodel. | WebObjects Builder uses a common namespace for all of the classes it encounters. It will simply use the last one it sees, and it will change whenever you edit the component or the eomodel. |
| Workaround | None. | None. |
|  |  |  |
|  |  |  |
| Reference | 2240571 | 2240571 |
| Problem | Moving, copying, or deleting a component no longer moves, copies, or deletes associated WebScript or .api files | Moving, copying, or deleting a component no longer moves, copies, or deletes associated WebScript or .api files |
| Description | In WebObjects 4.0 WebScript, .api, .java, and .h/.m files live outside the component. Because of this, moving or copying, or deleting a component no longer moves, copies, or deletes the WebScript, .api, .java, and .h/.m files. | In WebObjects 4.0 WebScript, .api, .java, and .h/.m files live outside the component. Because of this, moving or copying, or deleting a component no longer moves, copies, or deletes the WebScript, .api, .java, and .h/.m files. |
| Workaround | Copy or delete the associated files by hand. | Copy or delete the associated files by hand. |
|  |  |  |
|  |  |  |
| Reference | 2181346 | 2181346 |
| Problem | Centering several list items at once splits the list | Centering several list items at once splits the list |
| Description | If you center a single list item, the list item properly places a paragraph around its text and centers the paragraph, leaving the list itself intact. However, if you select several list items and center them, the list will be split at the selection boundaries, and the selected pieces will be centered. | If you center a single list item, the list item properly places a paragraph around its text and centers the paragraph, leaving the list itself intact. However, if you select several list items and center them, the list will be split at the selection boundaries, and the selected pieces will be centered. |
| Workaround | Center each list item independently. | Center each list item independently. |
|  |  |  |
|  |  |  |
| Reference | 2278982 | 2278982 |
| Problem | Opening components with very large tables causes WebObjects Builder to hang or crash. | Opening components with very large tables causes WebObjects Builder to hang or crash. |
| Description | A component containing a very large table (several thousand pixels by several thousand pixels, for example) will overtax WebObjects Builder, causing it to hang or crash. | A component containing a very large table (several thousand pixels by several thousand pixels, for example) will overtax WebObjects Builder, causing it to hang or crash. |
| Workaround | Basically none. Make the table smaller or edit the table with a machine that has more memory. | Basically none. Make the table smaller or edit the table with a machine that has more memory. |
|  |  |  |
|  |  |  |

---

### Monitor

|  |  |  |
| --- | --- | --- |
| Reference | 2426076 | 2426076 |
| Problem | On Mac OS X Server, deleting Monitor's death "history" has no effect. | On Mac OS X Server, deleting Monitor's death "history" has no effect. |
| Description | Suppose you have two deaths associated with a particular application instance.   If you choose "exception and death history" from the detail page and then select "delete death history," upon refresh the page shows the death history counter as having been reset. Subsequent refreshes, however, show it at two again. | Suppose you have two deaths associated with a particular application instance.   If you choose "exception and death history" from the detail page and then select "delete death history," upon refresh the page shows the death history counter as having been reset. Subsequent refreshes, however, show it at two again. |
| Workaround | None. | None. |
|  |  |  |
|  |  |  |
| Reference | 2426065 | 2426065 |
| Problem | Adding a host called foo.company.com to Monitor seems to work, but apps do not start. | Adding a host called foo.company.com to Monitor seems to work, but apps do not start. |
| Description | WebObjects uses the primary alias for a host, but Monitor does not determine this when you add a host by name. Hence one version of the name will work and another will not. That is, "foo" or "FOO" might work where "foo.company.com" doesn't. This is primarily a problem on Windows, where uppercase hostnames are common. | WebObjects uses the primary alias for a host, but Monitor does not determine this when you add a host by name. Hence one version of the name will work and another will not. That is, "foo" or "FOO" might work where "foo.company.com" doesn't. This is primarily a problem on Windows, where uppercase hostnames are common. |
| Workaround | Consistently use the primary alias: whichever hostname works for app launching. Change your hostname to lowercase in the TCP/IP or Network Properties control panel. | Consistently use the primary alias: whichever hostname works for app launching. Change your hostname to lowercase in the TCP/IP or Network Properties control panel. |
|  |  |  |
|  |  |  |
| Reference | 2425103 | 2425103 |
| Problem | WebObjects Monitor doesn't indicate which port it is running on. | WebObjects Monitor doesn't indicate which port it is running on. |
| Description | In response to customer requests, Monitor no longer emits any logging information under normal conditions. As such, Monitor no longer outputs the port it is running on.  Without knowing the port number, you can't directly connect to Monitor. | In response to customer requests, Monitor no longer emits any logging information under normal conditions. As such, Monitor no longer outputs the port it is running on.  Without knowing the port number, you can't directly connect to Monitor. |
| Workaround | Either connect via the WebServer and adaptor or tell Monitor which port it should use. To do this, set the WOPort user default:    defaults write Monitor WOPort <your favorite port>    or start it with the appropriate argument: -WOPort <your favorite port> | Either connect via the WebServer and adaptor or tell Monitor which port it should use. To do this, set the WOPort user default:    defaults write Monitor WOPort <your favorite port>    or start it with the appropriate argument: -WOPort <your favorite port> |
|  |  |  |
|  |  |  |
| Reference | 2424839 | 2424839 |
| Problem | Two WebObjects applications can listen on the same port on a machine running Windows NT | Two WebObjects applications can listen on the same port on a machine running Windows NT |
| Description | Due to an apparent bug in the way Windows implements TCP/IP, it's possible to start two WebObjects applications that listen on the same port on the same Windows NT machine. This gives inconsistent results and should be avoided. | Due to an apparent bug in the way Windows implements TCP/IP, it's possible to start two WebObjects applications that listen on the same port on the same Windows NT machine. This gives inconsistent results and should be avoided. |
| Workaround | Take care to use different ports for each application instance. | Take care to use different ports for each application instance. |
|  |  |  |
|  |  |  |
| Reference | 2424543 | 2424543 |
| Problem | I get a licensing error about running more than one instance, but I'm only running one. | I get a licensing error about running more than one instance, but I'm only running one. |
| Description | You can get this error running a single instance if it registers with wotaskd and is deemed a deployable instance (that is, it registers on a port that is known by wotaskd as configured for a deployed instance). This can happen if you have configured an instance using Monitor for that host on that port. The application will work when you connect to it through Direct Connect; this error only occurs if you're trying to connect through the WebServer.    There is currently no restriction on being able to configure application instances on a given host. | You can get this error running a single instance if it registers with wotaskd and is deemed a deployable instance (that is, it registers on a port that is known by wotaskd as configured for a deployed instance). This can happen if you have configured an instance using Monitor for that host on that port. The application will work when you connect to it through Direct Connect; this error only occurs if you're trying to connect through the WebServer.    There is currently no restriction on being able to configure application instances on a given host. |
| Workaround | Use Direct Connect when developing. Start test apps on a port other than the one specified for the configured instance. Remove the configured instance. | Use Direct Connect when developing. Start test apps on a port other than the one specified for the configured instance. Remove the configured instance. |
|  |  |  |
|  |  |  |
| Reference | 2259003 | 2259003 |
| Problem | Monitor doesn't save settings unless it is run as Administrator on Mac OS X Server | Monitor doesn't save settings unless it is run as Administrator on Mac OS X Server |
| Description | Monitor saves two files into /System/Library/WebObjects/Configuration. This directory is accessible only to the Administrator because one of the files contains sensitive deployment information. The other file contains the settings. | Monitor saves two files into /System/Library/WebObjects/Configuration. This directory is accessible only to the Administrator because one of the files contains sensitive deployment information. The other file contains the settings. |
| Workaround | Always run Monitor as the Administrator. Or, if security is not an issue, change the permissions of this directory. | Always run Monitor as the Administrator. Or, if security is not an issue, change the permissions of this directory. |
|  |  |  |
|  |  |  |

---

### WebScript

|  |  |  |
| --- | --- | --- |
| Reference | 2280236 | 2280236 |
| Problem | Exception handling in WebScript doesn't support VALUERETURN() the way that Objective-C does | Exception handling in WebScript doesn't support VALUERETURN() the way that Objective-C does |
| Description | In Objective-C, the VALUERETURN() macro accepts two arguments: the return value and the type. The WebScript version of VALUERETURN() only accepts one argument: the return value. | In Objective-C, the VALUERETURN() macro accepts two arguments: the return value and the type. The WebScript version of VALUERETURN() only accepts one argument: the return value. |
| Workaround | In WebScript, don't supply a type to VALUERETURN(). | In WebScript, don't supply a type to VALUERETURN(). |
|  |  |  |
|  |  |  |
| Reference | 2179411 | 2179411 |
| Problem | WebScript categories don't work unless component-definition caching is turned on. | WebScript categories don't work unless component-definition caching is turned on. |
| Description | If you define a category in a component's .wos file, you will receive an error at runtime like the following:    Errors parsing script file '/NextLibrary/WebServer/htdocs/WebObjects/MyWebStuff/MyApp.woa/MyComponent.wo/MyComponent.wos' into class 'WOScriptedClass(/WebObjects/MyWebStuff/MyApp.woa/MyComponent.wo/MyComponent)' with superclass 'WOComponent':  Exception while executing statement :   - methodInCategory {  ...    where methodInCategory is a method defined in the category. The problem arises because the script file is read more than once when component-definition caching is turned off. The first time the script is read, the category method is added to the runtime. The second time the script is read, the runtime considers the method a duplicate and produces an error. | If you define a category in a component's .wos file, you will receive an error at runtime like the following:    Errors parsing script file '/NextLibrary/WebServer/htdocs/WebObjects/MyWebStuff/MyApp.woa/MyComponent.wo/MyComponent.wos' into class 'WOScriptedClass(/WebObjects/MyWebStuff/MyApp.woa/MyComponent.wo/MyComponent)' with superclass 'WOComponent':  Exception while executing statement :   - methodInCategory {  ...    where methodInCategory is a method defined in the category. The problem arises because the script file is read more than once when component-definition caching is turned off. The first time the script is read, the category method is added to the runtime. The second time the script is read, the runtime considers the method a duplicate and produces an error. |
| Workaround | Turn on component-definition caching with the -WOCachingEnabled command line option. | Turn on component-definition caching with the -WOCachingEnabled command line option. |
|  |  |  |
|  |  |  |

---

### Client-Side Components

|  |  |  |
| --- | --- | --- |
| Reference | 2178197 | 2178197 |
| Problem | Client-Side Component snapshotting doesn't work when caching is turned off | Client-Side Component snapshotting doesn't work when caching is turned off |
| Description | A WOApplet won't snapshot the component values when component definition caching is disabled (that is, the -WOCachingEnabled YES option was not specified on the command line, or the message [WOApp setCachingEnabled:NO] was sent). This means that a request initiated by a client-side component will result in a response that will contain all the key-value pairs even though some of these pairs may not have changed during the request. This may have some side effects. You should make sure that your client-side component behaves the same way when caching is turned on (since snapshotting will work when caching is turned on). | A WOApplet won't snapshot the component values when component definition caching is disabled (that is, the -WOCachingEnabled YES option was not specified on the command line, or the message [WOApp setCachingEnabled:NO] was sent). This means that a request initiated by a client-side component will result in a response that will contain all the key-value pairs even though some of these pairs may not have changed during the request. This may have some side effects. You should make sure that your client-side component behaves the same way when caching is turned on (since snapshotting will work when caching is turned on). |
| Workaround | Turn component-definition caching on in order to enable snapshotting. | Turn component-definition caching on in order to enable snapshotting. |
|  |  |  |
|  |  |  |
| Reference | 2425261 | 2425261 |
| Problem | I am using Netscape 4.5 on Windows and Client-Side Components in Direct Connect mode and I am getting stuck on a page that contains a Java Applet | I am using Netscape 4.5 on Windows and Client-Side Components in Direct Connect mode and I am getting stuck on a page that contains a Java Applet |
| Description | When using Netscape 4.5 on Windows and Client-Side Components (for instance, TimeOffJavaCSC) in Direct Connect mode, if you access a page that contains Java client-side components you may find that clicking on submit has no effect. The Java console says that an IO exception was thrown. | When using Netscape 4.5 on Windows and Client-Side Components (for instance, TimeOffJavaCSC) in Direct Connect mode, if you access a page that contains Java client-side components you may find that clicking on submit has no effect. The Java console says that an IO exception was thrown. |
| Workaround | Microsoft Internet Explorer 5 on Windows will work properly, as should split-installing and accessing your application through a web server. | Microsoft Internet Explorer 5 on Windows will work properly, as should split-installing and accessing your application through a web server. |
|  |  |  |
|  |  |  |
| Reference | 2282366 | 2282366 |
| Problem | Client-side component won't run multithreaded. | Client-side component won't run multithreaded. |
| Description | Running Client-side components with concurrent request handling enabled, raises an exception. | Running Client-side components with concurrent request handling enabled, raises an exception. |
| Workaround | None. Client-side components are not thread-safe in WebObjects 4.0. You will have to run with concurrent request handling disabled. However, you can safely run with WOWorkerThreadCount > 1. | None. Client-side components are not thread-safe in WebObjects 4.0. You will have to run with concurrent request handling disabled. However, you can safely run with WOWorkerThreadCount > 1. |
|  |  |  |
|  |  |  |
| Reference | 2274609 | 2274609 |
| Problem | Netscape 4 crashes in the Element Tour example | Netscape 4 crashes in the Element Tour example |
| Description | Netscape 4 crashes when running the client-side component section of the element tour. | Netscape 4 crashes when running the client-side component section of the element tour. |
| Workaround | Use Netscape 4.5, or Microsoft's Internet Explorer 4.0. | Use Netscape 4.5, or Microsoft's Internet Explorer 4.0. |
|  |  |  |
|  |  |  |

---

### Playback

|  |  |  |
| --- | --- | --- |
| Reference | 2251966 | 2251966 |
| Problem | Playback Manager can't connect to remote hosts | Playback Manager can't connect to remote hosts |
| Description | Connection failures are typically due to security checks from the applet viewer tool. This tool has very restrictive rules when it accesses the network. WebObjects has no control over this tool, as it is distributed with each Java VM. | Connection failures are typically due to security checks from the applet viewer tool. This tool has very restrictive rules when it accesses the network. WebObjects has no control over this tool, as it is distributed with each Java VM. |
| Workaround | Follow the instructions in the ReadMe.html file located in the PlaybackManager.woa/Resources directory. The steps in the "Security Issues" paragraph are particularly important. | Follow the instructions in the ReadMe.html file located in the PlaybackManager.woa/Resources directory. The steps in the "Security Issues" paragraph are particularly important. |
|  |  |  |
|  |  |  |
| Reference | 2246048 | 2246048 |
| Problem | The Playback Manager's client applet doesn't work in Netscape's browsers | The Playback Manager's client applet doesn't work in Netscape's browsers |
| Description | Netscape's Java VM is much less reliable than Microsoft's. Only simple applets will run effectively in Netscape's browser. | Netscape's Java VM is much less reliable than Microsoft's. Only simple applets will run effectively in Netscape's browser. |
| Workaround | Don't use Netscape with playback manager if you intend to use the "start a simple playback" feature. Use Microsoft's Internet Explorer instead. | Don't use Netscape with playback manager if you intend to use the "start a simple playback" feature. Use Microsoft's Internet Explorer instead. |
|  |  |  |
|  |  |  |
| Reference | 2263639 | 2263639 |
| Problem | The PlaybackManager can't replay Java Client applets. | The PlaybackManager can't replay Java Client applets. |
| Description | Java Client applets use custom HTTP requests to talk to the WebObjects Application server. The PlaybackManager doesn't know how to register and replay these messages. | Java Client applets use custom HTTP requests to talk to the WebObjects Application server. The PlaybackManager doesn't know how to register and replay these messages. |
| Workaround | None. | None. |
|  |  |  |
|  |  |  |

---

### Examples

|  |  |  |
| --- | --- | --- |
| Reference | 2444812 | 2444812 |
| Problem | RelatedLinks example doesn't work "out of the box." | RelatedLinks example doesn't work "out of the box." |
| Description | As shipped with WebObjects 4.5, clicking on any of the buttons on the Main page of the RelatedLinks example results in either a blank page or an exception page. This is due to a recent change in Netscape's related links website (the RelatedLinks example sends a request to this site). | As shipped with WebObjects 4.5, clicking on any of the buttons on the Main page of the RelatedLinks example results in either a blank page or an exception page. This is due to a recent change in Netscape's related links website (the RelatedLinks example sends a request to this site). |
| Workaround | Replace the following line of code in the relatedLinksContent(String, boolean) method in ContentHelper.java:      connection.sendRequest(new WORequest("GET", rlQuery + webSite, httpVersion, null, null, null));   with:      connection.sendRequest(new WORequest("GET", rlQuery + webSite, httpVersion, new NSDictionary("en", "Accept-Language"), null, null)); | Replace the following line of code in the relatedLinksContent(String, boolean) method in ContentHelper.java:      connection.sendRequest(new WORequest("GET", rlQuery + webSite, httpVersion, null, null, null));   with:      connection.sendRequest(new WORequest("GET", rlQuery + webSite, httpVersion, new NSDictionary("en", "Accept-Language"), null, null)); |
|  |  |  |
|  |  |  |
| Reference | 2419399 | 2419399 |
| Problem | Mixing WebScript with Java in a WebObjects application is not recommended | Mixing WebScript with Java in a WebObjects application is not recommended |
| Description | Due to some complex interactions between WebScript and the JavaBridge, we recommend avoiding mixing WebScript and Java in the same application. The problem interactions have been observed, under certain conditions, around the locking and unlocking of editing contexts which can modify the current autorelease pool. | Due to some complex interactions between WebScript and the JavaBridge, we recommend avoiding mixing WebScript and Java in the same application. The problem interactions have been observed, under certain conditions, around the locking and unlocking of editing contexts which can modify the current autorelease pool. |
| Workaround | Convert any WebScript to Java (or Objective-C). | Convert any WebScript to Java (or Objective-C). |
|  |  |  |
|  |  |  |
| Reference | 2418123 | 2418123 |
| Problem | Netscape Navigator on Windows NT can crash when running the ElementTour example. | Netscape Navigator on Windows NT can crash when running the ElementTour example. |
| Description | Netscape Navigator 4.0 on Windows NT has been observed to crash when you click on the Client-Side Components link in the ElementTour example. Other browsers--OmniWeb, Intenet Explorer, and even Netscape Communicator--don't seem to have this problem. | Netscape Navigator 4.0 on Windows NT has been observed to crash when you click on the Client-Side Components link in the ElementTour example. Other browsers--OmniWeb, Intenet Explorer, and even Netscape Communicator--don't seem to have this problem. |
| Workaround | Access the example through a different browser. | Access the example through a different browser. |
|  |  |  |
|  |  |  |
| Reference | 2284519 | 2284519 |
| Problem | The Inheritance example doesn't let you add a new Movie. | The Inheritance example doesn't let you add a new Movie. |
| Description | The Inheritance example in System/Developer/Examples/WebObjects/TaskBasedExamples/Inheritance has the Movie entity marked as read-only, so you cannot add a new Movie using the example. If you attempt to add a new movie an exception will be raised. | The Inheritance example in System/Developer/Examples/WebObjects/TaskBasedExamples/Inheritance has the Movie entity marked as read-only, so you cannot add a new Movie using the example. If you attempt to add a new movie an exception will be raised. |
| Workaround | Don't attempt to add a new Movie using this example. If you want to reconfigure the example, use the Direct-to-Web Assistant to customize the application. | Don't attempt to add a new Movie using this example. If you want to reconfigure the example, use the Direct-to-Web Assistant to customize the application. |
|  |  |  |
|  |  |  |
| Reference | 2280169 | 2280169 |
| Problem | FDF1040EZ on Solaris: UnsatisfiedLinkError exception on clicking a link | FDF1040EZ on Solaris: UnsatisfiedLinkError exception on clicking a link |
| Description | Exception occured on hitting 'here' link after launching the app on   Solaris.  Errors:  java/lang/UnsatisfiedLinkError exception occurred while handling request:  java/lang/UnsatisfiedLinkError: no net in shared library path  Stack Trace:  java.lang.UnsatisfiedLinkError: no net in shared library path  at java.lang.Runtime.loadLibrary(Runtime.java)  at java.lang.System.loadLibrary(System.java)  at   at pdf.PDFStaticComponent.appendFdfToResponse(PDFStaticComponent.java:92)  at pdf.PDFStaticComponent.appendToResponse(PDFStaticComponent.java:55) | Exception occured on hitting 'here' link after launching the app on   Solaris.  Errors:  java/lang/UnsatisfiedLinkError exception occurred while handling request:  java/lang/UnsatisfiedLinkError: no net in shared library path  Stack Trace:  java.lang.UnsatisfiedLinkError: no net in shared library path  at java.lang.Runtime.loadLibrary(Runtime.java)  at java.lang.System.loadLibrary(System.java)  at   at pdf.PDFStaticComponent.appendFdfToResponse(PDFStaticComponent.java:92)  at pdf.PDFStaticComponent.appendToResponse(PDFStaticComponent.java:55) |
| Workaround | You need to set the LD_LIBRARY_PATH to include:  ${NEXT_ROOT}/Library/Executables:${NEXT_ROOT}/Library/JDK/lib/sparc/  native_threads | You need to set the LD_LIBRARY_PATH to include:  ${NEXT_ROOT}/Library/Executables:${NEXT_ROOT}/Library/JDK/lib/sparc/  native_threads |
|  |  |  |
|  |  |  |
| Reference | 2271407 | 2271407 |
| Problem | Netscape does not send "en" language choice if any other languages are chosen. | Netscape does not send "en" language choice if any other languages are chosen. |
| Description | The default language choice for Netscape is "en". If the user chooses any other language in addition to this, the "en" choice will not be included in the list of languages transmitted. Hence, some language other than english may be chosen. | The default language choice for Netscape is "en". If the user chooses any other language in addition to this, the "en" choice will not be included in the list of languages transmitted. Hence, some language other than english may be chosen. |
| Workaround | None | None |
|  |  |  |
|  |  |  |
| Reference | 2178914 | 2178914 |
| Problem | FDF Example: Exceptions are raised when loading some PDF pages | FDF Example: Exceptions are raised when loading some PDF pages |
| Description | When WebObjects loads certain PDF pages, a "PDF exception, expecting x fields, found y" exception is raised. This exception occurs because the PDF parser included in WebObjects expects only optimized PDF files. | When WebObjects loads certain PDF pages, a "PDF exception, expecting x fields, found y" exception is raised. This exception occurs because the PDF parser included in WebObjects expects only optimized PDF files. |
| Workaround | Ensure that all PDF files present in .wo directories are optimized. You can do this for a given PDF file by opening it in Acrobat Exchange and using the Save As command. | Ensure that all PDF files present in .wo directories are optimized. You can do this for a given PDF file by opening it in Acrobat Exchange and using the Save As command. |
|  |  |  |
|  |  |  |

---

### Documentation

|  |  |  |
| --- | --- | --- |
| Reference | 2302944 | 2302944 |
| Problem | NSProjectSearchPath is incorrectly documented in WebObjects Developer's Guide | NSProjectSearchPath is incorrectly documented in WebObjects Developer's Guide |
| Description | The Debugging chapter of the WebObjects Developer's Guide incorrectly states that you set your NSProjectSearchPath as follows:    % defaults write NSGlobalDomain NSProjectSearchPath @("someDirectory","someOtherDirectory", ...)    The "@" character is incorrect. The portion in parenthesis should instead be enclosed in single quotes, like this:    % defaults write NSGlobalDomain NSProjectSearchPath '("someDirectory","someOtherDirectory", ...)' | The Debugging chapter of the WebObjects Developer's Guide incorrectly states that you set your NSProjectSearchPath as follows:    % defaults write NSGlobalDomain NSProjectSearchPath @("someDirectory","someOtherDirectory", ...)    The "@" character is incorrect. The portion in parenthesis should instead be enclosed in single quotes, like this:    % defaults write NSGlobalDomain NSProjectSearchPath '("someDirectory","someOtherDirectory", ...)' |
| Workaround | Use the correct format, as described in the problem description above. | Use the correct format, as described in the problem description above. |
|  |  |  |
|  |  |  |
| Reference | 2415737 | 2415737 |
| Problem | Deploying WebObjects book images show a File Transfer button that doesn't appear in the final version of Monitor. | Deploying WebObjects book images show a File Transfer button that doesn't appear in the final version of Monitor. |
| Description | Due to security considerations, a planned "File Transfer" feature in the WebObjects Monitor application was pulled from the app after the Deploying WebObjects book was submitted to the release. All of the images in this book show a "File Transfer" button that doesn't appear in the final product. | Due to security considerations, a planned "File Transfer" feature in the WebObjects Monitor application was pulled from the app after the Deploying WebObjects book was submitted to the release. All of the images in this book show a "File Transfer" button that doesn't appear in the final product. |
| Workaround | None. | None. |
|  |  |  |
|  |  |  |
| Reference | 2410008 | 2410008 |
| Problem | The PDF documentation differs from the HTML documentation. | The PDF documentation differs from the HTML documentation. |
| Description | Some documentation was updated after the PDF files were produced. Only the HTML documentation reflects these changes. The following PDF-HTML discrepancies appear in the documentation:    Java Client Tutorial: The OpenBaseLite login panel on page 33 and the test interface screen shot on page 54 have been updated.    XML Framework Reference: The docodeRootObject method description in the WOXMLDecoder class now reads:    public synchronized Object decodeRootObject(String XMLFileURL)  ...If the XML resides within a file, XMLFileURL should be a URL that identifies the file containing the XML...    WebObjects Framework Reference: WOMessage now has two additional "appendHeader..." methods that do what is described under "setHeader...". The "setHeader..." methods now set, rather than append, headers in the receiver. The Java version of WOContext now has a constructor that takes a WORequest object as an argument. WOHTTPConnection has methods to set and get the connect, receive, and send timeout values.    Developing WebObjects Applications With Direct to Web: The directions for entering the rules on pages 51-52 have been corrected. | Some documentation was updated after the PDF files were produced. Only the HTML documentation reflects these changes. The following PDF-HTML discrepancies appear in the documentation:    Java Client Tutorial: The OpenBaseLite login panel on page 33 and the test interface screen shot on page 54 have been updated.    XML Framework Reference: The docodeRootObject method description in the WOXMLDecoder class now reads:    public synchronized Object decodeRootObject(String XMLFileURL)  ...If the XML resides within a file, XMLFileURL should be a URL that identifies the file containing the XML...    WebObjects Framework Reference: WOMessage now has two additional "appendHeader..." methods that do what is described under "setHeader...". The "setHeader..." methods now set, rather than append, headers in the receiver. The Java version of WOContext now has a constructor that takes a WORequest object as an argument. WOHTTPConnection has methods to set and get the connect, receive, and send timeout values.    Developing WebObjects Applications With Direct to Web: The directions for entering the rules on pages 51-52 have been corrected. |
| Workaround | Use the HTML version of the documentation--in certain areas it is more current. | Use the HTML version of the documentation--in certain areas it is more current. |
|  |  |  |
|  |  |  |
| Reference | 2394552 | 2394552 |
| Problem | wotaskd writes out a usable WOConfig.xml file. | wotaskd writes out a usable WOConfig.xml file. |
| Description | wotaskd now writes a WOConfig.xml file to /Local/Library/WebObjects/Configuration. This is an XML file in the same format as the XML returned by hitting wotaskd at port 1085, and it can be used to enable the file-based load balancing scheme. See "Accessing Configuration Information" in "What's New in WebObjects 4.5" for information on how to disable multicast mode and instead have your web server adaptors obtain their configuration information from this XML file. | wotaskd now writes a WOConfig.xml file to /Local/Library/WebObjects/Configuration. This is an XML file in the same format as the XML returned by hitting wotaskd at port 1085, and it can be used to enable the file-based load balancing scheme. See "Accessing Configuration Information" in "What's New in WebObjects 4.5" for information on how to disable multicast mode and instead have your web server adaptors obtain their configuration information from this XML file. |
| Workaround | None needed. | None needed. |
|  |  |  |
|  |  |  |
| Reference | 2359284 | 2359284 |
| Problem | "Disabling or Protecting Administrator Access" in "What's New in WebObjects 4.5" isn't quite correct for CGI. | "Disabling or Protecting Administrator Access" in "What's New in WebObjects 4.5" isn't quite correct for CGI. |
| Description | In the CGI section beneath "Disabling or Protecting Administrator Access" in the "What's New in WebObjects 4.5" document, you're told to uncomment some code in "main.c". In fact, the code is in WebObjects.c and can be found in the main() function. | In the CGI section beneath "Disabling or Protecting Administrator Access" in the "What's New in WebObjects 4.5" document, you're told to uncomment some code in "main.c". In fact, the code is in WebObjects.c and can be found in the main() function. |
| Workaround | Use environment variables as described later in the CGI section or uncomment the code in WebObjects.c. | Use environment variables as described later in the CGI section or uncomment the code in WebObjects.c. |
|  |  |  |
|  |  |  |
