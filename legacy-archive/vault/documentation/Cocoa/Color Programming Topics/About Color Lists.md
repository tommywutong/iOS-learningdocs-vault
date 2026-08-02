---
title: Color Programming Topics
apple_id: 10000082i
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: AppKit
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DrawColor/Concepts/AboutColorLists.html
archived_at: '2026-07-15T07:15:08.290174Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Color Programming Topics](Introduction%20to%20Color%20Programming%20Topics%20for%20Cocoa.md)


[Next](Working%20With%20Color%20Spaces.md)[Previous](About%20Color%20Spaces.md)

# About Color Lists

An [NSColorList](https://developer.apple.com/documentation/appkit/nscolorlist) is an ordered list of [NSColor](https://developer.apple.com/documentation/appkit/nscolor) objects, identified by keys. Instances of `NSColorList`, or more simply, color lists, are used to manage named lists of color objects. The list-mode color picker of an [NSColorPanel](https://developer.apple.com/documentation/appkit/nscolorpanel) object uses instances of `NSColorList` to represent any lists of colors that come with the system, as well as any lists created by the user. An application can use `NSColorList` to manage document-specific color lists, which may be added to an application’s `NSColorPanel` object using its [attachColorList:](https://developer.apple.com/documentation/appkit/nscolorpanel/1531970-attachcolorlist) method.

An `NSColorList` object is similar to a dictionary object: A color object is added to, looked up in, and removed from the list by specifying its key, which is a string object. These keys are used to identify the colors in the list and are used to display the color to the user in the color panel. In addition, colors can be inserted at specified positions in the list.

The color list has a name, specified when you create the object using either the `initWithName:` or `initWithName:fromFile:` method.

Instances of `NSColorList` are created for all user-created color lists (those in the color panel) and various color catalogs available on the system.

An `NSColorList` object saves and retrieves its colors from files with the extension “`.clr`” in directories defined by a standard search path. To access all the color lists in the standard search path, use the [availableColorLists](https://developer.apple.com/documentation/appkit/nscolorlist/1522127-availablecolorlists) method; this returns an array of `NSColorList` objects, from which you can retrieve the individual color lists by name.

The standard search path for color lists is:

- `/System/Library/Colors`
- `/Local/Library/Colors`
- `~/Library/Colors`

The color lists returned by the `availableColorLists` method include color catalogs, made up of colors defined in the `NSNamedColorSpace` color space. One example is the System color list, which appears in the macOS color panel under the name “Developer.” Note, however, that not all named color lists are catalogs. In general, lists created at runtime with NSColor and NSColorList methods are not catalogs.

`NSColorList` reads color list files in several different formats; it saves color lists using the archiver API.

`NSColorList` posts an `NSColorListDidChangeNotification` when a color list is changed.

[Next](Working%20With%20Color%20Spaces.md)[Previous](About%20Color%20Spaces.md)

