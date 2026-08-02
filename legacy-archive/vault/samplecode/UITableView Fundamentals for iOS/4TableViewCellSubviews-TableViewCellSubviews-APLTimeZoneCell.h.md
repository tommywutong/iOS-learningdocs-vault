---
title: UITableView Fundamentals for iOS
apple_id: DTS40007318
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2016-04-07'
source_url: https://developer.apple.com/library/archive/samplecode/TableViewSuite/Listings/4_TableViewCellSubviews_TableViewCellSubviews_APLTimeZoneCell_h.html
archived_at: '2026-07-18T03:26:15.176227Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UITableView Fundamentals for iOS](UITableView%20Fundamentals%20for%20iOS.md)


[Next](4TableViewCellSubviews-TableViewCellSubviews-APLAppDelegate.m.md)[Previous](4TableViewCellSubviews-TableViewCellSubviews-APLViewController.h.md)

# 4_TableViewCellSubviews/TableViewCellSubviews/APLTimeZoneCell.h

```objc

/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A simple UITableViewCell subclass that provides references to its subviews.
 */

@import UIKit;

@interface APLTimeZoneCell : UITableViewCell

@property (nonatomic, weak, readonly) UILabel *nameLabel;
@property (nonatomic, weak, readonly) UILabel *timeLabel;
@property (nonatomic, weak, readonly) UIImageView *timeImageView;

@end
```

[Next](4TableViewCellSubviews-TableViewCellSubviews-APLAppDelegate.m.md)[Previous](4TableViewCellSubviews-TableViewCellSubviews-APLViewController.h.md)

