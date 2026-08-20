---
title: File System Programming Guide
apple_id: TP40010672
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/MacOSXDirectories/MacOSXDirectories.html
archived_at: '2026-07-15T07:32:00.373308Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [File System Programming Guide](About%20Files%20and%20Directories.md)


[Next](File%20System%20Details.md)[Previous](Performance%20Tips.md)

# macOS Library Directory Details

The `Library` directories are where the system and your code store all of their related data and resources. In macOS, this directory can contain many different subdirectories, most of which are created automatically by the system. In iOS, the app installer creates only a few subdirectories in `~/Library` (such as `Caches` and `Preferences`) and your app is responsible for creating all others.

Table A-1 lists some of the common subdirectories you might find in a `Library` directory in macOS along with the types of files that belong there. You should always use these directories for their intended purposes. For information about the directories your app should be using the most, see [The Library Directory Stores App-Specific Files](File%20System%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmnzsfvbuqmrnknltc).

__Table A-1__  Subdirectories of the Library directory

| Subdirectory | Directory contents |
| `Application Support` | Contains all app-specific data and support files. These are the files that your app creates and manages on behalf of the user and can include files that contain user data.  By convention, all of these items should be put in a subdirectory whose name matches the bundle identifier of the app. For example, if your app is named MyApp and has the bundle identifier `com.example.MyApp`, you would put your app’s user-specific data files and resources in the `~/Library/Application Support/com.example.MyApp/` directory. Your app is responsible for creating this directory as needed.  Resources required by the app to run must be placed inside the app bundle itself. |
| `Assistants` | Contains programs that assist users in configuration or other tasks. |
| `Audio` | Contains audio plug-ins, loops, and device drivers. |
| `Autosave Information` | Contains app-specific autosave data. |
| `Caches` | Contains cached data that can be regenerated as needed. Apps should never rely on the existence of cache files. Cache files should be placed in a directory whose name matches the bundle identifier of the app.  By convention, apps should store cache files in a subdirectory whose name matches the bundle identifier of the app. For example, if your app is named MyApp and has the bundle identifier `com.example.MyApp`, you would put user-specific cache files in the `~/Library/Caches/com.example.MyApp/` directory. |
| `ColorPickers` | Contains resources for picking colors according to a certain model, such as the HLS (Hue Angle, Saturation, Lightness) picker or RGB picker. |
| `ColorSync` | Contains ColorSync profiles and scripts. |
| `Components` | Contains system bundles and extensions. |
| `Containers` | Contains the home directories for any sandboxed apps. (Available in the user domain only.) |
| `Contextual Menu Items` | Contains plug-ins for extending system-level contextual menus. |
| `Cookies` | Contains data files with web browser cookies. |
| `Developer` | Contains data used by Xcode and other developer tools. |
| `Dictionaries` | Contains language dictionaries for the spell checker. |
| `Documentation` | Contains documentation files and Apple Help packages intended for the users and administrators of the computer. (Apple Help packages are located in the `Documentation/Help` directory.) In the local domain, this directory contains the help packages shipped by Apple (excluding developer documentation). |
| `Extensions` | Contains device drivers and other kernel extensions. |
| `Favorites` | Contains aliases to frequently accessed folders, files, or websites. (Available in the user domain only.) |
| `Fonts` | Contains font files for both display and printing. |
| `Frameworks` | Contains [frameworks](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56) and shared libraries. The `Frameworks` directory in the system domain is for Apple-provided frameworks only. Developers should install their custom frameworks in either the local or user domain. |
| `Internet Plug-ins` | Contains plug-ins, libraries, and filters for web-browser content. |
| `Keyboards` | Contains keyboard definitions. |
| `LaunchAgents` | Specifies the agent apps to launch and run for the current user. |
| `LaunchDaemons` | Specifies the daemons to launch and run as root on the system. |
| `Logs` | Contains log files for the console and specific system services. Users can also view these logs using the Console app. |
| `Mail` | Contains the user’s mailboxes. (Available in the user domain only.) |
| `PreferencePanes` | Contains plug-ins for the System Preferences app. Developers should install their custom preference panes in the local domain. |
| `Preferences` | Contains the user’s preferences. You should never create files in this directory yourself. To get or set preference values, you should always use the [NSUserDefaults](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/cl/NSUserDefaults) class or an equivalent system-provided interface. |
| `Printers` | In the system and local domains, this directory contains print drivers, PPD plug-ins, and libraries needed to configure printers. In the user domain, this directory contains the user’s available printer configurations. |
| `QuickLook` | Contains QuickLook plug-ins. If your app defines a QuickLook plug-in for viewing custom document types, install it in this directory (user or local domains only). |
| `QuickTime` | Contains QuickTime components and extensions. |
| `Screen Savers` | Contains screen saver definitions. See _[Screen Saver Framework Reference](https://developer.apple.com/documentation/screensaver)_ for a description of the interfaces used to create screen saver plug-ins. |
| `Scripting Additions` | Contains scripts and scripting resources that extend the capabilities of AppleScript. |
| `Sounds` | Contains system alert sounds. |
| `StartupItems` | (Deprecated) Contains system and third-party scripts and programs to be run at boot time. (See _[Daemons and Services Programming Guide](../../Mac%20OSX/Daemons%20and%20Services%20Programming%20Guide/About%20Daemons%20and%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3te2i)_ for more information about starting up processes at boot time.) |
| `Web Server` | Contains web server content. This directory contains the CGI scripts and webpages to be served. (Available in the local domain only.) |

[Next](File%20System%20Details.md)[Previous](Performance%20Tips.md)

