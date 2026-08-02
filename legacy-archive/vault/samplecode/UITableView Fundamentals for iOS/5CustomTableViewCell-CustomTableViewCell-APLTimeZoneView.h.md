---
title: UITableView Fundamentals for iOS
apple_id: DTS40007318
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2016-04-07'
source_url: https://developer.apple.com/library/archive/samplecode/TableViewSuite/Listings/5_CustomTableViewCell_CustomTableViewCell_APLTimeZoneView_h.html
archived_at: '2026-07-18T03:26:15.568478Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UITableView Fundamentals for iOS](UITableView%20Fundamentals%20for%20iOS.md)


[Next](5CustomTableViewCell-CustomTableViewCell-main.m.md)[Previous](5CustomTableViewCell-CustomTableViewCell-APLAppDelegate.h.md)

# 5_CustomTableViewCell/CustomTableViewCell/APLTimeZoneView.h

```objc

/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A simple view to display various pieces of information about a time zone. Because the the view's content is fairly complex, it draws its content directly in drawRect: to optimize scolling performance.
  The implementation is very basic -- it doesn't attempt to constrain text to particular areas to aviod overlapping and so on. It does, though, illustrate response to highlighting.
 */

@import UIKit;

@class APLTimeZoneWrapper;

@interface APLTimeZoneView : UIView

@property (nonatomic) APLTimeZoneWrapper *timeZoneWrapper;
@property (nonatomic) NSString *abbreviation;
@property (nonatomic, getter=isHighlighted) BOOL highlighted;
@property (nonatomic, getter=isEditing) BOOL editing;

@end
```

[Next](5CustomTableViewCell-CustomTableViewCell-main.m.md)[Previous](5CustomTableViewCell-CustomTableViewCell-APLAppDelegate.h.md)

