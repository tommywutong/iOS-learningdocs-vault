---
title: 'ButtonMadness: Creating and Customizing AppKit Controls'
apple_id: DTS10004430
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-12-21'
source_url: https://developer.apple.com/library/archive/samplecode/ButtonMadness/Listings/ButtonMadness_DropDownButton_h.html
archived_at: '2026-07-18T03:02:21.055447Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ButtonMadness: Creating and Customizing AppKit Controls](ButtonMadness-%20Creating%20and%20Customizing%20AppKit%20Controls.md)


[Next](ButtonMadness-AppDelegate.h.md)[Previous](ButtonMadness-MyWindowController.h.md)

# ButtonMadness/DropDownButton.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 NSButton subclass for supporting drop down menus.
 */

@import Cocoa;

@interface DropDownButton : NSButton
{
    NSPopUpButtonCell *popUpCell;
}

@property (NS_NONATOMIC_IOSONLY) BOOL usesMenu;

@end
```

[Next](ButtonMadness-AppDelegate.h.md)[Previous](ButtonMadness-MyWindowController.h.md)

