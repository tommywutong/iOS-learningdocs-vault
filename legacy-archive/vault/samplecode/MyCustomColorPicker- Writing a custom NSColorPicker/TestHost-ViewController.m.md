---
title: 'MyCustomColorPicker: Writing a custom NSColorPicker'
apple_id: DTS10004111
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: AppKit
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/MyCustomColorPicker/Listings/TestHost_ViewController_m.html
archived_at: '2026-07-18T03:16:34.682026Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MyCustomColorPicker: Writing a custom NSColorPicker](MyCustomColorPicker-%20Writing%20a%20custom%20NSColorPicker.md)


[Next](ReadMe.md.md)[Previous](TestHost-AppDelegate.h.md)

# TestHost/ViewController.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 TestHost application view controller for testing our custom color picker plugin.
 */

#import "ViewController.h"

@implementation ViewController

- (IBAction)testAction:(id)sender
{
    NSColorPanel *panel = [NSColorPanel sharedColorPanel];
    if ([panel isVisible])
    {
        [panel orderOut:self];
    }
    else
    {
        [panel orderFront:self];
    }
}

@end
```

[Next](ReadMe.md.md)[Previous](TestHost-AppDelegate.h.md)

