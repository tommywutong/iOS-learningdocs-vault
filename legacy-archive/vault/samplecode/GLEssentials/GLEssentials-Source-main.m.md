---
title: GLEssentials
apple_id: DTS40010104
resource_type: Sample Code
platform: iOS|macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-08-07'
source_url: https://developer.apple.com/library/archive/samplecode/GLEssentials/Listings/GLEssentials_Source_main_m.html
archived_at: '2026-07-18T03:10:04.617492Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLEssentials](GLEssentials.md)


[Next](Readme.md.md)[Previous](GLEssentials.md)

# GLEssentials/Source/main.m

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Standard AppKit entry point.
 */

#ifdef TARGET_IOS
#import <UIKit/UIKit.h>
#import "AppDelegate.h"
#else // OS X
#import <Cocoa/Cocoa.h>
#endif

int main(int argc, char * argv[]) {

#ifdef TARGET_IOS
    @autoreleasepool {
        return UIApplicationMain(argc, argv, nil, NSStringFromClass([AppDelegate class]));
    }
#else
    return NSApplicationMain(argc, (const char**)argv);
#endif
}
```

[Next](Readme.md.md)[Previous](GLEssentials.md)

