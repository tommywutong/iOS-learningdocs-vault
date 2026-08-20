---
title: EKReminderSuite
apple_id: TP40015203
resource_type: Sample Code
platform: iOS
topic: null
technology: null
published: '2015-11-13'
source_url: https://developer.apple.com/library/archive/samplecode/EKReminderSuite/Listings/EKTimedReminders_EKTimedReminders_TimedReminder_h.html
archived_at: '2026-07-18T03:07:31.127686Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [EKReminderSuite](EKReminderSuite.md)


[Next](EKTimedReminders-EKTimedReminders-CustomCell.m.md)[Previous](EKTimedReminders-ReadMe.md.md)

# EKTimedReminders/EKTimedReminders/TimedReminder.h

```objc
/*

 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Model class representing a timed-based reminder.

 */

@interface TimedReminder : NSObject
// Reminder's title
@property (nonatomic, copy) NSString *title;
// Reminder's priority
@property (nonatomic, copy) NSString *priority;
// Reminder's recurrence frequency
@property (nonatomic, copy) NSString *frequency;
// Reminder's start date
@property (nonatomic, copy) NSDate *startDate;

-(instancetype)initWithTitle:(NSString *)title startDate: (NSDate *)startDate frequency:(NSString *)frequency priority: (NSString *)priority NS_DESIGNATED_INITIALIZER;

@end
```

[Next](EKTimedReminders-EKTimedReminders-CustomCell.m.md)[Previous](EKTimedReminders-ReadMe.md.md)

