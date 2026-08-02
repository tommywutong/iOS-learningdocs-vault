---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/EventKit.html
archived_at: '2026-07-18T02:52:24.194843Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# EventKit Changes

## EventKit

Added EKCalendar.colorAdded EKParticipant.ABPersonInAddressBook(ABAddressBook!) -> ABPerson!Modified EKAlarm

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKAlarm.absoluteDate

|  | Declaration |
| --- | --- |
| From | ``` var absoluteDate: NSDate! ``` |
| To | ``` @NSCopying var absoluteDate: NSDate! ``` |

Modified EKAlarm.init(absoluteDate: NSDate!)

|  | Declaration |
| --- | --- |
| From | ``` init(absoluteDate date: NSDate!) -> EKAlarm ``` |
| To | ``` init!(absoluteDate date: NSDate!) -> EKAlarm ``` |

Modified EKAlarm.emailAddress

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKAlarm.init(relativeOffset: NSTimeInterval)

|  | Declaration |
| --- | --- |
| From | ``` init(relativeOffset offset: NSTimeInterval) -> EKAlarm ``` |
| To | ``` init!(relativeOffset offset: NSTimeInterval) -> EKAlarm ``` |

Modified EKAlarm.soundName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKAlarm.structuredLocation

|  | Declaration |
| --- | --- |
| From | ``` var structuredLocation: EKStructuredLocation! ``` |
| To | ``` @NSCopying var structuredLocation: EKStructuredLocation! ``` |

