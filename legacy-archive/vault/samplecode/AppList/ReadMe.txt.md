---
title: AppList
apple_id: DTS40008859
resource_type: Sample Code
platform: macOS
topic: General
technology: AppKit
published: '2014-05-06'
source_url: https://developer.apple.com/library/archive/samplecode/AppList/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:01:06.973586Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AppList](AppList.md)


[Next](main.m.md)[Previous](AppList.md)

# ReadMe.txt

```
AppList
=======

"AppList" is a Cocoa sample application that demonstrates how to use the NSRunningApplication class provided by NSWorkspace.  NSRunningApplication can be used for inspecting and manipulating running applications on the system.  An array of these objects are by NSWorkspace using:

    NSArray *appList = [[NSWorkspace sharedWorkspace] runningApplications];

Only user applications can be tracked; this does not provide information about every process on the system.

Since NSRunningApplication has properties that vary, they can be observed with KVO.  So we use Cocoa bindings to display these properties to the user.  The properties are returned atomically so NSRunningApplication is thread safe.

Note: This app has been Sandboxed.


Sample Build Requirements
========================================================
Xcode 5.0, OS X 10.9


Sample Runtime Requirements
========================================================
OS X 10.8 or later


Using the Sample
========================================================
Simply build and run the sample using Xcode.  Select any application from the list to reveal its attributes on the right side of the window.  You can also hide and unhide an application.


Packaging List
========================================================
AppController.m
AppController.h
NSApp's main controller object that controls the hide ad unhide buttons.  It also contains a custom value transformer for mapping NSBundleExecutableArchitecture values to readable strings.

MainMenu.xib
Contains the menu bar and main window this app along with all the necessary Cocoa bindings to display application attributes. 


Copyright (C) 2008-2014 Apple Inc. All rights reserved.
```

[Next](main.m.md)[Previous](AppList.md)

