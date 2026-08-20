---
title: iAdSuite
apple_id: DTS40010198
resource_type: Sample Code
platform: iOS
topic: null
technology: iAd
published: '2013-05-28'
source_url: https://developer.apple.com/library/archive/samplecode/iAdSuite/Listings/ContainerBanner_ContainerBanner_AppDelegate_m.html
archived_at: '2026-07-18T03:29:30.309350Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iAdSuite](iAdSuite.md)


[Next](ContainerBanner-ContainerBanner-BannerViewController.m.md)[Previous](TabbedBanner-TabbedBanner-main.m.md)

# ContainerBanner/ContainerBanner/AppDelegate.m

```objc
/*
Copyright (C) 2013-2015 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Application delegate
*/

#import "AppDelegate.h"
#import "TextViewController.h"
#import "BannerViewController.h"

@implementation AppDelegate {
    BannerViewController *_bannerViewController;
}

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    self.window = [[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]];
    self.window.backgroundColor = [UIColor whiteColor];

    NSData *ipsumData = [NSData dataWithContentsOfURL:[[NSBundle mainBundle] URLForResource:@"ipsums" withExtension:@"plist"] options:NSDataReadingMappedIfSafe error:nil];
    NSDictionary *ipsums = [NSPropertyListSerialization propertyListWithData:ipsumData options:NSPropertyListImmutable format:nil error:nil];

    TextViewController *textViewController = [[TextViewController alloc] init];
    textViewController.title = NSLocalizedString(@"Original", @"Original");
    textViewController.text = ipsums[@"Original"];

    _bannerViewController = [[BannerViewController alloc] initWithContentViewController:textViewController];

    self.window.rootViewController = _bannerViewController;

    [self.window makeKeyAndVisible];
    return YES;
}

@end
```

[Next](ContainerBanner-ContainerBanner-BannerViewController.m.md)[Previous](TabbedBanner-TabbedBanner-main.m.md)

