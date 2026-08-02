---
title: Advanced UISearchBar
apple_id: DTS40013493
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2013-07-24'
source_url: https://developer.apple.com/library/archive/samplecode/AdvancedTableSearch/Listings/AdvancedTableSearch_APLDetailViewController_m.html
archived_at: '2026-07-18T03:00:48.865532Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Advanced UISearchBar](Advanced%20UISearchBar.md)


[Next](LICENSE.txt.md)[Previous](AdvancedTableSearch-APLViewController.m.md)

# AdvancedTableSearch/APLDetailViewController.m

```objc
/*
 Copyright (C) 2013-2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Detail view controller for the application. Implemented to support state restoration.
 */

#import "APLDetailViewController.h"

@interface APLDetailViewController ()
@property (nonatomic, strong) IBOutlet UILabel *productInfoLabel;
@end

@implementation APLDetailViewController

static NSString *ProductTitleKey = @"ProductTitleKey";
static NSString *ProductInfoKey = @"ProductInfoKey";

- (void)viewWillAppear:(BOOL)animated
{
    [super viewWillAppear:animated];

    self.navigationController.navigationBar.translucent = NO;

    self.productInfoLabel.text = self.productInfo;
}

- (void)encodeRestorableStateWithCoder:(NSCoder *)coder
{
    [super encodeRestorableStateWithCoder:coder];

    [coder encodeObject:self.title forKey:ProductTitleKey];
    [coder encodeObject:self.productInfoLabel.text forKey:ProductInfoKey];
}

- (void)decodeRestorableStateWithCoder:(NSCoder *)coder
{
    [super decodeRestorableStateWithCoder:coder];

    self.title = [coder decodeObjectForKey:ProductTitleKey];
    self.productInfo = [coder decodeObjectForKey:ProductInfoKey];
}

@end
```

[Next](LICENSE.txt.md)[Previous](AdvancedTableSearch-APLViewController.m.md)

