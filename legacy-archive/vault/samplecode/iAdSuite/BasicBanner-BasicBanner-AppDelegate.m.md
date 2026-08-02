---
title: iAdSuite
apple_id: DTS40010198
resource_type: Sample Code
platform: iOS
topic: null
technology: iAd
published: '2013-05-28'
source_url: https://developer.apple.com/library/archive/samplecode/iAdSuite/Listings/BasicBanner_BasicBanner_AppDelegate_m.html
archived_at: '2026-07-18T03:29:29.994860Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iAdSuite](iAdSuite.md)


[Next](BasicBanner-BasicBanner-AppDelegate.h.md)[Previous](LICENSE.txt.md)

# BasicBanner/BasicBanner/AppDelegate.m

```objc
/*
Copyright (C) 2013-2015 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Application delegate
*/

#import "AppDelegate.h"
#import "TextViewController.h"

@implementation AppDelegate

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    self.window = [[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]];
    self.window.backgroundColor = [UIColor whiteColor];

    NSData *ipsumData = [NSData dataWithContentsOfURL:[[NSBundle mainBundle] URLForResource:@"ipsums" withExtension:@"plist"] options:NSDataReadingMappedIfSafe error:nil];
    NSDictionary *ipsums = [NSPropertyListSerialization propertyListWithData:ipsumData options:NSPropertyListImmutable format:nil error:nil];

    TextViewController *textViewController = [[TextViewController alloc] init];
    textViewController.title = NSLocalizedString(@"Original", @"Original");
    textViewController.text = ipsums[@"Original"];

    self.window.rootViewController = textViewController;

    [self.window makeKeyAndVisible];
    return YES;
}

@end
```

[Next](BasicBanner-BasicBanner-AppDelegate.h.md)[Previous](LICENSE.txt.md)

