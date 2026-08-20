---
title: File System Overview
apple_id: 10000185i
resource_type: Guide
platform: macOS
topic: Data Management
technology: null
published: '2011-05-25'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPFileSystem/Articles/LibraryDirectory.html
archived_at: '2026-07-15T08:15:28.085800Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [File System Overview](Introduction%20to%20the%20File%20System%20Overview.md)


[Next](The%20Developer%20Directory.md)[Previous](File-System%20Domains.md)

# The Library Directory

The `Library` directory is a special directory used to store application-specific and system-specific resources. Each file-system domain has its own copy of the `Library` directory, with access levels to match the domain type. (See [File-System Domains](File-System%20Domains.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi4dclkdjjbeqskiizda) for a discussion of domains.) Although an application can use this directory to store internal data or temporary files, it is not intended for storage of the application [bundle](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Bundle.html#//apple_ref/doc/uid/TP40008195-CH4) itself or for user data files. Application bundles belong in an appropriate `/Applications` directory, while user data belongs in the user’s home directory.

The `Library` directory contains many standard subdirectories. System routines expect many of the standard subdirectories to exist, so it is never a good idea to delete subdirectories of `Library`. However, applications can create new subdirectories as needed to store application-specific data.

[Table 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi4deljrgaytambrfvbegskhijceurq) lists some of the directories that can appear in a `Library` directory. You should use this table to determine where to put files needed to support your software. This list is not complete, but it lists some of the most relevant directories for developers. Directories that do not appear in all domains are noted appropriately.

__Table 1__  Subdirectories of the Library directory

| Subdirectory | Directory contents |
| `Application Support` | Contains application-specific data and support files such as third-party plug-ins, helper applications, templates, and extra resources that are used by the application but not required for it to operate. This directory should never contain any kind of user data. By convention, all of these items should be put in a subdirectory named after the application. For example, third-party resources for the application MyApp would go in `Application Support/MyApp/`. Note that required resources should go inside the application bundle itself. |
| `Assistants` | Contains programs that assist users in configuration or other tasks. |
| `Audio` | Contains audio plug-ins and device drivers. |
| `Caches` | Contains cached data that can be regenerated as needed. Applications should never rely on the existence of cache files. Cache files should be placed in a directory whose name matches the bundle identifier of the application. Cache data should further be subdivided into user or session-specific subdirectories as needed. (See _[Multiple User Environment Programming Topics](../Multiple%20User%20Environment%20Programming%20Topics/Introduction%20to%20Multiple%20User%20Environments.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4da2i)_ in Mac OS X Documentation for user-specific guidelines.) |
| `ColorPickers` | Contains resources for picking colors according to a certain model, such as the HLS (Hue Angle, Saturation, Lightness) picker or RGB picker. |
| `ColorSync` | Contains ColorSync profiles and scripts. |
| `Components` | Contains system bundles and extensions. |
| `Contextual Menu Items` | Contains plug-ins for extending system-level contextual menus. |
| `Documentation` | Contains documentation files and Apple Help packages intended for the users and administrators of the computer. (Apple Help packages are located in the `Help` subdirectory.) In the local domain, this directory contains the help packages shipped by Apple (excluding developer documentation). |
| `Extensions` | Contains device drivers and other kernel extensions. (Available in the system domain only.) |
| `Favorites` | Contains aliases to frequently accessed folders, files, or websites. (Available in the user domain only.) |
| `Fonts` | Contains font files for both display and printing. |
| `Frameworks` | Contains [frameworks](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56) and shared libraries. The `Frameworks` directory in the system domain is for Apple-provided frameworks only. Developers should install their custom frameworks in either the local or user domain. |
| `Internet Plug-ins` | Contains plug-ins, libraries, and filters for web-browser content. |
| `Keyboards` | Contains keyboard definitions. |
| `Logs` | Contains log files for the console and specific system services. Users can also view these logs using the Console application. |
| `Mail` | Contains the user’s mailboxes. (Available in the user domain only.) |
| `PreferencePanes` | Contains plug-ins for the System Preferences application. Developers should install their custom preference panes in the local domain. |
| `Preferences` | Contains the user preferences. See _[Runtime Configuration Guidelines](../Runtime%20Configuration%20Guidelines/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3ta2i)_ for information about user preferences. |
| `Printers` | In the system and local domains, this directory contains print drivers, PPD plug-ins, and libraries needed to configure printers. In the user domain, this directory contains the user’s available printer configurations. |
| `QuickTime` | Contains QuickTime components and extensions. |
| `Screen Savers` | Contains screen saver definitions. See _[Screen Saver Framework Reference](https://developer.apple.com/documentation/screensaver)_ for a description of the interfaces used to create screen saver plug-ins. |
| `Scripting Additions` | Contains scripts and scripting resources that extend the capabilities of AppleScript. |
| `Sounds` | Contains system alert sounds. |
| `StartupItems` | Contains system and third-party scripts and programs to be run at boot time. (See _[Daemons and Services Programming Guide](../Daemons%20and%20Services%20Programming%20Guide/About%20Daemons%20and%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3te2i)_ for more information about starting up processes at boot time.) |
| `Web Server` | Contains web server content. This directory contains the CGI scripts and webpages to be served. (Available in the local domain only.) |

[Next](The%20Developer%20Directory.md)[Previous](File-System%20Domains.md)

