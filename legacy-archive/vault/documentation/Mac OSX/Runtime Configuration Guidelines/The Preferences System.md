---
title: Runtime Configuration Guidelines
apple_id: 10000170i
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: null
published: '2009-10-19'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPRuntimeConfig/Articles/UserPreferences.html
archived_at: '2026-07-15T08:16:27.233911Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Runtime Configuration Guidelines](Introduction.md)


[Next](Environment%20Variables.md)[Previous](Information%20Property%20List%20Files.md)

# The Preferences System

Preferences are application or system options that allow users to customize their working environment. Most applications read in some form of user preferences. For example, a document-based application may store preferences for the default font, automatic save options, or page setup information. Preferences are not limited to applications, however. You can read and write preference information, including user preferences, from any [frameworks](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56) or libraries you define.

The preferences system of macOS includes built-in support for preserving and restoring user settings across sessions. Both Carbon and Cocoa applications can use Core Foundation’s Preference Services for reading and writing preference information. Cocoa applications can also use the [NSUserDefaults](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/cl/NSUserDefaults) class to read user preferences.

The preferences system associates preference values with a key, which you use to retrieve the preference value later. User preferences have a scope based on a combination of the user login ID, application ID, and host (computer) name. This mechanism allows you to create preferences that apply at different levels. For example, you can save a preference value that applies to any of the following entities:

- the current user of your application on the current host
- all users of your application on a specific host connected to the local network
- the current user of your application on any host connected to the local network (the usual category for user preferences)
- any user of any application on any host connected to the local network

Applications should store only those preferences that represent information captured from the user. Storing the same set of default preferences for each user is an inefficient way to manage your application’s preferences. Preferences are stored in [property list](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/PropertyList.html#//apple_ref/doc/uid/TP40008195-CH44) files that must be parsed to read in the preference information. A more efficient way to manage preferences is to store a set of default preferences internally and then apply any user-customized preferences on top of the default set.

The preferences system stores preference data in files located in the `Library/Preferences` folder in the appropriate file-system domain. For example, if the preference applies to a single user, the file is written to the `Library/Preferences` folder in the user’s home directory. If the preference applies to all users on a network, it goes in `/Network/Library/Preferences`.

The name of each file in `Library/Preferences` is comprised of the application’s [bundle](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Bundle.html#//apple_ref/doc/uid/TP40008195-CH4) identifier followed by the `.plist` extension. For example, the bundle identifier for the TextEdit application is `com.apple.TextEdit` so its preferences file name is `com.apple.TextEdit.plist`.

To ensure that there are no naming conflicts, Apple strongly recommends that bundle identifiers take the same form as Java package names—your company’s unique domain name followed by the application or library name. For example, the Finder uses the identifier `com.apple.finder`. This scheme minimizes the possibility of name collision and leaves you the freedom to manage the identifier name space under your corporate domain. You assign this value to the `CFBundleIdentifier` key in your information property list file.

Problems might ensue if an application tries to write preferences to a location other than `Library/Preferences` in the appropriate file-system domain. For one thing, the preferences APIs aren’t designed for this difference. But more importantly, preferences stored in unexpected locations are excluded from the preferences search list and so might not be noticed by other applications, frameworks, or system services.

In macOS version 10.4 and later, preferences are saved in the binary plist format. You can convert a file from one format to another using the `plutil(1)` tool (for example so that you can examine the plist in XML form), but you should not rely on the format of the file. You should refrain from editing preference files manually. Entering incorrect information or malformed data could cause problems when your application tries to read the file later. The correct way to extract information from preference domains in your application is through the preferences APIs.

When your application searches for an existing preference value, the preferences system uses the current preference domain to limit the scope of the search. Similarly, when your application writes out new preferences, the values are scoped to the current domain.

Preference domains are identified by three pieces of information: a user ID, an application identifier, and a host name. In most cases, you would specify preferences for the current user and application. However, you might also decide to store application-level preferences. To do that, you would use the functions in the Core Foundation Preferences Utilities to specify exactly which domain you wanted to use. For information on how to use these routines, see _[Preferences Programming Topics for Core Foundation](../../Core%20Foundation/Preferences%20Programming%20Topics%20for%20Core%20Foundation/Introduction%20to%20Preferences%20Programming%20Topics%20for%20Core%20Foundation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezds2i)_.

Table 1 shows all of the preference domains. The routines for retrieving preferences search through the preference domains in the order shown here until they find the requested key. Thus, if a preference is not found in a more user-specific and application-specific domain, the routines search the more global domains for the information.

__Table 1__  Preference domains in search order

| Search order | User Scope | Application Scope | Host Scope |
| 1 | Current User | Current Application | Current Host |
| 2 | Current User | Current Application | Any Host |
| 3 | Current User | Any Application | Current Host |
| 4 | Current User | Any Application | Any Host |
| 5 | Any User | Current Application | Current Host |
| 6 | Any User | Current Application | Any Host |
| 7 | Any User | Any Application | Current Host |
| 8 | Any User | Any Application | Any Host |

The preferences system of macOS includes a command-line utility named `defaults` for reading, writing, and removing preferences (also known as user defaults) from the application domain or other domains. The `defaults` utility is invaluable as an aid for debugging applications. Many preferences are accessible through an application’s Preference dialog (or the equivalent), but preferences such as the position of a window aren’t always available. For those preferences, you can view them with the `defaults` utility.

To run the utility, launch the Terminal application and, in a BSD shell, enter `defaults` plus command options describing what you want. For a terse description of syntax and arguments, run the `defaults` command by itself. For a more complete description, read the man page for `defaults` or run the command with the `usage` argument:

```
$ defaults usage
```

You should avoid changing values using the `defaults` tool while the target application is running. If you make such a change, the application is unlikely to see the change and more likely to overwrite the new value you just specified.

[Next](Environment%20Variables.md)[Previous](Information%20Property%20List%20Files.md)

