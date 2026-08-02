---
title: 'Tabster: Various techniques in using UITabBarController'
apple_id: DTS40011213
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2018-02-15'
source_url: https://developer.apple.com/library/archive/samplecode/Tabster/Listings/Tabster_Classes_ModalViewController_m.html
archived_at: '2026-07-18T03:26:20.185473Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tabster: Various techniques in using UITabBarController](Tabster-%20Various%20techniques%20in%20using%20UITabBarController.md)


[Next](Tabster-Classes-FavoritesViewController.m.md)[Previous](LICENSE.txt.md)

# Tabster/Classes/ModalViewController.m

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
  See LICENSE.txt for this sample’s licensing information

  Abstract:
  The modal view controller for temporary UI interaction. 
 */

#import "ModalViewController.h"
#import "SubLevelViewController.h"

@interface ModalViewController ()

@property (weak, nonatomic) IBOutlet UILabel *titleLabel;

@end

#pragma mark -

@implementation ModalViewController

- (void)viewWillAppear:(BOOL)animated
{
    [super viewWillAppear:animated];
    self.titleLabel.text = self.owningViewController.currentSelectionTitle;
}

@end
```

[Next](Tabster-Classes-FavoritesViewController.m.md)[Previous](LICENSE.txt.md)