Modified EKAlarm.type

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKAuthorizationStatus [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified EKCalendar

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKCalendar.allowedEntityTypes

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKCalendar.calendarIdentifier

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKCalendar.init(forEntityType: EKEntityType, eventStore: EKEventStore!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(forEntityType entityType: EKEntityType, eventStore eventStore: EKEventStore!) -> EKCalendar ``` | OS X 10.10 |
| To | ``` init!(forEntityType entityType: EKEntityType, eventStore eventStore: EKEventStore!) -> EKCalendar ``` | OS X 10.8 |

Modified EKCalendar.immutable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKCalendar.subscribed

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKCalendarItem

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKCalendarItem.URL

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var URL: NSURL! ``` | OS X 10.10 |
| To | ``` @NSCopying var URL: NSURL! ``` | OS X 10.8 |

Modified EKCalendarItem.calendarItemExternalIdentifier

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKCalendarItem.calendarItemIdentifier

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKCalendarItem.creationDate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKCalendarItem.hasAlarms

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKCalendarItem.hasAttendees

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKCalendarItem.hasNotes

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKCalendarItem.hasRecurrenceRules

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKCalendarItem.recurrenceRules

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKCalendarItem.timeZone

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var timeZone: NSTimeZone! ``` | OS X 10.10 |
| To | ``` @NSCopying var timeZone: NSTimeZone! ``` | OS X 10.8 |

Modified EKEvent

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKEvent.birthdayPersonUniqueID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKEvent.endDate

|  | Declaration |
| --- | --- |
| From | ``` var endDate: NSDate! ``` |
| To | ``` @NSCopying var endDate: NSDate! ``` |

Modified EKEvent.init(eventStore: EKEventStore!)

|  | Declaration |
| --- | --- |
| From | ``` init(eventStore eventStore: EKEventStore!) -> EKEvent ``` |
| To | ``` init!(eventStore eventStore: EKEventStore!) -> EKEvent ``` |

Modified EKEvent.occurrenceDate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKEvent.startDate

|  | Declaration |
| --- | --- |
| From | ``` var startDate: NSDate! ``` |
| To | ``` @NSCopying var startDate: NSDate! ``` |

Modified EKEventStore

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKEventStore.init()

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init() ``` | OS X 10.10 |
| To | ``` init!() ``` | OS X 10.9 |

Modified EKEventStore.authorizationStatusForEntityType(EKEntityType) -> EKAuthorizationStatus [class]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified EKEventStore.calendarItemWithIdentifier(String!) -> EKCalendarItem!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKEventStore.calendarItemsWithExternalIdentifier(String!) -> [AnyObject]!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKEventStore.calendarWithIdentifier(String!) -> EKCalendar!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKEventStore.calendarsForEntityType(EKEntityType) -> [AnyObject]!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKEventStore.cancelFetchRequest(AnyObject!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKEventStore.commit(NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKEventStore.defaultCalendarForNewReminders() -> EKCalendar!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKEventStore.fetchRemindersMatchingPredicate(NSPredicate!, completion:(([AnyObject]!) -> Void)!) -> AnyObject!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKEventStore.predicateForCompletedRemindersWithCompletionDateStarting(NSDate!, ending: NSDate!, calendars:[AnyObject]!) -> NSPredicate!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKEventStore.predicateForIncompleteRemindersWithDueDateStarting(NSDate!, ending: NSDate!, calendars:[AnyObject]!) -> NSPredicate!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKEventStore.predicateForRemindersInCalendars([AnyObject]!) -> NSPredicate!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKEventStore.refreshSourcesIfNecessary()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKEventStore.removeCalendar(EKCalendar!, commit: Bool, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKEventStore.removeEvent(EKEvent!, span: EKSpan, commit: Bool, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKEventStore.removeReminder(EKReminder!, commit: Bool, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKEventStore.requestAccessToEntityType(EKEntityType, completion: EKEventStoreRequestAccessCompletionHandler!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified EKEventStore.reset()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKEventStore.saveCalendar(EKCalendar!, commit: Bool, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKEventStore.saveEvent(EKEvent!, span: EKSpan, commit: Bool, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKEventStore.saveReminder(EKReminder!, commit: Bool, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKEventStore.sourceWithIdentifier(String!) -> EKSource!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKEventStore.sources() -> [AnyObject]!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKParticipant

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKParticipant.isCurrentUser

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified EKRecurrenceDayOfWeek

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKRecurrenceDayOfWeek.init(_: Int)

|  | Declaration |
| --- | --- |
| From | ``` init(_ dayOfTheWeek: Int) -> EKRecurrenceDayOfWeek ``` |
| To | ``` init!(_ dayOfTheWeek: Int) -> EKRecurrenceDayOfWeek ``` |

Modified EKRecurrenceDayOfWeek.init(_: Int, weekNumber: Int)

|  | Declaration |
| --- | --- |
| From | ``` init(_ dayOfTheWeek: Int, weekNumber weekNumber: Int) -> EKRecurrenceDayOfWeek ``` |
| To | ``` init!(_ dayOfTheWeek: Int, weekNumber weekNumber: Int) -> EKRecurrenceDayOfWeek ``` |

Modified EKRecurrenceDayOfWeek.init(dayOfTheWeek: Int, weekNumber: Int)

|  | Declaration |
| --- | --- |
| From | ``` init(dayOfTheWeek dayOfTheWeek: Int, weekNumber weekNumber: Int) ``` |
| To | ``` init!(dayOfTheWeek dayOfTheWeek: Int, weekNumber weekNumber: Int) ``` |

Modified EKRecurrenceEnd

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKRecurrenceRule

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKRecurrenceRule.recurrenceEnd

|  | Declaration |
| --- | --- |
| From | ``` var recurrenceEnd: EKRecurrenceEnd! ``` |
| To | ``` @NSCopying var recurrenceEnd: EKRecurrenceEnd! ``` |

Modified EKRecurrenceRule.init(recurrenceWithFrequency: EKRecurrenceFrequency, interval: Int, daysOfTheWeek:[AnyObject]!, daysOfTheMonth:[AnyObject]!, monthsOfTheYear:[AnyObject]!, weeksOfTheYear:[AnyObject]!, daysOfTheYear:[AnyObject]!, setPositions:[AnyObject]!, end: EKRecurrenceEnd!)

|  | Declaration |
| --- | --- |
| From | ``` init(recurrenceWithFrequency type: EKRecurrenceFrequency, interval interval: Int, daysOfTheWeek days: [AnyObject]!, daysOfTheMonth monthDays: [AnyObject]!, monthsOfTheYear months: [AnyObject]!, weeksOfTheYear weeksOfTheYear: [AnyObject]!, daysOfTheYear daysOfTheYear: [AnyObject]!, setPositions setPositions: [AnyObject]!, end end: EKRecurrenceEnd!) ``` |
| To | ``` init!(recurrenceWithFrequency type: EKRecurrenceFrequency, interval interval: Int, daysOfTheWeek days: [AnyObject]!, daysOfTheMonth monthDays: [AnyObject]!, monthsOfTheYear months: [AnyObject]!, weeksOfTheYear weeksOfTheYear: [AnyObject]!, daysOfTheYear daysOfTheYear: [AnyObject]!, setPositions setPositions: [AnyObject]!, end end: EKRecurrenceEnd!) ``` |

Modified EKRecurrenceRule.init(recurrenceWithFrequency: EKRecurrenceFrequency, interval: Int, end: EKRecurrenceEnd!)

|  | Declaration |
| --- | --- |
| From | ``` init(recurrenceWithFrequency type: EKRecurrenceFrequency, interval interval: Int, end end: EKRecurrenceEnd!) ``` |
| To | ``` init!(recurrenceWithFrequency type: EKRecurrenceFrequency, interval interval: Int, end end: EKRecurrenceEnd!) ``` |

Modified EKReminder

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKReminder.completionDate

|  | Declaration |
| --- | --- |
| From | ``` var completionDate: NSDate! ``` |
| To | ``` @NSCopying var completionDate: NSDate! ``` |

Modified EKReminder.dueDateComponents

|  | Declaration |
| --- | --- |
| From | ``` var dueDateComponents: NSDateComponents! ``` |
| To | ``` @NSCopying var dueDateComponents: NSDateComponents! ``` |

Modified EKReminder.init(eventStore: EKEventStore!)

|  | Declaration |
| --- | --- |
| From | ``` init(eventStore eventStore: EKEventStore!) -> EKReminder ``` |
| To | ``` init!(eventStore eventStore: EKEventStore!) -> EKReminder ``` |

Modified EKReminder.startDateComponents

|  | Declaration |
| --- | --- |
| From | ``` var startDateComponents: NSDateComponents! ``` |
| To | ``` @NSCopying var startDateComponents: NSDateComponents! ``` |

Modified EKSource

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKSource.calendarsForEntityType(EKEntityType) -> Set<NSObject>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func calendarsForEntityType(_ entityType: EKEntityType) -> NSSet! ``` | OS X 10.10 |
| To | ``` func calendarsForEntityType(_ entityType: EKEntityType) -> Set<NSObject>! ``` | OS X 10.8 |

Modified EKStructuredLocation

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified EKStructuredLocation.init(title: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(title title: String!) -> EKStructuredLocation ``` |
| To | ``` init!(title title: String!) -> EKStructuredLocation ``` |

Modified DATETIME_COMPONENTS_DO_NOT_USE()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified DATE_COMPONENTS_DO_NOT_USE()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified EKErrorDomain

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let EKErrorDomain: NSString! ``` | OS X 10.10 |
| To | ``` let EKErrorDomain: String ``` | OS X 10.8 |

Modified EKEventSearchCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias EKEventSearchCallback = (EKEvent!, UnsafePointer<ObjCBool>) -> Void ``` |
| To | ``` typealias EKEventSearchCallback = (EKEvent!, UnsafeMutablePointer<ObjCBool>) -> Void ``` |

Modified EKEventStoreChangedNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let EKEventStoreChangedNotification: NSString! ``` | OS X 10.10 |
| To | ``` let EKEventStoreChangedNotification: String ``` | OS X 10.8 |

Modified EK_LOSE_FRACTIONAL_SECONDS_DO_NOT_USE()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

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
