---
title: EKReminderSuite
apple_id: TP40015203
resource_type: Sample Code
platform: iOS
topic: null
technology: null
published: '2015-11-13'
source_url: https://developer.apple.com/library/archive/samplecode/EKReminderSuite/Listings/Shared_Code_EKRSConstants_m.html
archived_at: '2026-07-18T03:07:31.699318Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [EKReminderSuite](EKReminderSuite.md)


[Next](EKLocationReminders-ReadMe.md.md)[Previous](Shared%20Code-EKRSHelperClass.h.md)

# Shared Code/EKRSConstants.m

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Constants used by various classes in the EKReminderSuite project.
 */

#import "EKRSConstants.h"

#pragma mark - EKRSReminderStore

NSString * const EKRSAccessDeniedNotification = @"EKRSAccessDeniedNotification";
NSString * const EKRSAccessGrantedNotification = @"EKRSAccessGrantedNotification";
NSString * const EKRSLocationRemindersNotification = @"EKRSIncompleteRemindersNotification";
NSString * const EKRSCompletedRemindersNotification = @"EKRSCompletedRemindersNotification";
NSString * const EKRSPastDueRemindersNotification = @"EKRSPastDueRemindersNotification";
NSString * const EKRSUpcomingRemindersNotification = @"EKRSUpcomingRemindersNotification";
NSString * const EKRSRefreshDataNotification = @"EKRSRefreshDataNotification";
NSString * const EKRSFailureNotification = @"EKRSFailureNotification";


#pragma mark - EKRSReminderStoreUtilities

NSString * const EKRSFrequencyNever = @"Never";
NSString * const EKRSFrequencyDaily = @"Daily";
NSString * const EKRSFrequencyWeekly = @"Weekly";
NSString * const EKRSFrequencyYearly = @"Yearly";
NSString * const EKRSFrequencyMonthly = @"Monthly";
NSString * const EKRSFrequencyBiweekly = @"Biweekly";

NSString * const EKRSAlarmLeaving = @"Leaving";
NSString * const EKRSAlarmArriving = @"Arriving";

NSString * const EKRSPriorityLow = @"Low";
NSString * const EKRSPriorityHigh = @"High";
NSString * const EKRSPriorityNone = @"None";
NSString * const EKRSPriorityMedium = @"Medium";

NSString * const EKRSSymbolPriorityLow = @"!";
NSString * const EKRSSymbolPriorityHigh = @"!!!";
NSString * const EKRSSymbolPriorityMedium = @"!!";

#pragma mark - TimedTabBarController

NSString * const TTBAccessGrantedNotification = @"TTBAccessGrantedNotification";
NSString * const TTBUpcomingRemindersNotification = @"TTBUpcomingRemindersNotification";
NSString * const TTBPastDueRemindersNotification = @"TTBPastDueRemindersNotification";
NSString * const TTBCompletedRemindersNotification = @"TTBCompletedRemindersNotification";


#pragma mark - LocationTabBarController

NSString * const LTBAccessGrantedNotification = @"LTBAccessGrantedNotification";
NSString * const LTBRemindersFetchedNotification = @"LTBRemindersFetchedNotification";

#pragma mark

NSString *const EKRSTitle = @"title";
NSString *const EKRSLocationRadius = @"radius";
NSString *const EKRSLocationProximity = @"proximity";
NSString *const EKRSDescription = @"description";
```

[Next](EKLocationReminders-ReadMe.md.md)[Previous](Shared%20Code-EKRSHelperClass.h.md)

