---
title: Application File Management
apple_id: 10000056i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2011-05-25'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AppFileMgmt/Concepts/SaveOpenPanels.html
archived_at: '2026-07-15T05:25:37.425573Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Application File Management](Introduction%20to%20Application%20File%20Management.md)


[Next](File%20Wrappers.md)[Previous](Introduction%20to%20Application%20File%20Management.md)

# The Save and Open Panels

[NSSavePanel](https://developer.apple.com/documentation/appkit/nssavepanel) creates and manages a Save panel, and allows you to run the panel in a modal loop. The Save panel provides a simple way for a user to specify a file to use when saving a document or other data. It can restrict the user to files of a certain type, as specified by an extension. It also allows you to do several other things with the Save panel:

- Add an accessory view to the panel.
- Customize the user interface of the panel, including the Hide Extension check box and the New Folder button.
- Modify the behavior of the panel through messages exchanged with a delegate.

[NSOpenPanel](https://developer.apple.com/documentation/appkit/nsopenpanel) provides the Open panel for the Cocoa user interface. Applications use the Open panel as a convenient way to query the user for the name of a file to open. The Open panel can only be run modally.

Most of this class’s behavior is defined by its superclass, [NSSavePanel](https://developer.apple.com/documentation/appkit/nssavepanel). `NSOpenPanel` adds to this behavior by:

- Letting you specify the types (by file-name extension or encoded HFS file type) of the items that will appear in the panel
- Letting the user select files, directories, or both
- Letting the user select multiple items at a time

[Next](File%20Wrappers.md)[Previous](Introduction%20to%20Application%20File%20Management.md)

