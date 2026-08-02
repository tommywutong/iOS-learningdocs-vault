---
title: UITableView Fundamentals for iOS
apple_id: DTS40007318
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2016-04-07'
source_url: https://developer.apple.com/library/archive/samplecode/TableViewSuite/Listings/Shared_Model_Wrappers_APLTimeZoneWrapper_h.html
archived_at: '2026-07-18T03:26:16.407970Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UITableView Fundamentals for iOS](UITableView%20Fundamentals%20for%20iOS.md)


[Next](Shared%20Model%20Wrappers-APLRegion.h.md)[Previous](Shared%20Model%20Wrappers-APLRegion.m.md)

# Shared Model Wrappers/APLTimeZoneWrapper.h

```objc

/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Object to represent a time zone, caching various derived properties that are expensive to compute.
 */

@import UIKit;

@interface APLTimeZoneWrapper : NSObject

@property (nonatomic) NSString *timeZoneLocaleName;
@property (nonatomic) NSTimeZone *timeZone;

@property (nonatomic) NSDate *date;
@property (nonatomic) NSCalendar *calendar;

@property (readonly, nonatomic) NSString *extendedDetailText;
@property (readonly, nonatomic) NSString *whichDay;
@property (readonly, nonatomic) NSString *abbreviation;
@property (readonly, nonatomic) NSString *gmtOffset;
@property (readonly, nonatomic) UIImage *image;

- (instancetype)initWithTimeZone:(NSTimeZone *)aTimeZone nameComponents:(NSArray *)nameComponents NS_DESIGNATED_INITIALIZER;

@end
```

[Next](Shared%20Model%20Wrappers-APLRegion.h.md)[Previous](Shared%20Model%20Wrappers-APLRegion.m.md)

