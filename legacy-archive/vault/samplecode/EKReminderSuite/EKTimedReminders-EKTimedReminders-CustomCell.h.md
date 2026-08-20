---
title: EKReminderSuite
apple_id: TP40015203
resource_type: Sample Code
platform: iOS
topic: null
technology: null
published: '2015-11-13'
source_url: https://developer.apple.com/library/archive/samplecode/EKReminderSuite/Listings/EKTimedReminders_EKTimedReminders_CustomCell_h.html
archived_at: '2026-07-18T03:07:30.657970Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [EKReminderSuite](EKReminderSuite.md)


[Next](EKTimedReminders-EKTimedReminders-UpcomingReminders.m.md)[Previous](EKTimedReminders-EKTimedReminders-AddTimedReminder.m.md)

# EKTimedReminders/EKTimedReminders/CustomCell.h

```objc
/*

 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A custom UITableViewCell that contains a Checkbox control in addition to its accessory control.

 */

#import "Checkbox.h"

@interface CustomCell : UITableViewCell
@property (weak, nonatomic) IBOutlet UILabel *title;
@property (weak, nonatomic) IBOutlet UILabel *priority;
@property (weak, nonatomic) IBOutlet UILabel *dateAndFrequency;
@property (weak, nonatomic) IBOutlet Checkbox *checkBox;

@end
```

[Next](EKTimedReminders-EKTimedReminders-UpcomingReminders.m.md)[Previous](EKTimedReminders-EKTimedReminders-AddTimedReminder.m.md)

