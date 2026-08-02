---
title: AppleScript Overview
apple_id: 10000156i
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptX/Concepts/as_related_apps.html
archived_at: '2026-07-15T05:19:33.510129Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [AppleScript Overview](Introduction%20to%20AppleScript%20Overview.md)


[Next](Document%20Revision%20History.md)[Previous](Automator.md)

# AppleScript Utilities and Applications

Apple provides a number of utilities and applications in OS X to enhance the features of AppleScript and your scripts. You can get additional information on some items described in this section by searching in Mac Help in the Finder or by going to the [AppleScript](http://www.macosxautomation.com/applescript/index.html) website.

AppleScript Utility, located in `/Applications/AppleScript`, is an application that first became available in OS X version 10.4. Starting in OS X version 10.5, this utility is itself scriptable.

AppleScript Utility helps you manage several AppleScript-related features in OS X that were formerly available separately. For example, AppleScript Utility provides an interface to:

- Select a default script editor (to be launched when you double-click a script file.
- Enable or disable GUI scripting (described in [System Events and GUI Scripting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytknzqfuytcnbzga3ti)).

  Prior to OS X v10.4, GUI scripting was enabled through the “Enable access for assistive devices” checkbox in the Universal Access preference pane in System Preferences.
- Launch the Folder Actions Setup application (described in [Folder Actions Setup](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytknzqfuytcnbygeztg)).
- Specify settings for the Script menu.

  The Script menu provides access to scripts for performing tasks such as the following:

  - Opening AppleScript related folders.
  - Working with Apple applications such as Address Book, Mail, and Script Editor.
  - Working with parts of the OS, such as ColorSync, Finder, and Folder Actions.
  - Working with features such as internet services, printing, and URLs.

  In OS X version 10.3, you install and remove the Script menu with utility applications located in `/Applications/AppleScript`.

Folder Actions is a feature that lets you associate scripts with folders. A script is executed when the folder to which it is attached is opened or closed, moved or resized, or has items added or removed.

Folder Actions Setup, located in `/Applications/AppleScript`, is an application that first became available in OS X version 10.3. Starting in OS X version 10.5, Folder Actions Setup is itself scriptable.

This utility helps you perform tasks related to Folder Actions, including the following:

- Enable or disable Folder Actions.
- View the folders that currently have scripts attached and view the attached scripts.
- Add folders to or remove folders from the list of folders.
- Attach one or more scripts to a folder.
- Remove attached scripts from a folder.
- Enable or disable scripts attached to a folder.

System Events is an agent (or faceless background application) that supplies the terminology for using a number of features in AppleScript scripts. Among these features is GUI scripting, which allows your scripts to perform some actions in applications that have no built-in scripting support. System Events, which is located in `/System/Library/CoreServices`, has been part of OS X since version 10.1 (Puma), though its features have evolved since that release.

The following are some of the terminology suites supplied by System Events in OS X version 10.4 (and where noted, in version 10.5). For more information, display the application dictionary, as described in [Displaying Scripting Dictionaries](Scripting%20with%20AppleScript.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytknryfuytcnjtgaydm). You can also get information on many of the features supported by System Events in Mac Help (from the Help menu in OS X) and at the AppleScript [GUI Scripting](http://www.macosxautomation.com/applescript/uiscripting/index.html) web page at the [AppleScript in OS X](http://www.macosxautomation.com/applescript/index.html) website.

- Accounts suite and Login Items suite

  System Events supports scripting of the System Preferences Accounts pane through the terminology in these two suites.
- Audio File suite and Movie File suite

  Available starting in OS X version 10.5, these suites provide terminology for accessing audio files and movie files, and the data they contain.
- Desktop suite

  Available starting in OS X version 10.5, this suite provides access to Desktop preferences, such as the current desktop picture or pictures folder, and the interval for changing the desktop picture.
- Disk-Folder-File suite

  Provides terminology to access disks, files, and folders without targeting the Finder. This can be more efficient than using the Finder, and can prevent certain kinds of conflicts.
- Dock Preferences suite and Expose Preferences suite

  Available starting in OS X version 10.5, these suites provide terminology for accessing Dock preferences, as well as Exposé (including Spaces) and Dashboard mouse and key preferences.
- Folder Actions suite

  Starting with AppleScript 1.9.0 in Mac OS version 10.2, System Events supports the Folder Actions feature, described in [Folder Actions Setup](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytknzqfuytcnbygeztg).
- Network Preferences suite

  Available starting in OS X version 10.5, this suite provides terminology for working with items such as connections and disconnections, network locations, and network services.
- Power suite

  Provides commands for sleeping, logging out, shutting down, or restarting your computer.
- Property List suite

  Provides terminology for reading and writing the information in property list files.
- Processes suite

  Provides classes and commands for GUI Scripting, a feature available starting in OS X version 10.3 that allows scripters to control applications that are either not scriptable or only partially scriptable. With GUI Scripting, AppleScript scripts can select menu items, push buttons, and perform other tasks to control the interfaces of most non-Classic applications. However, as the name implies, GUI scripting works by scripting the user interface, and so tends to result in fragile scripts. For example, items in an application’s user interface may change in various ways between releases, or even between launches of the application, depending on preference settings and other factors.

  This suite is called the Processes suite because in GUI scripting, the root for any script must be a process (represented by an instance of the `application process class`). The GUI Scripting architecture is based on the accessibility support in OS X, which must be enabled, in OS X v10.4, through the AppleScript Utility. Prior to OS X v10.4, GUI scripting was enabled through the “Enable access for assistive devices” checkbox in the Universal Access preference pane in System Preferences.

  For more information, see the [GUI Scripting](http://www.macosxautomation.com/applescript/uiscripting/index.html) web page.
- QuickTime File suite

  Available starting in OS X version 10.5, this suite provides terminology for working with QuickTime files, including data, annotations, and tracks.
- Security suite

  Available starting in OS X version 10.5, this suite provides access to Security preferences, such as automatic login and password requirements.
- System Events suite

  This suite provides a great deal of terminology for working with parts of the OS. That includes properties for accessing certain folders (preferences folder, favorites folder, desktop pictures folder, and so on), the startup disk, and other useful items.
- XML suite

  Provides terminology for working with information in XML files.

Like System Events, Image Events is an agent (or faceless background application) that is located in `/System/Library/CoreServices`. Image Events supports the manipulation, from scripts, of images and image-related data through operations such as cropping, embedding, matching, padding, profiling, rotating, and scaling. These operations are typically used in print, web, and media publishing.

Image Events has been part of OS X since version 10.4 and provides access to the built-in service called SIPS (Scriptable Image Processing Server) that became available in that OS release.

You can find more information on Image Events in Mac Help (from the OS X Help menu) or at the [Image Events](http://www.macosxautomation.com/applescript/imageevents/index.html) web page. You can also examine the Image Events dictionary with Script Editor, as described in [Displaying Scripting Dictionaries](Scripting%20with%20AppleScript.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytknryfuytcnjtgaydm). SIPS is described in [Technical Note TN2035 ColorSync on OS X](https://developer.apple.com/technotes/tn/tn2035.html#TNTAG58). You can also get some information about SIPS by typing `sips --help` in a Terminal window.

Database Events is a simple, scratchpad database implementation for use in AppleScript scripts. It allows any script applet to create and edit its own database.

You can use Database Events to create a new database with a file associated with it or to open a database file to access its database. Databases contain records, records contain fields, and fields contain a name and a value. The assignment of names and values is free form, as the scripter defines it. Databases persist in the file system, across executions of Database Events.

Database Events has been part of OS X since version 10.4. Like System Events, Database Events is an agent (or faceless background application) that is located in `/System/Library/CoreServices`.

You can examine the Database Events dictionary with Script Editor, as described in [Displaying Scripting Dictionaries](Scripting%20with%20AppleScript.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytknryfuytcnjtgaydm).

[Next](Document%20Revision%20History.md)[Previous](Automator.md)

