---
title: EKReminderSuite
apple_id: TP40015203
resource_type: Sample Code
platform: iOS
topic: null
technology: null
published: '2015-11-13'
source_url: https://developer.apple.com/library/archive/samplecode/EKReminderSuite/Listings/EKLocationReminders_EKLocationReminders_LocationReminder_m.html
archived_at: '2026-07-18T03:07:29.297074Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [EKReminderSuite](EKReminderSuite.md)


[Next](EKLocationReminders-EKLocationReminders-MyAnnotation.h.md)[Previous](EKLocationReminders-EKLocationReminders-AppDelegate.m.md)

# EKLocationReminders/EKLocationReminders/LocationReminder.m

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Model class representing a location reminder.
 */

#import "LocationReminder.h"

@implementation LocationReminder


-(instancetype)init
{
    self = [self initWithTitle:nil proximity:nil structureLocation:nil];
    if (self != nil)
    {
    }
    return self;
}


-(instancetype)initWithTitle:(NSString *)name proximity:(NSString *)proximity structureLocation:(EKStructuredLocation *)location
{
    self = [super init];
    if(self != nil)
    {
        _title = name;
        _proximity = proximity;
        _structuredLocation = location;
    }
    return self;
}

@end
```

[Next](EKLocationReminders-EKLocationReminders-MyAnnotation.h.md)[Previous](EKLocationReminders-EKLocationReminders-AppDelegate.m.md)

