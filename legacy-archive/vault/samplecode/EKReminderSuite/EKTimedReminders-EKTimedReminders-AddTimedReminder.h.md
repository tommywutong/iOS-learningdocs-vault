---
title: EKReminderSuite
apple_id: TP40015203
resource_type: Sample Code
platform: iOS
topic: null
technology: null
published: '2015-11-13'
source_url: https://developer.apple.com/library/archive/samplecode/EKReminderSuite/Listings/EKTimedReminders_EKTimedReminders_AddTimedReminder_h.html
archived_at: '2026-07-18T03:07:30.094529Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [EKReminderSuite](EKReminderSuite.md)


[Next](EKTimedReminders-EKTimedReminders-RepeatViewController.m.md)[Previous](EKTimedReminders-EKTimedReminders-CompletedReminders.m.md)

# EKTimedReminders/EKTimedReminders/AddTimedReminder.h

```objc
/*

 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This view controller allows you to enter the title, priority, and alarm (time and frequency) information for a new reminder.

 */

#import "TimedReminder.h"

@interface AddTimedReminder : UITableViewController
// Used to pass back the user input to the AddTimedReminder view controller
@property (nonatomic, strong) TimedReminder *reminder;

@end
```

[Next](EKTimedReminders-EKTimedReminders-RepeatViewController.m.md)[Previous](EKTimedReminders-EKTimedReminders-CompletedReminders.m.md)

