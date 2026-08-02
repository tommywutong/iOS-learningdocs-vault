---
title: TheElements
apple_id: DTS40007419
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: null
published: '2015-08-25'
source_url: https://developer.apple.com/library/archive/samplecode/TheElements/Listings/Classes_ElementsDataSourceProtocol_h.html
archived_at: '2026-07-18T03:26:45.806693Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TheElements](TheElements.md)


[Next](Classes-PeriodicElements.h.md)[Previous](Classes-AtomicElementFlippedView.m.md)

# Classes/ElementsDataSourceProtocol.h

```objc
/*
Copyright (C) 2015 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Protocol that defines information each Element tableview datasource must provide.
*/


@import UIKit;
#import "AtomicElement.h"

@protocol ElementsDataSource <NSObject>

@required

// these properties are used by the view controller
// for the navigation and tab bar
@property (readonly) NSString *name;
@property (readonly) NSString *navigationBarName;
@property (readonly) UIImage *tabBarImage;

// this property determines the style of table view displayed
@property (readonly) UITableViewStyle tableViewStyle;

// provides a standardized means of asking for the element at the specific
// index path, regardless of the sorting or display technique for the specific
// datasource
- (AtomicElement *)atomicElementForIndexPath:(NSIndexPath *)indexPath;

@optional

// this optional protocol allows us to send the datasource this message, since it has the 
// required information
- (NSString *)tableView:(UITableView *)tableView titleForHeaderInSection:(NSInteger)section;

@end
```

[Next](Classes-PeriodicElements.h.md)[Previous](Classes-AtomicElementFlippedView.m.md)

