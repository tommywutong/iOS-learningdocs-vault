---
title: Simple UISearchBar with State Restoration
apple_id: DTS40007848
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2013-05-23'
source_url: https://developer.apple.com/library/archive/samplecode/TableSearch/Listings/TableSearch_APLDetailViewController_m.html
archived_at: '2026-07-18T03:26:12.356919Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Simple UISearchBar with State Restoration](Simple%20UISearchBar%20with%20State%20Restoration.md)


[Next](Document%20Revision%20History.md)[Previous](TableSearch-APLViewController.m.md)

# TableSearch/APLDetailViewController.m

```objc

/*
 Copyright (C) 2013-2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Detail view controller for the application. Implemented to support state restoration.
 */

#import "APLDetailViewController.h"

@implementation APLDetailViewController

static NSString *ProductTitleKey = @"ProductTitleKey";


- (void) encodeRestorableStateWithCoder:(NSCoder *)coder
{
    [super encodeRestorableStateWithCoder:coder];
    [coder encodeObject:self.title forKey:ProductTitleKey];
}


- (void) decodeRestorableStateWithCoder:(NSCoder *)coder
{
    [super decodeRestorableStateWithCoder:coder];
    self.title = [coder decodeObjectForKey:ProductTitleKey];
}


@end
```

[Next](Document%20Revision%20History.md)[Previous](TableSearch-APLViewController.m.md)

