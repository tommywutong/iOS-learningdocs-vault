---
title: 'Fox: Building a SceneKit Game with the Xcode Scene Editor'
apple_id: TP40016154
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: General
technology: SceneKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/Fox/Listings/Objective_C_iOS_main_m.html
archived_at: '2026-07-18T03:08:53.324686Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fox: Building a SceneKit Game with the Xcode Scene Editor](Fox-%20Building%20a%20SceneKit%20Game%20with%20the%20Xcode%20Scene%20Editor.md)


[Next](Objective-C-iOS-AAPLAppDelegate.h.md)[Previous](Objective-C-iOS-AAPLAppDelegate.m.md)

# Objective-C/iOS/main.m

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This sample code demonstrates how to use Xcode to build a SceneKit level, choose the renderer in between Metal and OpenGL ES, add positional audio triggers, and setup light maps with the new material properties.
  It also demonstrates the usage of particle systems, complex material settings including normal and illumination maps. SceneKit's physics is used to detect collisions with walls, ground, enemy and to collect collectable items.
  This sample app also show how to use SpriteKit to achieve the 2D game overlays (for score and congratulations screen).
 */

@import UIKit;

#import "AAPLAppDelegate.h"

int main(int argc, char * argv[]) {
    @autoreleasepool {
        return UIApplicationMain(argc, argv, nil, NSStringFromClass([AAPLAppDelegate class]));
    }
}
```

[Next](Objective-C-iOS-AAPLAppDelegate.h.md)[Previous](Objective-C-iOS-AAPLAppDelegate.m.md)

