---
title: LightTable
apple_id: DTS40008927
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2017-08-17'
source_url: https://developer.apple.com/library/archive/samplecode/LightTable/Listings/ReadMe_md.html
archived_at: '2026-07-18T03:13:31.794748Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LightTable](LightTable.md)


[Next](LICENSE.txt.md)[Previous](LightTable-InputTrackers.h.md)

# ReadMe.md

```
# LightTable

## DESCRIPTION

The "Hello World" of multi-touch applications, LightTable. This sample project demonstrates how to use mouse and multi-touch events to provide an enhanced user experience.

Drop images on the Light table and resize them using two fingers and a multi-touch capable trackpad. Double-click the slide to adjust the image size and placement within the slide.

## REQUIREMENTS

### BUILD

macOS 10.12.3 or later  
Xcode 8.2.1 or later

### RUNTIME

macOS 10.12.3 or later  
Multi-touch capable trackpad

## PACKAGING LIST

`LTWindowController.h/.m`   
The controller for the document window. Also, this class handles the menu event to bring in and dismiss the tools view.

`LTViewController.h/.m`  
This is the controller for the view. It sets up the bindings between the view and the array controller. Also, it defines the animation to bring in and dismiss the tools view.

`LTView.h/.m `  
This is a custom view that manages drawing and layout of the slides. It allows the user to adjust slides via the mouse or individual touches on the trackpad. All tracking is done with the help of a collection of InputTrackers.

`InputTacker.h/m`  
This is the base class for InputTrackers. Input Trackers are a technique to factor the various input tracking needs of a view without using tracking loops or complicated internal variables. See InputTracker.h for more information.

`ClickTracker.h/.m`  
An InputTracker that looks for single and double clicks.

`DragTracker.h/.m`  
An InputTracker that tracks the dragging of the mouse.

`DualTouchTracker.h/.m`  
An InputTracker that tracks two touches as they move on the trackpad.

## CHANGES FROM PREVIOUS VERSIONS

Version 2.0  
- Updated to ARC and modern Objective-C.  
- Implemented Storyboards in place of the XIB based interface, including the reorganization of bindings.  
- Removed the three-finger swipe gesture.  
- Updated the sample project description.  

Version 1.0
- First version.  

Copyright (C) 2009-2017 Apple Inc. All rights reserved.
```

[Next](LICENSE.txt.md)[Previous](LightTable-InputTrackers.h.md)

