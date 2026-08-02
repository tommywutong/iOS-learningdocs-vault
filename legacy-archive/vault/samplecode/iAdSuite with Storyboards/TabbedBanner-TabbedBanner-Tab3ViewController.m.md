---
title: iAdSuite with Storyboards
apple_id: DTS40013458
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2015-10-29'
source_url: https://developer.apple.com/library/archive/samplecode/iAdSuite_Storyboard/Listings/TabbedBanner_TabbedBanner_Tab3ViewController_m.html
archived_at: '2026-07-18T03:29:33.157983Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iAdSuite with Storyboards](iAdSuite%20with%20Storyboards.md)


[Next](TabbedBanner-TabbedBanner-Tab1ViewController.h.md)[Previous](TabbedBanner-TabbedBanner-Tab2ViewController.h.md)

# TabbedBanner/TabbedBanner/Tab3ViewController.m

```objc
/*
Copyright (C) 2015 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
View controller for tab 3.
*/

#import "Tab3ViewController.h"

@interface Tab3ViewController ()

@end

@implementation Tab3ViewController

- (void)viewDidLoad
{
    [super viewDidLoad];

    NSDictionary *ipsums = [NSDictionary dictionaryWithContentsOfURL:[[NSBundle mainBundle] URLForResource:@"ipsums" withExtension:@"plist"]];
    self.text = ipsums[@"Vegan"];
}

@end
```

[Next](TabbedBanner-TabbedBanner-Tab1ViewController.h.md)[Previous](TabbedBanner-TabbedBanner-Tab2ViewController.h.md)

