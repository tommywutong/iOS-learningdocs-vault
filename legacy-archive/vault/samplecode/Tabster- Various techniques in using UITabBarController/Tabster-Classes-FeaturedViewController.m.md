---
title: 'Tabster: Various techniques in using UITabBarController'
apple_id: DTS40011213
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2018-02-15'
source_url: https://developer.apple.com/library/archive/samplecode/Tabster/Listings/Tabster_Classes_FeaturedViewController_m.html
archived_at: '2026-07-18T03:26:19.866469Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tabster: Various techniques in using UITabBarController](Tabster-%20Various%20techniques%20in%20using%20UITabBarController.md)


[Next](Document%20Revision%20History.md)[Previous](Tabster-Classes-ThreeViewController.m.md)

# Tabster/Classes/FeaturedViewController.m

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
  See LICENSE.txt for this sample’s licensing information

  Abstract:
  The "Featured" view controller. 
 */

#import "FeaturedViewController.h"

@interface FeaturedViewController ()

@property (nonatomic, weak) IBOutlet UILabel *titleLabel;

@end

#pragma mark -

@implementation FeaturedViewController

- (void)viewWillAppear:(BOOL)animated
{
    [super viewWillAppear:animated];

    // If we were navigated to through the More screen table, then we have a navigation bar which
    // also means we have a title.  So hide the title label in this case, otherwise, we need it.
    //
    self.titleLabel.hidden = [self.parentViewController isKindOfClass:[UINavigationController class]] ? YES : NO;
}

@end
```

[Next](Document%20Revision%20History.md)[Previous](Tabster-Classes-ThreeViewController.m.md)

