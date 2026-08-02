---
title: EKReminderSuite
apple_id: TP40015203
resource_type: Sample Code
platform: iOS
topic: null
technology: null
published: '2015-11-13'
source_url: https://developer.apple.com/library/archive/samplecode/EKReminderSuite/Listings/EKTimedReminders_EKTimedReminders_TimedReminderStore_h.html
archived_at: '2026-07-18T03:07:31.045861Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [EKReminderSuite](EKReminderSuite.md)


[Next](EKTimedReminders-EKTimedReminders-RepeatViewController.h.md)[Previous](EKTimedReminders-EKTimedReminders-CustomCell.m.md)

# EKTimedReminders/EKTimedReminders/TimedReminderStore.h

```objc
/*

 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 An EKRSReminderStore subclass that shows how to create recurring timed-based reminders using EKReminder,
         EKAlarm, and EKRecurrenceRule.

 */

#import "TimedReminder.h"
#import "EKRSReminderStore.h"

@interface TimedReminderStore : EKRSReminderStore
+(TimedReminderStore *)sharedInstance;
-(void)createTimedReminder:(TimedReminder *)reminder;

@end
```

[Next](EKTimedReminders-EKTimedReminders-RepeatViewController.h.md)[Previous](EKTimedReminders-EKTimedReminders-CustomCell.m.md)

