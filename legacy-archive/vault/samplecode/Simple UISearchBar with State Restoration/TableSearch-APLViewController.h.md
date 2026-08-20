---
title: Simple UISearchBar with State Restoration
apple_id: DTS40007848
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2013-05-23'
source_url: https://developer.apple.com/library/archive/samplecode/TableSearch/Listings/TableSearch_APLViewController_h.html
archived_at: '2026-07-18T03:26:12.468100Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Simple UISearchBar with State Restoration](Simple%20UISearchBar%20with%20State%20Restoration.md)


[Next](TableSearch-APLProduct.h.md)[Previous](TableSearch-APLDetailViewController.h.md)

# TableSearch/APLViewController.h

```objc

/*
 Copyright (C) 2013-2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Main table view controller for the application.
 */

#import <UIKit/UIKit.h>

@interface APLViewController : UITableViewController <UISearchDisplayDelegate, UISearchBarDelegate>

@property (nonatomic) NSArray *products; // The master content.

@end
```

[Next](TableSearch-APLProduct.h.md)[Previous](TableSearch-APLDetailViewController.h.md)

