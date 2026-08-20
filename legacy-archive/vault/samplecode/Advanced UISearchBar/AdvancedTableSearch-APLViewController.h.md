---
title: Advanced UISearchBar
apple_id: DTS40013493
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2013-07-24'
source_url: https://developer.apple.com/library/archive/samplecode/AdvancedTableSearch/Listings/AdvancedTableSearch_APLViewController_h.html
archived_at: '2026-07-18T03:00:48.987508Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Advanced UISearchBar](Advanced%20UISearchBar.md)


[Next](AdvancedTableSearch-APLProduct.h.md)[Previous](AdvancedTableSearch-APLDetailViewController.h.md)

# AdvancedTableSearch/APLViewController.h

```objc
/*
 Copyright (C) 2013-2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Main table view controller for the application.
 */

#import <UIKit/UIKit.h>

@interface APLViewController : UITableViewController <UISearchDisplayDelegate, UISearchBarDelegate>

@property (nonatomic) NSArray *products; // the table's master content

@end
```

[Next](AdvancedTableSearch-APLProduct.h.md)[Previous](AdvancedTableSearch-APLDetailViewController.h.md)

