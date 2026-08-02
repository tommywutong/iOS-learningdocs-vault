---
title: 'MyCustomColorPicker: Writing a custom NSColorPicker'
apple_id: DTS10004111
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: AppKit
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/MyCustomColorPicker/Listings/ReadMe_md.html
archived_at: '2026-07-18T03:16:34.546822Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MyCustomColorPicker: Writing a custom NSColorPicker](MyCustomColorPicker-%20Writing%20a%20custom%20NSColorPicker.md)


[Next](Document%20Revision%20History.md)[Previous](TestHost-ViewController.m.md)

# ReadMe.md

```objc
# MyColorPicker

## Description

"MyColorPicker" is a sample Cocoa bundle that shows how to write your own custom color picker.  When installed properly, the custom color picker will appear in the system's "Colors" window or NSColorPanel whenever the user tries to choose a particular color, usually from the "Font" panel or an NSColorWell control.

The Mac OS X Color pickers come in different varieties.  The built in pickers are: Grayscale-Alpha, Red-Green-Blue, Cyan-Yellow-Magenta-Black, Hue Saturation-Brightness, Custom palette, Custom color list, and Color wheel.  MyColorPicker is a simple illustration of picking the commons colors red, green, blue, white and even gray.

## Architecture

You build your own custom color picker as a bundle by subclassing NSColorPicker. The NSColorPicker class is an abstract superclass that implements the NSColorPickingDefault protocol. The NSColorPickingDefault and NSColorPickingCustom protocols define a way to add color pickers (custom user interfaces for color selection) to the NSColorPanel.

MyColorPicker is launched by adopting the NSColorPickingCustom's protocol -

    - (NSView *)provideNewView:(BOOL)initialRequest

The parameter "initialRequest" is YES on the very first call.  At that moment you ask your NSBundle to load its nib.

This color picker example also includes the facility for a preference panel, should you choose to implement one.

## Installation

The Xcode project will build and automatically install this color picker into the user's ColorPickers directory found at -

    ~/Library/ColorPickers/MyColorPicker.colorpicker

This is set in the "Installation Directory" option in the Target Build Settings in Xcode.

## Testing

To test MyColorPicker, you obviously need to launch an application that uses the Color Picker user interface, most conveniently through the Font Panel.  This sample includes a "TestHost" target application, that when run, will load MyColorPicker and allow Xcode to debug it.  To debug it, set breakpoints inside MyColorPicker.m, and select the target "TestHost" and run it.

## Documentation

For detailed technical documentation on the "NSColorPickerCustom" Protocol Reference, refer to the following link -

    http://developer.apple.com/documentation/Cocoa/Reference/ApplicationKit/Protocols/NSColorPickingCustom_Protocol/index.html

For the "NSColorPickingDefault" Protocol Reference, refer to the following link -

    http://developer.apple.com/documentation/Cocoa/Reference/ApplicationKit/Protocols/NSColorPickingDefault_Protocol/index.html

Related documentation on color programming topics for Cocoa, refer to the following link -

    http://developer.apple.com/documentation/Cocoa/Conceptual/DrawColor/index.html

## Requirements

### Build

macOS SDK 10.10 or later.

### Runtime

macOS 10.0 or later

Copyright (C) 2006-2017 Apple Inc. All rights reserved.
```

[Next](Document%20Revision%20History.md)[Previous](TestHost-ViewController.m.md)

