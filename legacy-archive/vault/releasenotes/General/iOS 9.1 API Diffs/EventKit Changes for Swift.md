---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Swift/EventKit.html
archived_at: '2026-07-18T02:57:08.038488Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# EventKit Changes for Swift

### EventKit

Modified [EKAlarm](https://developer.apple.com/documentation/eventkit/ekalarm)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [EKAlarmProximity [enum]](https://developer.apple.com/documentation/eventkit/ekalarmproximity)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [EKAlarmType [enum]](https://developer.apple.com/documentation/eventkit/ekalarmtype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [EKAuthorizationStatus [enum]](https://developer.apple.com/documentation/eventkit/ekauthorizationstatus)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [EKCalendar](https://developer.apple.com/documentation/eventkit/ekcalendar)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [EKCalendarItem](https://developer.apple.com/documentation/eventkit/ekcalendaritem)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [EKCalendarType [enum]](https://developer.apple.com/documentation/eventkit/ekcalendartype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [EKEntityType [enum]](https://developer.apple.com/documentation/eventkit/ekentitytype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [EKErrorCode [enum]](https://developer.apple.com/documentation/eventkit/ekerrorcode)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` enum EKErrorCode : Int {     case EventNotMutable     case NoCalendar     case NoStartDate     case NoEndDate     case DatesInverted     case InternalFailure     case CalendarReadOnly     case DurationGreaterThanRecurrence     case AlarmGreaterThanRecurrence     case StartDateTooFarInFuture     case StartDateCollidesWithOtherOccurrence     case ObjectBelongsToDifferentStore     case InvitesCannotBeMoved     case InvalidSpan     case CalendarHasNoSource     case CalendarSourceCannotBeModified     case CalendarIsImmutable     case SourceDoesNotAllowCalendarAddDelete     case RecurringReminderRequiresDueDate     case StructuredLocationsNotSupported     case ReminderLocationsNotSupported     case AlarmProximityNotSupported     case CalendarDoesNotAllowEvents     case CalendarDoesNotAllowReminders     case SourceDoesNotAllowReminders     case SourceDoesNotAllowEvents     case PriorityIsInvalid     case InvalidEntityType     case ProcedureAlarmsNotMutable     case EventStoreNotAuthorized     case OSNotSupported     case Last } extension EKErrorCode : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } extension EKErrorCode : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } ``` | Equatable, ErrorType, Hashable, RawRepresentable |
| To | ``` enum EKErrorCode : Int {     case EventNotMutable     case NoCalendar     case NoStartDate     case NoEndDate     case DatesInverted     case InternalFailure     case CalendarReadOnly     case DurationGreaterThanRecurrence     case AlarmGreaterThanRecurrence     case StartDateTooFarInFuture     case StartDateCollidesWithOtherOccurrence     case ObjectBelongsToDifferentStore     case InvitesCannotBeMoved     case InvalidSpan     case CalendarHasNoSource     case CalendarSourceCannotBeModified     case CalendarIsImmutable     case SourceDoesNotAllowCalendarAddDelete     case RecurringReminderRequiresDueDate     case StructuredLocationsNotSupported     case ReminderLocationsNotSupported     case AlarmProximityNotSupported     case CalendarDoesNotAllowEvents     case CalendarDoesNotAllowReminders     case SourceDoesNotAllowReminders     case SourceDoesNotAllowEvents     case PriorityIsInvalid     case InvalidEntityType     case ProcedureAlarmsNotMutable     case EventStoreNotAuthorized     case OSNotSupported     case Last } extension EKErrorCode : _BridgedNSError { } extension EKErrorCode : _BridgedNSError { } ``` | -- |

Modified [EKEvent](https://developer.apple.com/documentation/eventkit/ekevent)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [EKEventAvailability [enum]](https://developer.apple.com/documentation/eventkit/ekeventavailability)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [EKEventStatus [enum]](https://developer.apple.com/documentation/eventkit/ekeventstatus)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [EKEventStore](https://developer.apple.com/documentation/eventkit/ekeventstore)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [EKObject](https://developer.apple.com/documentation/eventkit/ekobject)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [EKParticipant](https://developer.apple.com/documentation/eventkit/ekparticipant)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [EKParticipantRole [enum]](https://developer.apple.com/documentation/eventkit/ekparticipantrole)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [EKParticipantScheduleStatus [enum]](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [EKParticipantStatus [enum]](https://developer.apple.com/documentation/eventkit/ekparticipantstatus)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [EKParticipantType [enum]](https://developer.apple.com/documentation/eventkit/ekparticipanttype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [EKRecurrenceDayOfWeek](https://developer.apple.com/documentation/eventkit/ekrecurrencedayofweek)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [EKRecurrenceEnd](https://developer.apple.com/documentation/eventkit/ekrecurrenceend)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [EKRecurrenceFrequency [enum]](https://developer.apple.com/documentation/eventkit/ekrecurrencefrequency)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [EKRecurrenceRule](https://developer.apple.com/documentation/eventkit/ekrecurrencerule)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [EKReminder](https://developer.apple.com/documentation/eventkit/ekreminder)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [EKReminderPriority [enum]](https://developer.apple.com/documentation/eventkit/ekreminderpriority)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [EKSource](https://developer.apple.com/documentation/eventkit/eksource)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [EKSourceType [enum]](https://developer.apple.com/documentation/eventkit/eksourcetype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [EKSpan [enum]](https://developer.apple.com/documentation/eventkit/ekspan)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [EKStructuredLocation](https://developer.apple.com/documentation/eventkit/ekstructuredlocation)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [EKWeekday [enum]](https://developer.apple.com/documentation/eventkit/ekweekday)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

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
