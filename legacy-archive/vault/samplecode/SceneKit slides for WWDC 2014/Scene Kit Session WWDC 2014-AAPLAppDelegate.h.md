---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_AAPLAppDelegate_h.html
archived_at: '2026-07-18T03:23:13.612922Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-Resources-Scenes.scnassets-earth-Credit.txt.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-AAPLAppDelegate.m.md)

# Scene Kit Session WWDC 2014/AAPLAppDelegate.h

```objc
/*
Copyright (C) 2014-2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
This is the main controller for the application. It instantiates and runs a presentation.
*/

#import <SceneKit/SceneKit.h>
#import "AAPLPresentationViewController.h"

@interface AAPLAppDelegate : NSObject <NSApplicationDelegate, AAPLPresentationDelegate>

@property (assign) IBOutlet NSWindow *window;
@property (assign) IBOutlet NSMenu *goMenu;

// Go to the previous or next slide
- (IBAction)nextSlide:(id)sender;
- (IBAction)previousSlide:(id)sender;

@end
```

[Next](Scene%20Kit%20Session%20WWDC%202014-Resources-Scenes.scnassets-earth-Credit.txt.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-AAPLAppDelegate.m.md)

