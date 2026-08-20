---
title: EKReminderSuite
apple_id: TP40015203
resource_type: Sample Code
platform: iOS
topic: null
technology: null
published: '2015-11-13'
source_url: https://developer.apple.com/library/archive/samplecode/EKReminderSuite/Listings/EKTimedReminders_EKTimedReminders_TimedReminder_m.html
archived_at: '2026-07-18T03:07:31.192460Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [EKReminderSuite](EKReminderSuite.md)


[Next](EKTimedReminders-EKTimedReminders-PastDueReminders.h.md)[Previous](EKTimedReminders-EKTimedReminders-main.m.md)

# EKTimedReminders/EKTimedReminders/TimedReminder.m

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Model class representing a timed-based reminder.
 */

#import "TimedReminder.h"

@implementation TimedReminder

-(instancetype)init
{
    self = [self initWithTitle:nil startDate:nil frequency:nil priority:nil];
    if (self != nil)
    {
    }
    return self;
}


-(instancetype)initWithTitle:(NSString *)title startDate:(NSDate *)startDate frequency:(NSString *)frequency priority:(NSString *)priority
{
    self = [super init];
    if(self != nil)
    {
        _title = title;
        _startDate = startDate;
        _frequency = frequency;
        _priority = priority;
    }
    return self;
}

@end
```

[Next](EKTimedReminders-EKTimedReminders-PastDueReminders.h.md)[Previous](EKTimedReminders-EKTimedReminders-main.m.md)

