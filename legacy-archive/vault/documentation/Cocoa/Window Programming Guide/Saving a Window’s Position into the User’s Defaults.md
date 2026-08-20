---
title: Window Programming Guide
apple_id: 10000031i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-11-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/WinPanel/Tasks/SavingWindowPosition.html
archived_at: '2026-07-15T07:21:16.050051Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Window Programming Guide](Introduction.md)


[Next](Minimizing%20Windows.md)[Previous](Sizing%20and%20Placing%20Windows.md)

# Saving a Window’s Position into the User’s Defaults

A window can store its placement in the user defaults system, so that it appears in the same location the next time the user starts the application. The [saveFrameUsingName:](https://developer.apple.com/documentation/appkit/nswindow/1419290-saveframe) method stores the frame rectangle, and [setFrameUsingName:](https://developer.apple.com/documentation/appkit/nswindow/1419723-setframeusingname) sets it from the value in user defaults. You can also use the [setFrameAutosaveName:](https://developer.apple.com/documentation/appkit/nswindow/1419509-setframeautosavename) method to have a window save the frame rectangle any time it changes. However, for the correct frame to be saved, you must ensure that the window controller for the window in question doesn’t cascade the windows under its charge. You accomplish this task by sending [setShouldCascadeWindows:](https://developer.apple.com/documentation/appkit/nswindowcontroller/1528177-shouldcascadewindows)`NO` to the controller, as shown in Listing 1.

__Listing 1__  Saving a window’s frame automatically

```
NSWindow *window = // the window in question
[[window windowController] setShouldCascadeWindows:NO];      // Tell the controller to not cascade its windows.
[window setFrameAutosaveName:[window representedFilename]];  // Specify the autosave name for the window.
```

To expunge a frame rectangle from the defaults system, use the class method [removeFrameUsingName:](https://developer.apple.com/documentation/appkit/nswindow/1419313-removeframeusingname).

[Next](Minimizing%20Windows.md)[Previous](Sizing%20and%20Placing%20Windows.md)

