---
title: EKReminderSuite
apple_id: TP40015203
resource_type: Sample Code
platform: iOS
topic: null
technology: null
published: '2015-11-13'
source_url: https://developer.apple.com/library/archive/samplecode/EKReminderSuite/Listings/EKTimedReminders_EKTimedReminders_TimedReminderStore_m.html
archived_at: '2026-07-18T03:07:31.083691Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [EKReminderSuite](EKReminderSuite.md)


[Next](EKTimedReminders-EKTimedReminders-Checkbox.m.md)[Previous](EKTimedReminders-EKTimedReminders-AppDelegate.m.md)

# EKTimedReminders/EKTimedReminders/TimedReminderStore.m

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 An EKRSReminderStore subclass that shows how to create recurring timed-based reminders using EKReminder,
         EKAlarm, and EKRecurrenceRule.
 */

#import "EKRSConstants.h"
#import "TimedReminderStore.h"
#import "EKRSReminderStoreUtilities.h"

@implementation TimedReminderStore

+(TimedReminderStore *)sharedInstance
{
    static dispatch_once_t onceToken;
    static TimedReminderStore * timedReminderStoreSharedInstance;

    dispatch_once(&onceToken, ^{
        timedReminderStoreSharedInstance = [[TimedReminderStore alloc] init];
    });
    return timedReminderStoreSharedInstance;
}


#pragma mark - Create Timed-Based Reminder

// Create a timed-based reminder
-(void)createTimedReminder:(TimedReminder *)reminder
{
    EKReminder *myReminder = [EKReminder reminderWithEventStore:self.eventStore];
    myReminder.title = reminder.title;
    myReminder.calendar = self.calendar;
    myReminder.priority = [myReminder priorityMatchingName:reminder.priority];

    // Create the date components of the reminder's start date components
    NSCalendar *gregorian = [[NSCalendar alloc] initWithCalendarIdentifier:NSCalendarIdentifierGregorian];
    NSUInteger unitFlags = NSCalendarUnitSecond | NSCalendarUnitMinute | NSCalendarUnitHour | NSCalendarUnitDay | NSCalendarUnitMonth | NSCalendarUnitYear;
    NSDateComponents *dateComponents = [gregorian components:unitFlags fromDate:reminder.startDate];
    dateComponents.timeZone = myReminder.timeZone;


    // For iOS apps, EventKit requires a start date if a due date was set
    myReminder.startDateComponents = dateComponents;
    myReminder.dueDateComponents = dateComponents;

    // Create a recurrence rule if the reminder repeats itself over a given period of time
    if (![reminder.frequency isEqualToString:EKRSFrequencyNever])
    {
        EKRecurrenceRule *rule  = [[EKRecurrenceRule alloc] init];
        // Fetch the recurrence rule matching the reminder's frequency, then apply it to myReminder
        [myReminder addRecurrenceRule:[rule recurrenceRuleMatchingFrequency:reminder.frequency]];
    }

    // Create an alarm that will fire at a specific date and time
    EKAlarm *alarm = [EKAlarm alarmWithAbsoluteDate:reminder.startDate];
    // Attach an alarm to the reminder
    [myReminder addAlarm:alarm];

    // Attempt to save the reminder
    [self save:myReminder];
}

@end
```

[Next](EKTimedReminders-EKTimedReminders-Checkbox.m.md)[Previous](EKTimedReminders-EKTimedReminders-AppDelegate.m.md)

