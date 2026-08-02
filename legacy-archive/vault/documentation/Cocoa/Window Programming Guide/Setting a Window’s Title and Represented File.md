---
title: Window Programming Guide
apple_id: 10000031i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-11-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/WinPanel/Tasks/SettingWindowTitle.html
archived_at: '2026-07-15T07:21:17.984189Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Window Programming Guide](Introduction.md)


[Next](Setting%20Attributes%20for%20the%20Window%E2%80%99s%20Image.md)[Previous](Setting%20a%20Window%E2%80%99s%20Appearance.md)

# Setting a Window’s Title and Represented File

A titled window can display an arbitrary title or one derived from a filename. The [setTitle:](https://developer.apple.com/documentation/appkit/nswindow/1419404-title) method puts an arbitrary string on the title bar. The [setTitleWithRepresentedFilename:](https://developer.apple.com/documentation/appkit/nswindow/1419192-settitlewithrepresentedfilename) method formats a filename in the title bar in a readable format and associates the window with that file. You can set the associated file without changing the title using [setRepresentedFilename:](https://developer.apple.com/documentation/appkit/nswindow/1419631-representedfilename). You can use the association between the window and the file in any way you see fit. One convenience offered by the [NSWindow](https://developer.apple.com/documentation/appkit/nswindow) class is marking the file as having been changed, so that the user is prompted to save it on closing the window. The method for marking the document as having been changed is [setDocumentEdited:](https://developer.apple.com/documentation/appkit/nswindow/1419311-documentedited). When the window closes, its delegate can check if the files has been changed using [isDocumentEdited](https://developer.apple.com/documentation/appkit/nswindow/1419311-isdocumentedited) to see whether the document needs to be saved.

Additionally, starting in OS X version 10.5, you can set a window’s represented document by URL using the [setRepresentedURL:](https://developer.apple.com/documentation/appkit/nswindow/1419066-representedurl) method. You can get the URL of the document currently represented by a window using the [representedURL](https://developer.apple.com/documentation/appkit/nswindow/1419066-representedurl) method. The window will automatically use the known icon for the file type of the specified file, if one exists. To customize the document icon, you can use the following code segment:

`[[NSWindow standardWindowButton:NSWindowDocumentIconButton] setImage:customImage]`.

By default, a Command-click or Control-click on the rectangle containing a window’s document icon button and title will show a path popup. To customize this behavior, you can implement [window:shouldPopUpDocumentPathMenu:](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419465-window) in your window’s delegate. You can return `NO` from this method to stop the window from showing the path popup.

You can also customize the document icon’s default drag behavior by implementing the [window:shouldDragDocumentWithEvent:from:withPasteboard:](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419452-window) in the window’s delegate. You can return `NO` to prohibit dragging the document icon.

[Next](Setting%20Attributes%20for%20the%20Window%E2%80%99s%20Image.md)[Previous](Setting%20a%20Window%E2%80%99s%20Appearance.md)

