---
title: VideoSnake
apple_id: DTS40012327
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/VideoSnake/Listings/main_m.html
archived_at: '2026-07-18T03:27:55.345617Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [VideoSnake](VideoSnake.md)


[Next](Classes-VideoSnakeSessionManager.m.md)[Previous](VideoSnake.md)

# main.m

```objc
/*
 <codex>
 <abstract>Standard main file.</abstract>
 </codex>
 */

#import <UIKit/UIKit.h>

#import "VideoSnakeAppDelegate.h"

int main(int argc, char *argv[])
{
    int retVal = 0;
    @autoreleasepool {
        retVal = UIApplicationMain(argc, argv, nil, NSStringFromClass([VideoSnakeAppDelegate class]));
    }
    return retVal;
}
```

[Next](Classes-VideoSnakeSessionManager.m.md)[Previous](VideoSnake.md)

