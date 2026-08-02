---
title: UITableView Fundamentals for iOS
apple_id: DTS40007318
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2016-04-07'
source_url: https://developer.apple.com/library/archive/samplecode/TableViewSuite/Listings/5_CustomTableViewCell_CustomTableViewCell_APLTimeZoneCell_h.html
archived_at: '2026-07-18T03:26:15.493700Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UITableView Fundamentals for iOS](UITableView%20Fundamentals%20for%20iOS.md)


[Next](5CustomTableViewCell-CustomTableViewCell-APLTimeZoneView.m.md)[Previous](5CustomTableViewCell-CustomTableViewCell-APLViewController.h.md)

# 5_CustomTableViewCell/CustomTableViewCell/APLTimeZoneCell.h

```objc

/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A table view cell to display various pieces of information about a time zone. Since the content is fairly complex and can't readily be rendered using three simple subviews, it uses a TimeZoneView to display the content.
 */

@import UIKit;

@class APLTimeZoneWrapper;

@interface APLTimeZoneCell : UITableViewCell

- (void)setTimeZoneWrapper:(APLTimeZoneWrapper *)newTimeZoneWrapper;
- (void)redisplay;

@end
```

[Next](5CustomTableViewCell-CustomTableViewCell-APLTimeZoneView.m.md)[Previous](5CustomTableViewCell-CustomTableViewCell-APLViewController.h.md)

