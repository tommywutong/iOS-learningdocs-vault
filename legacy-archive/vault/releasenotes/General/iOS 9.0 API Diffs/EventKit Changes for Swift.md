---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/EventKit.html
archived_at: '2026-07-18T02:56:48.612570Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# EventKit Changes for Swift

### EventKit

Removed EKCalendarType [struct]Removed EKCalendarType.init(_: UInt32)Removed EKCalendarType.valueRemoved EKErrorCode.init(_: UInt32)Removed EKErrorCode.valueRemoved EKEventAvailability [struct]Removed EKEventAvailability.init(_: Int32)Removed EKEventAvailability.valueRemoved EKEventStatus [struct]Removed EKEventStatus.init(_: UInt32)Removed EKEventStatus.valueRemoved EKEventStore.sources() -> [AnyObject]!Removed EKObject.hasChanges() -> BoolRemoved [EKObject.isNew() -> Bool](https://developer.apple.com/documentation/eventkit/ekobject/1812546-isnew)Removed EKParticipant.isCurrentUserRemoved EKParticipantRole [struct]Removed EKParticipantRole.init(_: UInt32)Removed EKParticipantRole.valueRemoved EKParticipantStatus [struct]Removed EKParticipantStatus.init(_: UInt32)Removed EKParticipantStatus.valueRemoved EKParticipantType [struct]Removed EKParticipantType.init(_: UInt32)Removed EKParticipantType.valueRemoved EKRecurrenceFrequency [struct]Removed EKRecurrenceFrequency.init(_: UInt32)Removed EKRecurrenceFrequency.valueRemoved EKSourceType [struct]Removed EKSourceType.init(_: UInt32)Removed EKSourceType.valueRemoved EKSpan [struct]Removed EKSpan.init(_: UInt32)Removed EKSpan.valueRemoved EKAlarmProximityRemoved EKAlarmProximityEnterRemoved EKAlarmProximityLeaveRemoved EKAlarmProximityNoneRemoved EKCalendarEventAvailabilityBusyRemoved EKCalendarEventAvailabilityFreeRemoved EKCalendarEventAvailabilityMaskRemoved EKCalendarEventAvailabilityNoneRemoved EKCalendarEventAvailabilityTentativeRemoved EKCalendarEventAvailabilityUnavailableRemoved EKCalendarTypeBirthdayRemoved EKCalendarTypeCalDAVRemoved EKCalendarTypeExchangeRemoved EKCalendarTypeLocalRemoved EKCalendarTypeSubscriptionRemoved EKEntityMaskRemoved EKEntityMaskEventRemoved EKEntityMaskReminderRemoved EKEntityTypeRemoved EKEntityTypeEventRemoved EKEntityTypeReminderRemoved EKEventAvailabilityBusyRemoved EKEventAvailabilityFreeRemoved EKEventAvailabilityNotSupportedRemoved EKEventAvailabilityTentativeRemoved EKEventAvailabilityUnavailableRemoved EKEventStatusCanceledRemoved EKEventStatusConfirmedRemoved EKEventStatusNoneRemoved EKEventStatusTentativeRemoved EKFridayRemoved EKMondayRemoved EKParticipantRoleChairRemoved EKParticipantRoleNonParticipantRemoved EKParticipantRoleOptionalRemoved EKParticipantRoleRequiredRemoved EKParticipantRoleUnknownRemoved EKParticipantStatusAcceptedRemoved EKParticipantStatusCompletedRemoved EKParticipantStatusDeclinedRemoved EKParticipantStatusDelegatedRemoved EKParticipantStatusInProcessRemoved EKParticipantStatusPendingRemoved EKParticipantStatusTentativeRemoved EKParticipantStatusUnknownRemoved EKParticipantTypeGroupRemoved EKParticipantTypePersonRemoved EKParticipantTypeResourceRemoved EKParticipantTypeRoomRemoved EKParticipantTypeUnknownRemoved EKRecurrenceFrequencyDailyRemoved EKRecurrenceFrequencyMonthlyRemoved EKRecurrenceFrequencyWeeklyRemoved EKRecurrenceFrequencyYearlyRemoved EKSaturdayRemoved EKSourceTypeBirthdaysRemoved EKSourceTypeCalDAVRemoved EKSourceTypeExchangeRemoved EKSourceTypeLocalRemoved EKSourceTypeMobileMeRemoved EKSourceTypeSubscribedRemoved EKSpanFutureEventsRemoved EKSpanThisEventRemoved EKSundayRemoved EKThursdayRemoved EKTuesdayRemoved EKWednesdayAdded [EKAlarmProximity [enum]](https://developer.apple.com/documentation/eventkit/ekalarmproximity)Added [EKAlarmProximity.Enter](https://developer.apple.com/documentation/eventkit/ekalarmproximity/enter)Added [EKAlarmProximity.Leave](https://developer.apple.com/documentation/eventkit/ekalarmproximity/leave)Added [EKAlarmProximity.None](https://developer.apple.com/documentation/eventkit/ekalarmproximity/ekalarmproximitynone)Added [EKAlarmType [enum]](https://developer.apple.com/documentation/eventkit/ekalarmtype)Added [EKAlarmType.Audio](https://developer.apple.com/documentation/eventkit/ekalarmtype/audio)Added [EKAlarmType.Display](https://developer.apple.com/documentation/eventkit/ekalarmtype/ekalarmtypedisplay)Added [EKAlarmType.Email](https://developer.apple.com/documentation/eventkit/ekalarmtype/email)Added [EKAlarmType.Procedure](https://developer.apple.com/documentation/eventkit/ekalarmtype/ekalarmtypeprocedure)Added [EKCalendarEventAvailabilityMask [struct]](https://developer.apple.com/documentation/eventkit/ekcalendareventavailabilitymask)Added [EKCalendarEventAvailabilityMask.Busy](https://developer.apple.com/documentation/eventkit/ekcalendareventavailabilitymask/ekcalendareventavailabilitybusy)Added [EKCalendarEventAvailabilityMask.Free](https://developer.apple.com/documentation/eventkit/ekcalendareventavailabilitymask/1451912-free)Added EKCalendarEventAvailabilityMask.init(rawValue: UInt)Added [EKCalendarEventAvailabilityMask.None](https://developer.apple.com/documentation/eventkit/ekcalendareventavailabilitymask/ekcalendareventavailabilitynone)Added [EKCalendarEventAvailabilityMask.Tentative](https://developer.apple.com/documentation/eventkit/ekcalendareventavailabilitymask/1451814-tentative)Added [EKCalendarEventAvailabilityMask.Unavailable](https://developer.apple.com/documentation/eventkit/ekcalendareventavailabilitymask/1451855-unavailable)Added [EKCalendarType [enum]](https://developer.apple.com/documentation/eventkit/ekcalendartype)Added [EKCalendarType.Birthday](https://developer.apple.com/documentation/eventkit/ekcalendartype/ekcalendartypebirthday)Added [EKCalendarType.CalDAV](https://developer.apple.com/documentation/eventkit/ekcalendartype/ekcalendartypecaldav)Added [EKCalendarType.Exchange](https://developer.apple.com/documentation/eventkit/ekcalendartype/ekcalendartypeexchange)Added [EKCalendarType.Local](https://developer.apple.com/documentation/eventkit/ekcalendartype/ekcalendartypelocal)Added [EKCalendarType.Subscription](https://developer.apple.com/documentation/eventkit/ekcalendartype/subscription)Added [EKEntityMask [struct]](https://developer.apple.com/documentation/eventkit/ekentitymask)Added [EKEntityMask.Event](https://developer.apple.com/documentation/eventkit/ekentitymask/ekentitymaskevent)Added EKEntityMask.init(rawValue: UInt)Added [EKEntityMask.Reminder](https://developer.apple.com/documentation/eventkit/ekentitymask/ekentitymaskreminder)Added [EKEntityType [enum]](https://developer.apple.com/documentation/eventkit/ekentitytype)Added [EKEntityType.Event](https://developer.apple.com/documentation/eventkit/ekentitytype/event)Added [EKEntityType.Reminder](https://developer.apple.com/documentation/eventkit/ekentitytype/ekentitytypereminder)Added [EKErrorCode.EventStoreNotAuthorized](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerroreventstorenotauthorized)Added [EKErrorCode.OSNotSupported](https://developer.apple.com/documentation/eventkit/ekerror/code/osnotsupported)Added [EKErrorCode.ProcedureAlarmsNotMutable](https://developer.apple.com/documentation/eventkit/ekerror/code/procedurealarmsnotmutable)Added [EKErrorCode.SourceDoesNotAllowEvents](https://developer.apple.com/documentation/eventkit/ekerror/code/sourcedoesnotallowevents)Added [EKEvent.birthdayContactIdentifier](https://developer.apple.com/documentation/eventkit/ekevent/1507349-birthdaycontactidentifier)Added [EKEvent.occurrenceDate](https://developer.apple.com/documentation/eventkit/ekevent/1507244-occurrencedate)Added [EKEvent.structuredLocation](https://developer.apple.com/documentation/eventkit/ekevent/1507185-structuredlocation)Added [EKEventAvailability [enum]](https://developer.apple.com/documentation/eventkit/ekeventavailability)Added [EKEventAvailability.Busy](https://developer.apple.com/documentation/eventkit/ekeventavailability/busy)Added [EKEventAvailability.Free](https://developer.apple.com/documentation/eventkit/ekeventavailability/ekeventavailabilityfree)Added [EKEventAvailability.NotSupported](https://developer.apple.com/documentation/eventkit/ekeventavailability/ekeventavailabilitynotsupported)Added [EKEventAvailability.Tentative](https://developer.apple.com/documentation/eventkit/ekeventavailability/ekeventavailabilitytentative)Added [EKEventAvailability.Unavailable](https://developer.apple.com/documentation/eventkit/ekeventavailability/unavailable)Added [EKEventStatus [enum]](https://developer.apple.com/documentation/eventkit/ekeventstatus)Added [EKEventStatus.Canceled](https://developer.apple.com/documentation/eventkit/ekeventstatus/ekeventstatuscanceled)Added [EKEventStatus.Confirmed](https://developer.apple.com/documentation/eventkit/ekeventstatus/confirmed)Added [EKEventStatus.None](https://developer.apple.com/documentation/eventkit/ekeventstatus/none)Added [EKEventStatus.Tentative](https://developer.apple.com/documentation/eventkit/ekeventstatus/tentative)Added [EKEventStore.init()](https://developer.apple.com/documentation/eventkit/ekeventstore/1507252-init)Added [EKEventStore.sources](https://developer.apple.com/documentation/eventkit/ekeventstore/1507315-sources)Added [EKObject.hasChanges](https://developer.apple.com/documentation/eventkit/ekobject/1507333-haschanges)Added [EKObject.new](https://developer.apple.com/documentation/eventkit/ekobject/1507402-isnew)Added [EKParticipant.contactPredicate](https://developer.apple.com/documentation/eventkit/ekparticipant/1507163-contactpredicate)Added [EKParticipant.currentUser](https://developer.apple.com/documentation/eventkit/ekparticipant/1507248-iscurrentuser)Added [EKParticipantRole [enum]](https://developer.apple.com/documentation/eventkit/ekparticipantrole)Added [EKParticipantRole.Chair](https://developer.apple.com/documentation/eventkit/ekparticipantrole/ekparticipantrolechair)Added [EKParticipantRole.NonParticipant](https://developer.apple.com/documentation/eventkit/ekparticipantrole/nonparticipant)Added [EKParticipantRole.Optional](https://developer.apple.com/documentation/eventkit/ekparticipantrole/ekparticipantroleoptional)Added [EKParticipantRole.Required](https://developer.apple.com/documentation/eventkit/ekparticipantrole/required)Added [EKParticipantRole.Unknown](https://developer.apple.com/documentation/eventkit/ekparticipantrole/unknown)Added [EKParticipantScheduleStatus [enum]](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus)Added [EKParticipantScheduleStatus.CannotDeliver](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/ekparticipantschedulestatuscannotdeliver)Added [EKParticipantScheduleStatus.Delivered](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/ekparticipantschedulestatusdelivered)Added [EKParticipantScheduleStatus.DeliveryFailed](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/deliveryfailed)Added [EKParticipantScheduleStatus.None](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/none)Added [EKParticipantScheduleStatus.NoPrivileges](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/noprivileges)Added [EKParticipantScheduleStatus.Pending](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/pending)Added [EKParticipantScheduleStatus.RecipientNotAllowed](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/recipientnotallowed)Added [EKParticipantScheduleStatus.RecipientNotRecognized](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/ekparticipantschedulestatusrecipientnotrecognized)Added [EKParticipantScheduleStatus.Sent](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/sent)Added [EKParticipantStatus [enum]](https://developer.apple.com/documentation/eventkit/ekparticipantstatus)Added [EKParticipantStatus.Accepted](https://developer.apple.com/documentation/eventkit/ekparticipantstatus/accepted)Added [EKParticipantStatus.Completed](https://developer.apple.com/documentation/eventkit/ekparticipantstatus/completed)Added [EKParticipantStatus.Declined](https://developer.apple.com/documentation/eventkit/ekparticipantstatus/declined)Added [EKParticipantStatus.Delegated](https://developer.apple.com/documentation/eventkit/ekparticipantstatus/delegated)Added [EKParticipantStatus.InProcess](https://developer.apple.com/documentation/eventkit/ekparticipantstatus/ekparticipantstatusinprocess)Added [EKParticipantStatus.Pending](https://developer.apple.com/documentation/eventkit/ekparticipantstatus/pending)Added [EKParticipantStatus.Tentative](https://developer.apple.com/documentation/eventkit/ekparticipantstatus/tentative)Added [EKParticipantStatus.Unknown](https://developer.apple.com/documentation/eventkit/ekparticipantstatus/ekparticipantstatusunknown)Added [EKParticipantType [enum]](https://developer.apple.com/documentation/eventkit/ekparticipanttype)Added [EKParticipantType.Group](https://developer.apple.com/documentation/eventkit/ekparticipanttype/ekparticipanttypegroup)Added [EKParticipantType.Person](https://developer.apple.com/documentation/eventkit/ekparticipanttype/person)Added [EKParticipantType.Resource](https://developer.apple.com/documentation/eventkit/ekparticipanttype/ekparticipanttyperesource)Added [EKParticipantType.Room](https://developer.apple.com/documentation/eventkit/ekparticipanttype/ekparticipanttyperoom)Added [EKParticipantType.Unknown](https://developer.apple.com/documentation/eventkit/ekparticipanttype/ekparticipanttypeunknown)Added [EKRecurrenceFrequency [enum]](https://developer.apple.com/documentation/eventkit/ekrecurrencefrequency)Added [EKRecurrenceFrequency.Daily](https://developer.apple.com/documentation/eventkit/ekrecurrencefrequency/ekrecurrencefrequencydaily)Added [EKRecurrenceFrequency.Monthly](https://developer.apple.com/documentation/eventkit/ekrecurrencefrequency/ekrecurrencefrequencymonthly)Added [EKRecurrenceFrequency.Weekly](https://developer.apple.com/documentation/eventkit/ekrecurrencefrequency/ekrecurrencefrequencyweekly)Added [EKRecurrenceFrequency.Yearly](https://developer.apple.com/documentation/eventkit/ekrecurrencefrequency/yearly)Added [EKReminderPriority [enum]](https://developer.apple.com/documentation/eventkit/ekreminderpriority)Added [EKReminderPriority.High](https://developer.apple.com/documentation/eventkit/ekreminderpriority/ekreminderpriorityhigh)Added [EKReminderPriority.Low](https://developer.apple.com/documentation/eventkit/ekreminderpriority/ekreminderprioritylow)Added [EKReminderPriority.Medium](https://developer.apple.com/documentation/eventkit/ekreminderpriority/ekreminderprioritymedium)Added [EKReminderPriority.None](https://developer.apple.com/documentation/eventkit/ekreminderpriority/ekreminderprioritynone)Added [EKSourceType [enum]](https://developer.apple.com/documentation/eventkit/eksourcetype)Added [EKSourceType.Birthdays](https://developer.apple.com/documentation/eventkit/eksourcetype/eksourcetypebirthdays)Added [EKSourceType.CalDAV](https://developer.apple.com/documentation/eventkit/eksourcetype/eksourcetypecaldav)Added [EKSourceType.Exchange](https://developer.apple.com/documentation/eventkit/eksourcetype/exchange)Added [EKSourceType.Local](https://developer.apple.com/documentation/eventkit/eksourcetype/eksourcetypelocal)Added [EKSourceType.MobileMe](https://developer.apple.com/documentation/eventkit/eksourcetype/eksourcetypemobileme)Added [EKSourceType.Subscribed](https://developer.apple.com/documentation/eventkit/eksourcetype/eksourcetypesubscribed)Added [EKSpan [enum]](https://developer.apple.com/documentation/eventkit/ekspan)Added [EKSpan.FutureEvents](https://developer.apple.com/documentation/eventkit/ekspan/ekspanfutureevents)Added [EKSpan.ThisEvent](https://developer.apple.com/documentation/eventkit/ekspan/thisevent)Added [EKStructuredLocation.init(mapItem: MKMapItem)](https://developer.apple.com/documentation/eventkit/ekstructuredlocation/1507493-init)Added [EKWeekday [enum]](https://developer.apple.com/documentation/eventkit/ekweekday)Added [EKWeekday.EKFriday](https://developer.apple.com/documentation/eventkit/ekweekday/1451835-ekfriday)Added [EKWeekday.EKMonday](https://developer.apple.com/documentation/eventkit/ekweekday/1451967-ekmonday)Added [EKWeekday.EKSaturday](https://developer.apple.com/documentation/eventkit/ekweekday/1451995-eksaturday)Added [EKWeekday.EKSunday](https://developer.apple.com/documentation/eventkit/ekweekday/1451896-eksunday)Added [EKWeekday.EKThursday](https://developer.apple.com/documentation/eventkit/ekweekday/1451894-ekthursday)Added [EKWeekday.EKTuesday](https://developer.apple.com/documentation/eventkit/ekweekday/ektuesday)Added [EKWeekday.EKWednesday](https://developer.apple.com/documentation/eventkit/ekweekday/1451817-ekwednesday)Added [EKWeekday.Friday](https://developer.apple.com/documentation/eventkit/ekweekday/ekweekdayfriday)Added [EKWeekday.Monday](https://developer.apple.com/documentation/eventkit/ekweekday/monday)Added [EKWeekday.Saturday](https://developer.apple.com/documentation/eventkit/ekweekday/ekweekdaysaturday)Added [EKWeekday.Sunday](https://developer.apple.com/documentation/eventkit/ekweekday/sunday)Added [EKWeekday.Thursday](https://developer.apple.com/documentation/eventkit/ekweekday/ekweekdaythursday)Added [EKWeekday.Tuesday](https://developer.apple.com/documentation/eventkit/ekweekday/ekweekdaytuesday)Added [EKWeekday.Wednesday](https://developer.apple.com/documentation/eventkit/ekweekday/wednesday)Modified [EKAlarm](https://developer.apple.com/documentation/eventkit/ekalarm)

|  | Declaration |
| --- | --- |
| From | ``` class EKAlarm : EKObject, NSCopying {     init!(absoluteDate date: NSDate!) -> EKAlarm     class func alarmWithAbsoluteDate(_ date: NSDate!) -> EKAlarm!     init!(relativeOffset offset: NSTimeInterval) -> EKAlarm     class func alarmWithRelativeOffset(_ offset: NSTimeInterval) -> EKAlarm!     var relativeOffset: NSTimeInterval     @NSCopying var absoluteDate: NSDate!     @NSCopying var structuredLocation: EKStructuredLocation!     var proximity: EKAlarmProximity } ``` |
| To | ``` class EKAlarm : EKObject, NSCopying {      init(absoluteDate date: NSDate)     class func alarmWithAbsoluteDate(_ date: NSDate) -> EKAlarm      init(relativeOffset offset: NSTimeInterval)     class func alarmWithRelativeOffset(_ offset: NSTimeInterval) -> EKAlarm     var relativeOffset: NSTimeInterval     @NSCopying var absoluteDate: NSDate?     @NSCopying var structuredLocation: EKStructuredLocation?     var proximity: EKAlarmProximity     var type: EKAlarmType { get }     var emailAddress: String?     var soundName: String?     @NSCopying var url: NSURL? } ``` |

Modified [EKAlarm.absoluteDate](https://developer.apple.com/documentation/eventkit/ekalarm/1507486-absolutedate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var absoluteDate: NSDate! ``` |
| To | ``` @NSCopying var absoluteDate: NSDate? ``` |

Modified [EKAlarm.init(absoluteDate: NSDate)](https://developer.apple.com/documentation/eventkit/ekalarm/1507130-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(absoluteDate date: NSDate!) -> EKAlarm ``` |
| To | ``` init(absoluteDate date: NSDate) ``` |

Modified [EKAlarm.init(relativeOffset: NSTimeInterval)](https://developer.apple.com/documentation/eventkit/ekalarm/1507338-alarmwithrelativeoffset)

|  | Declaration |
| --- | --- |
| From | ``` init!(relativeOffset offset: NSTimeInterval) -> EKAlarm ``` |
| To | ``` init(relativeOffset offset: NSTimeInterval) ``` |

Modified [EKAlarm.structuredLocation](https://developer.apple.com/documentation/eventkit/ekalarm/1507331-structuredlocation)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var structuredLocation: EKStructuredLocation! ``` |
| To | ``` @NSCopying var structuredLocation: EKStructuredLocation? ``` |

Modified [EKAuthorizationStatus [enum]](https://developer.apple.com/documentation/eventkit/ekauthorizationstatus)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [EKCalendar](https://developer.apple.com/documentation/eventkit/ekcalendar)

|  | Declaration |
| --- | --- |
| From | ``` class EKCalendar : EKObject {     init!(eventStore eventStore: EKEventStore!) -> EKCalendar     class func calendarWithEventStore(_ eventStore: EKEventStore!) -> EKCalendar!     init!(forEntityType entityType: EKEntityType, eventStore eventStore: EKEventStore!) -> EKCalendar     class func calendarForEntityType(_ entityType: EKEntityType, eventStore eventStore: EKEventStore!) -> EKCalendar!     var source: EKSource!     var calendarIdentifier: String! { get }     var title: String!     var type: EKCalendarType { get }     var allowsContentModifications: Bool { get }     var subscribed: Bool { get }     var immutable: Bool { get }     var CGColor: CGColor!     var supportedEventAvailabilities: EKCalendarEventAvailabilityMask { get }     var allowedEntityTypes: EKEntityMask { get } } ``` |
| To | ``` class EKCalendar : EKObject {      init(eventStore eventStore: EKEventStore)     class func calendarWithEventStore(_ eventStore: EKEventStore) -> EKCalendar      init(forEntityType entityType: EKEntityType, eventStore eventStore: EKEventStore)     class func calendarForEntityType(_ entityType: EKEntityType, eventStore eventStore: EKEventStore) -> EKCalendar     var source: EKSource     var calendarIdentifier: String { get }     var title: String     var type: EKCalendarType { get }     var allowsContentModifications: Bool { get }     var subscribed: Bool { get }     var immutable: Bool { get }     var CGColor: CGColor     var supportedEventAvailabilities: EKCalendarEventAvailabilityMask { get }     var allowedEntityTypes: EKEntityMask { get } } ``` |

Modified [EKCalendar.calendarIdentifier](https://developer.apple.com/documentation/eventkit/ekcalendar/1507380-calendaridentifier)

|  | Declaration |
| --- | --- |
| From | ``` var calendarIdentifier: String! { get } ``` |
| To | ``` var calendarIdentifier: String { get } ``` |

Modified [EKCalendar.CGColor](https://developer.apple.com/documentation/eventkit/ekcalendar/1615894-cgcolor)

|  | Declaration |
| --- | --- |
| From | ``` var CGColor: CGColor! ``` |
| To | ``` var CGColor: CGColor ``` |

Modified [EKCalendar.init(forEntityType: EKEntityType, eventStore: EKEventStore)](https://developer.apple.com/documentation/eventkit/ekcalendar/1507516-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(forEntityType entityType: EKEntityType, eventStore eventStore: EKEventStore!) -> EKCalendar ``` |
| To | ``` init(forEntityType entityType: EKEntityType, eventStore eventStore: EKEventStore) ``` |

Modified [EKCalendar.source](https://developer.apple.com/documentation/eventkit/ekcalendar/1507288-source)

|  | Declaration |
| --- | --- |
| From | ``` var source: EKSource! ``` |
| To | ``` var source: EKSource ``` |

Modified [EKCalendar.title](https://developer.apple.com/documentation/eventkit/ekcalendar/1507487-title)

|  | Declaration |
| --- | --- |
| From | ``` var title: String! ``` |
| To | ``` var title: String ``` |

Modified [EKCalendarItem](https://developer.apple.com/documentation/eventkit/ekcalendaritem)

|  | Declaration |
| --- | --- |
| From | ``` class EKCalendarItem : EKObject {     var UUID: String! { get }     var calendar: EKCalendar!     var calendarItemIdentifier: String! { get }     var calendarItemExternalIdentifier: String! { get }     var title: String!     var location: String!     var notes: String!     @NSCopying var URL: NSURL!     var lastModifiedDate: NSDate! { get }     var creationDate: NSDate! { get }     @NSCopying var timeZone: NSTimeZone!     var hasAlarms: Bool { get }     var hasRecurrenceRules: Bool { get }     var hasAttendees: Bool { get }     var hasNotes: Bool { get }     var attendees: [AnyObject]! { get }     var alarms: [AnyObject]!     func addAlarm(_ alarm: EKAlarm!)     func removeAlarm(_ alarm: EKAlarm!)     var recurrenceRules: [AnyObject]!     func addRecurrenceRule(_ rule: EKRecurrenceRule!)     func removeRecurrenceRule(_ rule: EKRecurrenceRule!) } ``` |
| To | ``` class EKCalendarItem : EKObject {     var UUID: String { get }     var calendar: EKCalendar     var calendarItemIdentifier: String { get }     var calendarItemExternalIdentifier: String { get }     var title: String     var location: String?     var notes: String?     @NSCopying var URL: NSURL?     var lastModifiedDate: NSDate? { get }     var creationDate: NSDate? { get }     @NSCopying var timeZone: NSTimeZone?     var hasAlarms: Bool { get }     var hasRecurrenceRules: Bool { get }     var hasAttendees: Bool { get }     var hasNotes: Bool { get }     var attendees: [EKParticipant]? { get }     var alarms: [EKAlarm]?     func addAlarm(_ alarm: EKAlarm)     func removeAlarm(_ alarm: EKAlarm)     var recurrenceRules: [EKRecurrenceRule]?     func addRecurrenceRule(_ rule: EKRecurrenceRule)     func removeRecurrenceRule(_ rule: EKRecurrenceRule) } ``` |

Modified [EKCalendarItem.addAlarm(_: EKAlarm)](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507397-addalarm)

|  | Declaration |
| --- | --- |
| From | ``` func addAlarm(_ alarm: EKAlarm!) ``` |
| To | ``` func addAlarm(_ alarm: EKAlarm) ``` |

Modified [EKCalendarItem.addRecurrenceRule(_: EKRecurrenceRule)](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507256-addrecurrencerule)

|  | Declaration |
| --- | --- |
| From | ``` func addRecurrenceRule(_ rule: EKRecurrenceRule!) ``` |
| To | ``` func addRecurrenceRule(_ rule: EKRecurrenceRule) ``` |

Modified [EKCalendarItem.alarms](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507211-alarms)

|  | Declaration |
| --- | --- |
| From | ``` var alarms: [AnyObject]! ``` |
| To | ``` var alarms: [EKAlarm]? ``` |

Modified [EKCalendarItem.attendees](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507140-attendees)

|  | Declaration |
| --- | --- |
| From | ``` var attendees: [AnyObject]! { get } ``` |
| To | ``` var attendees: [EKParticipant]? { get } ``` |

Modified [EKCalendarItem.calendar](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507169-calendar)

|  | Declaration |
| --- | --- |
| From | ``` var calendar: EKCalendar! ``` |
| To | ``` var calendar: EKCalendar ``` |

Modified [EKCalendarItem.calendarItemExternalIdentifier](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507283-calendaritemexternalidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var calendarItemExternalIdentifier: String! { get } ``` |
| To | ``` var calendarItemExternalIdentifier: String { get } ``` |

Modified [EKCalendarItem.calendarItemIdentifier](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507075-calendaritemidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var calendarItemIdentifier: String! { get } ``` |
| To | ``` var calendarItemIdentifier: String { get } ``` |

Modified [EKCalendarItem.creationDate](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507213-creationdate)

|  | Declaration |
| --- | --- |
| From | ``` var creationDate: NSDate! { get } ``` |
| To | ``` var creationDate: NSDate? { get } ``` |

Modified [EKCalendarItem.lastModifiedDate](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507374-lastmodifieddate)

|  | Declaration |
| --- | --- |
| From | ``` var lastModifiedDate: NSDate! { get } ``` |
| To | ``` var lastModifiedDate: NSDate? { get } ``` |

Modified [EKCalendarItem.location](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507269-location)

|  | Declaration |
| --- | --- |
| From | ``` var location: String! ``` |
| To | ``` var location: String? ``` |

Modified [EKCalendarItem.notes](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507507-notes)

|  | Declaration |
| --- | --- |
| From | ``` var notes: String! ``` |
| To | ``` var notes: String? ``` |

Modified [EKCalendarItem.recurrenceRules](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507135-recurrencerules)

|  | Declaration |
| --- | --- |
| From | ``` var recurrenceRules: [AnyObject]! ``` |
| To | ``` var recurrenceRules: [EKRecurrenceRule]? ``` |

Modified [EKCalendarItem.removeAlarm(_: EKAlarm)](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507133-removealarm)

|  | Declaration |
| --- | --- |
| From | ``` func removeAlarm(_ alarm: EKAlarm!) ``` |
| To | ``` func removeAlarm(_ alarm: EKAlarm) ``` |

Modified [EKCalendarItem.removeRecurrenceRule(_: EKRecurrenceRule)](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507495-removerecurrencerule)

|  | Declaration |
| --- | --- |
| From | ``` func removeRecurrenceRule(_ rule: EKRecurrenceRule!) ``` |
| To | ``` func removeRecurrenceRule(_ rule: EKRecurrenceRule) ``` |

Modified [EKCalendarItem.timeZone](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507104-timezone)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var timeZone: NSTimeZone! ``` |
| To | ``` @NSCopying var timeZone: NSTimeZone? ``` |

Modified [EKCalendarItem.title](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507305-title)

|  | Declaration |
| --- | --- |
| From | ``` var title: String! ``` |
| To | ``` var title: String ``` |

Modified [EKCalendarItem.URL](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507265-url)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var URL: NSURL! ``` |
| To | ``` @NSCopying var URL: NSURL? ``` |

Modified [EKErrorCode [enum]](https://developer.apple.com/documentation/eventkit/ekerrorcode)

|  | Declaration | Protocols | Introduction | Raw Value Type |
| --- | --- | --- | --- | --- |
| From | ``` struct EKErrorCode {     init(_ value: UInt32)     var value: UInt32 } ``` | -- | iOS 8.1 | -- |
| To | ``` enum EKErrorCode : Int {     case EventNotMutable     case NoCalendar     case NoStartDate     case NoEndDate     case DatesInverted     case InternalFailure     case CalendarReadOnly     case DurationGreaterThanRecurrence     case AlarmGreaterThanRecurrence     case StartDateTooFarInFuture     case StartDateCollidesWithOtherOccurrence     case ObjectBelongsToDifferentStore     case InvitesCannotBeMoved     case InvalidSpan     case CalendarHasNoSource     case CalendarSourceCannotBeModified     case CalendarIsImmutable     case SourceDoesNotAllowCalendarAddDelete     case RecurringReminderRequiresDueDate     case StructuredLocationsNotSupported     case ReminderLocationsNotSupported     case AlarmProximityNotSupported     case CalendarDoesNotAllowEvents     case CalendarDoesNotAllowReminders     case SourceDoesNotAllowReminders     case SourceDoesNotAllowEvents     case PriorityIsInvalid     case InvalidEntityType     case ProcedureAlarmsNotMutable     case EventStoreNotAuthorized     case OSNotSupported     case Last } extension EKErrorCode : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } extension EKErrorCode : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } ``` | Equatable, ErrorType, Hashable, RawRepresentable | iOS 9.0 | Int |

Modified [EKErrorCode.AlarmGreaterThanRecurrence](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerroralarmgreaterthanrecurrence)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | EKErrorAlarmGreaterThanRecurrence | ``` var EKErrorAlarmGreaterThanRecurrence: EKErrorCode { get } ``` | iOS 8.0 |
| To | AlarmGreaterThanRecurrence | ``` case AlarmGreaterThanRecurrence ``` | iOS 9.0 |

Modified [EKErrorCode.AlarmProximityNotSupported](https://developer.apple.com/documentation/eventkit/ekerror/code/alarmproximitynotsupported)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | EKErrorAlarmProximityNotSupported | ``` var EKErrorAlarmProximityNotSupported: EKErrorCode { get } ``` | iOS 8.0 |
| To | AlarmProximityNotSupported | ``` case AlarmProximityNotSupported ``` | iOS 9.0 |

Modified [EKErrorCode.CalendarDoesNotAllowEvents](https://developer.apple.com/documentation/eventkit/ekerror/code/calendardoesnotallowevents)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | EKErrorCalendarDoesNotAllowEvents | ``` var EKErrorCalendarDoesNotAllowEvents: EKErrorCode { get } ``` | iOS 8.0 |
| To | CalendarDoesNotAllowEvents | ``` case CalendarDoesNotAllowEvents ``` | iOS 9.0 |

Modified [EKErrorCode.CalendarDoesNotAllowReminders](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerrorcalendardoesnotallowreminders)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | EKErrorCalendarDoesNotAllowReminders | ``` var EKErrorCalendarDoesNotAllowReminders: EKErrorCode { get } ``` | iOS 8.0 |
| To | CalendarDoesNotAllowReminders | ``` case CalendarDoesNotAllowReminders ``` | iOS 9.0 |

Modified [EKErrorCode.CalendarHasNoSource](https://developer.apple.com/documentation/eventkit/ekerror/code/calendarhasnosource)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | EKErrorCalendarHasNoSource | ``` var EKErrorCalendarHasNoSource: EKErrorCode { get } ``` | iOS 8.0 |
| To | CalendarHasNoSource | ``` case CalendarHasNoSource ``` | iOS 9.0 |

Modified [EKErrorCode.CalendarIsImmutable](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerrorcalendarisimmutable)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | EKErrorCalendarIsImmutable | ``` var EKErrorCalendarIsImmutable: EKErrorCode { get } ``` | iOS 8.0 |
| To | CalendarIsImmutable | ``` case CalendarIsImmutable ``` | iOS 9.0 |

Modified [EKErrorCode.CalendarReadOnly](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerrorcalendarreadonly)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | EKErrorCalendarReadOnly | ``` var EKErrorCalendarReadOnly: EKErrorCode { get } ``` | iOS 8.0 |
| To | CalendarReadOnly | ``` case CalendarReadOnly ``` | iOS 9.0 |

Modified [EKErrorCode.CalendarSourceCannotBeModified](https://developer.apple.com/documentation/eventkit/ekerror/code/calendarsourcecannotbemodified)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | EKErrorCalendarSourceCannotBeModified | ``` var EKErrorCalendarSourceCannotBeModified: EKErrorCode { get } ``` | iOS 8.0 |
| To | CalendarSourceCannotBeModified | ``` case CalendarSourceCannotBeModified ``` | iOS 9.0 |

Modified [EKErrorCode.DatesInverted](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerrordatesinverted)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | EKErrorDatesInverted | ``` var EKErrorDatesInverted: EKErrorCode { get } ``` | iOS 8.0 |
| To | DatesInverted | ``` case DatesInverted ``` | iOS 9.0 |

Modified [EKErrorCode.DurationGreaterThanRecurrence](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerrordurationgreaterthanrecurrence)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | EKErrorDurationGreaterThanRecurrence | ``` var EKErrorDurationGreaterThanRecurrence: EKErrorCode { get } ``` | iOS 8.0 |
| To | DurationGreaterThanRecurrence | ``` case DurationGreaterThanRecurrence ``` | iOS 9.0 |

Modified [EKErrorCode.EventNotMutable](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerroreventnotmutable)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | EKErrorEventNotMutable | ``` var EKErrorEventNotMutable: EKErrorCode { get } ``` | iOS 8.0 |
| To | EventNotMutable | ``` case EventNotMutable ``` | iOS 9.0 |

Modified [EKErrorCode.InternalFailure](https://developer.apple.com/documentation/eventkit/ekerror/code/internalfailure)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | EKErrorInternalFailure | ``` var EKErrorInternalFailure: EKErrorCode { get } ``` | iOS 8.0 |
| To | InternalFailure | ``` case InternalFailure ``` | iOS 9.0 |

Modified [EKErrorCode.InvalidEntityType](https://developer.apple.com/documentation/eventkit/ekerror/code/invalidentitytype)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | EKErrorInvalidEntityType | ``` var EKErrorInvalidEntityType: EKErrorCode { get } ``` | iOS 8.0 |
| To | InvalidEntityType | ``` case InvalidEntityType ``` | iOS 9.0 |

Modified [EKErrorCode.InvalidSpan](https://developer.apple.com/documentation/eventkit/ekerror/code/invalidspan)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | EKErrorInvalidSpan | ``` var EKErrorInvalidSpan: EKErrorCode { get } ``` | iOS 8.0 |
| To | InvalidSpan | ``` case InvalidSpan ``` | iOS 9.0 |

Modified [EKErrorCode.InvitesCannotBeMoved](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerrorinvitescannotbemoved)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | EKErrorInvitesCannotBeMoved | ``` var EKErrorInvitesCannotBeMoved: EKErrorCode { get } ``` | iOS 8.0 |
| To | InvitesCannotBeMoved | ``` case InvitesCannotBeMoved ``` | iOS 9.0 |

Modified [EKErrorCode.Last](https://developer.apple.com/documentation/eventkit/ekerror/code/last)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | EKErrorLast | ``` var EKErrorLast: EKErrorCode { get } ``` | iOS 8.0 |
| To | Last | ``` case Last ``` | iOS 9.0 |

Modified [EKErrorCode.NoCalendar](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerrornocalendar)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | EKErrorNoCalendar | ``` var EKErrorNoCalendar: EKErrorCode { get } ``` | iOS 8.0 |
| To | NoCalendar | ``` case NoCalendar ``` | iOS 9.0 |

Modified [EKErrorCode.NoEndDate](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerrornoenddate)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | EKErrorNoEndDate | ``` var EKErrorNoEndDate: EKErrorCode { get } ``` | iOS 8.0 |
| To | NoEndDate | ``` case NoEndDate ``` | iOS 9.0 |

Modified [EKErrorCode.NoStartDate](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerrornostartdate)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | EKErrorNoStartDate | ``` var EKErrorNoStartDate: EKErrorCode { get } ``` | iOS 8.0 |
| To | NoStartDate | ``` case NoStartDate ``` | iOS 9.0 |

Modified [EKErrorCode.ObjectBelongsToDifferentStore](https://developer.apple.com/documentation/eventkit/ekerror/code/objectbelongstodifferentstore)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | EKErrorObjectBelongsToDifferentStore | ``` var EKErrorObjectBelongsToDifferentStore: EKErrorCode { get } ``` | iOS 8.0 |
| To | ObjectBelongsToDifferentStore | ``` case ObjectBelongsToDifferentStore ``` | iOS 9.0 |

Modified [EKErrorCode.PriorityIsInvalid](https://developer.apple.com/documentation/eventkit/ekerror/code/priorityisinvalid)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | EKErrorPriorityIsInvalid | ``` var EKErrorPriorityIsInvalid: EKErrorCode { get } ``` | iOS 8.0 |
| To | PriorityIsInvalid | ``` case PriorityIsInvalid ``` | iOS 9.0 |

Modified [EKErrorCode.RecurringReminderRequiresDueDate](https://developer.apple.com/documentation/eventkit/ekerror/code/recurringreminderrequiresduedate)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | EKErrorRecurringReminderRequiresDueDate | ``` var EKErrorRecurringReminderRequiresDueDate: EKErrorCode { get } ``` | iOS 8.0 |
| To | RecurringReminderRequiresDueDate | ``` case RecurringReminderRequiresDueDate ``` | iOS 9.0 |

Modified [EKErrorCode.ReminderLocationsNotSupported](https://developer.apple.com/documentation/eventkit/ekerror/code/reminderlocationsnotsupported)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | EKErrorReminderLocationsNotSupported | ``` var EKErrorReminderLocationsNotSupported: EKErrorCode { get } ``` | iOS 8.0 |
| To | ReminderLocationsNotSupported | ``` case ReminderLocationsNotSupported ``` | iOS 9.0 |

Modified [EKErrorCode.SourceDoesNotAllowCalendarAddDelete](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerrorsourcedoesnotallowcalendaradddelete)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | EKErrorSourceDoesNotAllowCalendarAddDelete | ``` var EKErrorSourceDoesNotAllowCalendarAddDelete: EKErrorCode { get } ``` | iOS 8.0 |
| To | SourceDoesNotAllowCalendarAddDelete | ``` case SourceDoesNotAllowCalendarAddDelete ``` | iOS 9.0 |

Modified [EKErrorCode.SourceDoesNotAllowReminders](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerrorsourcedoesnotallowreminders)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | EKErrorSourceDoesNotAllowReminders | ``` var EKErrorSourceDoesNotAllowReminders: EKErrorCode { get } ``` | iOS 8.0 |
| To | SourceDoesNotAllowReminders | ``` case SourceDoesNotAllowReminders ``` | iOS 9.0 |

Modified [EKErrorCode.StartDateCollidesWithOtherOccurrence](https://developer.apple.com/documentation/eventkit/ekerror/code/startdatecollideswithotheroccurrence)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | EKErrorStartDateCollidesWithOtherOccurrence | ``` var EKErrorStartDateCollidesWithOtherOccurrence: EKErrorCode { get } ``` | iOS 8.0 |
| To | StartDateCollidesWithOtherOccurrence | ``` case StartDateCollidesWithOtherOccurrence ``` | iOS 9.0 |

Modified [EKErrorCode.StartDateTooFarInFuture](https://developer.apple.com/documentation/eventkit/ekerror/code/startdatetoofarinfuture)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | EKErrorStartDateTooFarInFuture | ``` var EKErrorStartDateTooFarInFuture: EKErrorCode { get } ``` | iOS 8.0 |
| To | StartDateTooFarInFuture | ``` case StartDateTooFarInFuture ``` | iOS 9.0 |

Modified [EKErrorCode.StructuredLocationsNotSupported](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerrorstructuredlocationsnotsupported)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | EKErrorStructuredLocationsNotSupported | ``` var EKErrorStructuredLocationsNotSupported: EKErrorCode { get } ``` | iOS 8.0 |
| To | StructuredLocationsNotSupported | ``` case StructuredLocationsNotSupported ``` | iOS 9.0 |

Modified [EKEvent](https://developer.apple.com/documentation/eventkit/ekevent)

|  | Declaration |
| --- | --- |
| From | ``` class EKEvent : EKCalendarItem {     init!(eventStore eventStore: EKEventStore!) -> EKEvent     class func eventWithEventStore(_ eventStore: EKEventStore!) -> EKEvent!     var eventIdentifier: String! { get }     var allDay: Bool     @NSCopying var startDate: NSDate!     @NSCopying var endDate: NSDate!     func compareStartDateWithEvent(_ other: EKEvent!) -> NSComparisonResult     var organizer: EKParticipant! { get }     var availability: EKEventAvailability     var status: EKEventStatus { get }     var isDetached: Bool { get }     func refresh() -> Bool     var birthdayPersonID: Int { get } } ``` |
| To | ``` class EKEvent : EKCalendarItem {      init(eventStore eventStore: EKEventStore)     class func eventWithEventStore(_ eventStore: EKEventStore) -> EKEvent     var eventIdentifier: String { get }     var allDay: Bool     @NSCopying var startDate: NSDate     @NSCopying var endDate: NSDate     @NSCopying var structuredLocation: EKStructuredLocation?     func compareStartDateWithEvent(_ other: EKEvent) -> NSComparisonResult     var organizer: EKParticipant? { get }     var availability: EKEventAvailability     var status: EKEventStatus { get }     var isDetached: Bool { get }     var occurrenceDate: NSDate { get }     func refresh() -> Bool     var birthdayContactIdentifier: String? { get }     var birthdayPersonID: Int { get }     var birthdayPersonUniqueID: String? { get } } ``` |

Modified [EKEvent.birthdayPersonID](https://developer.apple.com/documentation/eventkit/ekevent/1615845-birthdaypersonid)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [EKEvent.compareStartDateWithEvent(_: EKEvent) -> NSComparisonResult](https://developer.apple.com/documentation/eventkit/ekevent/1507335-comparestartdatewithevent)

|  | Declaration |
| --- | --- |
| From | ``` func compareStartDateWithEvent(_ other: EKEvent!) -> NSComparisonResult ``` |
| To | ``` func compareStartDateWithEvent(_ other: EKEvent) -> NSComparisonResult ``` |

Modified [EKEvent.endDate](https://developer.apple.com/documentation/eventkit/ekevent/1507121-enddate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var endDate: NSDate! ``` |
| To | ``` @NSCopying var endDate: NSDate ``` |

Modified [EKEvent.eventIdentifier](https://developer.apple.com/documentation/eventkit/ekevent/1507437-eventidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var eventIdentifier: String! { get } ``` |
| To | ``` var eventIdentifier: String { get } ``` |

Modified [EKEvent.init(eventStore: EKEventStore)](https://developer.apple.com/documentation/eventkit/ekevent/1507483-eventwitheventstore)

|  | Declaration |
| --- | --- |
| From | ``` init!(eventStore eventStore: EKEventStore!) -> EKEvent ``` |
| To | ``` init(eventStore eventStore: EKEventStore) ``` |

Modified [EKEvent.organizer](https://developer.apple.com/documentation/eventkit/ekevent/1507357-organizer)

|  | Declaration |
| --- | --- |
| From | ``` var organizer: EKParticipant! { get } ``` |
| To | ``` var organizer: EKParticipant? { get } ``` |

Modified [EKEvent.startDate](https://developer.apple.com/documentation/eventkit/ekevent/1507372-startdate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var startDate: NSDate! ``` |
| To | ``` @NSCopying var startDate: NSDate ``` |

Modified [EKEventStore](https://developer.apple.com/documentation/eventkit/ekeventstore)

|  | Declaration |
| --- | --- |
| From | ``` class EKEventStore : NSObject {     class func authorizationStatusForEntityType(_ entityType: EKEntityType) -> EKAuthorizationStatus     func requestAccessToEntityType(_ entityType: EKEntityType, completion completion: EKEventStoreRequestAccessCompletionHandler!)     var eventStoreIdentifier: String! { get }     func sources() -> [AnyObject]!     func sourceWithIdentifier(_ identifier: String!) -> EKSource!     var calendars: [AnyObject]! { get }     func calendarsForEntityType(_ entityType: EKEntityType) -> [AnyObject]!     var defaultCalendarForNewEvents: EKCalendar! { get }     func defaultCalendarForNewReminders() -> EKCalendar!     func calendarWithIdentifier(_ identifier: String!) -> EKCalendar!     func saveCalendar(_ calendar: EKCalendar!, commit commit: Bool, error error: NSErrorPointer) -> Bool     func removeCalendar(_ calendar: EKCalendar!, commit commit: Bool, error error: NSErrorPointer) -> Bool     func calendarItemWithIdentifier(_ identifier: String!) -> EKCalendarItem!     func calendarItemsWithExternalIdentifier(_ externalIdentifier: String!) -> [AnyObject]!     func saveEvent(_ event: EKEvent!, span span: EKSpan, error error: NSErrorPointer) -> Bool     func removeEvent(_ event: EKEvent!, span span: EKSpan, error error: NSErrorPointer) -> Bool     func saveEvent(_ event: EKEvent!, span span: EKSpan, commit commit: Bool, error error: NSErrorPointer) -> Bool     func removeEvent(_ event: EKEvent!, span span: EKSpan, commit commit: Bool, error error: NSErrorPointer) -> Bool     func eventWithIdentifier(_ identifier: String!) -> EKEvent!     func eventsMatchingPredicate(_ predicate: NSPredicate!) -> [AnyObject]!     func enumerateEventsMatchingPredicate(_ predicate: NSPredicate!, usingBlock block: EKEventSearchCallback!)     func predicateForEventsWithStartDate(_ startDate: NSDate!, endDate endDate: NSDate!, calendars calendars: [AnyObject]!) -> NSPredicate!     func saveReminder(_ reminder: EKReminder!, commit commit: Bool, error error: NSErrorPointer) -> Bool     func removeReminder(_ reminder: EKReminder!, commit commit: Bool, error error: NSErrorPointer) -> Bool     func fetchRemindersMatchingPredicate(_ predicate: NSPredicate!, completion completion: (([AnyObject]!) -> Void)!) -> AnyObject!     func cancelFetchRequest(_ fetchIdentifier: AnyObject!)     func predicateForRemindersInCalendars(_ calendars: [AnyObject]!) -> NSPredicate!     func predicateForIncompleteRemindersWithDueDateStarting(_ startDate: NSDate!, ending endDate: NSDate!, calendars calendars: [AnyObject]!) -> NSPredicate!     func predicateForCompletedRemindersWithCompletionDateStarting(_ startDate: NSDate!, ending endDate: NSDate!, calendars calendars: [AnyObject]!) -> NSPredicate!     func commit(_ error: NSErrorPointer) -> Bool     func reset()     func refreshSourcesIfNecessary() } ``` |
| To | ``` class EKEventStore : NSObject {     class func authorizationStatusForEntityType(_ entityType: EKEntityType) -> EKAuthorizationStatus     init(accessToEntityTypes entityTypes: EKEntityMask)     init()     init(sources sources: [EKSource])     func requestAccessToEntityType(_ entityType: EKEntityType, completion completion: EKEventStoreRequestAccessCompletionHandler)     var eventStoreIdentifier: String { get }     var delegateSources: [EKSource] { get }     var sources: [EKSource] { get }     func sourceWithIdentifier(_ identifier: String) -> EKSource     var calendars: [EKCalendar] { get }     func calendarsForEntityType(_ entityType: EKEntityType) -> [EKCalendar]     var defaultCalendarForNewEvents: EKCalendar { get }     func defaultCalendarForNewReminders() -> EKCalendar     func calendarWithIdentifier(_ identifier: String) -> EKCalendar?     func saveCalendar(_ calendar: EKCalendar, commit commit: Bool) throws     func removeCalendar(_ calendar: EKCalendar, commit commit: Bool) throws     func calendarItemWithIdentifier(_ identifier: String) -> EKCalendarItem     func calendarItemsWithExternalIdentifier(_ externalIdentifier: String) -> [EKCalendarItem]     func saveEvent(_ event: EKEvent, span span: EKSpan) throws     func removeEvent(_ event: EKEvent, span span: EKSpan) throws     func saveEvent(_ event: EKEvent, span span: EKSpan, commit commit: Bool) throws     func removeEvent(_ event: EKEvent, span span: EKSpan, commit commit: Bool) throws     func eventWithIdentifier(_ identifier: String) -> EKEvent?     func eventsMatchingPredicate(_ predicate: NSPredicate) -> [EKEvent]     func enumerateEventsMatchingPredicate(_ predicate: NSPredicate, usingBlock block: EKEventSearchCallback)     func predicateForEventsWithStartDate(_ startDate: NSDate, endDate endDate: NSDate, calendars calendars: [EKCalendar]?) -> NSPredicate     func saveReminder(_ reminder: EKReminder, commit commit: Bool) throws     func removeReminder(_ reminder: EKReminder, commit commit: Bool) throws     func fetchRemindersMatchingPredicate(_ predicate: NSPredicate, completion completion: ([EKReminder]?) -> Void) -> AnyObject     func cancelFetchRequest(_ fetchIdentifier: AnyObject)     func predicateForRemindersInCalendars(_ calendars: [EKCalendar]?) -> NSPredicate     func predicateForIncompleteRemindersWithDueDateStarting(_ startDate: NSDate?, ending endDate: NSDate?, calendars calendars: [EKCalendar]?) -> NSPredicate     func predicateForCompletedRemindersWithCompletionDateStarting(_ startDate: NSDate?, ending endDate: NSDate?, calendars calendars: [EKCalendar]?) -> NSPredicate     func commit() throws     func reset()     func refreshSourcesIfNecessary() } ``` |

Modified [EKEventStore.calendarItemsWithExternalIdentifier(_: String) -> [EKCalendarItem]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507281-calendaritems)

|  | Declaration |
| --- | --- |
| From | ``` func calendarItemsWithExternalIdentifier(_ externalIdentifier: String!) -> [AnyObject]! ``` |
| To | ``` func calendarItemsWithExternalIdentifier(_ externalIdentifier: String) -> [EKCalendarItem] ``` |

Modified [EKEventStore.calendarItemWithIdentifier(_: String) -> EKCalendarItem](https://developer.apple.com/documentation/eventkit/ekeventstore/1507433-calendaritemwithidentifier)

|  | Declaration |
| --- | --- |
| From | ``` func calendarItemWithIdentifier(_ identifier: String!) -> EKCalendarItem! ``` |
| To | ``` func calendarItemWithIdentifier(_ identifier: String) -> EKCalendarItem ``` |

Modified [EKEventStore.calendarsForEntityType(_: EKEntityType) -> [EKCalendar]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507128-calendarsforentitytype)

|  | Declaration |
| --- | --- |
| From | ``` func calendarsForEntityType(_ entityType: EKEntityType) -> [AnyObject]! ``` |
| To | ``` func calendarsForEntityType(_ entityType: EKEntityType) -> [EKCalendar] ``` |

Modified [EKEventStore.calendarWithIdentifier(_: String) -> EKCalendar?](https://developer.apple.com/documentation/eventkit/ekeventstore/1507484-calendar)

|  | Declaration |
| --- | --- |
| From | ``` func calendarWithIdentifier(_ identifier: String!) -> EKCalendar! ``` |
| To | ``` func calendarWithIdentifier(_ identifier: String) -> EKCalendar? ``` |

Modified [EKEventStore.cancelFetchRequest(_: AnyObject)](https://developer.apple.com/documentation/eventkit/ekeventstore/1507342-cancelfetchrequest)

|  | Declaration |
| --- | --- |
| From | ``` func cancelFetchRequest(_ fetchIdentifier: AnyObject!) ``` |
| To | ``` func cancelFetchRequest(_ fetchIdentifier: AnyObject) ``` |

Modified [EKEventStore.commit() throws](https://developer.apple.com/documentation/eventkit/ekeventstore/1507424-commit)

|  | Declaration |
| --- | --- |
| From | ``` func commit(_ error: NSErrorPointer) -> Bool ``` |
| To | ``` func commit() throws ``` |

Modified [EKEventStore.defaultCalendarForNewEvents](https://developer.apple.com/documentation/eventkit/ekeventstore/1507062-defaultcalendarfornewevents)

|  | Declaration |
| --- | --- |
| From | ``` var defaultCalendarForNewEvents: EKCalendar! { get } ``` |
| To | ``` var defaultCalendarForNewEvents: EKCalendar { get } ``` |

Modified [EKEventStore.defaultCalendarForNewReminders() -> EKCalendar](https://developer.apple.com/documentation/eventkit/ekeventstore/1507543-defaultcalendarfornewreminders)

|  | Declaration |
| --- | --- |
| From | ``` func defaultCalendarForNewReminders() -> EKCalendar! ``` |
| To | ``` func defaultCalendarForNewReminders() -> EKCalendar ``` |

Modified [EKEventStore.enumerateEventsMatchingPredicate(_: NSPredicate, usingBlock: EKEventSearchCallback)](https://developer.apple.com/documentation/eventkit/ekeventstore/1507518-enumerateeventsmatchingpredicate)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateEventsMatchingPredicate(_ predicate: NSPredicate!, usingBlock block: EKEventSearchCallback!) ``` |
| To | ``` func enumerateEventsMatchingPredicate(_ predicate: NSPredicate, usingBlock block: EKEventSearchCallback) ``` |

Modified [EKEventStore.eventsMatchingPredicate(_: NSPredicate) -> [EKEvent]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507183-eventsmatchingpredicate)

|  | Declaration |
| --- | --- |
| From | ``` func eventsMatchingPredicate(_ predicate: NSPredicate!) -> [AnyObject]! ``` |
| To | ``` func eventsMatchingPredicate(_ predicate: NSPredicate) -> [EKEvent] ``` |

Modified [EKEventStore.eventStoreIdentifier](https://developer.apple.com/documentation/eventkit/ekeventstore/1507442-eventstoreidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var eventStoreIdentifier: String! { get } ``` |
| To | ``` var eventStoreIdentifier: String { get } ``` |

Modified [EKEventStore.eventWithIdentifier(_: String) -> EKEvent?](https://developer.apple.com/documentation/eventkit/ekeventstore/1507490-event)

|  | Declaration |
| --- | --- |
| From | ``` func eventWithIdentifier(_ identifier: String!) -> EKEvent! ``` |
| To | ``` func eventWithIdentifier(_ identifier: String) -> EKEvent? ``` |

Modified [EKEventStore.fetchRemindersMatchingPredicate(_: NSPredicate, completion: ([EKReminder]?) -> Void) -> AnyObject](https://developer.apple.com/documentation/eventkit/ekeventstore/1507500-fetchreminders)

|  | Declaration |
| --- | --- |
| From | ``` func fetchRemindersMatchingPredicate(_ predicate: NSPredicate!, completion completion: (([AnyObject]!) -> Void)!) -> AnyObject! ``` |
| To | ``` func fetchRemindersMatchingPredicate(_ predicate: NSPredicate, completion completion: ([EKReminder]?) -> Void) -> AnyObject ``` |

Modified [EKEventStore.predicateForCompletedRemindersWithCompletionDateStarting(_: NSDate?, ending: NSDate?, calendars: [EKCalendar]?) -> NSPredicate](https://developer.apple.com/documentation/eventkit/ekeventstore/1507447-predicateforcompletedreminderswi)

|  | Declaration |
| --- | --- |
| From | ``` func predicateForCompletedRemindersWithCompletionDateStarting(_ startDate: NSDate!, ending endDate: NSDate!, calendars calendars: [AnyObject]!) -> NSPredicate! ``` |
| To | ``` func predicateForCompletedRemindersWithCompletionDateStarting(_ startDate: NSDate?, ending endDate: NSDate?, calendars calendars: [EKCalendar]?) -> NSPredicate ``` |

Modified [EKEventStore.predicateForEventsWithStartDate(_: NSDate, endDate: NSDate, calendars: [EKCalendar]?) -> NSPredicate](https://developer.apple.com/documentation/eventkit/ekeventstore/1507479-predicateforevents)

|  | Declaration |
| --- | --- |
| From | ``` func predicateForEventsWithStartDate(_ startDate: NSDate!, endDate endDate: NSDate!, calendars calendars: [AnyObject]!) -> NSPredicate! ``` |
| To | ``` func predicateForEventsWithStartDate(_ startDate: NSDate, endDate endDate: NSDate, calendars calendars: [EKCalendar]?) -> NSPredicate ``` |

Modified [EKEventStore.predicateForIncompleteRemindersWithDueDateStarting(_: NSDate?, ending: NSDate?, calendars: [EKCalendar]?) -> NSPredicate](https://developer.apple.com/documentation/eventkit/ekeventstore/1507143-predicateforincompleteremindersw)

|  | Declaration |
| --- | --- |
| From | ``` func predicateForIncompleteRemindersWithDueDateStarting(_ startDate: NSDate!, ending endDate: NSDate!, calendars calendars: [AnyObject]!) -> NSPredicate! ``` |
| To | ``` func predicateForIncompleteRemindersWithDueDateStarting(_ startDate: NSDate?, ending endDate: NSDate?, calendars calendars: [EKCalendar]?) -> NSPredicate ``` |

Modified [EKEventStore.predicateForRemindersInCalendars(_: [EKCalendar]?) -> NSPredicate](https://developer.apple.com/documentation/eventkit/ekeventstore/1507086-predicateforreminders)

|  | Declaration |
| --- | --- |
| From | ``` func predicateForRemindersInCalendars(_ calendars: [AnyObject]!) -> NSPredicate! ``` |
| To | ``` func predicateForRemindersInCalendars(_ calendars: [EKCalendar]?) -> NSPredicate ``` |

Modified [EKEventStore.removeCalendar(_: EKCalendar, commit: Bool) throws](https://developer.apple.com/documentation/eventkit/ekeventstore/1507523-removecalendar)

|  | Declaration |
| --- | --- |
| From | ``` func removeCalendar(_ calendar: EKCalendar!, commit commit: Bool, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func removeCalendar(_ calendar: EKCalendar, commit commit: Bool) throws ``` |

Modified [EKEventStore.removeEvent(_: EKEvent, span: EKSpan) throws](https://developer.apple.com/documentation/eventkit/ekeventstore/1615882-removeevent)

|  | Declaration |
| --- | --- |
| From | ``` func removeEvent(_ event: EKEvent!, span span: EKSpan, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func removeEvent(_ event: EKEvent, span span: EKSpan) throws ``` |

Modified [EKEventStore.removeEvent(_: EKEvent, span: EKSpan, commit: Bool) throws](https://developer.apple.com/documentation/eventkit/ekeventstore/1507469-remove)

|  | Declaration |
| --- | --- |
| From | ``` func removeEvent(_ event: EKEvent!, span span: EKSpan, commit commit: Bool, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func removeEvent(_ event: EKEvent, span span: EKSpan, commit commit: Bool) throws ``` |

Modified [EKEventStore.removeReminder(_: EKReminder, commit: Bool) throws](https://developer.apple.com/documentation/eventkit/ekeventstore/1507108-removereminder)

|  | Declaration |
| --- | --- |
| From | ``` func removeReminder(_ reminder: EKReminder!, commit commit: Bool, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func removeReminder(_ reminder: EKReminder, commit commit: Bool) throws ``` |

Modified [EKEventStore.requestAccessToEntityType(_: EKEntityType, completion: EKEventStoreRequestAccessCompletionHandler)](https://developer.apple.com/documentation/eventkit/ekeventstore/1507547-requestaccesstoentitytype)

|  | Declaration |
| --- | --- |
| From | ``` func requestAccessToEntityType(_ entityType: EKEntityType, completion completion: EKEventStoreRequestAccessCompletionHandler!) ``` |
| To | ``` func requestAccessToEntityType(_ entityType: EKEntityType, completion completion: EKEventStoreRequestAccessCompletionHandler) ``` |

Modified [EKEventStore.saveCalendar(_: EKCalendar, commit: Bool) throws](https://developer.apple.com/documentation/eventkit/ekeventstore/1507080-savecalendar)

|  | Declaration |
| --- | --- |
| From | ``` func saveCalendar(_ calendar: EKCalendar!, commit commit: Bool, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func saveCalendar(_ calendar: EKCalendar, commit commit: Bool) throws ``` |

Modified [EKEventStore.saveEvent(_: EKEvent, span: EKSpan) throws](https://developer.apple.com/documentation/eventkit/ekeventstore/1615881-save)

|  | Declaration |
| --- | --- |
| From | ``` func saveEvent(_ event: EKEvent!, span span: EKSpan, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func saveEvent(_ event: EKEvent, span span: EKSpan) throws ``` |

Modified [EKEventStore.saveEvent(_: EKEvent, span: EKSpan, commit: Bool) throws](https://developer.apple.com/documentation/eventkit/ekeventstore/1507295-save)

|  | Declaration |
| --- | --- |
| From | ``` func saveEvent(_ event: EKEvent!, span span: EKSpan, commit commit: Bool, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func saveEvent(_ event: EKEvent, span span: EKSpan, commit commit: Bool) throws ``` |

Modified [EKEventStore.saveReminder(_: EKReminder, commit: Bool) throws](https://developer.apple.com/documentation/eventkit/ekeventstore/1507181-save)

|  | Declaration |
| --- | --- |
| From | ``` func saveReminder(_ reminder: EKReminder!, commit commit: Bool, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func saveReminder(_ reminder: EKReminder, commit commit: Bool) throws ``` |

Modified [EKEventStore.sourceWithIdentifier(_: String) -> EKSource](https://developer.apple.com/documentation/eventkit/ekeventstore/1507521-sourcewithidentifier)

|  | Declaration |
| --- | --- |
| From | ``` func sourceWithIdentifier(_ identifier: String!) -> EKSource! ``` |
| To | ``` func sourceWithIdentifier(_ identifier: String) -> EKSource ``` |

Modified [EKObject](https://developer.apple.com/documentation/eventkit/ekobject)

|  | Declaration |
| --- | --- |
| From | ``` class EKObject : NSObject {     func hasChanges() -> Bool     func isNew() -> Bool     func reset()     func rollback()     func refresh() -> Bool } ``` |
| To | ``` class EKObject : NSObject {     var hasChanges: Bool { get }     var new: Bool { get }     func reset()     func rollback()     func refresh() -> Bool } ``` |

Modified [EKParticipant](https://developer.apple.com/documentation/eventkit/ekparticipant)

|  | Declaration |
| --- | --- |
| From | ``` class EKParticipant : EKObject, NSCopying {     var URL: NSURL! { get }     var name: String! { get }     var participantStatus: EKParticipantStatus { get }     var participantRole: EKParticipantRole { get }     var participantType: EKParticipantType { get }     var isCurrentUser: Bool { get }     func ABRecordWithAddressBook(_ addressBook: ABAddressBook!) -> Unmanaged<ABRecord>! } ``` |
| To | ``` class EKParticipant : EKObject, NSCopying {     var URL: NSURL { get }     var name: String? { get }     var participantStatus: EKParticipantStatus { get }     var participantRole: EKParticipantRole { get }     var participantType: EKParticipantType { get }     var currentUser: Bool { get }     var contactPredicate: NSPredicate { get }     func ABRecordWithAddressBook(_ addressBook: ABAddressBook) -> ABRecord? } ``` |

Modified [EKParticipant.ABRecordWithAddressBook(_: ABAddressBook) -> ABRecord?](https://developer.apple.com/documentation/eventkit/ekparticipant/1615895-abrecordwithaddressbook)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func ABRecordWithAddressBook(_ addressBook: ABAddressBook!) -> Unmanaged<ABRecord>! ``` | -- |
| To | ``` func ABRecordWithAddressBook(_ addressBook: ABAddressBook) -> ABRecord? ``` | iOS 9.0 |

Modified [EKParticipant.name](https://developer.apple.com/documentation/eventkit/ekparticipant/1507480-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String? { get } ``` |

Modified [EKParticipant.URL](https://developer.apple.com/documentation/eventkit/ekparticipant/1507435-url)

|  | Declaration |
| --- | --- |
| From | ``` var URL: NSURL! { get } ``` |
| To | ``` var URL: NSURL { get } ``` |

Modified [EKRecurrenceDayOfWeek](https://developer.apple.com/documentation/eventkit/ekrecurrencedayofweek)

|  | Declaration |
| --- | --- |
| From | ``` class EKRecurrenceDayOfWeek : NSObject, NSCopying {     init!(_ dayOfTheWeek: Int) -> EKRecurrenceDayOfWeek     class func dayOfWeek(_ dayOfTheWeek: Int) -> EKRecurrenceDayOfWeek!     init!(_ dayOfTheWeek: Int, weekNumber weekNumber: Int) -> EKRecurrenceDayOfWeek     class func dayOfWeek(_ dayOfTheWeek: Int, weekNumber weekNumber: Int) -> EKRecurrenceDayOfWeek!     init!(dayOfTheWeek dayOfTheWeek: Int, weekNumber weekNumber: Int)     var dayOfTheWeek: Int { get }     var weekNumber: Int { get } } ``` |
| To | ``` class EKRecurrenceDayOfWeek : NSObject, NSCopying {     convenience init(_ dayOfTheWeek: EKWeekday)     class func dayOfWeek(_ dayOfTheWeek: EKWeekday) -> Self     convenience init(_ dayOfTheWeek: EKWeekday, weekNumber weekNumber: Int)     class func dayOfWeek(_ dayOfTheWeek: EKWeekday, weekNumber weekNumber: Int) -> Self     init(dayOfTheWeek dayOfTheWeek: EKWeekday, weekNumber weekNumber: Int)     var dayOfTheWeek: EKWeekday { get }     var weekNumber: Int { get } } ``` |

Modified [EKRecurrenceDayOfWeek.dayOfTheWeek](https://developer.apple.com/documentation/eventkit/ekrecurrencedayofweek/1448579-dayoftheweek)

|  | Declaration |
| --- | --- |
| From | ``` var dayOfTheWeek: Int { get } ``` |
| To | ``` var dayOfTheWeek: EKWeekday { get } ``` |

Modified [EKRecurrenceDayOfWeek.init(_: EKWeekday)](https://developer.apple.com/documentation/eventkit/ekrecurrencedayofweek/1448589-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(_ dayOfTheWeek: Int) -> EKRecurrenceDayOfWeek ``` |
| To | ``` convenience init(_ dayOfTheWeek: EKWeekday) ``` |

Modified [EKRecurrenceDayOfWeek.init(_: EKWeekday, weekNumber: Int)](https://developer.apple.com/documentation/eventkit/ekrecurrencedayofweek/1448591-dayofweek)

|  | Declaration |
| --- | --- |
| From | ``` init!(_ dayOfTheWeek: Int, weekNumber weekNumber: Int) -> EKRecurrenceDayOfWeek ``` |
| To | ``` convenience init(_ dayOfTheWeek: EKWeekday, weekNumber weekNumber: Int) ``` |

Modified [EKRecurrenceDayOfWeek.init(dayOfTheWeek: EKWeekday, weekNumber: Int)](https://developer.apple.com/documentation/eventkit/ekrecurrencedayofweek/1448581-initwithdayoftheweek)

|  | Declaration |
| --- | --- |
| From | ``` init!(dayOfTheWeek dayOfTheWeek: Int, weekNumber weekNumber: Int) ``` |
| To | ``` init(dayOfTheWeek dayOfTheWeek: EKWeekday, weekNumber weekNumber: Int) ``` |

Modified [EKRecurrenceEnd](https://developer.apple.com/documentation/eventkit/ekrecurrenceend)

|  | Declaration |
| --- | --- |
| From | ``` class EKRecurrenceEnd : NSObject, NSCopying {     class func recurrenceEndWithEndDate(_ endDate: NSDate!) -> AnyObject!     class func recurrenceEndWithOccurrenceCount(_ occurrenceCount: Int) -> AnyObject!     var endDate: NSDate! { get }     var occurrenceCount: Int { get } } ``` |
| To | ``` class EKRecurrenceEnd : NSObject, NSCopying {     convenience init(endDate endDate: NSDate)     class func recurrenceEndWithEndDate(_ endDate: NSDate) -> Self     convenience init(occurrenceCount occurrenceCount: Int)     class func recurrenceEndWithOccurrenceCount(_ occurrenceCount: Int) -> Self     var endDate: NSDate? { get }     var occurrenceCount: Int { get } } ``` |

Modified [EKRecurrenceEnd.endDate](https://developer.apple.com/documentation/eventkit/ekrecurrenceend/1415648-enddate)

|  | Declaration |
| --- | --- |
| From | ``` var endDate: NSDate! { get } ``` |
| To | ``` var endDate: NSDate? { get } ``` |

Modified [EKRecurrenceEnd.init(endDate: NSDate)](https://developer.apple.com/documentation/eventkit/ekrecurrenceend/1415644-init)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | recurrenceEndWithEndDate(_:) | ``` class func recurrenceEndWithEndDate(_ endDate: NSDate!) -> AnyObject! ``` | iOS 8.0 |
| To | init(endDate:) | ``` convenience init(endDate endDate: NSDate) ``` | iOS 9.0 |

Modified [EKRecurrenceEnd.init(occurrenceCount: Int)](https://developer.apple.com/documentation/eventkit/ekrecurrenceend/1415640-recurrenceendwithoccurrencecount)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | recurrenceEndWithOccurrenceCount(_:) | ``` class func recurrenceEndWithOccurrenceCount(_ occurrenceCount: Int) -> AnyObject! ``` | iOS 8.0 |
| To | init(occurrenceCount:) | ``` convenience init(occurrenceCount occurrenceCount: Int) ``` | iOS 9.0 |

Modified [EKRecurrenceRule](https://developer.apple.com/documentation/eventkit/ekrecurrencerule)

|  | Declaration |
| --- | --- |
| From | ``` class EKRecurrenceRule : EKObject, NSCopying {     init!(recurrenceWithFrequency type: EKRecurrenceFrequency, interval interval: Int, end end: EKRecurrenceEnd!)     init!(recurrenceWithFrequency type: EKRecurrenceFrequency, interval interval: Int, daysOfTheWeek days: [AnyObject]!, daysOfTheMonth monthDays: [AnyObject]!, monthsOfTheYear months: [AnyObject]!, weeksOfTheYear weeksOfTheYear: [AnyObject]!, daysOfTheYear daysOfTheYear: [AnyObject]!, setPositions setPositions: [AnyObject]!, end end: EKRecurrenceEnd!)     var calendarIdentifier: String! { get }     @NSCopying var recurrenceEnd: EKRecurrenceEnd!     var frequency: EKRecurrenceFrequency { get }     var interval: Int { get }     var firstDayOfTheWeek: Int { get }     var daysOfTheWeek: [AnyObject]! { get }     var daysOfTheMonth: [AnyObject]! { get }     var daysOfTheYear: [AnyObject]! { get }     var weeksOfTheYear: [AnyObject]! { get }     var monthsOfTheYear: [AnyObject]! { get }     var setPositions: [AnyObject]! { get } } ``` |
| To | ``` class EKRecurrenceRule : EKObject, NSCopying {     init(recurrenceWithFrequency type: EKRecurrenceFrequency, interval interval: Int, end end: EKRecurrenceEnd?)     init(recurrenceWithFrequency type: EKRecurrenceFrequency, interval interval: Int, daysOfTheWeek days: [EKRecurrenceDayOfWeek]?, daysOfTheMonth monthDays: [NSNumber]?, monthsOfTheYear months: [NSNumber]?, weeksOfTheYear weeksOfTheYear: [NSNumber]?, daysOfTheYear daysOfTheYear: [NSNumber]?, setPositions setPositions: [NSNumber]?, end end: EKRecurrenceEnd?)     var calendarIdentifier: String { get }     @NSCopying var recurrenceEnd: EKRecurrenceEnd?     var frequency: EKRecurrenceFrequency { get }     var interval: Int { get }     var firstDayOfTheWeek: Int { get }     var daysOfTheWeek: [EKRecurrenceDayOfWeek]? { get }     var daysOfTheMonth: [NSNumber]? { get }     var daysOfTheYear: [NSNumber]? { get }     var weeksOfTheYear: [NSNumber]? { get }     var monthsOfTheYear: [NSNumber]? { get }     var setPositions: [NSNumber]? { get } } ``` |

Modified [EKRecurrenceRule.calendarIdentifier](https://developer.apple.com/documentation/eventkit/ekrecurrencerule/1507340-calendaridentifier)

|  | Declaration |
| --- | --- |
| From | ``` var calendarIdentifier: String! { get } ``` |
| To | ``` var calendarIdentifier: String { get } ``` |

Modified [EKRecurrenceRule.daysOfTheMonth](https://developer.apple.com/documentation/eventkit/ekrecurrencerule/1507410-daysofthemonth)

|  | Declaration |
| --- | --- |
| From | ``` var daysOfTheMonth: [AnyObject]! { get } ``` |
| To | ``` var daysOfTheMonth: [NSNumber]? { get } ``` |

Modified [EKRecurrenceRule.daysOfTheWeek](https://developer.apple.com/documentation/eventkit/ekrecurrencerule/1507538-daysoftheweek)

|  | Declaration |
| --- | --- |
| From | ``` var daysOfTheWeek: [AnyObject]! { get } ``` |
| To | ``` var daysOfTheWeek: [EKRecurrenceDayOfWeek]? { get } ``` |

Modified [EKRecurrenceRule.daysOfTheYear](https://developer.apple.com/documentation/eventkit/ekrecurrencerule/1507439-daysoftheyear)

|  | Declaration |
| --- | --- |
| From | ``` var daysOfTheYear: [AnyObject]! { get } ``` |
| To | ``` var daysOfTheYear: [NSNumber]? { get } ``` |

Modified [EKRecurrenceRule.init(recurrenceWithFrequency: EKRecurrenceFrequency, interval: Int, daysOfTheWeek: [EKRecurrenceDayOfWeek]?, daysOfTheMonth: [NSNumber]?, monthsOfTheYear: [NSNumber]?, weeksOfTheYear: [NSNumber]?, daysOfTheYear: [NSNumber]?, setPositions: [NSNumber]?, end: EKRecurrenceEnd?)](https://developer.apple.com/documentation/eventkit/ekrecurrencerule/1507320-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(recurrenceWithFrequency type: EKRecurrenceFrequency, interval interval: Int, daysOfTheWeek days: [AnyObject]!, daysOfTheMonth monthDays: [AnyObject]!, monthsOfTheYear months: [AnyObject]!, weeksOfTheYear weeksOfTheYear: [AnyObject]!, daysOfTheYear daysOfTheYear: [AnyObject]!, setPositions setPositions: [AnyObject]!, end end: EKRecurrenceEnd!) ``` |
| To | ``` init(recurrenceWithFrequency type: EKRecurrenceFrequency, interval interval: Int, daysOfTheWeek days: [EKRecurrenceDayOfWeek]?, daysOfTheMonth monthDays: [NSNumber]?, monthsOfTheYear months: [NSNumber]?, weeksOfTheYear weeksOfTheYear: [NSNumber]?, daysOfTheYear daysOfTheYear: [NSNumber]?, setPositions setPositions: [NSNumber]?, end end: EKRecurrenceEnd?) ``` |

Modified [EKRecurrenceRule.init(recurrenceWithFrequency: EKRecurrenceFrequency, interval: Int, end: EKRecurrenceEnd?)](https://developer.apple.com/documentation/eventkit/ekrecurrencerule/1507273-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(recurrenceWithFrequency type: EKRecurrenceFrequency, interval interval: Int, end end: EKRecurrenceEnd!) ``` |
| To | ``` init(recurrenceWithFrequency type: EKRecurrenceFrequency, interval interval: Int, end end: EKRecurrenceEnd?) ``` |

Modified [EKRecurrenceRule.monthsOfTheYear](https://developer.apple.com/documentation/eventkit/ekrecurrencerule/1507449-monthsoftheyear)

|  | Declaration |
| --- | --- |
| From | ``` var monthsOfTheYear: [AnyObject]! { get } ``` |
| To | ``` var monthsOfTheYear: [NSNumber]? { get } ``` |

Modified [EKRecurrenceRule.recurrenceEnd](https://developer.apple.com/documentation/eventkit/ekrecurrencerule/1507254-recurrenceend)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var recurrenceEnd: EKRecurrenceEnd! ``` |
| To | ``` @NSCopying var recurrenceEnd: EKRecurrenceEnd? ``` |

Modified [EKRecurrenceRule.setPositions](https://developer.apple.com/documentation/eventkit/ekrecurrencerule/1507378-setpositions)

|  | Declaration |
| --- | --- |
| From | ``` var setPositions: [AnyObject]! { get } ``` |
| To | ``` var setPositions: [NSNumber]? { get } ``` |

Modified [EKRecurrenceRule.weeksOfTheYear](https://developer.apple.com/documentation/eventkit/ekrecurrencerule/1507400-weeksoftheyear)

|  | Declaration |
| --- | --- |
| From | ``` var weeksOfTheYear: [AnyObject]! { get } ``` |
| To | ``` var weeksOfTheYear: [NSNumber]? { get } ``` |

Modified [EKReminder](https://developer.apple.com/documentation/eventkit/ekreminder)

|  | Declaration |
| --- | --- |
| From | ``` class EKReminder : EKCalendarItem {     init!(eventStore eventStore: EKEventStore!) -> EKReminder     class func reminderWithEventStore(_ eventStore: EKEventStore!) -> EKReminder!     @NSCopying var startDateComponents: NSDateComponents!     @NSCopying var dueDateComponents: NSDateComponents!     var completed: Bool     @NSCopying var completionDate: NSDate!     var priority: Int } ``` |
| To | ``` class EKReminder : EKCalendarItem {      init(eventStore eventStore: EKEventStore)     class func reminderWithEventStore(_ eventStore: EKEventStore) -> EKReminder     @NSCopying var startDateComponents: NSDateComponents?     @NSCopying var dueDateComponents: NSDateComponents?     var completed: Bool     @NSCopying var completionDate: NSDate?     var priority: Int } ``` |

Modified [EKReminder.completionDate](https://developer.apple.com/documentation/eventkit/ekreminder/1507286-completiondate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var completionDate: NSDate! ``` |
| To | ``` @NSCopying var completionDate: NSDate? ``` |

Modified [EKReminder.dueDateComponents](https://developer.apple.com/documentation/eventkit/ekreminder/1507383-duedatecomponents)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var dueDateComponents: NSDateComponents! ``` |
| To | ``` @NSCopying var dueDateComponents: NSDateComponents? ``` |

Modified [EKReminder.init(eventStore: EKEventStore)](https://developer.apple.com/documentation/eventkit/ekreminder/1507429-reminderwitheventstore)

|  | Declaration |
| --- | --- |
| From | ``` init!(eventStore eventStore: EKEventStore!) -> EKReminder ``` |
| To | ``` init(eventStore eventStore: EKEventStore) ``` |

Modified [EKReminder.startDateComponents](https://developer.apple.com/documentation/eventkit/ekreminder/1507558-startdatecomponents)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var startDateComponents: NSDateComponents! ``` |
| To | ``` @NSCopying var startDateComponents: NSDateComponents? ``` |

Modified [EKSource](https://developer.apple.com/documentation/eventkit/eksource)

|  | Declaration |
| --- | --- |
| From | ``` class EKSource : EKObject {     var sourceIdentifier: String! { get }     var sourceType: EKSourceType { get }     var title: String! { get }     var calendars: Set<NSObject>! { get }     func calendarsForEntityType(_ entityType: EKEntityType) -> Set<NSObject>! } ``` |
| To | ``` class EKSource : EKObject {     var sourceIdentifier: String { get }     var sourceType: EKSourceType { get }     var title: String { get }     var calendars: Set<EKCalendar> { get }     func calendarsForEntityType(_ entityType: EKEntityType) -> Set<EKCalendar> } ``` |

Modified [EKSource.calendarsForEntityType(_: EKEntityType) -> Set<EKCalendar>](https://developer.apple.com/documentation/eventkit/eksource/1507387-calendarsforentitytype)

|  | Declaration |
| --- | --- |
| From | ``` func calendarsForEntityType(_ entityType: EKEntityType) -> Set<NSObject>! ``` |
| To | ``` func calendarsForEntityType(_ entityType: EKEntityType) -> Set<EKCalendar> ``` |

Modified [EKSource.sourceIdentifier](https://developer.apple.com/documentation/eventkit/eksource/1507275-sourceidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var sourceIdentifier: String! { get } ``` |
| To | ``` var sourceIdentifier: String { get } ``` |

Modified [EKSource.title](https://developer.apple.com/documentation/eventkit/eksource/1507385-title)

|  | Declaration |
| --- | --- |
| From | ``` var title: String! { get } ``` |
| To | ``` var title: String { get } ``` |

Modified [EKStructuredLocation](https://developer.apple.com/documentation/eventkit/ekstructuredlocation)

|  | Declaration |
| --- | --- |
| From | ``` class EKStructuredLocation : EKObject, NSCopying {     init!(title title: String!) -> EKStructuredLocation     class func locationWithTitle(_ title: String!) -> EKStructuredLocation!     var title: String!     var geoLocation: CLLocation!     var radius: Double } ``` |
| To | ``` class EKStructuredLocation : EKObject, NSCopying {     convenience init(title title: String)     class func locationWithTitle(_ title: String) -> Self     convenience init(mapItem mapItem: MKMapItem)     class func locationWithMapItem(_ mapItem: MKMapItem) -> Self     var title: String     var geoLocation: CLLocation?     var radius: Double } ``` |

Modified [EKStructuredLocation.geoLocation](https://developer.apple.com/documentation/eventkit/ekstructuredlocation/1507110-geolocation)

|  | Declaration |
| --- | --- |
| From | ``` var geoLocation: CLLocation! ``` |
| To | ``` var geoLocation: CLLocation? ``` |

Modified [EKStructuredLocation.init(title: String)](https://developer.apple.com/documentation/eventkit/ekstructuredlocation/1507366-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(title title: String!) -> EKStructuredLocation ``` |
| To | ``` convenience init(title title: String) ``` |

Modified [EKStructuredLocation.title](https://developer.apple.com/documentation/eventkit/ekstructuredlocation/1507137-title)

|  | Declaration |
| --- | --- |
| From | ``` var title: String! ``` |
| To | ``` var title: String ``` |

Modified [EKEventSearchCallback](https://developer.apple.com/documentation/eventkit/ekeventsearchcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias EKEventSearchCallback = (EKEvent!, UnsafeMutablePointer<ObjCBool>) -> Void ``` |
| To | ``` typealias EKEventSearchCallback = (EKEvent, UnsafeMutablePointer<ObjCBool>) -> Void ``` |

Modified [EKEventStoreRequestAccessCompletionHandler](https://developer.apple.com/documentation/eventkit/ekeventstorerequestaccesscompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias EKEventStoreRequestAccessCompletionHandler = (Bool, NSError!) -> Void ``` |
| To | ``` typealias EKEventStoreRequestAccessCompletionHandler = (Bool, NSError?) -> Void ``` |

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
