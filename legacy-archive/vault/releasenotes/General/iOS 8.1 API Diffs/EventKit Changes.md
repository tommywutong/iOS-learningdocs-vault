---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/EventKit.html
archived_at: '2026-07-18T02:56:11.663258Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# EventKit Changes

## EventKit

Modified EKAlarm

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified EKAlarm.init(absoluteDate: NSDate!)

|  | Declaration |
| --- | --- |
| From | ``` init(absoluteDate date: NSDate!) -> EKAlarm ``` |
| To | ``` init!(absoluteDate date: NSDate!) -> EKAlarm ``` |

Modified EKAlarm.init(relativeOffset: NSTimeInterval)

|  | Declaration |
| --- | --- |
| From | ``` init(relativeOffset offset: NSTimeInterval) -> EKAlarm ``` |
| To | ``` init!(relativeOffset offset: NSTimeInterval) -> EKAlarm ``` |

Modified EKAuthorizationStatus [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified EKCalendar

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified EKCalendar.allowedEntityTypes

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified EKCalendar.calendarIdentifier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified EKCalendar.init(eventStore: EKEventStore!)

|  | Declaration |
| --- | --- |
| From | ``` init(eventStore eventStore: EKEventStore!) -> EKCalendar ``` |
| To | ``` init!(eventStore eventStore: EKEventStore!) -> EKCalendar ``` |

Modified EKCalendar.init(forEntityType: EKEntityType, eventStore: EKEventStore!)

|  | Declaration |
| --- | --- |
| From | ``` init(forEntityType entityType: EKEntityType, eventStore eventStore: EKEventStore!) -> EKCalendar ``` |
| To | ``` init!(forEntityType entityType: EKEntityType, eventStore eventStore: EKEventStore!) -> EKCalendar ``` |

Modified EKCalendar.immutable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified EKCalendar.subscribed

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified EKCalendarItem

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified EKCalendarItem.URL

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified EKCalendarItem.calendarItemExternalIdentifier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified EKCalendarItem.calendarItemIdentifier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified EKCalendarItem.creationDate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified EKCalendarItem.hasAlarms

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified EKCalendarItem.hasAttendees

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified EKCalendarItem.hasNotes

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified EKCalendarItem.hasRecurrenceRules

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified EKCalendarItem.recurrenceRules

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified EKCalendarItem.timeZone

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified EKEvent

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified EKEvent.birthdayPersonID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified EKEvent.init(eventStore: EKEventStore!)

|  | Declaration |
| --- | --- |
| From | ``` init(eventStore eventStore: EKEventStore!) -> EKEvent ``` |
| To | ``` init!(eventStore eventStore: EKEventStore!) -> EKEvent ``` |

Modified EKEventStore

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified EKEventStore.authorizationStatusForEntityType(EKEntityType) -> EKAuthorizationStatus [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified EKEventStore.calendarItemWithIdentifier(String!) -> EKCalendarItem!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified EKEventStore.calendarItemsWithExternalIdentifier(String!) -> [AnyObject]!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified EKEventStore.calendarWithIdentifier(String!) -> EKCalendar!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified EKEventStore.calendarsForEntityType(EKEntityType) -> [AnyObject]!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified EKEventStore.cancelFetchRequest(AnyObject!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified EKEventStore.commit(NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified EKEventStore.defaultCalendarForNewReminders() -> EKCalendar!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified EKEventStore.fetchRemindersMatchingPredicate(NSPredicate!, completion:(([AnyObject]!) -> Void)!) -> AnyObject!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified EKEventStore.predicateForCompletedRemindersWithCompletionDateStarting(NSDate!, ending: NSDate!, calendars:[AnyObject]!) -> NSPredicate!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified EKEventStore.predicateForIncompleteRemindersWithDueDateStarting(NSDate!, ending: NSDate!, calendars:[AnyObject]!) -> NSPredicate!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified EKEventStore.predicateForRemindersInCalendars([AnyObject]!) -> NSPredicate!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified EKEventStore.refreshSourcesIfNecessary()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified EKEventStore.removeCalendar(EKCalendar!, commit: Bool, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified EKEventStore.removeEvent(EKEvent!, span: EKSpan, commit: Bool, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified EKEventStore.removeEvent(EKEvent!, span: EKSpan, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified EKEventStore.removeReminder(EKReminder!, commit: Bool, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified EKEventStore.requestAccessToEntityType(EKEntityType, completion: EKEventStoreRequestAccessCompletionHandler!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified EKEventStore.reset()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified EKEventStore.saveCalendar(EKCalendar!, commit: Bool, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified EKEventStore.saveEvent(EKEvent!, span: EKSpan, commit: Bool, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified EKEventStore.saveEvent(EKEvent!, span: EKSpan, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified EKEventStore.saveReminder(EKReminder!, commit: Bool, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified EKEventStore.sourceWithIdentifier(String!) -> EKSource!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified EKEventStore.sources() -> [AnyObject]!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified EKParticipant

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified EKParticipant.ABRecordWithAddressBook(ABAddressBook!) -> Unmanaged<ABRecord>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified EKParticipant.isCurrentUser

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified EKRecurrenceDayOfWeek

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

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
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified EKRecurrenceRule

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

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
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified EKReminder.init(eventStore: EKEventStore!)

|  | Declaration |
| --- | --- |
| From | ``` init(eventStore eventStore: EKEventStore!) -> EKReminder ``` |
| To | ``` init!(eventStore eventStore: EKEventStore!) -> EKReminder ``` |

Modified EKSource

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified EKSource.calendarsForEntityType(EKEntityType) -> NSSet!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified EKStructuredLocation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified EKStructuredLocation.init(title: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(title title: String!) -> EKStructuredLocation ``` |
| To | ``` init!(title title: String!) -> EKStructuredLocation ``` |

Modified EKErrorDomain

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified EKEventStoreChangedNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

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
