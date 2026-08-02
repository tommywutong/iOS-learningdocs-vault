---
title: Workspace Services Programming Topics
apple_id: 10000100i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2009-06-25'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Workspace/Articles/InformationAboutFiles.html
archived_at: '2026-07-15T07:21:20.971113Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Workspace Services Programming Topics](Introduction%20to%20Workspace%20Services.md)


[Next](Manipulating%20Files.md)[Previous](Use%20of%20.app%20Extension.md)

# Retrieving Information About Files

This document explains how to use NSWorkspace to retrieve information about files.

To retrieve the file type and what application opens a file, use NSWorkspace’s `getInfoForFile:application:type:` method. The string passed to the method must be the full pathname of the desired file. This code fragment retrieves the application and type for the file at `fullPath`:

```
NSString *fullPath;    // Assume this exists.
NSString *theApplication;
NSString *theType;

[[NSWorkspace sharedWorkspace] getInfoForFile:fullPath
                               application:&theApplication
                               type:&theType];
[theApplication retain];
[theType retain];
```

To retrieve other file information, use the `NSFileManager` methods `displayNameAtPath:`, `fileExtensionHidden`, `fileHFSCreatorCode`, `fileHFSTypeCode`, and `fileAttributesAtPath:traverseLink:`.

To retrieve the full pathname for an application, use the `fullPathForApplication:` method. The provided application name can either include or omit the `.app` extension.

To find out if a pathname points to a file package, use the `isFilePackageAtPath:` method.

The methods `iconForFile:` and `iconForFiles:` retrieve the icon for a file or the icons for an array of files. Files should be specified with full pathnames. The `iconForFileType:` method provides the icon for a given file extension or encoded HFS file type. This code fragment retrieves the icon for the file at `fullPath`, and resizes it to full 128 pixels by 128 pixels resolution:

```
NSString *fullPath;    // Assume this exists.
NSImage *theIcon;

theIcon = [[[NSWorkspace sharedWorkspace] iconForFile:fullPath] retain];
[theIcon setSize:NSMakeSize(128.0,128.0)];
```

To retrieve a generic icon, call the `NSFileTypeForHFSTypeCode` function with one of the icon constants defined by Icon Services in the Carbon framework (see `Standard Finder Icon Constants` in _Icon Services and Utilities Reference_), then use the `iconForFileType:` method with the result. This code fragment retrieves the generic application icon at full size:

```objc
#import <Carbon/Carbon.h>
// ...
NSImage *theIcon;

theIcon = [[[NSWorkspace sharedWorkspace]
              iconForFileType:
              NSFileTypeForHFSTypeCode(kGenericApplicationIcon)] retain];
[theIcon setSize:NSMakeSize(128.0,128.0)];
```

[Next](Manipulating%20Files.md)[Previous](Use%20of%20.app%20Extension.md)

