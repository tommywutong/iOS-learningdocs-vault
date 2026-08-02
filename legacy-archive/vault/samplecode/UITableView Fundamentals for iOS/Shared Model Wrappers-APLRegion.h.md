---
title: UITableView Fundamentals for iOS
apple_id: DTS40007318
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2016-04-07'
source_url: https://developer.apple.com/library/archive/samplecode/TableViewSuite/Listings/Shared_Model_Wrappers_APLRegion_h.html
archived_at: '2026-07-18T03:26:16.314531Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UITableView Fundamentals for iOS](UITableView%20Fundamentals%20for%20iOS.md)


[Next](3SimpleIndexedTableView-SimpleIndexedTableView-APLAppDelegate.h.md)[Previous](Shared%20Model%20Wrappers-APLTimeZoneWrapper.h.md)

# Shared Model Wrappers/APLRegion.h

```objc

/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Object to represent a region containing the corresponding time zone wrappers.
 */

@import Foundation;

@interface APLRegion : NSObject

@property (nonatomic) NSString *name;
@property (nonatomic) NSCalendar *calendar;

+ (instancetype)regionNamed:(NSString *)name;
+ (instancetype)newRegionWithName:(NSString *)regionName;

- (void)addTimeZone:(NSTimeZone *)timeZone nameComponents:(NSArray *)nameComponents;
- (void)sortZones;
- (void)setDate:(NSDate *)date;

@property (nonatomic) NSArray *timeZoneWrappers;

@end
```

[Next](3SimpleIndexedTableView-SimpleIndexedTableView-APLAppDelegate.h.md)[Previous](Shared%20Model%20Wrappers-APLTimeZoneWrapper.h.md)

