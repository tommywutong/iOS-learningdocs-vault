---
title: 'Tabster: Various techniques in using UITabBarController'
apple_id: DTS40011213
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2018-02-15'
source_url: https://developer.apple.com/library/archive/samplecode/Tabster/Listings/Tabster_Classes_FourViewController_m.html
archived_at: '2026-07-18T03:26:19.971195Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tabster: Various techniques in using UITabBarController](Tabster-%20Various%20techniques%20in%20using%20UITabBarController.md)


[Next](Tabster-Classes-TwoViewController.h.md)[Previous](Tabster-Classes-OneViewController.m.md)

# Tabster/Classes/FourViewController.m

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
  See LICENSE.txt for this sample’s licensing information

  Abstract:
  The view controller for page four. 
 */

#import "FourViewController.h"

@interface FourViewController ()

@property (weak, nonatomic) IBOutlet UILabel *titleLabel;

@end

#pragma mark -

@implementation FourViewController

- (void)awakeFromNib
{
    [super awakeFromNib];

    // Make our tabbar icon a custom one;
    // we could do it in Interface Builder, but this is just to illustrate a point about
    // using awakeFromNib vs. viewDidLoad.
    //
    UITabBarItem *customTab = [[UITabBarItem alloc] initWithTitle:NSLocalizedString(@"Four", @"")
                                                            image:[UIImage imageNamed:@"tab4.png"]
                                                              tag:0];
    self.tabBarItem = customTab;
}

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

[Next](Tabster-Classes-TwoViewController.h.md)[Previous](Tabster-Classes-OneViewController.m.md)

