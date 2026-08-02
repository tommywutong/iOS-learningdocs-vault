---
title: RosyWriter
apple_id: DTS40011110
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/RosyWriter/Listings/main_m.html
archived_at: '2026-07-18T03:22:22.148219Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [RosyWriter](RosyWriter.md)


[Next](Classes-RosyWriterOpenGLRenderer.h.md)[Previous](RosyWriter.md)

# main.m

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Standard main file.
 */

#import <UIKit/UIKit.h>

#import "RosyWriterAppDelegate.h"

int main(int argc, char *argv[])
{
    int retVal = 0;
    @autoreleasepool {
        retVal = UIApplicationMain( argc, argv, nil, NSStringFromClass( [RosyWriterAppDelegate class] ) );
    }
    return retVal;
}
```

[Next](Classes-RosyWriterOpenGLRenderer.h.md)[Previous](RosyWriter.md)

