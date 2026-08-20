---
title: CircleLayout
apple_id: DTS40012315
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2015-07-31'
source_url: https://developer.apple.com/library/archive/samplecode/CircleLayout/Listings/CircleLayout_AppDelegate_m.html
archived_at: '2026-07-18T03:03:20.121301Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CircleLayout](CircleLayout.md)


[Next](CircleLayout-ViewController.m.md)[Previous](CircleLayout-ViewController.h.md)

# CircleLayout/AppDelegate.m

```objc
/*
Copyright (C) 2015 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Simple app delegate.
*/

#import "AppDelegate.h"

#import "ViewController.h"
#import "CircleLayout.h"

@interface AppDelegate ()
@property (strong, nonatomic) ViewController *viewController;
@end

@implementation AppDelegate

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    self.window = [[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]];
    _viewController = [[ViewController alloc] initWithCollectionViewLayout:[[CircleLayout alloc] init]];

    self.window.rootViewController = self.viewController;

    [self.window makeKeyAndVisible];
    return YES;
}


@end
```

[Next](CircleLayout-ViewController.m.md)[Previous](CircleLayout-ViewController.h.md)

