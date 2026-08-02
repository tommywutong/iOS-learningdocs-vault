---
title: OS X v10.9 API Diffs
apple_id: TP40013007
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_9/EventKit.html
archived_at: '2026-07-18T02:54:12.294376Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.9 API Diffs](OS%20X%20v10.8%20to%20OS%20X%20v10.9%20API%20Differences.md)


# EventKit Changes

## EventKit

EKAlarm.hModified [EKAlarm.url](https://developer.apple.com/documentation/eventkit/ekalarm/1589757-url)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

EKCalendarItem.hModified [EKCalendarItem.attendees](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507140-attendees)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly) NSArray \*attendees |
| To | @property(nonatomic, copy, readonly) NSArray \*attendees |

EKError.hAdded [EKErrorEventStoreNotAuthorized](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerroreventstorenotauthorized)Added [EKErrorInvalidEntityType](https://developer.apple.com/documentation/eventkit/ekerror/code/invalidentitytype)Added [EKErrorPriorityIsInvalid](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerrorpriorityisinvalid)Added [EKErrorProcedureAlarmsNotMutable](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerrorprocedurealarmsnotmutable)EKEventStore.hAdded [+[EKEventStore authorizationStatusForEntityType:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507239-authorizationstatus)Added [-[EKEventStore init]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507252-init)Added [-[EKEventStore requestAccessToEntityType:completion:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507547-requestaccess)Added [EKAuthorizationStatus](https://developer.apple.com/documentation/eventkit/ekauthorizationstatus)Added [EKAuthorizationStatusAuthorized](https://developer.apple.com/documentation/eventkit/ekauthorizationstatus/ekauthorizationstatusauthorized)Added [EKAuthorizationStatusDenied](https://developer.apple.com/documentation/eventkit/ekauthorizationstatus/denied)Added [EKAuthorizationStatusNotDetermined](https://developer.apple.com/documentation/eventkit/ekauthorizationstatus/ekauthorizationstatusnotdetermined)Added [EKAuthorizationStatusRestricted](https://developer.apple.com/documentation/eventkit/ekauthorizationstatus/restricted)Added [EKEventStoreRequestAccessCompletionHandler](https://developer.apple.com/documentation/eventkit/ekeventstorerequestaccesscompletionhandler)Modified [-[EKEventStore fetchRemindersMatchingPredicate:completion:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507500-fetchremindersmatchingpredicate)

|  | Declaration |
| --- | --- |
| From | - (id)fetchRemindersMatchingPredicate:(NSPredicate \*)predicate completion:(void (^)(NSArray \*))completion |
| To | - (id)fetchRemindersMatchingPredicate:(NSPredicate \*)predicate completion:(void (^)(NSArray \*reminders))completion |

Modified [-[EKEventStore initWithAccessToEntityTypes:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1536382-initwithaccesstoentitytypes)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

EKParticipant.hAdded EKParticipant.isCurrentUserEKReminder.hAdded [EKReminder.priority](https://developer.apple.com/documentation/eventkit/ekreminder/1507173-priority)EKTypes.hAdded [EKReminderPriority](https://developer.apple.com/documentation/eventkit/ekreminderpriority)Added [EKReminderPriorityHigh](https://developer.apple.com/documentation/eventkit/ekreminderpriority/ekreminderpriorityhigh)Added [EKReminderPriorityLow](https://developer.apple.com/documentation/eventkit/ekreminderpriority/ekreminderprioritylow)Added [EKReminderPriorityMedium](https://developer.apple.com/documentation/eventkit/ekreminderpriority/ekreminderprioritymedium)Added [EKReminderPriorityNone](https://developer.apple.com/documentation/eventkit/ekreminderpriority/ekreminderprioritynone)

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
