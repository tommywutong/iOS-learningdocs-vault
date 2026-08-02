---
title: Using External Displays
apple_id: DTS40010724
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2013-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/ExternalDisplay/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:08:02.346902Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Using External Displays](Using%20External%20Displays.md)


[Next](ExternalDisplay-ExternalDisplayAppDelegate.h.md)[Previous](Using%20External%20Displays.md)

# ReadMe.txt

```
### ExternalDisplay ###

===========================================================================
DESCRIPTION:

How to show content on an external display.

===========================================================================
BUILD REQUIREMENTS:

iOS 7.0 SDK or later

===========================================================================
RUNTIME REQUIREMENTS:

iOS 6.0 or later

===========================================================================
USING THE SAMPLE:

Build and run the sample on an iOS device that supports external displays
such as iPad or iPhone 4. Plug in a display using the Apple iPad Dock 
Connector to VGA Adapter or Apple Component AV Cable.

When an external display is detected, the app will show the available
display resolutions. Select one from the picker and tap Set.

Tap the Presentation Mode switch to toggle the contents shown on the
external display.

===========================================================================
PACKAGING LIST:

main.m - Main entry point for this sample.

ExternalDisplayAppDelegate.h/.m - The application's delegate that sets up
    the main window and navigation controller.

ExternalDisplayViewController.h/.m - The main view controller. Also serves
    as a delegate for the presentation mode view controller to receive
    changes to the presence and resolution of an external display.

    Draws an image of a "1" on the external display if presentation
    mode is on or a "2" if presentation mode is off.

PresoModeViewController.h/.m - Encapsulates all state and behavior related
    to detecting an external display being attached or removed,
    determining the available display modes (resolutions), and enabling
    the app's "presentation mode". "Presentation mode" simply indicates
    whether the app should show some of the content from the device
    display on the external display or show something different.

    When a new external display resolution is selected, creates a
    window and view of the new size and hands the window back to its
    delegate for drawing.

===========================================================================
CHANGES FROM PREVIOUS VERSIONS:

Version 1.1
- Modernized for iOS 6 and 7.

Version 1.0
- First version.

===========================================================================
Copyright (C) 2011-13 Apple Inc. All rights reserved.
```

[Next](ExternalDisplay-ExternalDisplayAppDelegate.h.md)[Previous](Using%20External%20Displays.md)

