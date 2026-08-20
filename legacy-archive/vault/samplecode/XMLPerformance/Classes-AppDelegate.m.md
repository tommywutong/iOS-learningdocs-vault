---
title: XMLPerformance
apple_id: DTS40008094
resource_type: Sample Code
platform: iOS
topic: Performance
technology: Foundation
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/XMLPerformance/Listings/Classes_AppDelegate_m.html
archived_at: '2026-07-18T03:28:29.366371Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [XMLPerformance](XMLPerformance.md)


[Next](Classes-Song.m.md)[Previous](main.m.md)

# Classes/AppDelegate.m

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Application delegate
 */


#import "AppDelegate.h"
#import "Statistics.h"


@implementation AppDelegate

@synthesize window;

- (void)applicationWillTerminate:(UIApplication *)application {
    CloseStatisticsDatabase();
}

@end
```

[Next](Classes-Song.m.md)[Previous](main.m.md)

