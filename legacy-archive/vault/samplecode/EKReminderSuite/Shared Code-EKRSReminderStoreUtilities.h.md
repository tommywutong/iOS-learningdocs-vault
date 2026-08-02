---
title: EKReminderSuite
apple_id: TP40015203
resource_type: Sample Code
platform: iOS
topic: null
technology: null
published: '2015-11-13'
source_url: https://developer.apple.com/library/archive/samplecode/EKReminderSuite/Listings/Shared_Code_EKRSReminderStoreUtilities_h.html
archived_at: '2026-07-18T03:07:31.932981Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [EKReminderSuite](EKReminderSuite.md)


[Next](Shared%20Code-EKRSReminderStore.m.md)[Previous](Shared%20Code-EKRSHelperClass.m.md)

# Shared Code/EKRSReminderStoreUtilities.h

```objc
/*

 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This class creates categories for the EKAlarm, EKRecurrenceRule, and EKReminder classes.

 */

#pragma mark - EKAlarm Additions
@interface EKAlarm (AlarmAdditions)
-(EKAlarmProximity)proximityMatchingName:(NSString *)name;
-(NSString *)nameMatchingProximity:(EKAlarmProximity)proximity;

@end


#pragma mark - EKRecurrenceRule Additions
@interface EKRecurrenceRule (RecurrenceRuleAdditions)
-(EKRecurrenceFrequency)frequencyMatchingName:(NSString *)name;
-(NSString *)nameMatchingFrequency:(EKRecurrenceFrequency)frequency;

-(NSUInteger)intervalMatchingFrequency:(NSString *)frequency;

-(EKRecurrenceRule *)recurrenceRuleMatchingFrequency:(NSString *)frequency;
-(NSString *)nameMatchingRecurrenceRuleWithFrequency:(EKRecurrenceFrequency)frequency interval:(NSInteger)interval;

@end


#pragma mark - EKReminder Additions
@interface EKReminder (EKReminderAdditions)
-(NSInteger)priorityMatchingName:(NSString *)name;
-(NSString *)symbolMatchingPriority:(NSInteger)priority;

@end
```

[Next](Shared%20Code-EKRSReminderStore.m.md)[Previous](Shared%20Code-EKRSHelperClass.m.md)

