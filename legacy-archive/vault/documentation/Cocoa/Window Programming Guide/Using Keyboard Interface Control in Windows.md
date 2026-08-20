---
title: Window Programming Guide
apple_id: 10000031i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-11-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/WinPanel/Tasks/KeyboardInterfaceWindows.html
archived_at: '2026-07-15T07:21:14.367632Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Window Programming Guide](Introduction.md)


[Next](Using%20the%20Window%E2%80%99s%20Field%20Editor.md)[Previous](Handling%20Events%20in%20Windows.md)

# Using Keyboard Interface Control in Windows

A window’s first responder is often a view object selected by the user clicking it. For text fields and other view objects (mainly subclasses of [NSControl](https://developer.apple.com/documentation/appkit/nscontrol)), the user can select the first responder with the keyboard using the Tab and Shift keys. The [NSView](https://developer.apple.com/documentation/appkit/nsview) class defines the methods for setting up and examining the loop of objects that the user can select in this manner. A view that’s the first responder is called the _key view_, and the views that can become the key view in a window are linked together in the window’s _key view loop_. You normally set up the key view loop using Interface Builder, establishing connections between the `nextKeyView` outlets of views in the window and setting the window’s `initialFirstResponder` outlet to the view that you want selected when the window is first placed onscreen. If you do not set this outlet, the window sets a key loop (not necessarily the same as the one you would have specified!) and picks a default initial first responder for you.

In addition to the key view loop, a window can have a _default button cell_, which uses the Return (or Enter) key as its key equivalent. The `setDefaultButtonCell:` method establishes this button cell; you can also set it in Interface Builder by setting a button cell’s key equivalent to `'\r'`. The default button cell draws itself as a focal element for keyboard interface control unless another button cell is focused on. In this case, it temporarily draws itself as normal and disables its key equivalent. Another default key established by the [NSWindow](https://developer.apple.com/documentation/appkit/nswindow) class is the Escape key, which immediately aborts a modal loop (described in [How Modal Windows Work](How%20Modal%20Windows%20Work.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgizdglkdjjbekqkeijaq)).

See _[NSResponder Class Reference](https://developer.apple.com/documentation/appkit/nsresponder)_ for more information on keyboard interface control.

[Next](Using%20the%20Window%E2%80%99s%20Field%20Editor.md)[Previous](Handling%20Events%20in%20Windows.md)

