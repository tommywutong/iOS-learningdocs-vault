---
title: Window Programming Guide
apple_id: 10000031i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-11-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/WinPanel/Tasks/UsingWindowFieldEditor.html
archived_at: '2026-07-15T07:21:18.968841Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Window Programming Guide](Introduction.md)


[Next](Using%20Window%20Notifications%20and%20Delegate%20Methods.md)[Previous](Using%20Keyboard%20Interface%20Control%20in%20Windows.md)

# Using the Window’s Field Editor

Each window has a text object that is shared for light editing tasks. This object, the window’s _field editor_, is inserted in the view hierarchy when an object needs to edit some text and removed when the object is finished. The field editor is used by [NSTextField](https://developer.apple.com/documentation/appkit/nstextfield) objects and other controls, for example, to edit the text that they display. The [fieldEditor:forObject:](https://developer.apple.com/documentation/appkit/nswindow/1419647-fieldeditor) method returns a window’s field editor, after asking the delegate for a substitute using [windowWillReturnFieldEditor:toObject:](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419416-windowwillreturnfieldeditor). You can override the [fieldEditor:forObject:](https://developer.apple.com/documentation/appkit/nswindow/1419647-fieldeditor) method of [NSWindow](https://developer.apple.com/documentation/appkit/nswindow) in subclasses or provide a delegate to substitute a class of text object different from the [NSTextView](https://developer.apple.com/documentation/appkit/nstextview) default, thereby customizing text editing in your application.

[Next](Using%20Window%20Notifications%20and%20Delegate%20Methods.md)[Previous](Using%20Keyboard%20Interface%20Control%20in%20Windows.md)

