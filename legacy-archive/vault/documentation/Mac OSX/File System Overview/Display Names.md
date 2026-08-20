---
title: File System Overview
apple_id: 10000185i
resource_type: Guide
platform: macOS
topic: Data Management
technology: null
published: '2011-05-25'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPFileSystem/Articles/DisplayNames.html
archived_at: '2026-07-15T08:15:25.340295Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [File System Overview](Introduction%20to%20the%20File%20System%20Overview.md)


[Next](BSD%20Permissions%20and%20Ownership.md)[Previous](Filename%20Extensions.md)

# Display Names

Display names are an aspect of the Mac OS X user experience that all applications should support. A display name is a generated name for a file, directory, or application that is based on the user’s current preferences. Display names let each user customize their view of the file system without modifying the file system or affecting the views of other users. Mac OS X currently supports the following display-name customizations:

- Application and directory name localization
- Filename extension hiding

The localization of applications and directories gives users a more complete localization experience than they might previously have had. Applications can have different names depending on the user’s current language preferences. Application-defined directories can also be localized to make it possible for users to navigate the file system in their native language. Mac OS X automatically localizes the names of many well-known system directories.

Filename extension hiding provides comfort to Macintosh users who are used to the file-naming conventions of earlier versions of the operating system. Each user can decide whether to show or hide filename extensions. Users sharing the same system still see things their way. See [Filename Extensions](Filename%20Extensions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi4tolkdjjbeqskiizda) for more information.

Display names should not be confused with the actual names of files, directories, and applications in the file system. Display names are based on file-system names but are modified to reflect the current user’s preferences. For example, the home directory of an English-speaking user has a `Pictures` directory. If the user changes the preferred language to German, the directory name is still `Pictures`, but now that directory appears in the Finder as the `Bilder` folder.

You cannot use display names to manipulate actual files and directories in the file system. You use display names only as read-only strings in your application’s user interface. Display names should always be placed in non-editable controls or in controls whose data is treated as read-only. For example, you would use a display name in the title bar of a document window, in a read-only text field, or in a menu. You would typically not use display names in an editable text field, especially if the user could modify the text and save the changes.

You should always use display name strings immediately after retrieving them. Display names should not be considered persistent, that is, assume they can change from one call to the next. You should never write the display name of a file to your application preferences or store that name in your internal data structures. If you need to refer to a file, store a copy of the actual file name instead.

Mac OS X uses display names in the Finder and in its Open and Save dialogs. If you are writing a GUI-based application, you should support display names to avoid discrepancies between the files users pick and the names they see in your application. However, if you are writing a command-line application, you should not use display names. Mac OS X does not support display names in the Darwin and Classic environments. Applications in those environments must operate on the actual file-system names.

Because display names are for display only, you should use them only in your application’s user interface. For example, if you have a document window open, you would use the display name for the title bar of the window. You should also use display names in other places in your windows where you show filenames, and getting a display name should always be the last thing done before setting the name in a corresponding text field or label.

Carbon application developers can get the display name for a file from Launch Services. The `LSCopyDisplayNameForRef` and `LSCopyDisplayNameForURL` functions return the display name for `FSRef` and `CFURLRef` types, respectively. For information about these functions, see _[Launch Services Reference](https://developer.apple.com/documentation/coreservices/launch_services)_.

[Cocoa](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Cocoa.html#//apple_ref/doc/uid/TP40008195-CH9) application developers can get the display name of a file using the [displayNameAtPath:](https://developer.apple.com/documentation/foundation/nsfilemanager/1409751-displaynameatpath) method of [NSFileManager](https://developer.apple.com/documentation/foundation/filemanager).

The display name of an application can be [localized](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Internationalization.html#//apple_ref/doc/uid/TP40008195-CH23) for the current user. To provide localized versions of your application's display name, you use the existing [bundle](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Bundle.html#//apple_ref/doc/uid/TP40008195-CH4) localization mechanism.

The `Resources` directory of an application bundle can contain multiple `.lproj` subdirectories, each containing the localized resources for one language. One of the files you can put in these language subdirectories is a `InfoPlist.strings` file, which stores localized values for some information property list keys. To specify a localized name for your application, include the `CFBundleDisplayName` key in this file and set the value to the localized name of the application.

For display names, Mac OS X prefers user-customized names over any names contained in the application bundle. If the user changes the name of an application, that name is reflected in the file system. If the user-customized name doesn’t match the value of the `CFBundleDisplayName` key in the application’s information property list file (`Info.plist`), the system displays the user-customized name regardless of the current language settings. However, if the values do match, Mac OS X uses the localized names stored in the application.

For more information about application bundles and their configuration, see _[Bundle Programming Guide](../../Core%20Foundation/Bundle%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2i)_.

If your application installs any custom support directories, you can provide [localized](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Internationalization.html#//apple_ref/doc/uid/TP40008195-CH23) versions of those directory names. A localized directory name shows up as the display name of the directory. Your code must still use the original directory name (not the display name) when accessing the directory's contents.

Providing localized names for directories is not required and should be done only for directories whose names you know in advance. It should not be done for any user-specified directories.

To provide a localized display name for a directory, do the following:

1. Add the extension `.localized` to the directory name.
2. From the Terminal application, create a subdirectory inside the directory called `.localized`.
3. Inside the `.localized` subdirectory, put one or more strings files corresponding to the localizations you support.

Each strings file is a Unicode text file. The name of the file is the appropriate two-letter language code followed by the `.strings` extension. For example, a localized Release Notes directory with English, Japanese, and German localizations would have the following directory structure:

```
Release Notes.localized/
    .localized/
        en.strings
        de.strings
        ja.strings
```

Inside each strings file, include a single string entry to map the nonlocalized directory name to the localized name. When specifying the original directory name, do not include the `.localized` extension you just added. For example, to map the name “Release Notes” to a localized directory name, each strings file would have an entry similar to the following:

```
"Release Notes" = "Localized name";
```

For information on creating a strings file, see “Extracting Localizable Strings From Your Code” in _[Internationalization and Localization Guide](../Internationalization%20and%20Localization%20Guide/About%20Internationalization%20and%20Localization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2i)_.

[Next](BSD%20Permissions%20and%20Ownership.md)[Previous](Filename%20Extensions.md)

