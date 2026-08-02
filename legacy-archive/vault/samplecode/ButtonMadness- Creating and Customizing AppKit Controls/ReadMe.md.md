---
title: 'ButtonMadness: Creating and Customizing AppKit Controls'
apple_id: DTS10004430
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-12-21'
source_url: https://developer.apple.com/library/archive/samplecode/ButtonMadness/Listings/ReadMe_md.html
archived_at: '2026-07-18T03:02:21.432350Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ButtonMadness: Creating and Customizing AppKit Controls](ButtonMadness-%20Creating%20and%20Customizing%20AppKit%20Controls.md)


[Next](ButtonMadness-AppDelegate.m.md)[Previous](ButtonMadness-main.m.md)

# ReadMe.md

```
# ButtonMadness

## Description

"ButtonMadness" is a Cocoa application that demonstrates how to use the various type of `NSButton` and `NSControl` classes.  It demonstrates two approaches: 1) creating buttons using Interface Builder, 2) creating the same buttons using code.  Apple recommends that you design your application with Xcode's Interface Builder whenever possible.  However, there may be an occasion when you need to do control creation using code in situations where you don't exactly know the make up of your UI until the application or user loads something.  This sample shows both approaches as it gives you an idea of the "magic" that goes on behind the scenes in Interface Builder to create the standard UI elements.  So this sample gives you the knowledge in programmatically creating these buttons, affect their behavior, and setting their target/action connections.

### General Approach

Create a "CustomView" placeholder in the nib file - this will determine the placement and size of the control.
- Note that you may choose to not use a placeholder view and determine its location coordinates and size on your own.
- For convenience, this sample simply leverages the CustomView for easy control placement.

At view loading time -
- Create an instance of the desired class, and set its frame to match the placeholder.
- Set up the attributes of the control.
- Add the newly created control as a subView of the parent view (in our case NSBox).
- Remove the placeholder CustomView.

### Features

"ButtonMadness" shows off the following:

1. `NSPopUpButton` - Pull down and popup style menus.

2. `NSButton` - Icon buttons: normal or momentary type buttons.  It also includes a special custom button "DropDownButton" for menus.

3. Grouped Radios - A stack view of group radio buttons.

4. `NSColorWell`

5. `NSSegmentedControl` - Introduces a special Objective-C category to un-select all segments.

6. `NSLevelIndicator` - Includes the ability to change them to the four known indicator styles.

To examine the action results of these controls, refer to the Console Log or Run Log.

## Requirements

### Build Requirements

macOS 10.13 SDK or later

### Runtime Requirements

Mac OS X 10.11 or later

Copyright (C) 2007-2017, Apple Inc.
```

[Next](ButtonMadness-AppDelegate.m.md)[Previous](ButtonMadness-main.m.md)

