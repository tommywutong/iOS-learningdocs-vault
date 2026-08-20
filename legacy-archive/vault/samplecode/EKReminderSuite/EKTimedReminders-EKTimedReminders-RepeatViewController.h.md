---
title: EKReminderSuite
apple_id: TP40015203
resource_type: Sample Code
platform: iOS
topic: null
technology: null
published: '2015-11-13'
source_url: https://developer.apple.com/library/archive/samplecode/EKReminderSuite/Listings/EKTimedReminders_EKTimedReminders_RepeatViewController_h.html
archived_at: '2026-07-18T03:07:30.877074Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [EKReminderSuite](EKReminderSuite.md)


[Next](EKTimedReminders-EKTimedReminders-UpcomingReminders.h.md)[Previous](EKTimedReminders-EKTimedReminders-TimedReminderStore.h.md)

# EKTimedReminders/EKTimedReminders/RepeatViewController.h

```objc
/*

 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This view controller allows you to select a recurrence frequency for a reminder, which is Never, Daily, Weekly, Biweekly, Monthly, or Yearly.
         It passes the selected frequency to the AddTimedReminder view controller via the prepareForSegue:sender: method.

 */

@interface RepeatViewController : UITableViewController
// Keep track of the displayed frequency
@property(nonatomic, copy) NSString *displayedFrequency;

@end
```

[Next](EKTimedReminders-EKTimedReminders-UpcomingReminders.h.md)[Previous](EKTimedReminders-EKTimedReminders-TimedReminderStore.h.md)

