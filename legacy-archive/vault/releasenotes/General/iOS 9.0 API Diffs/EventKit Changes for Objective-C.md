---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/EventKit.html
archived_at: '2026-07-18T02:56:32.699174Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# EventKit Changes for Objective-C

### EventKit

#### EKCalendar.h

Modified [EKCalendar.source](https://developer.apple.com/documentation/eventkit/ekcalendar/1507288-source)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) EKSource *source ``` |
| To | ``` @property(nonatomic, strong, nonnull) EKSource *source ``` |

#### EKCalendarItem.h

Modified [EKCalendarItem.alarms](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507211-alarms)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *alarms ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<EKAlarm *> *alarms ``` |

Modified [EKCalendarItem.attendees](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507140-attendees)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *attendees ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSArray<__kindof EKParticipant *> *attendees ``` |

Modified [EKCalendarItem.calendar](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507169-calendar)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) EKCalendar *calendar ``` |
| To | ``` @property(nonatomic, strong, nonnull) EKCalendar *calendar ``` |

Modified [EKCalendarItem.recurrenceRules](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507135-recurrencerules)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *recurrenceRules ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<EKRecurrenceRule *> *recurrenceRules ``` |

#### EKError.h

Added [EKErrorEventStoreNotAuthorized](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerroreventstorenotauthorized)Added [EKErrorOSNotSupported](https://developer.apple.com/documentation/eventkit/ekerror/code/osnotsupported)Added [EKErrorProcedureAlarmsNotMutable](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerrorprocedurealarmsnotmutable)Added [EKErrorSourceDoesNotAllowEvents](https://developer.apple.com/documentation/eventkit/ekerror/code/sourcedoesnotallowevents)

#### EKEvent.h

Added [EKEvent.birthdayContactIdentifier](https://developer.apple.com/documentation/eventkit/ekevent/1507349-birthdaycontactidentifier)Added [EKEvent.occurrenceDate](https://developer.apple.com/documentation/eventkit/ekevent/1507244-occurrencedate)Added [EKEvent.structuredLocation](https://developer.apple.com/documentation/eventkit/ekevent/1507185-structuredlocation)Modified [EKEvent.birthdayPersonID](https://developer.apple.com/documentation/eventkit/ekevent/1615845-birthdaypersonid)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

#### EKEventStore.h

Added [-[EKEventStore init]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507252-init)Modified [-[EKEventStore calendarItemsWithExternalIdentifier:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507281-calendaritems)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)calendarItemsWithExternalIdentifier:(NSString *)externalIdentifier ``` |
| To | ``` - (NSArray<EKCalendarItem *> * _Nonnull)calendarItemsWithExternalIdentifier:(NSString * _Nonnull)externalIdentifier ``` |

Modified [EKEventStore.calendars](https://developer.apple.com/documentation/eventkit/ekeventstore/1623680-calendars)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *calendars ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<EKCalendar *> *calendars ``` |

Modified [-[EKEventStore calendarsForEntityType:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507128-calendars)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)calendarsForEntityType:(EKEntityType)entityType ``` |
| To | ``` - (NSArray<EKCalendar *> * _Nonnull)calendarsForEntityType:(EKEntityType)entityType ``` |

Modified [-[EKEventStore eventsMatchingPredicate:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507183-events)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)eventsMatchingPredicate:(NSPredicate *)predicate ``` |
| To | ``` - (NSArray<EKEvent *> * _Nonnull)eventsMatchingPredicate:(NSPredicate * _Nonnull)predicate ``` |

Modified [-[EKEventStore fetchRemindersMatchingPredicate:completion:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507500-fetchremindersmatchingpredicate)

|  | Declaration |
| --- | --- |
| From | ``` - (id)fetchRemindersMatchingPredicate:(NSPredicate *)predicate completion:(void (^)(NSArray *reminders))completion ``` |
| To | ``` - (id _Nonnull)fetchRemindersMatchingPredicate:(NSPredicate * _Nonnull)predicate completion:(void (^ _Nonnull)(NSArray<EKReminder *> * _Nullable reminders))completion ``` |

Modified [-[EKEventStore predicateForCompletedRemindersWithCompletionDateStarting:ending:calendars:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507447-predicateforcompletedreminders)

|  | Declaration |
| --- | --- |
| From | ``` - (NSPredicate *)predicateForCompletedRemindersWithCompletionDateStarting:(NSDate *)startDate ending:(NSDate *)endDate calendars:(NSArray *)calendars ``` |
| To | ``` - (NSPredicate * _Nonnull)predicateForCompletedRemindersWithCompletionDateStarting:(NSDate * _Nullable)startDate ending:(NSDate * _Nullable)endDate calendars:(NSArray<EKCalendar *> * _Nullable)calendars ``` |

Modified [-[EKEventStore predicateForEventsWithStartDate:endDate:calendars:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507479-predicateforevents)

|  | Declaration |
| --- | --- |
| From | ``` - (NSPredicate *)predicateForEventsWithStartDate:(NSDate *)startDate endDate:(NSDate *)endDate calendars:(NSArray *)calendars ``` |
| To | ``` - (NSPredicate * _Nonnull)predicateForEventsWithStartDate:(NSDate * _Nonnull)startDate endDate:(NSDate * _Nonnull)endDate calendars:(NSArray<EKCalendar *> * _Nullable)calendars ``` |

Modified [-[EKEventStore predicateForIncompleteRemindersWithDueDateStarting:ending:calendars:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507143-predicateforincompletereminders)

|  | Declaration |
| --- | --- |
| From | ``` - (NSPredicate *)predicateForIncompleteRemindersWithDueDateStarting:(NSDate *)startDate ending:(NSDate *)endDate calendars:(NSArray *)calendars ``` |
| To | ``` - (NSPredicate * _Nonnull)predicateForIncompleteRemindersWithDueDateStarting:(NSDate * _Nullable)startDate ending:(NSDate * _Nullable)endDate calendars:(NSArray<EKCalendar *> * _Nullable)calendars ``` |

Modified [-[EKEventStore predicateForRemindersInCalendars:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507086-predicateforreminders)

|  | Declaration |
| --- | --- |
| From | ``` - (NSPredicate *)predicateForRemindersInCalendars:(NSArray *)calendars ``` |
| To | ``` - (NSPredicate * _Nonnull)predicateForRemindersInCalendars:(NSArray<EKCalendar *> * _Nullable)calendars ``` |

Modified [EKEventStore.sources](https://developer.apple.com/documentation/eventkit/ekeventstore/1507315-sources)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)sources ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<EKSource *> *sources ``` |

#### EKObject.h

Removed [-[EKObject isNew]](https://developer.apple.com/documentation/eventkit/ekobject/1812546-isnew)Added [EKObject.new](https://developer.apple.com/documentation/eventkit/ekobject/1507402-isnew)Modified [EKObject.hasChanges](https://developer.apple.com/documentation/eventkit/ekobject/1507333-haschanges)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)hasChanges ``` |
| To | ``` @property(nonatomic, readonly) BOOL hasChanges ``` |

#### EKParticipant.h

Removed EKParticipant.isCurrentUserAdded [EKParticipant.contactPredicate](https://developer.apple.com/documentation/eventkit/ekparticipant/1507163-contactpredicate)Added [EKParticipant.currentUser](https://developer.apple.com/documentation/eventkit/ekparticipant/1507248-currentuser)Modified [-[EKParticipant ABRecordWithAddressBook:]](https://developer.apple.com/documentation/eventkit/ekparticipant/1615895-abrecordwithaddressbook)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

#### EKRecurrenceDayOfWeek.h

Modified [EKRecurrenceDayOfWeek.dayOfTheWeek](https://developer.apple.com/documentation/eventkit/ekrecurrencedayofweek/1448579-dayoftheweek)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSInteger dayOfTheWeek ``` |
| To | ``` @property(nonatomic, readonly) EKWeekday dayOfTheWeek ``` |

Modified [+[EKRecurrenceDayOfWeek dayOfWeek:]](https://developer.apple.com/documentation/eventkit/ekrecurrencedayofweek/1448589-dayofweek)

|  | Declaration |
| --- | --- |
| From | ``` + (EKRecurrenceDayOfWeek *)dayOfWeek:(NSInteger)dayOfTheWeek ``` |
| To | ``` + (instancetype _Nonnull)dayOfWeek:(EKWeekday)dayOfTheWeek ``` |

Modified [+[EKRecurrenceDayOfWeek dayOfWeek:weekNumber:]](https://developer.apple.com/documentation/eventkit/ekrecurrencedayofweek/1448591-init)

|  | Declaration |
| --- | --- |
| From | ``` + (EKRecurrenceDayOfWeek *)dayOfWeek:(NSInteger)dayOfTheWeek weekNumber:(NSInteger)weekNumber ``` |
| To | ``` + (instancetype _Nonnull)dayOfWeek:(EKWeekday)dayOfTheWeek weekNumber:(NSInteger)weekNumber ``` |

Modified [-[EKRecurrenceDayOfWeek initWithDayOfTheWeek:weekNumber:]](https://developer.apple.com/documentation/eventkit/ekrecurrencedayofweek/1448581-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithDayOfTheWeek:(NSInteger)dayOfTheWeek weekNumber:(NSInteger)weekNumber ``` |
| To | ``` - (id _Nonnull)initWithDayOfTheWeek:(EKWeekday)dayOfTheWeek weekNumber:(NSInteger)weekNumber ``` |

#### EKRecurrenceEnd.h

Modified [+[EKRecurrenceEnd recurrenceEndWithEndDate:]](https://developer.apple.com/documentation/eventkit/ekrecurrenceend/1415644-init)

|  | Declaration |
| --- | --- |
| From | ``` + (id)recurrenceEndWithEndDate:(NSDate *)endDate ``` |
| To | ``` + (instancetype _Nonnull)recurrenceEndWithEndDate:(NSDate * _Nonnull)endDate ``` |

Modified [+[EKRecurrenceEnd recurrenceEndWithOccurrenceCount:]](https://developer.apple.com/documentation/eventkit/ekrecurrenceend/1415640-init)

|  | Declaration |
| --- | --- |
| From | ``` + (id)recurrenceEndWithOccurrenceCount:(NSUInteger)occurrenceCount ``` |
| To | ``` + (instancetype _Nonnull)recurrenceEndWithOccurrenceCount:(NSUInteger)occurrenceCount ``` |

#### EKRecurrenceRule.h

Modified [EKRecurrenceRule.daysOfTheMonth](https://developer.apple.com/documentation/eventkit/ekrecurrencerule/1507410-daysofthemonth)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *daysOfTheMonth ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSArray<NSNumber *> *daysOfTheMonth ``` |

Modified [EKRecurrenceRule.daysOfTheWeek](https://developer.apple.com/documentation/eventkit/ekrecurrencerule/1507538-daysoftheweek)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *daysOfTheWeek ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSArray<EKRecurrenceDayOfWeek *> *daysOfTheWeek ``` |

Modified [EKRecurrenceRule.daysOfTheYear](https://developer.apple.com/documentation/eventkit/ekrecurrencerule/1507439-daysoftheyear)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *daysOfTheYear ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSArray<NSNumber *> *daysOfTheYear ``` |

Modified [-[EKRecurrenceRule initRecurrenceWithFrequency:interval:daysOfTheWeek:daysOfTheMonth:monthsOfTheYear:weeksOfTheYear:daysOfTheYear:setPositions:end:]](https://developer.apple.com/documentation/eventkit/ekrecurrencerule/1507320-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initRecurrenceWithFrequency:(EKRecurrenceFrequency)type interval:(NSInteger)interval daysOfTheWeek:(NSArray *)days daysOfTheMonth:(NSArray *)monthDays monthsOfTheYear:(NSArray *)months weeksOfTheYear:(NSArray *)weeksOfTheYear daysOfTheYear:(NSArray *)daysOfTheYear setPositions:(NSArray *)setPositions end:(EKRecurrenceEnd *)end ``` |
| To | ``` - (instancetype _Nonnull)initRecurrenceWithFrequency:(EKRecurrenceFrequency)type interval:(NSInteger)interval daysOfTheWeek:(NSArray<EKRecurrenceDayOfWeek *> * _Nullable)days daysOfTheMonth:(NSArray<NSNumber *> * _Nullable)monthDays monthsOfTheYear:(NSArray<NSNumber *> * _Nullable)months weeksOfTheYear:(NSArray<NSNumber *> * _Nullable)weeksOfTheYear daysOfTheYear:(NSArray<NSNumber *> * _Nullable)daysOfTheYear setPositions:(NSArray<NSNumber *> * _Nullable)setPositions end:(EKRecurrenceEnd * _Nullable)end ``` |

Modified [-[EKRecurrenceRule initRecurrenceWithFrequency:interval:end:]](https://developer.apple.com/documentation/eventkit/ekrecurrencerule/1507273-initrecurrencewithfrequency)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initRecurrenceWithFrequency:(EKRecurrenceFrequency)type interval:(NSInteger)interval end:(EKRecurrenceEnd *)end ``` |
| To | ``` - (instancetype _Nonnull)initRecurrenceWithFrequency:(EKRecurrenceFrequency)type interval:(NSInteger)interval end:(EKRecurrenceEnd * _Nullable)end ``` |

Modified [EKRecurrenceRule.monthsOfTheYear](https://developer.apple.com/documentation/eventkit/ekrecurrencerule/1507449-monthsoftheyear)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *monthsOfTheYear ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSArray<NSNumber *> *monthsOfTheYear ``` |

Modified [EKRecurrenceRule.setPositions](https://developer.apple.com/documentation/eventkit/ekrecurrencerule/1507378-setpositions)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *setPositions ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSArray<NSNumber *> *setPositions ``` |

Modified [EKRecurrenceRule.weeksOfTheYear](https://developer.apple.com/documentation/eventkit/ekrecurrencerule/1507400-weeksoftheyear)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *weeksOfTheYear ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSArray<NSNumber *> *weeksOfTheYear ``` |

#### EKReminder.h

Modified [EKReminder.priority](https://developer.apple.com/documentation/eventkit/ekreminder/1507173-priority)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic) NSInteger priority ``` |
| To | ``` @property(nonatomic) NSUInteger priority ``` |

#### EKSource.h

Modified [EKSource.calendars](https://developer.apple.com/documentation/eventkit/eksource/1624237-calendars)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSSet *calendars ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSSet<EKCalendar *> *calendars ``` |

Modified [-[EKSource calendarsForEntityType:]](https://developer.apple.com/documentation/eventkit/eksource/1507387-calendarsforentitytype)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSet *)calendarsForEntityType:(EKEntityType)entityType ``` |
| To | ``` - (NSSet<EKCalendar *> * _Nonnull)calendarsForEntityType:(EKEntityType)entityType ``` |

#### EKStructuredLocation.h

Added [+[EKStructuredLocation locationWithMapItem:]](https://developer.apple.com/documentation/eventkit/ekstructuredlocation/1507493-init)Modified [EKStructuredLocation.geoLocation](https://developer.apple.com/documentation/eventkit/ekstructuredlocation/1507110-geolocation)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) CLLocation *geoLocation ``` |
| To | ``` @property(nonatomic, strong, nullable) CLLocation *geoLocation ``` |

Modified [+[EKStructuredLocation locationWithTitle:]](https://developer.apple.com/documentation/eventkit/ekstructuredlocation/1507366-init)

|  | Declaration |
| --- | --- |
| From | ``` + (EKStructuredLocation *)locationWithTitle:(NSString *)title ``` |
| To | ``` + (instancetype _Nonnull)locationWithTitle:(NSString * _Nonnull)title ``` |

Modified [EKStructuredLocation.title](https://developer.apple.com/documentation/eventkit/ekstructuredlocation/1507137-title)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSString *title ``` |
| To | ``` @property(nonatomic, strong, nonnull) NSString *title ``` |

#### EKTypes.h

Added [EKAlarmType](https://developer.apple.com/documentation/eventkit/ekalarmtype)Added [EKAlarmTypeAudio](https://developer.apple.com/documentation/eventkit/ekalarmtype/audio)Added [EKAlarmTypeDisplay](https://developer.apple.com/documentation/eventkit/ekalarmtype/ekalarmtypedisplay)Added [EKAlarmTypeEmail](https://developer.apple.com/documentation/eventkit/ekalarmtype/email)Added [EKAlarmTypeProcedure](https://developer.apple.com/documentation/eventkit/ekalarmtype/procedure)Added [EKParticipantScheduleStatus](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus)Added [EKParticipantScheduleStatusCannotDeliver](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/ekparticipantschedulestatuscannotdeliver)Added [EKParticipantScheduleStatusDelivered](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/ekparticipantschedulestatusdelivered)Added [EKParticipantScheduleStatusDeliveryFailed](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/ekparticipantschedulestatusdeliveryfailed)Added [EKParticipantScheduleStatusNone](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/none)Added [EKParticipantScheduleStatusNoPrivileges](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/ekparticipantschedulestatusnoprivileges)Added [EKParticipantScheduleStatusPending](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/ekparticipantschedulestatuspending)Added [EKParticipantScheduleStatusRecipientNotAllowed](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/recipientnotallowed)Added [EKParticipantScheduleStatusRecipientNotRecognized](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/ekparticipantschedulestatusrecipientnotrecognized)Added [EKParticipantScheduleStatusSent](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/sent)Added [EKReminderPriority](https://developer.apple.com/documentation/eventkit/ekreminderpriority)Added [EKReminderPriorityHigh](https://developer.apple.com/documentation/eventkit/ekreminderpriority/ekreminderpriorityhigh)Added [EKReminderPriorityLow](https://developer.apple.com/documentation/eventkit/ekreminderpriority/ekreminderprioritylow)Added [EKReminderPriorityMedium](https://developer.apple.com/documentation/eventkit/ekreminderpriority/ekreminderprioritymedium)Added [EKReminderPriorityNone](https://developer.apple.com/documentation/eventkit/ekreminderpriority/ekreminderprioritynone)Added [EKWeekday](https://developer.apple.com/documentation/eventkit/ekweekday)Added [EKWeekdayFriday](https://developer.apple.com/documentation/eventkit/ekweekday/ekweekdayfriday)Added [EKWeekdayMonday](https://developer.apple.com/documentation/eventkit/ekweekday/ekweekdaymonday)Added [EKWeekdaySaturday](https://developer.apple.com/documentation/eventkit/ekweekday/saturday)Added [EKWeekdaySunday](https://developer.apple.com/documentation/eventkit/ekweekday/ekweekdaysunday)Added [EKWeekdayThursday](https://developer.apple.com/documentation/eventkit/ekweekday/thursday)Added [EKWeekdayTuesday](https://developer.apple.com/documentation/eventkit/ekweekday/ekweekdaytuesday)Added [EKWeekdayWednesday](https://developer.apple.com/documentation/eventkit/ekweekday/ekweekdaywednesday)Modified [EKFriday](https://developer.apple.com/documentation/eventkit/ekweekday/1451835-ekfriday)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [EKMonday](https://developer.apple.com/documentation/eventkit/ekweekday/ekmonday)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [EKSaturday](https://developer.apple.com/documentation/eventkit/ekweekday/eksaturday)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [EKSunday](https://developer.apple.com/documentation/eventkit/ekweekday/eksunday)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [EKThursday](https://developer.apple.com/documentation/eventkit/ekweekday/1451894-ekthursday)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [EKTuesday](https://developer.apple.com/documentation/eventkit/ekweekday/1451993-ektuesday)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [EKWednesday](https://developer.apple.com/documentation/eventkit/ekweekday/1451817-ekwednesday)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
