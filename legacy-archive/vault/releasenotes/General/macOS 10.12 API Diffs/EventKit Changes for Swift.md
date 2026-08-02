---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/EventKit.html
archived_at: '2026-07-18T02:51:16.948484Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# EventKit Changes for Swift

### EventKit

Removed [EKCalendarEventAvailabilityMask.None](https://developer.apple.com/documentation/eventkit/ekcalendareventavailabilitymask/ekcalendareventavailabilitynone)Added [EKError [struct]](https://developer.apple.com/documentation/eventkit/ekerror)Added [EKError.alarmGreaterThanRecurrence](https://developer.apple.com/documentation/eventkit/ekerror/2325704-alarmgreaterthanrecurrence)Added [EKError.alarmProximityNotSupported](https://developer.apple.com/documentation/eventkit/ekerror/2325694-alarmproximitynotsupported)Added [EKError.calendarDoesNotAllowEvents](https://developer.apple.com/documentation/eventkit/ekerror/2325681-calendardoesnotallowevents)Added [EKError.calendarDoesNotAllowReminders](https://developer.apple.com/documentation/eventkit/ekerror/2325683-calendardoesnotallowreminders)Added [EKError.calendarHasNoSource](https://developer.apple.com/documentation/eventkit/ekerror/2325696-calendarhasnosource)Added [EKError.calendarIsImmutable](https://developer.apple.com/documentation/eventkit/ekerror/2325706-calendarisimmutable)Added [EKError.calendarReadOnly](https://developer.apple.com/documentation/eventkit/ekerror/2325692-calendarreadonly)Added [EKError.calendarSourceCannotBeModified](https://developer.apple.com/documentation/eventkit/ekerror/2325684-calendarsourcecannotbemodified)Added [EKError.datesInverted](https://developer.apple.com/documentation/eventkit/ekerror/2325708-datesinverted)Added [EKError.durationGreaterThanRecurrence](https://developer.apple.com/documentation/eventkit/ekerror/2325699-durationgreaterthanrecurrence)Added [EKError.eventNotMutable](https://developer.apple.com/documentation/eventkit/ekerror/2325679-eventnotmutable)Added [EKError.eventStoreNotAuthorized](https://developer.apple.com/documentation/eventkit/ekerror/2325687-eventstorenotauthorized)Added EKError.init(_nsError: NSError)Added [EKError.internalFailure](https://developer.apple.com/documentation/eventkit/ekerror/2325695-internalfailure)Added [EKError.invalidEntityType](https://developer.apple.com/documentation/eventkit/ekerror/2325698-invalidentitytype)Added [EKError.invalidSpan](https://developer.apple.com/documentation/eventkit/ekerror/2325701-invalidspan)Added [EKError.invitesCannotBeMoved](https://developer.apple.com/documentation/eventkit/ekerror/2325690-invitescannotbemoved)Added [EKError.last](https://developer.apple.com/documentation/eventkit/ekerror/2325691-last)Added [EKError.noCalendar](https://developer.apple.com/documentation/eventkit/ekerror/2325689-nocalendar)Added [EKError.noEndDate](https://developer.apple.com/documentation/eventkit/ekerror/2325685-noenddate)Added [EKError.noStartDate](https://developer.apple.com/documentation/eventkit/ekerror/2325697-nostartdate)Added [EKError.objectBelongsToDifferentStore](https://developer.apple.com/documentation/eventkit/ekerror/2325703-objectbelongstodifferentstore)Added [EKError.osNotSupported](https://developer.apple.com/documentation/eventkit/ekerror/2325702-osnotsupported)Added [EKError.priorityIsInvalid](https://developer.apple.com/documentation/eventkit/ekerror/2325709-priorityisinvalid)Added [EKError.procedureAlarmsNotMutable](https://developer.apple.com/documentation/eventkit/ekerror/2325700-procedurealarmsnotmutable)Added [EKError.recurringReminderRequiresDueDate](https://developer.apple.com/documentation/eventkit/ekerror/2325678-recurringreminderrequiresduedate)Added [EKError.reminderLocationsNotSupported](https://developer.apple.com/documentation/eventkit/ekerror/2325686-reminderlocationsnotsupported)Added [EKError.sourceDoesNotAllowCalendarAddDelete](https://developer.apple.com/documentation/eventkit/ekerror/2325693-sourcedoesnotallowcalendaradddel)Added [EKError.sourceDoesNotAllowEvents](https://developer.apple.com/documentation/eventkit/ekerror/2325705-sourcedoesnotallowevents)Added [EKError.sourceDoesNotAllowReminders](https://developer.apple.com/documentation/eventkit/ekerror/2325682-sourcedoesnotallowreminders)Added [EKError.startDateCollidesWithOtherOccurrence](https://developer.apple.com/documentation/eventkit/ekerror/2325707-startdatecollideswithotheroccurr)Added [EKError.startDateTooFarInFuture](https://developer.apple.com/documentation/eventkit/ekerror/2325680-startdatetoofarinfuture)Added [EKError.structuredLocationsNotSupported](https://developer.apple.com/documentation/eventkit/ekerror/2325688-structuredlocationsnotsupported)Modified [EKAlarm](https://developer.apple.com/documentation/eventkit/ekalarm)

|  | Declaration |
| --- | --- |
| From | ``` class EKAlarm : EKObject, NSCopying {      init(absoluteDate date: NSDate)     class func alarmWithAbsoluteDate(_ date: NSDate) -> EKAlarm      init(relativeOffset offset: NSTimeInterval)     class func alarmWithRelativeOffset(_ offset: NSTimeInterval) -> EKAlarm     var relativeOffset: NSTimeInterval     @NSCopying var absoluteDate: NSDate?     @NSCopying var structuredLocation: EKStructuredLocation?     var proximity: EKAlarmProximity     var type: EKAlarmType { get }     var emailAddress: String?     var soundName: String?     @NSCopying var url: NSURL? } ``` |
| To | ``` class EKAlarm : EKObject, NSCopying {      init(absoluteDate date: Date)     class func withAbsoluteDate(_ date: Date) -> EKAlarm      init(relativeOffset offset: TimeInterval)     class func withRelativeOffset(_ offset: TimeInterval) -> EKAlarm     var relativeOffset: TimeInterval     var absoluteDate: Date?     @NSCopying var structuredLocation: EKStructuredLocation?     var proximity: EKAlarmProximity     var type: EKAlarmType { get }     var emailAddress: String?     var soundName: String?     var url: URL? } ``` |

Modified [EKAlarm.absoluteDate](https://developer.apple.com/documentation/eventkit/ekalarm/1507486-absolutedate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var absoluteDate: NSDate? ``` |
| To | ``` var absoluteDate: Date? ``` |

Modified [EKAlarm.init(absoluteDate: Date)](https://developer.apple.com/documentation/eventkit/ekalarm/1507130-init)

|  | Declaration |
| --- | --- |
| From | ``` init(absoluteDate date: NSDate) ``` |
| To | ``` init(absoluteDate date: Date) ``` |

Modified [EKAlarm.init(relativeOffset: TimeInterval)](https://developer.apple.com/documentation/eventkit/ekalarm/1507338-alarmwithrelativeoffset)

|  | Declaration |
| --- | --- |
| From | ``` init(relativeOffset offset: NSTimeInterval) ``` |
| To | ``` init(relativeOffset offset: TimeInterval) ``` |

Modified [EKAlarm.relativeOffset](https://developer.apple.com/documentation/eventkit/ekalarm/1507491-relativeoffset)

|  | Declaration |
| --- | --- |
| From | ``` var relativeOffset: NSTimeInterval ``` |
| To | ``` var relativeOffset: TimeInterval ``` |

Modified [EKAlarmProximity [enum]](https://developer.apple.com/documentation/eventkit/ekalarmproximity)

|  | Declaration |
| --- | --- |
| From | ``` enum EKAlarmProximity : Int {     case None     case Enter     case Leave } ``` |
| To | ``` enum EKAlarmProximity : Int {     case none     case enter     case leave } ``` |

Modified [EKAlarmProximity.enter](https://developer.apple.com/documentation/eventkit/ekalarmproximity/enter)

|  | Declaration |
| --- | --- |
| From | ``` case Enter ``` |
| To | ``` case enter ``` |

Modified [EKAlarmProximity.leave](https://developer.apple.com/documentation/eventkit/ekalarmproximity/leave)

|  | Declaration |
| --- | --- |
| From | ``` case Leave ``` |
| To | ``` case leave ``` |

Modified [EKAlarmProximity.none](https://developer.apple.com/documentation/eventkit/ekalarmproximity/ekalarmproximitynone)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [EKAlarmType [enum]](https://developer.apple.com/documentation/eventkit/ekalarmtype)

|  | Declaration |
| --- | --- |
| From | ``` enum EKAlarmType : Int {     case Display     case Audio     case Procedure     case Email } ``` |
| To | ``` enum EKAlarmType : Int {     case display     case audio     case procedure     case email } ``` |

Modified [EKAlarmType.audio](https://developer.apple.com/documentation/eventkit/ekalarmtype/audio)

|  | Declaration |
| --- | --- |
| From | ``` case Audio ``` |
| To | ``` case audio ``` |

Modified [EKAlarmType.display](https://developer.apple.com/documentation/eventkit/ekalarmtype/ekalarmtypedisplay)

|  | Declaration |
| --- | --- |
| From | ``` case Display ``` |
| To | ``` case display ``` |

Modified [EKAlarmType.email](https://developer.apple.com/documentation/eventkit/ekalarmtype/email)

|  | Declaration |
| --- | --- |
| From | ``` case Email ``` |
| To | ``` case email ``` |

Modified [EKAlarmType.procedure](https://developer.apple.com/documentation/eventkit/ekalarmtype/ekalarmtypeprocedure)

|  | Declaration |
| --- | --- |
| From | ``` case Procedure ``` |
| To | ``` case procedure ``` |

Modified [EKAuthorizationStatus [enum]](https://developer.apple.com/documentation/eventkit/ekauthorizationstatus)

|  | Declaration |
| --- | --- |
| From | ``` enum EKAuthorizationStatus : Int {     case NotDetermined     case Restricted     case Denied     case Authorized } ``` |
| To | ``` enum EKAuthorizationStatus : Int {     case notDetermined     case restricted     case denied     case authorized } ``` |

Modified [EKAuthorizationStatus.authorized](https://developer.apple.com/documentation/eventkit/ekauthorizationstatus/authorized)

|  | Declaration |
| --- | --- |
| From | ``` case Authorized ``` |
| To | ``` case authorized ``` |

Modified [EKAuthorizationStatus.denied](https://developer.apple.com/documentation/eventkit/ekauthorizationstatus/denied)

|  | Declaration |
| --- | --- |
| From | ``` case Denied ``` |
| To | ``` case denied ``` |

Modified [EKAuthorizationStatus.notDetermined](https://developer.apple.com/documentation/eventkit/ekauthorizationstatus/notdetermined)

|  | Declaration |
| --- | --- |
| From | ``` case NotDetermined ``` |
| To | ``` case notDetermined ``` |

Modified [EKAuthorizationStatus.restricted](https://developer.apple.com/documentation/eventkit/ekauthorizationstatus/ekauthorizationstatusrestricted)

|  | Declaration |
| --- | --- |
| From | ``` case Restricted ``` |
| To | ``` case restricted ``` |

Modified [EKCalendar](https://developer.apple.com/documentation/eventkit/ekcalendar)

|  | Declaration |
| --- | --- |
| From | ``` class EKCalendar : EKObject {      init(eventStore eventStore: EKEventStore)     class func calendarWithEventStore(_ eventStore: EKEventStore) -> EKCalendar      init(forEntityType entityType: EKEntityType, eventStore eventStore: EKEventStore)     class func calendarForEntityType(_ entityType: EKEntityType, eventStore eventStore: EKEventStore) -> EKCalendar     var source: EKSource     var calendarIdentifier: String { get }     var title: String     var type: EKCalendarType { get }     var allowsContentModifications: Bool { get }     var subscribed: Bool { get }     var immutable: Bool { get }     @NSCopying var color: NSColor     var supportedEventAvailabilities: EKCalendarEventAvailabilityMask { get }     var allowedEntityTypes: EKEntityMask { get } } ``` |
| To | ``` class EKCalendar : EKObject {      init(eventStore eventStore: EKEventStore)     class func withEventStore(_ eventStore: EKEventStore) -> EKCalendar      init(for entityType: EKEntityType, eventStore eventStore: EKEventStore)     class func forEntityType(_ entityType: EKEntityType, eventStore eventStore: EKEventStore) -> EKCalendar     var source: EKSource     var calendarIdentifier: String { get }     var title: String     var type: EKCalendarType { get }     var allowsContentModifications: Bool { get }     var isSubscribed: Bool { get }     var isImmutable: Bool { get }     @NSCopying var color: NSColor     var supportedEventAvailabilities: EKCalendarEventAvailabilityMask { get }     var allowedEntityTypes: EKEntityMask { get } } ``` |

Modified [EKCalendar.init(for: EKEntityType, eventStore: EKEventStore)](https://developer.apple.com/documentation/eventkit/ekcalendar/1507516-init)

|  | Declaration |
| --- | --- |
| From | ``` init(forEntityType entityType: EKEntityType, eventStore eventStore: EKEventStore) ``` |
| To | ``` init(for entityType: EKEntityType, eventStore eventStore: EKEventStore) ``` |

Modified [EKCalendar.isImmutable](https://developer.apple.com/documentation/eventkit/ekcalendar/1507084-immutable)

|  | Declaration |
| --- | --- |
| From | ``` var immutable: Bool { get } ``` |
| To | ``` var isImmutable: Bool { get } ``` |

Modified [EKCalendar.isSubscribed](https://developer.apple.com/documentation/eventkit/ekcalendar/1507471-subscribed)

|  | Declaration |
| --- | --- |
| From | ``` var subscribed: Bool { get } ``` |
| To | ``` var isSubscribed: Bool { get } ``` |

Modified [EKCalendarEventAvailabilityMask [struct]](https://developer.apple.com/documentation/eventkit/ekcalendareventavailabilitymask)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct EKCalendarEventAvailabilityMask : OptionSetType {     init(rawValue rawValue: UInt)     static var None: EKCalendarEventAvailabilityMask { get }     static var Busy: EKCalendarEventAvailabilityMask { get }     static var Free: EKCalendarEventAvailabilityMask { get }     static var Tentative: EKCalendarEventAvailabilityMask { get }     static var Unavailable: EKCalendarEventAvailabilityMask { get } } ``` | OptionSetType |
| To | ``` struct EKCalendarEventAvailabilityMask : OptionSet {     init(rawValue rawValue: UInt)     static var none: EKCalendarEventAvailabilityMask { get }     static var busy: EKCalendarEventAvailabilityMask { get }     static var free: EKCalendarEventAvailabilityMask { get }     static var tentative: EKCalendarEventAvailabilityMask { get }     static var unavailable: EKCalendarEventAvailabilityMask { get }     func intersect(_ other: EKCalendarEventAvailabilityMask) -> EKCalendarEventAvailabilityMask     func exclusiveOr(_ other: EKCalendarEventAvailabilityMask) -> EKCalendarEventAvailabilityMask     mutating func unionInPlace(_ other: EKCalendarEventAvailabilityMask)     mutating func intersectInPlace(_ other: EKCalendarEventAvailabilityMask)     mutating func exclusiveOrInPlace(_ other: EKCalendarEventAvailabilityMask)     func isSubsetOf(_ other: EKCalendarEventAvailabilityMask) -> Bool     func isDisjointWith(_ other: EKCalendarEventAvailabilityMask) -> Bool     func isSupersetOf(_ other: EKCalendarEventAvailabilityMask) -> Bool     mutating func subtractInPlace(_ other: EKCalendarEventAvailabilityMask)     func isStrictSupersetOf(_ other: EKCalendarEventAvailabilityMask) -> Bool     func isStrictSubsetOf(_ other: EKCalendarEventAvailabilityMask) -> Bool } extension EKCalendarEventAvailabilityMask {     func union(_ other: EKCalendarEventAvailabilityMask) -> EKCalendarEventAvailabilityMask     func intersection(_ other: EKCalendarEventAvailabilityMask) -> EKCalendarEventAvailabilityMask     func symmetricDifference(_ other: EKCalendarEventAvailabilityMask) -> EKCalendarEventAvailabilityMask } extension EKCalendarEventAvailabilityMask {     func contains(_ member: EKCalendarEventAvailabilityMask) -> Bool     mutating func insert(_ newMember: EKCalendarEventAvailabilityMask) -> (inserted: Bool, memberAfterInsert: EKCalendarEventAvailabilityMask)     mutating func remove(_ member: EKCalendarEventAvailabilityMask) -> EKCalendarEventAvailabilityMask?     mutating func update(with newMember: EKCalendarEventAvailabilityMask) -> EKCalendarEventAvailabilityMask? } extension EKCalendarEventAvailabilityMask {     convenience init()     mutating func formUnion(_ other: EKCalendarEventAvailabilityMask)     mutating func formIntersection(_ other: EKCalendarEventAvailabilityMask)     mutating func formSymmetricDifference(_ other: EKCalendarEventAvailabilityMask) } extension EKCalendarEventAvailabilityMask {     convenience init<S : Sequence where S.Iterator.Element == EKCalendarEventAvailabilityMask>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: EKCalendarEventAvailabilityMask...)     mutating func subtract(_ other: EKCalendarEventAvailabilityMask)     func isSubset(of other: EKCalendarEventAvailabilityMask) -> Bool     func isSuperset(of other: EKCalendarEventAvailabilityMask) -> Bool     func isDisjoint(with other: EKCalendarEventAvailabilityMask) -> Bool     func subtracting(_ other: EKCalendarEventAvailabilityMask) -> EKCalendarEventAvailabilityMask     var isEmpty: Bool { get }     func isStrictSuperset(of other: EKCalendarEventAvailabilityMask) -> Bool     func isStrictSubset(of other: EKCalendarEventAvailabilityMask) -> Bool } ``` | OptionSet |

Modified [EKCalendarEventAvailabilityMask.busy](https://developer.apple.com/documentation/eventkit/ekcalendareventavailabilitymask/ekcalendareventavailabilitybusy)

|  | Declaration |
| --- | --- |
| From | ``` static var Busy: EKCalendarEventAvailabilityMask { get } ``` |
| To | ``` static var busy: EKCalendarEventAvailabilityMask { get } ``` |

Modified [EKCalendarEventAvailabilityMask.free](https://developer.apple.com/documentation/eventkit/ekcalendareventavailabilitymask/1451912-free)

|  | Declaration |
| --- | --- |
| From | ``` static var Free: EKCalendarEventAvailabilityMask { get } ``` |
| To | ``` static var free: EKCalendarEventAvailabilityMask { get } ``` |

Modified [EKCalendarEventAvailabilityMask.tentative](https://developer.apple.com/documentation/eventkit/ekcalendareventavailabilitymask/1451814-tentative)

|  | Declaration |
| --- | --- |
| From | ``` static var Tentative: EKCalendarEventAvailabilityMask { get } ``` |
| To | ``` static var tentative: EKCalendarEventAvailabilityMask { get } ``` |

Modified [EKCalendarEventAvailabilityMask.unavailable](https://developer.apple.com/documentation/eventkit/ekcalendareventavailabilitymask/1451855-unavailable)

|  | Declaration |
| --- | --- |
| From | ``` static var Unavailable: EKCalendarEventAvailabilityMask { get } ``` |
| To | ``` static var unavailable: EKCalendarEventAvailabilityMask { get } ``` |

Modified [EKCalendarItem](https://developer.apple.com/documentation/eventkit/ekcalendaritem)

|  | Declaration |
| --- | --- |
| From | ``` class EKCalendarItem : EKObject {     var UUID: String { get }     var calendar: EKCalendar     var calendarItemIdentifier: String { get }     var calendarItemExternalIdentifier: String { get }     var title: String     var location: String?     var notes: String?     @NSCopying var URL: NSURL?     var lastModifiedDate: NSDate? { get }     var creationDate: NSDate? { get }     @NSCopying var timeZone: NSTimeZone?     var hasAlarms: Bool { get }     var hasRecurrenceRules: Bool { get }     var hasAttendees: Bool { get }     var hasNotes: Bool { get }     var attendees: [EKParticipant]? { get }     var alarms: [EKAlarm]?     func addAlarm(_ alarm: EKAlarm)     func removeAlarm(_ alarm: EKAlarm)     var recurrenceRules: [EKRecurrenceRule]?     func addRecurrenceRule(_ rule: EKRecurrenceRule)     func removeRecurrenceRule(_ rule: EKRecurrenceRule) } ``` |
| To | ``` class EKCalendarItem : EKObject {     var uuid: String { get }     var calendar: EKCalendar     var calendarItemIdentifier: String { get }     var calendarItemExternalIdentifier: String { get }     var title: String     var location: String?     var notes: String?     var url: URL?     var lastModifiedDate: Date? { get }     var creationDate: Date? { get }     var timeZone: TimeZone?     var hasAlarms: Bool { get }     var hasRecurrenceRules: Bool { get }     var hasAttendees: Bool { get }     var hasNotes: Bool { get }     var attendees: [EKParticipant]? { get }     var alarms: [EKAlarm]?     func addAlarm(_ alarm: EKAlarm)     func removeAlarm(_ alarm: EKAlarm)     var recurrenceRules: [EKRecurrenceRule]?     func addRecurrenceRule(_ rule: EKRecurrenceRule)     func removeRecurrenceRule(_ rule: EKRecurrenceRule) } ``` |

Modified [EKCalendarItem.creationDate](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507213-creationdate)

|  | Declaration |
| --- | --- |
| From | ``` var creationDate: NSDate? { get } ``` |
| To | ``` var creationDate: Date? { get } ``` |

Modified [EKCalendarItem.lastModifiedDate](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507374-lastmodifieddate)

|  | Declaration |
| --- | --- |
| From | ``` var lastModifiedDate: NSDate? { get } ``` |
| To | ``` var lastModifiedDate: Date? { get } ``` |

Modified [EKCalendarItem.timeZone](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507104-timezone)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var timeZone: NSTimeZone? ``` |
| To | ``` var timeZone: TimeZone? ``` |

Modified [EKCalendarItem.url](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507265-url)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var URL: NSURL? ``` |
| To | ``` var url: URL? ``` |

Modified [EKCalendarType [enum]](https://developer.apple.com/documentation/eventkit/ekcalendartype)

|  | Declaration |
| --- | --- |
| From | ``` enum EKCalendarType : Int {     case Local     case CalDAV     case Exchange     case Subscription     case Birthday } ``` |
| To | ``` enum EKCalendarType : Int {     case local     case calDAV     case exchange     case subscription     case birthday } ``` |

Modified [EKCalendarType.birthday](https://developer.apple.com/documentation/eventkit/ekcalendartype/ekcalendartypebirthday)

|  | Declaration |
| --- | --- |
| From | ``` case Birthday ``` |
| To | ``` case birthday ``` |

Modified [EKCalendarType.calDAV](https://developer.apple.com/documentation/eventkit/ekcalendartype/ekcalendartypecaldav)

|  | Declaration |
| --- | --- |
| From | ``` case CalDAV ``` |
| To | ``` case calDAV ``` |

Modified [EKCalendarType.exchange](https://developer.apple.com/documentation/eventkit/ekcalendartype/ekcalendartypeexchange)

|  | Declaration |
| --- | --- |
| From | ``` case Exchange ``` |
| To | ``` case exchange ``` |

Modified [EKCalendarType.local](https://developer.apple.com/documentation/eventkit/ekcalendartype/ekcalendartypelocal)

|  | Declaration |
| --- | --- |
| From | ``` case Local ``` |
| To | ``` case local ``` |

Modified [EKCalendarType.subscription](https://developer.apple.com/documentation/eventkit/ekcalendartype/subscription)

|  | Declaration |
| --- | --- |
| From | ``` case Subscription ``` |
| To | ``` case subscription ``` |

Modified [EKEntityMask [struct]](https://developer.apple.com/documentation/eventkit/ekentitymask)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct EKEntityMask : OptionSetType {     init(rawValue rawValue: UInt)     static var Event: EKEntityMask { get }     static var Reminder: EKEntityMask { get } } ``` | OptionSetType |
| To | ``` struct EKEntityMask : OptionSet {     init(rawValue rawValue: UInt)     static var event: EKEntityMask { get }     static var reminder: EKEntityMask { get }     func intersect(_ other: EKEntityMask) -> EKEntityMask     func exclusiveOr(_ other: EKEntityMask) -> EKEntityMask     mutating func unionInPlace(_ other: EKEntityMask)     mutating func intersectInPlace(_ other: EKEntityMask)     mutating func exclusiveOrInPlace(_ other: EKEntityMask)     func isSubsetOf(_ other: EKEntityMask) -> Bool     func isDisjointWith(_ other: EKEntityMask) -> Bool     func isSupersetOf(_ other: EKEntityMask) -> Bool     mutating func subtractInPlace(_ other: EKEntityMask)     func isStrictSupersetOf(_ other: EKEntityMask) -> Bool     func isStrictSubsetOf(_ other: EKEntityMask) -> Bool } extension EKEntityMask {     func union(_ other: EKEntityMask) -> EKEntityMask     func intersection(_ other: EKEntityMask) -> EKEntityMask     func symmetricDifference(_ other: EKEntityMask) -> EKEntityMask } extension EKEntityMask {     func contains(_ member: EKEntityMask) -> Bool     mutating func insert(_ newMember: EKEntityMask) -> (inserted: Bool, memberAfterInsert: EKEntityMask)     mutating func remove(_ member: EKEntityMask) -> EKEntityMask?     mutating func update(with newMember: EKEntityMask) -> EKEntityMask? } extension EKEntityMask {     convenience init()     mutating func formUnion(_ other: EKEntityMask)     mutating func formIntersection(_ other: EKEntityMask)     mutating func formSymmetricDifference(_ other: EKEntityMask) } extension EKEntityMask {     convenience init<S : Sequence where S.Iterator.Element == EKEntityMask>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: EKEntityMask...)     mutating func subtract(_ other: EKEntityMask)     func isSubset(of other: EKEntityMask) -> Bool     func isSuperset(of other: EKEntityMask) -> Bool     func isDisjoint(with other: EKEntityMask) -> Bool     func subtracting(_ other: EKEntityMask) -> EKEntityMask     var isEmpty: Bool { get }     func isStrictSuperset(of other: EKEntityMask) -> Bool     func isStrictSubset(of other: EKEntityMask) -> Bool } ``` | OptionSet |

Modified [EKEntityMask.event](https://developer.apple.com/documentation/eventkit/ekentitymask/ekentitymaskevent)

|  | Declaration |
| --- | --- |
| From | ``` static var Event: EKEntityMask { get } ``` |
| To | ``` static var event: EKEntityMask { get } ``` |

Modified [EKEntityMask.reminder](https://developer.apple.com/documentation/eventkit/ekentitymask/ekentitymaskreminder)

|  | Declaration |
| --- | --- |
| From | ``` static var Reminder: EKEntityMask { get } ``` |
| To | ``` static var reminder: EKEntityMask { get } ``` |

Modified [EKEntityType [enum]](https://developer.apple.com/documentation/eventkit/ekentitytype)

|  | Declaration |
| --- | --- |
| From | ``` enum EKEntityType : UInt {     case Event     case Reminder } ``` |
| To | ``` enum EKEntityType : UInt {     case event     case reminder } ``` |

Modified [EKEntityType.event](https://developer.apple.com/documentation/eventkit/ekentitytype/event)

|  | Declaration |
| --- | --- |
| From | ``` case Event ``` |
| To | ``` case event ``` |

Modified [EKEntityType.reminder](https://developer.apple.com/documentation/eventkit/ekentitytype/ekentitytypereminder)

|  | Declaration |
| --- | --- |
| From | ``` case Reminder ``` |
| To | ``` case reminder ``` |

Modified [EKError.Code [enum]](https://developer.apple.com/documentation/eventkit/ekerrorcode)

|  | Declaration |
| --- | --- |
| From | ``` enum EKErrorCode : Int {     case EventNotMutable     case NoCalendar     case NoStartDate     case NoEndDate     case DatesInverted     case InternalFailure     case CalendarReadOnly     case DurationGreaterThanRecurrence     case AlarmGreaterThanRecurrence     case StartDateTooFarInFuture     case StartDateCollidesWithOtherOccurrence     case ObjectBelongsToDifferentStore     case InvitesCannotBeMoved     case InvalidSpan     case CalendarHasNoSource     case CalendarSourceCannotBeModified     case CalendarIsImmutable     case SourceDoesNotAllowCalendarAddDelete     case RecurringReminderRequiresDueDate     case StructuredLocationsNotSupported     case ReminderLocationsNotSupported     case AlarmProximityNotSupported     case CalendarDoesNotAllowEvents     case CalendarDoesNotAllowReminders     case SourceDoesNotAllowReminders     case SourceDoesNotAllowEvents     case PriorityIsInvalid     case InvalidEntityType     case ProcedureAlarmsNotMutable     case EventStoreNotAuthorized     case OSNotSupported     case Last } extension EKErrorCode : _BridgedNSError { } extension EKErrorCode : _BridgedNSError { } ``` |
| To | ``` enum Code : Int {         typealias _ErrorType = EKError         case eventNotMutable         case noCalendar         case noStartDate         case noEndDate         case datesInverted         case internalFailure         case calendarReadOnly         case durationGreaterThanRecurrence         case alarmGreaterThanRecurrence         case startDateTooFarInFuture         case startDateCollidesWithOtherOccurrence         case objectBelongsToDifferentStore         case invitesCannotBeMoved         case invalidSpan         case calendarHasNoSource         case calendarSourceCannotBeModified         case calendarIsImmutable         case sourceDoesNotAllowCalendarAddDelete         case recurringReminderRequiresDueDate         case structuredLocationsNotSupported         case reminderLocationsNotSupported         case alarmProximityNotSupported         case calendarDoesNotAllowEvents         case calendarDoesNotAllowReminders         case sourceDoesNotAllowReminders         case sourceDoesNotAllowEvents         case priorityIsInvalid         case invalidEntityType         case procedureAlarmsNotMutable         case eventStoreNotAuthorized         case osNotSupported         case last     } ``` |

Modified [EKError.Code.alarmGreaterThanRecurrence](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerroralarmgreaterthanrecurrence)

|  | Declaration |
| --- | --- |
| From | ``` case AlarmGreaterThanRecurrence ``` |
| To | ``` case alarmGreaterThanRecurrence ``` |

Modified [EKError.Code.alarmProximityNotSupported](https://developer.apple.com/documentation/eventkit/ekerror/code/alarmproximitynotsupported)

|  | Declaration |
| --- | --- |
| From | ``` case AlarmProximityNotSupported ``` |
| To | ``` case alarmProximityNotSupported ``` |

Modified [EKError.Code.calendarDoesNotAllowEvents](https://developer.apple.com/documentation/eventkit/ekerror/code/calendardoesnotallowevents)

|  | Declaration |
| --- | --- |
| From | ``` case CalendarDoesNotAllowEvents ``` |
| To | ``` case calendarDoesNotAllowEvents ``` |

Modified [EKError.Code.calendarDoesNotAllowReminders](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerrorcalendardoesnotallowreminders)

|  | Declaration |
| --- | --- |
| From | ``` case CalendarDoesNotAllowReminders ``` |
| To | ``` case calendarDoesNotAllowReminders ``` |

Modified [EKError.Code.calendarHasNoSource](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerrorcalendarhasnosource)

|  | Declaration |
| --- | --- |
| From | ``` case CalendarHasNoSource ``` |
| To | ``` case calendarHasNoSource ``` |

Modified [EKError.Code.calendarIsImmutable](https://developer.apple.com/documentation/eventkit/ekerror/code/calendarisimmutable)

|  | Declaration |
| --- | --- |
| From | ``` case CalendarIsImmutable ``` |
| To | ``` case calendarIsImmutable ``` |

Modified [EKError.Code.calendarReadOnly](https://developer.apple.com/documentation/eventkit/ekerror/code/calendarreadonly)

|  | Declaration |
| --- | --- |
| From | ``` case CalendarReadOnly ``` |
| To | ``` case calendarReadOnly ``` |

Modified [EKError.Code.calendarSourceCannotBeModified](https://developer.apple.com/documentation/eventkit/ekerror/code/calendarsourcecannotbemodified)

|  | Declaration |
| --- | --- |
| From | ``` case CalendarSourceCannotBeModified ``` |
| To | ``` case calendarSourceCannotBeModified ``` |

Modified [EKError.Code.datesInverted](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerrordatesinverted)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case DatesInverted ``` | OS X 10.11 |
| To | ``` case datesInverted ``` | OS X 10.12 |

Modified [EKError.Code.durationGreaterThanRecurrence](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerrordurationgreaterthanrecurrence)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case DurationGreaterThanRecurrence ``` | OS X 10.11 |
| To | ``` case durationGreaterThanRecurrence ``` | OS X 10.12 |

Modified [EKError.Code.eventNotMutable](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerroreventnotmutable)

|  | Declaration |
| --- | --- |
| From | ``` case EventNotMutable ``` |
| To | ``` case eventNotMutable ``` |

Modified [EKError.Code.eventStoreNotAuthorized](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerroreventstorenotauthorized)

|  | Declaration |
| --- | --- |
| From | ``` case EventStoreNotAuthorized ``` |
| To | ``` case eventStoreNotAuthorized ``` |

Modified [EKError.Code.internalFailure](https://developer.apple.com/documentation/eventkit/ekerror/code/internalfailure)

|  | Declaration |
| --- | --- |
| From | ``` case InternalFailure ``` |
| To | ``` case internalFailure ``` |

Modified [EKError.Code.invalidEntityType](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerrorinvalidentitytype)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidEntityType ``` |
| To | ``` case invalidEntityType ``` |

Modified [EKError.Code.invalidSpan](https://developer.apple.com/documentation/eventkit/ekerror/code/invalidspan)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case InvalidSpan ``` | OS X 10.11 |
| To | ``` case invalidSpan ``` | OS X 10.12 |

Modified [EKError.Code.invitesCannotBeMoved](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerrorinvitescannotbemoved)

|  | Declaration |
| --- | --- |
| From | ``` case InvitesCannotBeMoved ``` |
| To | ``` case invitesCannotBeMoved ``` |

Modified [EKError.Code.last](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerrorlast)

|  | Declaration |
| --- | --- |
| From | ``` case Last ``` |
| To | ``` case last ``` |

Modified [EKError.Code.noCalendar](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerrornocalendar)

|  | Declaration |
| --- | --- |
| From | ``` case NoCalendar ``` |
| To | ``` case noCalendar ``` |

Modified [EKError.Code.noEndDate](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerrornoenddate)

|  | Declaration |
| --- | --- |
| From | ``` case NoEndDate ``` |
| To | ``` case noEndDate ``` |

Modified [EKError.Code.noStartDate](https://developer.apple.com/documentation/eventkit/ekerror/code/nostartdate)

|  | Declaration |
| --- | --- |
| From | ``` case NoStartDate ``` |
| To | ``` case noStartDate ``` |

Modified [EKError.Code.objectBelongsToDifferentStore](https://developer.apple.com/documentation/eventkit/ekerror/code/objectbelongstodifferentstore)

|  | Declaration |
| --- | --- |
| From | ``` case ObjectBelongsToDifferentStore ``` |
| To | ``` case objectBelongsToDifferentStore ``` |

Modified [EKError.Code.osNotSupported](https://developer.apple.com/documentation/eventkit/ekerror/code/osnotsupported)

|  | Declaration |
| --- | --- |
| From | ``` case OSNotSupported ``` |
| To | ``` case osNotSupported ``` |

Modified [EKError.Code.priorityIsInvalid](https://developer.apple.com/documentation/eventkit/ekerror/code/priorityisinvalid)

|  | Declaration |
| --- | --- |
| From | ``` case PriorityIsInvalid ``` |
| To | ``` case priorityIsInvalid ``` |

Modified [EKError.Code.procedureAlarmsNotMutable](https://developer.apple.com/documentation/eventkit/ekerror/code/procedurealarmsnotmutable)

|  | Declaration |
| --- | --- |
| From | ``` case ProcedureAlarmsNotMutable ``` |
| To | ``` case procedureAlarmsNotMutable ``` |

Modified [EKError.Code.recurringReminderRequiresDueDate](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerrorrecurringreminderrequiresduedate)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case RecurringReminderRequiresDueDate ``` | OS X 10.11 |
| To | ``` case recurringReminderRequiresDueDate ``` | OS X 10.12 |

Modified [EKError.Code.reminderLocationsNotSupported](https://developer.apple.com/documentation/eventkit/ekerror/code/reminderlocationsnotsupported)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case ReminderLocationsNotSupported ``` | OS X 10.11 |
| To | ``` case reminderLocationsNotSupported ``` | OS X 10.12 |

Modified [EKError.Code.sourceDoesNotAllowCalendarAddDelete](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerrorsourcedoesnotallowcalendaradddelete)

|  | Declaration |
| --- | --- |
| From | ``` case SourceDoesNotAllowCalendarAddDelete ``` |
| To | ``` case sourceDoesNotAllowCalendarAddDelete ``` |

Modified [EKError.Code.sourceDoesNotAllowEvents](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerrorsourcedoesnotallowevents)

|  | Declaration |
| --- | --- |
| From | ``` case SourceDoesNotAllowEvents ``` |
| To | ``` case sourceDoesNotAllowEvents ``` |

Modified [EKError.Code.sourceDoesNotAllowReminders](https://developer.apple.com/documentation/eventkit/ekerror/code/sourcedoesnotallowreminders)

|  | Declaration |
| --- | --- |
| From | ``` case SourceDoesNotAllowReminders ``` |
| To | ``` case sourceDoesNotAllowReminders ``` |

Modified [EKError.Code.startDateCollidesWithOtherOccurrence](https://developer.apple.com/documentation/eventkit/ekerror/code/startdatecollideswithotheroccurrence)

|  | Declaration |
| --- | --- |
| From | ``` case StartDateCollidesWithOtherOccurrence ``` |
| To | ``` case startDateCollidesWithOtherOccurrence ``` |

Modified [EKError.Code.startDateTooFarInFuture](https://developer.apple.com/documentation/eventkit/ekerror/code/startdatetoofarinfuture)

|  | Declaration |
| --- | --- |
| From | ``` case StartDateTooFarInFuture ``` |
| To | ``` case startDateTooFarInFuture ``` |

Modified [EKError.Code.structuredLocationsNotSupported](https://developer.apple.com/documentation/eventkit/ekerrorcode/ekerrorstructuredlocationsnotsupported)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case StructuredLocationsNotSupported ``` | OS X 10.11 |
| To | ``` case structuredLocationsNotSupported ``` | OS X 10.12 |

Modified [EKEvent](https://developer.apple.com/documentation/eventkit/ekevent)

|  | Declaration |
| --- | --- |
| From | ``` class EKEvent : EKCalendarItem {      init(eventStore eventStore: EKEventStore)     class func eventWithEventStore(_ eventStore: EKEventStore) -> EKEvent     var eventIdentifier: String { get }     var allDay: Bool     @NSCopying var startDate: NSDate     @NSCopying var endDate: NSDate     @NSCopying var structuredLocation: EKStructuredLocation?     func compareStartDateWithEvent(_ other: EKEvent) -> NSComparisonResult     var organizer: EKParticipant? { get }     var availability: EKEventAvailability     var status: EKEventStatus { get }     var isDetached: Bool { get }     var occurrenceDate: NSDate { get }     func refresh() -> Bool     var birthdayContactIdentifier: String? { get }     var birthdayPersonID: Int { get }     var birthdayPersonUniqueID: String? { get } } ``` |
| To | ``` class EKEvent : EKCalendarItem {      init(eventStore eventStore: EKEventStore)     class func withEventStore(_ eventStore: EKEventStore) -> EKEvent     var eventIdentifier: String { get }     var isAllDay: Bool     var startDate: Date     var endDate: Date     @NSCopying var structuredLocation: EKStructuredLocation?     func compareStartDate(with other: EKEvent) -> ComparisonResult     var organizer: EKParticipant? { get }     var availability: EKEventAvailability     var status: EKEventStatus { get }     var isDetached: Bool { get }     var occurrenceDate: Date { get }     func refresh() -> Bool     var birthdayContactIdentifier: String? { get }     var birthdayPersonID: Int { get }     var birthdayPersonUniqueID: String? { get } } ``` |

Modified [EKEvent.compareStartDate(with: EKEvent) -> ComparisonResult](https://developer.apple.com/documentation/eventkit/ekevent/1507335-comparestartdatewithevent)

|  | Declaration |
| --- | --- |
| From | ``` func compareStartDateWithEvent(_ other: EKEvent) -> NSComparisonResult ``` |
| To | ``` func compareStartDate(with other: EKEvent) -> ComparisonResult ``` |

Modified [EKEvent.endDate](https://developer.apple.com/documentation/eventkit/ekevent/1507121-enddate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var endDate: NSDate ``` |
| To | ``` var endDate: Date ``` |

Modified [EKEvent.isAllDay](https://developer.apple.com/documentation/eventkit/ekevent/1507482-allday)

|  | Declaration |
| --- | --- |
| From | ``` var allDay: Bool ``` |
| To | ``` var isAllDay: Bool ``` |

Modified [EKEvent.occurrenceDate](https://developer.apple.com/documentation/eventkit/ekevent/1507244-occurrencedate)

|  | Declaration |
| --- | --- |
| From | ``` var occurrenceDate: NSDate { get } ``` |
| To | ``` var occurrenceDate: Date { get } ``` |

Modified [EKEvent.startDate](https://developer.apple.com/documentation/eventkit/ekevent/1507372-startdate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var startDate: NSDate ``` |
| To | ``` var startDate: Date ``` |

Modified [EKEventAvailability [enum]](https://developer.apple.com/documentation/eventkit/ekeventavailability)

|  | Declaration |
| --- | --- |
| From | ``` enum EKEventAvailability : Int {     case NotSupported     case Busy     case Free     case Tentative     case Unavailable } ``` |
| To | ``` enum EKEventAvailability : Int {     case notSupported     case busy     case free     case tentative     case unavailable } ``` |

Modified [EKEventAvailability.busy](https://developer.apple.com/documentation/eventkit/ekeventavailability/busy)

|  | Declaration |
| --- | --- |
| From | ``` case Busy ``` |
| To | ``` case busy ``` |

Modified [EKEventAvailability.free](https://developer.apple.com/documentation/eventkit/ekeventavailability/ekeventavailabilityfree)

|  | Declaration |
| --- | --- |
| From | ``` case Free ``` |
| To | ``` case free ``` |

Modified [EKEventAvailability.notSupported](https://developer.apple.com/documentation/eventkit/ekeventavailability/ekeventavailabilitynotsupported)

|  | Declaration |
| --- | --- |
| From | ``` case NotSupported ``` |
| To | ``` case notSupported ``` |

Modified [EKEventAvailability.tentative](https://developer.apple.com/documentation/eventkit/ekeventavailability/ekeventavailabilitytentative)

|  | Declaration |
| --- | --- |
| From | ``` case Tentative ``` |
| To | ``` case tentative ``` |

Modified [EKEventAvailability.unavailable](https://developer.apple.com/documentation/eventkit/ekeventavailability/unavailable)

|  | Declaration |
| --- | --- |
| From | ``` case Unavailable ``` |
| To | ``` case unavailable ``` |

Modified [EKEventStatus [enum]](https://developer.apple.com/documentation/eventkit/ekeventstatus)

|  | Declaration |
| --- | --- |
| From | ``` enum EKEventStatus : Int {     case None     case Confirmed     case Tentative     case Canceled } ``` |
| To | ``` enum EKEventStatus : Int {     case none     case confirmed     case tentative     case canceled } ``` |

Modified [EKEventStatus.canceled](https://developer.apple.com/documentation/eventkit/ekeventstatus/ekeventstatuscanceled)

|  | Declaration |
| --- | --- |
| From | ``` case Canceled ``` |
| To | ``` case canceled ``` |

Modified [EKEventStatus.confirmed](https://developer.apple.com/documentation/eventkit/ekeventstatus/confirmed)

|  | Declaration |
| --- | --- |
| From | ``` case Confirmed ``` |
| To | ``` case confirmed ``` |

Modified [EKEventStatus.none](https://developer.apple.com/documentation/eventkit/ekeventstatus/none)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [EKEventStatus.tentative](https://developer.apple.com/documentation/eventkit/ekeventstatus/tentative)

|  | Declaration |
| --- | --- |
| From | ``` case Tentative ``` |
| To | ``` case tentative ``` |

Modified [EKEventStore](https://developer.apple.com/documentation/eventkit/ekeventstore)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class EKEventStore : NSObject {     class func authorizationStatusForEntityType(_ entityType: EKEntityType) -> EKAuthorizationStatus     init(accessToEntityTypes entityTypes: EKEntityMask)     init()     init(sources sources: [EKSource])     func requestAccessToEntityType(_ entityType: EKEntityType, completion completion: EKEventStoreRequestAccessCompletionHandler)     var eventStoreIdentifier: String { get }     var delegateSources: [EKSource] { get }     var sources: [EKSource] { get }     func sourceWithIdentifier(_ identifier: String) -> EKSource     var calendars: [EKCalendar] { get }     func calendarsForEntityType(_ entityType: EKEntityType) -> [EKCalendar]     var defaultCalendarForNewEvents: EKCalendar { get }     func defaultCalendarForNewReminders() -> EKCalendar     func calendarWithIdentifier(_ identifier: String) -> EKCalendar?     func saveCalendar(_ calendar: EKCalendar, commit commit: Bool) throws     func removeCalendar(_ calendar: EKCalendar, commit commit: Bool) throws     func calendarItemWithIdentifier(_ identifier: String) -> EKCalendarItem     func calendarItemsWithExternalIdentifier(_ externalIdentifier: String) -> [EKCalendarItem]     func saveEvent(_ event: EKEvent, span span: EKSpan) throws     func removeEvent(_ event: EKEvent, span span: EKSpan) throws     func saveEvent(_ event: EKEvent, span span: EKSpan, commit commit: Bool) throws     func removeEvent(_ event: EKEvent, span span: EKSpan, commit commit: Bool) throws     func eventWithIdentifier(_ identifier: String) -> EKEvent?     func eventsMatchingPredicate(_ predicate: NSPredicate) -> [EKEvent]     func enumerateEventsMatchingPredicate(_ predicate: NSPredicate, usingBlock block: EKEventSearchCallback)     func predicateForEventsWithStartDate(_ startDate: NSDate, endDate endDate: NSDate, calendars calendars: [EKCalendar]?) -> NSPredicate     func saveReminder(_ reminder: EKReminder, commit commit: Bool) throws     func removeReminder(_ reminder: EKReminder, commit commit: Bool) throws     func fetchRemindersMatchingPredicate(_ predicate: NSPredicate, completion completion: ([EKReminder]?) -> Void) -> AnyObject     func cancelFetchRequest(_ fetchIdentifier: AnyObject)     func predicateForRemindersInCalendars(_ calendars: [EKCalendar]?) -> NSPredicate     func predicateForIncompleteRemindersWithDueDateStarting(_ startDate: NSDate?, ending endDate: NSDate?, calendars calendars: [EKCalendar]?) -> NSPredicate     func predicateForCompletedRemindersWithCompletionDateStarting(_ startDate: NSDate?, ending endDate: NSDate?, calendars calendars: [EKCalendar]?) -> NSPredicate     func commit() throws     func reset()     func refreshSourcesIfNecessary() } ``` | -- |
| To | ``` class EKEventStore : NSObject {     class func authorizationStatus(for entityType: EKEntityType) -> EKAuthorizationStatus     init(accessToEntityTypes entityTypes: EKEntityMask)     init()     init(sources sources: [EKSource])     func requestAccess(to entityType: EKEntityType, completion completion: EventKit.EKEventStoreRequestAccessCompletionHandler)     var eventStoreIdentifier: String { get }     var delegateSources: [EKSource] { get }     var sources: [EKSource] { get }     func source(withIdentifier identifier: String) -> EKSource     var calendars: [EKCalendar] { get }     func calendars(for entityType: EKEntityType) -> [EKCalendar]     var defaultCalendarForNewEvents: EKCalendar { get }     func defaultCalendarForNewReminders() -> EKCalendar     func calendar(withIdentifier identifier: String) -> EKCalendar?     func saveCalendar(_ calendar: EKCalendar, commit commit: Bool) throws     func removeCalendar(_ calendar: EKCalendar, commit commit: Bool) throws     func calendarItem(withIdentifier identifier: String) -> EKCalendarItem     func calendarItems(withExternalIdentifier externalIdentifier: String) -> [EKCalendarItem]     func save(_ event: EKEvent, span span: EKSpan) throws     func remove(_ event: EKEvent, span span: EKSpan) throws     func save(_ event: EKEvent, span span: EKSpan, commit commit: Bool) throws     func remove(_ event: EKEvent, span span: EKSpan, commit commit: Bool) throws     func event(withIdentifier identifier: String) -> EKEvent?     func events(matching predicate: NSPredicate) -> [EKEvent]     func enumerateEvents(matching predicate: NSPredicate, using block: EventKit.EKEventSearchCallback)     func predicateForEvents(withStart startDate: Date, end endDate: Date, calendars calendars: [EKCalendar]?) -> NSPredicate     func save(_ reminder: EKReminder, commit commit: Bool) throws     func remove(_ reminder: EKReminder, commit commit: Bool) throws     func fetchReminders(matching predicate: NSPredicate, completion completion: @escaping ([EKReminder]?) -> Swift.Void) -> Any     func cancelFetchRequest(_ fetchIdentifier: Any)     func predicateForReminders(in calendars: [EKCalendar]?) -> NSPredicate     func predicateForIncompleteReminders(withDueDateStarting startDate: Date?, ending endDate: Date?, calendars calendars: [EKCalendar]?) -> NSPredicate     func predicateForCompletedReminders(withCompletionDateStarting startDate: Date?, ending endDate: Date?, calendars calendars: [EKCalendar]?) -> NSPredicate     func commit() throws     func reset()     func refreshSourcesIfNecessary()     func actionProperty() -> String!     func title(for person: ABPerson!, identifier identifier: String!) -> String!     func performAction(for person: ABPerson!, identifier identifier: String!)     func shouldEnableAction(for person: ABPerson!, identifier identifier: String!) -> Bool     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any?     func discardEditing()     func commitEditing() -> Bool     func commitEditing(withDelegate delegate: Any?, didCommit didCommitSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func commitEditingAndReturnError() throws     func objectDidBeginEditing(_ editor: Any)     func objectDidEndEditing(_ editor: Any)     class func setDefaultPlaceholder(_ placeholder: Any?, forMarker marker: Any?, withBinding binding: String)     class func defaultPlaceholder(forMarker marker: Any?, withBinding binding: String) -> Any?     class func exposeBinding(_ binding: String)     var exposedBindings: [String] { get }     func valueClassForBinding(_ binding: String) -> AnyClass?     func bind(_ binding: String, to observable: Any, withKeyPath keyPath: String, options options: [String : Any]? = nil)     func unbind(_ binding: String)     func infoForBinding(_ binding: String) -> [String : Any]?     func optionDescriptionsForBinding(_ binding: String) -> [NSAttributeDescription]     func validateToolbarItem(_ item: NSToolbarItem) -> Bool     func application(_ sender: NSApplication, delegateHandlesKey key: String) -> Bool     func tableView(_ tableView: NSTableView, writeRows rows: [Any], to pboard: NSPasteboard) -> Bool     func textStorageWillProcessEditing(_ notification: Notification)     func textStorageDidProcessEditing(_ notification: Notification)     func panel(_ sender: Any, isValidFilename filename: String) -> Bool     func panel(_ sender: Any, directoryDidChange path: String)     func panel(_ sender: Any, compareFilename name1: String, with name2: String, caseSensitive caseSensitive: Bool) -> ComparisonResult     func panel(_ sender: Any, shouldShowFilename filename: String) -> Bool     func awakeFromNib()     func prepareForInterfaceBuilder()     func changeColor(_ sender: Any?)     func pasteboard(_ sender: NSPasteboard, provideDataForType type: String)     func pasteboardChangedOwner(_ sender: NSPasteboard)     func validateMenuItem(_ menuItem: NSMenuItem) -> Bool     func validModesForFontPanel(_ fontPanel: NSFontPanel) -> Int     func changeFont(_ sender: Any?)     func fontManager(_ sender: Any, willIncludeFont fontName: String) -> Bool     func controlTextDidBeginEditing(_ obj: Notification)     func controlTextDidEndEditing(_ obj: Notification)     func controlTextDidChange(_ obj: Notification)     func view(_ view: NSView, stringForToolTip tag: NSToolTipTag, point point: NSPoint, userData data: UnsafeMutableRawPointer?) -> String     func layer(_ layer: CALayer, shouldInheritContentsScale newScale: CGFloat, from window: NSWindow) -> Bool     func namesOfPromisedFilesDropped(atDestination dropDestination: URL) -> [String]?     func draggingSourceOperationMask(forLocal flag: Bool) -> NSDragOperation     func draggedImage(_ image: NSImage!, beganAt screenPoint: NSPoint)     func draggedImage(_ image: NSImage!, endedAt screenPoint: NSPoint, operation operation: NSDragOperation)     func draggedImage(_ image: NSImage!, movedTo screenPoint: NSPoint)     func ignoreModifierKeysWhileDragging() -> Bool     func draggedImage(_ image: NSImage!, endedAt screenPoint: NSPoint, deposited flag: Bool)     func accessibilitySetOverrideValue(_ value: Any?, forAttribute attribute: String) -> Bool     func accessibilityAttributeNames() -> [Any]     func accessibilityAttributeValue(_ attribute: String) -> Any?     func accessibilityIsAttributeSettable(_ attribute: String) -> Bool     func accessibilitySetValue(_ value: Any?, forAttribute attribute: String)     func accessibilityParameterizedAttributeNames() -> [Any]     func accessibilityAttributeValue(_ attribute: String, forParameter parameter: Any?) -> Any?     func accessibilityActionNames() -> [Any]     func accessibilityActionDescription(_ action: String) -> String?     func accessibilityPerformAction(_ action: String)     func accessibilityIsIgnored() -> Bool     func accessibilityHitTest(_ point: NSPoint) -> Any?     var accessibilityFocusedUIElement: Any? { get }     func accessibilityIndex(ofChild child: Any) -> Int     func accessibilityArrayAttributeCount(_ attribute: String) -> Int     func accessibilityArrayAttributeValues(_ attribute: String, index index: Int, maxCount maxCount: Int) -> [Any]     var accessibilityNotifiesWhenDestroyed: Bool { get }     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension EKEventStore : CVarArg { } extension EKEventStore : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [EKEventStore.authorizationStatus(for: EKEntityType) -> EKAuthorizationStatus [class]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507239-authorizationstatus)

|  | Declaration |
| --- | --- |
| From | ``` class func authorizationStatusForEntityType(_ entityType: EKEntityType) -> EKAuthorizationStatus ``` |
| To | ``` class func authorizationStatus(for entityType: EKEntityType) -> EKAuthorizationStatus ``` |

Modified [EKEventStore.calendar(withIdentifier: String) -> EKCalendar?](https://developer.apple.com/documentation/eventkit/ekeventstore/1507484-calendar)

|  | Declaration |
| --- | --- |
| From | ``` func calendarWithIdentifier(_ identifier: String) -> EKCalendar? ``` |
| To | ``` func calendar(withIdentifier identifier: String) -> EKCalendar? ``` |

Modified [EKEventStore.calendarItem(withIdentifier: String) -> EKCalendarItem](https://developer.apple.com/documentation/eventkit/ekeventstore/1507433-calendaritemwithidentifier)

|  | Declaration |
| --- | --- |
| From | ``` func calendarItemWithIdentifier(_ identifier: String) -> EKCalendarItem ``` |
| To | ``` func calendarItem(withIdentifier identifier: String) -> EKCalendarItem ``` |

Modified [EKEventStore.calendarItems(withExternalIdentifier: String) -> [EKCalendarItem]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507281-calendaritems)

|  | Declaration |
| --- | --- |
| From | ``` func calendarItemsWithExternalIdentifier(_ externalIdentifier: String) -> [EKCalendarItem] ``` |
| To | ``` func calendarItems(withExternalIdentifier externalIdentifier: String) -> [EKCalendarItem] ``` |

Modified [EKEventStore.calendars(for: EKEntityType) -> [EKCalendar]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507128-calendarsforentitytype)

|  | Declaration |
| --- | --- |
| From | ``` func calendarsForEntityType(_ entityType: EKEntityType) -> [EKCalendar] ``` |
| To | ``` func calendars(for entityType: EKEntityType) -> [EKCalendar] ``` |

Modified [EKEventStore.cancelFetchRequest(_: Any)](https://developer.apple.com/documentation/eventkit/ekeventstore/1507342-cancelfetchrequest)

|  | Declaration |
| --- | --- |
| From | ``` func cancelFetchRequest(_ fetchIdentifier: AnyObject) ``` |
| To | ``` func cancelFetchRequest(_ fetchIdentifier: Any) ``` |

Modified [EKEventStore.enumerateEvents(matching: NSPredicate, using: EventKit.EKEventSearchCallback)](https://developer.apple.com/documentation/eventkit/ekeventstore/1507518-enumerateeventsmatchingpredicate)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateEventsMatchingPredicate(_ predicate: NSPredicate, usingBlock block: EKEventSearchCallback) ``` |
| To | ``` func enumerateEvents(matching predicate: NSPredicate, using block: EventKit.EKEventSearchCallback) ``` |

Modified [EKEventStore.event(withIdentifier: String) -> EKEvent?](https://developer.apple.com/documentation/eventkit/ekeventstore/1507490-event)

|  | Declaration |
| --- | --- |
| From | ``` func eventWithIdentifier(_ identifier: String) -> EKEvent? ``` |
| To | ``` func event(withIdentifier identifier: String) -> EKEvent? ``` |

Modified [EKEventStore.events(matching: NSPredicate) -> [EKEvent]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507183-eventsmatchingpredicate)

|  | Declaration |
| --- | --- |
| From | ``` func eventsMatchingPredicate(_ predicate: NSPredicate) -> [EKEvent] ``` |
| To | ``` func events(matching predicate: NSPredicate) -> [EKEvent] ``` |

Modified [EKEventStore.fetchReminders(matching: NSPredicate, completion: ([EKReminder]?) -> Swift.Void) -> Any](https://developer.apple.com/documentation/eventkit/ekeventstore/1507500-fetchreminders)

|  | Declaration |
| --- | --- |
| From | ``` func fetchRemindersMatchingPredicate(_ predicate: NSPredicate, completion completion: ([EKReminder]?) -> Void) -> AnyObject ``` |
| To | ``` func fetchReminders(matching predicate: NSPredicate, completion completion: @escaping ([EKReminder]?) -> Swift.Void) -> Any ``` |

Modified [EKEventStore.predicateForCompletedReminders(withCompletionDateStarting: Date?, ending: Date?, calendars: [EKCalendar]?) -> NSPredicate](https://developer.apple.com/documentation/eventkit/ekeventstore/1507447-predicateforcompletedreminderswi)

|  | Declaration |
| --- | --- |
| From | ``` func predicateForCompletedRemindersWithCompletionDateStarting(_ startDate: NSDate?, ending endDate: NSDate?, calendars calendars: [EKCalendar]?) -> NSPredicate ``` |
| To | ``` func predicateForCompletedReminders(withCompletionDateStarting startDate: Date?, ending endDate: Date?, calendars calendars: [EKCalendar]?) -> NSPredicate ``` |

Modified [EKEventStore.predicateForEvents(withStart: Date, end: Date, calendars: [EKCalendar]?) -> NSPredicate](https://developer.apple.com/documentation/eventkit/ekeventstore/1507479-predicateforevents)

|  | Declaration |
| --- | --- |
| From | ``` func predicateForEventsWithStartDate(_ startDate: NSDate, endDate endDate: NSDate, calendars calendars: [EKCalendar]?) -> NSPredicate ``` |
| To | ``` func predicateForEvents(withStart startDate: Date, end endDate: Date, calendars calendars: [EKCalendar]?) -> NSPredicate ``` |

Modified [EKEventStore.predicateForIncompleteReminders(withDueDateStarting: Date?, ending: Date?, calendars: [EKCalendar]?) -> NSPredicate](https://developer.apple.com/documentation/eventkit/ekeventstore/1507143-predicateforincompleteremindersw)

|  | Declaration |
| --- | --- |
| From | ``` func predicateForIncompleteRemindersWithDueDateStarting(_ startDate: NSDate?, ending endDate: NSDate?, calendars calendars: [EKCalendar]?) -> NSPredicate ``` |
| To | ``` func predicateForIncompleteReminders(withDueDateStarting startDate: Date?, ending endDate: Date?, calendars calendars: [EKCalendar]?) -> NSPredicate ``` |

Modified [EKEventStore.predicateForReminders(in: [EKCalendar]?) -> NSPredicate](https://developer.apple.com/documentation/eventkit/ekeventstore/1507086-predicateforreminders)

|  | Declaration |
| --- | --- |
| From | ``` func predicateForRemindersInCalendars(_ calendars: [EKCalendar]?) -> NSPredicate ``` |
| To | ``` func predicateForReminders(in calendars: [EKCalendar]?) -> NSPredicate ``` |

Modified [EKEventStore.remove(_: EKReminder, commit: Bool) throws](https://developer.apple.com/documentation/eventkit/ekeventstore/1507108-removereminder)

|  | Declaration |
| --- | --- |
| From | ``` func removeReminder(_ reminder: EKReminder, commit commit: Bool) throws ``` |
| To | ``` func remove(_ reminder: EKReminder, commit commit: Bool) throws ``` |

Modified [EKEventStore.remove(_: EKEvent, span: EKSpan, commit: Bool) throws](https://developer.apple.com/documentation/eventkit/ekeventstore/1507469-remove)

|  | Declaration |
| --- | --- |
| From | ``` func removeEvent(_ event: EKEvent, span span: EKSpan, commit commit: Bool) throws ``` |
| To | ``` func remove(_ event: EKEvent, span span: EKSpan, commit commit: Bool) throws ``` |

Modified [EKEventStore.requestAccess(to: EKEntityType, completion: EventKit.EKEventStoreRequestAccessCompletionHandler)](https://developer.apple.com/documentation/eventkit/ekeventstore/1507547-requestaccesstoentitytype)

|  | Declaration |
| --- | --- |
| From | ``` func requestAccessToEntityType(_ entityType: EKEntityType, completion completion: EKEventStoreRequestAccessCompletionHandler) ``` |
| To | ``` func requestAccess(to entityType: EKEntityType, completion completion: EventKit.EKEventStoreRequestAccessCompletionHandler) ``` |

Modified [EKEventStore.save(_: EKReminder, commit: Bool) throws](https://developer.apple.com/documentation/eventkit/ekeventstore/1507181-save)

|  | Declaration |
| --- | --- |
| From | ``` func saveReminder(_ reminder: EKReminder, commit commit: Bool) throws ``` |
| To | ``` func save(_ reminder: EKReminder, commit commit: Bool) throws ``` |

Modified [EKEventStore.save(_: EKEvent, span: EKSpan, commit: Bool) throws](https://developer.apple.com/documentation/eventkit/ekeventstore/1507295-save)

|  | Declaration |
| --- | --- |
| From | ``` func saveEvent(_ event: EKEvent, span span: EKSpan, commit commit: Bool) throws ``` |
| To | ``` func save(_ event: EKEvent, span span: EKSpan, commit commit: Bool) throws ``` |

Modified [EKEventStore.source(withIdentifier: String) -> EKSource](https://developer.apple.com/documentation/eventkit/ekeventstore/1507521-sourcewithidentifier)

|  | Declaration |
| --- | --- |
| From | ``` func sourceWithIdentifier(_ identifier: String) -> EKSource ``` |
| To | ``` func source(withIdentifier identifier: String) -> EKSource ``` |

Modified [EKObject](https://developer.apple.com/documentation/eventkit/ekobject)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class EKObject : NSObject {     var hasChanges: Bool { get }     var new: Bool { get }     func reset()     func rollback()     func refresh() -> Bool } ``` | -- |
| To | ``` class EKObject : NSObject {     var hasChanges: Bool { get }     var isNew: Bool { get }     func reset()     func rollback()     func refresh() -> Bool     func actionProperty() -> String!     func title(for person: ABPerson!, identifier identifier: String!) -> String!     func performAction(for person: ABPerson!, identifier identifier: String!)     func shouldEnableAction(for person: ABPerson!, identifier identifier: String!) -> Bool     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any?     func discardEditing()     func commitEditing() -> Bool     func commitEditing(withDelegate delegate: Any?, didCommit didCommitSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func commitEditingAndReturnError() throws     func objectDidBeginEditing(_ editor: Any)     func objectDidEndEditing(_ editor: Any)     class func setDefaultPlaceholder(_ placeholder: Any?, forMarker marker: Any?, withBinding binding: String)     class func defaultPlaceholder(forMarker marker: Any?, withBinding binding: String) -> Any?     class func exposeBinding(_ binding: String)     var exposedBindings: [String] { get }     func valueClassForBinding(_ binding: String) -> AnyClass?     func bind(_ binding: String, to observable: Any, withKeyPath keyPath: String, options options: [String : Any]? = nil)     func unbind(_ binding: String)     func infoForBinding(_ binding: String) -> [String : Any]?     func optionDescriptionsForBinding(_ binding: String) -> [NSAttributeDescription]     func validateToolbarItem(_ item: NSToolbarItem) -> Bool     func application(_ sender: NSApplication, delegateHandlesKey key: String) -> Bool     func tableView(_ tableView: NSTableView, writeRows rows: [Any], to pboard: NSPasteboard) -> Bool     func textStorageWillProcessEditing(_ notification: Notification)     func textStorageDidProcessEditing(_ notification: Notification)     func panel(_ sender: Any, isValidFilename filename: String) -> Bool     func panel(_ sender: Any, directoryDidChange path: String)     func panel(_ sender: Any, compareFilename name1: String, with name2: String, caseSensitive caseSensitive: Bool) -> ComparisonResult     func panel(_ sender: Any, shouldShowFilename filename: String) -> Bool     func awakeFromNib()     func prepareForInterfaceBuilder()     func changeColor(_ sender: Any?)     func pasteboard(_ sender: NSPasteboard, provideDataForType type: String)     func pasteboardChangedOwner(_ sender: NSPasteboard)     func validateMenuItem(_ menuItem: NSMenuItem) -> Bool     func validModesForFontPanel(_ fontPanel: NSFontPanel) -> Int     func changeFont(_ sender: Any?)     func fontManager(_ sender: Any, willIncludeFont fontName: String) -> Bool     func controlTextDidBeginEditing(_ obj: Notification)     func controlTextDidEndEditing(_ obj: Notification)     func controlTextDidChange(_ obj: Notification)     func view(_ view: NSView, stringForToolTip tag: NSToolTipTag, point point: NSPoint, userData data: UnsafeMutableRawPointer?) -> String     func layer(_ layer: CALayer, shouldInheritContentsScale newScale: CGFloat, from window: NSWindow) -> Bool     func namesOfPromisedFilesDropped(atDestination dropDestination: URL) -> [String]?     func draggingSourceOperationMask(forLocal flag: Bool) -> NSDragOperation     func draggedImage(_ image: NSImage!, beganAt screenPoint: NSPoint)     func draggedImage(_ image: NSImage!, endedAt screenPoint: NSPoint, operation operation: NSDragOperation)     func draggedImage(_ image: NSImage!, movedTo screenPoint: NSPoint)     func ignoreModifierKeysWhileDragging() -> Bool     func draggedImage(_ image: NSImage!, endedAt screenPoint: NSPoint, deposited flag: Bool)     func accessibilitySetOverrideValue(_ value: Any?, forAttribute attribute: String) -> Bool     func accessibilityAttributeNames() -> [Any]     func accessibilityAttributeValue(_ attribute: String) -> Any?     func accessibilityIsAttributeSettable(_ attribute: String) -> Bool     func accessibilitySetValue(_ value: Any?, forAttribute attribute: String)     func accessibilityParameterizedAttributeNames() -> [Any]     func accessibilityAttributeValue(_ attribute: String, forParameter parameter: Any?) -> Any?     func accessibilityActionNames() -> [Any]     func accessibilityActionDescription(_ action: String) -> String?     func accessibilityPerformAction(_ action: String)     func accessibilityIsIgnored() -> Bool     func accessibilityHitTest(_ point: NSPoint) -> Any?     var accessibilityFocusedUIElement: Any? { get }     func accessibilityIndex(ofChild child: Any) -> Int     func accessibilityArrayAttributeCount(_ attribute: String) -> Int     func accessibilityArrayAttributeValues(_ attribute: String, index index: Int, maxCount maxCount: Int) -> [Any]     var accessibilityNotifiesWhenDestroyed: Bool { get }     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension EKObject : CVarArg { } extension EKObject : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [EKObject.isNew](https://developer.apple.com/documentation/eventkit/ekobject/1507402-isnew)

|  | Declaration |
| --- | --- |
| From | ``` var new: Bool { get } ``` |
| To | ``` var isNew: Bool { get } ``` |

Modified [EKParticipant](https://developer.apple.com/documentation/eventkit/ekparticipant)

|  | Declaration |
| --- | --- |
| From | ``` class EKParticipant : EKObject, NSCopying {     var URL: NSURL { get }     var name: String? { get }     var participantStatus: EKParticipantStatus { get }     var participantRole: EKParticipantRole { get }     var participantType: EKParticipantType { get }     var currentUser: Bool { get }     var contactPredicate: NSPredicate { get }     func ABPersonInAddressBook(_ addressBook: ABAddressBook) -> ABPerson? } ``` |
| To | ``` class EKParticipant : EKObject, NSCopying {     var url: URL { get }     var name: String? { get }     var participantStatus: EKParticipantStatus { get }     var participantRole: EKParticipantRole { get }     var participantType: EKParticipantType { get }     var isCurrentUser: Bool { get }     var contactPredicate: NSPredicate { get }     func abPerson(in addressBook: ABAddressBook) -> ABPerson? } ``` |

Modified [EKParticipant.abPerson(in: ABAddressBook) -> ABPerson?](https://developer.apple.com/documentation/eventkit/ekparticipant/1507504-abperson)

|  | Declaration |
| --- | --- |
| From | ``` func ABPersonInAddressBook(_ addressBook: ABAddressBook) -> ABPerson? ``` |
| To | ``` func abPerson(in addressBook: ABAddressBook) -> ABPerson? ``` |

Modified [EKParticipant.isCurrentUser](https://developer.apple.com/documentation/eventkit/ekparticipant/1507248-iscurrentuser)

|  | Declaration |
| --- | --- |
| From | ``` var currentUser: Bool { get } ``` |
| To | ``` var isCurrentUser: Bool { get } ``` |

Modified [EKParticipant.url](https://developer.apple.com/documentation/eventkit/ekparticipant/1507435-url)

|  | Declaration |
| --- | --- |
| From | ``` var URL: NSURL { get } ``` |
| To | ``` var url: URL { get } ``` |

Modified [EKParticipantRole [enum]](https://developer.apple.com/documentation/eventkit/ekparticipantrole)

|  | Declaration |
| --- | --- |
| From | ``` enum EKParticipantRole : Int {     case Unknown     case Required     case Optional     case Chair     case NonParticipant } ``` |
| To | ``` enum EKParticipantRole : Int {     case unknown     case required     case optional     case chair     case nonParticipant } ``` |

Modified [EKParticipantRole.chair](https://developer.apple.com/documentation/eventkit/ekparticipantrole/ekparticipantrolechair)

|  | Declaration |
| --- | --- |
| From | ``` case Chair ``` |
| To | ``` case chair ``` |

Modified [EKParticipantRole.nonParticipant](https://developer.apple.com/documentation/eventkit/ekparticipantrole/nonparticipant)

|  | Declaration |
| --- | --- |
| From | ``` case NonParticipant ``` |
| To | ``` case nonParticipant ``` |

Modified [EKParticipantRole.optional](https://developer.apple.com/documentation/eventkit/ekparticipantrole/ekparticipantroleoptional)

|  | Declaration |
| --- | --- |
| From | ``` case Optional ``` |
| To | ``` case optional ``` |

Modified [EKParticipantRole.required](https://developer.apple.com/documentation/eventkit/ekparticipantrole/required)

|  | Declaration |
| --- | --- |
| From | ``` case Required ``` |
| To | ``` case required ``` |

Modified [EKParticipantRole.unknown](https://developer.apple.com/documentation/eventkit/ekparticipantrole/unknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [EKParticipantScheduleStatus [enum]](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus)

|  | Declaration |
| --- | --- |
| From | ``` enum EKParticipantScheduleStatus : Int {     case None     case Pending     case Sent     case Delivered     case RecipientNotRecognized     case NoPrivileges     case DeliveryFailed     case CannotDeliver     case RecipientNotAllowed } ``` |
| To | ``` enum EKParticipantScheduleStatus : Int {     case none     case pending     case sent     case delivered     case recipientNotRecognized     case noPrivileges     case deliveryFailed     case cannotDeliver     case recipientNotAllowed } ``` |

Modified [EKParticipantScheduleStatus.cannotDeliver](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/ekparticipantschedulestatuscannotdeliver)

|  | Declaration |
| --- | --- |
| From | ``` case CannotDeliver ``` |
| To | ``` case cannotDeliver ``` |

Modified [EKParticipantScheduleStatus.delivered](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/ekparticipantschedulestatusdelivered)

|  | Declaration |
| --- | --- |
| From | ``` case Delivered ``` |
| To | ``` case delivered ``` |

Modified [EKParticipantScheduleStatus.deliveryFailed](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/deliveryfailed)

|  | Declaration |
| --- | --- |
| From | ``` case DeliveryFailed ``` |
| To | ``` case deliveryFailed ``` |

Modified [EKParticipantScheduleStatus.none](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/none)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [EKParticipantScheduleStatus.noPrivileges](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/noprivileges)

|  | Declaration |
| --- | --- |
| From | ``` case NoPrivileges ``` |
| To | ``` case noPrivileges ``` |

Modified [EKParticipantScheduleStatus.pending](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/pending)

|  | Declaration |
| --- | --- |
| From | ``` case Pending ``` |
| To | ``` case pending ``` |

Modified [EKParticipantScheduleStatus.recipientNotAllowed](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/recipientnotallowed)

|  | Declaration |
| --- | --- |
| From | ``` case RecipientNotAllowed ``` |
| To | ``` case recipientNotAllowed ``` |

Modified [EKParticipantScheduleStatus.recipientNotRecognized](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/ekparticipantschedulestatusrecipientnotrecognized)

|  | Declaration |
| --- | --- |
| From | ``` case RecipientNotRecognized ``` |
| To | ``` case recipientNotRecognized ``` |

Modified [EKParticipantScheduleStatus.sent](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/sent)

|  | Declaration |
| --- | --- |
| From | ``` case Sent ``` |
| To | ``` case sent ``` |

Modified [EKParticipantStatus [enum]](https://developer.apple.com/documentation/eventkit/ekparticipantstatus)

|  | Declaration |
| --- | --- |
| From | ``` enum EKParticipantStatus : Int {     case Unknown     case Pending     case Accepted     case Declined     case Tentative     case Delegated     case Completed     case InProcess } ``` |
| To | ``` enum EKParticipantStatus : Int {     case unknown     case pending     case accepted     case declined     case tentative     case delegated     case completed     case inProcess } ``` |

Modified [EKParticipantStatus.accepted](https://developer.apple.com/documentation/eventkit/ekparticipantstatus/accepted)

|  | Declaration |
| --- | --- |
| From | ``` case Accepted ``` |
| To | ``` case accepted ``` |

Modified [EKParticipantStatus.completed](https://developer.apple.com/documentation/eventkit/ekparticipantstatus/completed)

|  | Declaration |
| --- | --- |
| From | ``` case Completed ``` |
| To | ``` case completed ``` |

Modified [EKParticipantStatus.declined](https://developer.apple.com/documentation/eventkit/ekparticipantstatus/declined)

|  | Declaration |
| --- | --- |
| From | ``` case Declined ``` |
| To | ``` case declined ``` |

Modified [EKParticipantStatus.delegated](https://developer.apple.com/documentation/eventkit/ekparticipantstatus/delegated)

|  | Declaration |
| --- | --- |
| From | ``` case Delegated ``` |
| To | ``` case delegated ``` |

Modified [EKParticipantStatus.inProcess](https://developer.apple.com/documentation/eventkit/ekparticipantstatus/ekparticipantstatusinprocess)

|  | Declaration |
| --- | --- |
| From | ``` case InProcess ``` |
| To | ``` case inProcess ``` |

Modified [EKParticipantStatus.pending](https://developer.apple.com/documentation/eventkit/ekparticipantstatus/pending)

|  | Declaration |
| --- | --- |
| From | ``` case Pending ``` |
| To | ``` case pending ``` |

Modified [EKParticipantStatus.tentative](https://developer.apple.com/documentation/eventkit/ekparticipantstatus/tentative)

|  | Declaration |
| --- | --- |
| From | ``` case Tentative ``` |
| To | ``` case tentative ``` |

Modified [EKParticipantStatus.unknown](https://developer.apple.com/documentation/eventkit/ekparticipantstatus/ekparticipantstatusunknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [EKParticipantType [enum]](https://developer.apple.com/documentation/eventkit/ekparticipanttype)

|  | Declaration |
| --- | --- |
| From | ``` enum EKParticipantType : Int {     case Unknown     case Person     case Room     case Resource     case Group } ``` |
| To | ``` enum EKParticipantType : Int {     case unknown     case person     case room     case resource     case group } ``` |

Modified [EKParticipantType.group](https://developer.apple.com/documentation/eventkit/ekparticipanttype/ekparticipanttypegroup)

|  | Declaration |
| --- | --- |
| From | ``` case Group ``` |
| To | ``` case group ``` |

Modified [EKParticipantType.person](https://developer.apple.com/documentation/eventkit/ekparticipanttype/person)

|  | Declaration |
| --- | --- |
| From | ``` case Person ``` |
| To | ``` case person ``` |

Modified [EKParticipantType.resource](https://developer.apple.com/documentation/eventkit/ekparticipanttype/ekparticipanttyperesource)

|  | Declaration |
| --- | --- |
| From | ``` case Resource ``` |
| To | ``` case resource ``` |

Modified [EKParticipantType.room](https://developer.apple.com/documentation/eventkit/ekparticipanttype/ekparticipanttyperoom)

|  | Declaration |
| --- | --- |
| From | ``` case Room ``` |
| To | ``` case room ``` |

Modified [EKParticipantType.unknown](https://developer.apple.com/documentation/eventkit/ekparticipanttype/ekparticipanttypeunknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [EKRecurrenceDayOfWeek](https://developer.apple.com/documentation/eventkit/ekrecurrencedayofweek)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class EKRecurrenceDayOfWeek : NSObject, NSCopying {     convenience init(_ dayOfTheWeek: EKWeekday)     class func dayOfWeek(_ dayOfTheWeek: EKWeekday) -> Self     convenience init(_ dayOfTheWeek: EKWeekday, weekNumber weekNumber: Int)     class func dayOfWeek(_ dayOfTheWeek: EKWeekday, weekNumber weekNumber: Int) -> Self     init(dayOfTheWeek dayOfTheWeek: EKWeekday, weekNumber weekNumber: Int)     var dayOfTheWeek: EKWeekday { get }     var weekNumber: Int { get } } ``` | NSCopying |
| To | ``` class EKRecurrenceDayOfWeek : NSObject, NSCopying {     convenience init(_ dayOfTheWeek: EKWeekday)     class func day(ofWeek dayOfTheWeek: EKWeekday) -> Self     convenience init(_ dayOfTheWeek: EKWeekday, weekNumber weekNumber: Int)     class func day(ofWeek dayOfTheWeek: EKWeekday, weekNumber weekNumber: Int) -> Self     init(dayOfTheWeek dayOfTheWeek: EKWeekday, weekNumber weekNumber: Int)     var dayOfTheWeek: EKWeekday { get }     var weekNumber: Int { get }     func actionProperty() -> String!     func title(for person: ABPerson!, identifier identifier: String!) -> String!     func performAction(for person: ABPerson!, identifier identifier: String!)     func shouldEnableAction(for person: ABPerson!, identifier identifier: String!) -> Bool     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any?     func discardEditing()     func commitEditing() -> Bool     func commitEditing(withDelegate delegate: Any?, didCommit didCommitSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func commitEditingAndReturnError() throws     func objectDidBeginEditing(_ editor: Any)     func objectDidEndEditing(_ editor: Any)     class func setDefaultPlaceholder(_ placeholder: Any?, forMarker marker: Any?, withBinding binding: String)     class func defaultPlaceholder(forMarker marker: Any?, withBinding binding: String) -> Any?     class func exposeBinding(_ binding: String)     var exposedBindings: [String] { get }     func valueClassForBinding(_ binding: String) -> AnyClass?     func bind(_ binding: String, to observable: Any, withKeyPath keyPath: String, options options: [String : Any]? = nil)     func unbind(_ binding: String)     func infoForBinding(_ binding: String) -> [String : Any]?     func optionDescriptionsForBinding(_ binding: String) -> [NSAttributeDescription]     func validateToolbarItem(_ item: NSToolbarItem) -> Bool     func application(_ sender: NSApplication, delegateHandlesKey key: String) -> Bool     func tableView(_ tableView: NSTableView, writeRows rows: [Any], to pboard: NSPasteboard) -> Bool     func textStorageWillProcessEditing(_ notification: Notification)     func textStorageDidProcessEditing(_ notification: Notification)     func panel(_ sender: Any, isValidFilename filename: String) -> Bool     func panel(_ sender: Any, directoryDidChange path: String)     func panel(_ sender: Any, compareFilename name1: String, with name2: String, caseSensitive caseSensitive: Bool) -> ComparisonResult     func panel(_ sender: Any, shouldShowFilename filename: String) -> Bool     func awakeFromNib()     func prepareForInterfaceBuilder()     func changeColor(_ sender: Any?)     func pasteboard(_ sender: NSPasteboard, provideDataForType type: String)     func pasteboardChangedOwner(_ sender: NSPasteboard)     func validateMenuItem(_ menuItem: NSMenuItem) -> Bool     func validModesForFontPanel(_ fontPanel: NSFontPanel) -> Int     func changeFont(_ sender: Any?)     func fontManager(_ sender: Any, willIncludeFont fontName: String) -> Bool     func controlTextDidBeginEditing(_ obj: Notification)     func controlTextDidEndEditing(_ obj: Notification)     func controlTextDidChange(_ obj: Notification)     func view(_ view: NSView, stringForToolTip tag: NSToolTipTag, point point: NSPoint, userData data: UnsafeMutableRawPointer?) -> String     func layer(_ layer: CALayer, shouldInheritContentsScale newScale: CGFloat, from window: NSWindow) -> Bool     func namesOfPromisedFilesDropped(atDestination dropDestination: URL) -> [String]?     func draggingSourceOperationMask(forLocal flag: Bool) -> NSDragOperation     func draggedImage(_ image: NSImage!, beganAt screenPoint: NSPoint)     func draggedImage(_ image: NSImage!, endedAt screenPoint: NSPoint, operation operation: NSDragOperation)     func draggedImage(_ image: NSImage!, movedTo screenPoint: NSPoint)     func ignoreModifierKeysWhileDragging() -> Bool     func draggedImage(_ image: NSImage!, endedAt screenPoint: NSPoint, deposited flag: Bool)     func accessibilitySetOverrideValue(_ value: Any?, forAttribute attribute: String) -> Bool     func accessibilityAttributeNames() -> [Any]     func accessibilityAttributeValue(_ attribute: String) -> Any?     func accessibilityIsAttributeSettable(_ attribute: String) -> Bool     func accessibilitySetValue(_ value: Any?, forAttribute attribute: String)     func accessibilityParameterizedAttributeNames() -> [Any]     func accessibilityAttributeValue(_ attribute: String, forParameter parameter: Any?) -> Any?     func accessibilityActionNames() -> [Any]     func accessibilityActionDescription(_ action: String) -> String?     func accessibilityPerformAction(_ action: String)     func accessibilityIsIgnored() -> Bool     func accessibilityHitTest(_ point: NSPoint) -> Any?     var accessibilityFocusedUIElement: Any? { get }     func accessibilityIndex(ofChild child: Any) -> Int     func accessibilityArrayAttributeCount(_ attribute: String) -> Int     func accessibilityArrayAttributeValues(_ attribute: String, index index: Int, maxCount maxCount: Int) -> [Any]     var accessibilityNotifiesWhenDestroyed: Bool { get }     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension EKRecurrenceDayOfWeek : CVarArg { } extension EKRecurrenceDayOfWeek : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [EKRecurrenceEnd](https://developer.apple.com/documentation/eventkit/ekrecurrenceend)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class EKRecurrenceEnd : NSObject, NSCopying {     convenience init(endDate endDate: NSDate)     class func recurrenceEndWithEndDate(_ endDate: NSDate) -> Self     convenience init(occurrenceCount occurrenceCount: Int)     class func recurrenceEndWithOccurrenceCount(_ occurrenceCount: Int) -> Self     var endDate: NSDate? { get }     var occurrenceCount: Int { get } } ``` | NSCopying |
| To | ``` class EKRecurrenceEnd : NSObject, NSCopying {     convenience init(end endDate: Date)     class func withEnd(_ endDate: Date) -> Self     convenience init(occurrenceCount occurrenceCount: Int)     class func withOccurrenceCount(_ occurrenceCount: Int) -> Self     var endDate: Date? { get }     var occurrenceCount: Int { get }     func actionProperty() -> String!     func title(for person: ABPerson!, identifier identifier: String!) -> String!     func performAction(for person: ABPerson!, identifier identifier: String!)     func shouldEnableAction(for person: ABPerson!, identifier identifier: String!) -> Bool     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any?     func discardEditing()     func commitEditing() -> Bool     func commitEditing(withDelegate delegate: Any?, didCommit didCommitSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func commitEditingAndReturnError() throws     func objectDidBeginEditing(_ editor: Any)     func objectDidEndEditing(_ editor: Any)     class func setDefaultPlaceholder(_ placeholder: Any?, forMarker marker: Any?, withBinding binding: String)     class func defaultPlaceholder(forMarker marker: Any?, withBinding binding: String) -> Any?     class func exposeBinding(_ binding: String)     var exposedBindings: [String] { get }     func valueClassForBinding(_ binding: String) -> AnyClass?     func bind(_ binding: String, to observable: Any, withKeyPath keyPath: String, options options: [String : Any]? = nil)     func unbind(_ binding: String)     func infoForBinding(_ binding: String) -> [String : Any]?     func optionDescriptionsForBinding(_ binding: String) -> [NSAttributeDescription]     func validateToolbarItem(_ item: NSToolbarItem) -> Bool     func application(_ sender: NSApplication, delegateHandlesKey key: String) -> Bool     func tableView(_ tableView: NSTableView, writeRows rows: [Any], to pboard: NSPasteboard) -> Bool     func textStorageWillProcessEditing(_ notification: Notification)     func textStorageDidProcessEditing(_ notification: Notification)     func panel(_ sender: Any, isValidFilename filename: String) -> Bool     func panel(_ sender: Any, directoryDidChange path: String)     func panel(_ sender: Any, compareFilename name1: String, with name2: String, caseSensitive caseSensitive: Bool) -> ComparisonResult     func panel(_ sender: Any, shouldShowFilename filename: String) -> Bool     func awakeFromNib()     func prepareForInterfaceBuilder()     func changeColor(_ sender: Any?)     func pasteboard(_ sender: NSPasteboard, provideDataForType type: String)     func pasteboardChangedOwner(_ sender: NSPasteboard)     func validateMenuItem(_ menuItem: NSMenuItem) -> Bool     func validModesForFontPanel(_ fontPanel: NSFontPanel) -> Int     func changeFont(_ sender: Any?)     func fontManager(_ sender: Any, willIncludeFont fontName: String) -> Bool     func controlTextDidBeginEditing(_ obj: Notification)     func controlTextDidEndEditing(_ obj: Notification)     func controlTextDidChange(_ obj: Notification)     func view(_ view: NSView, stringForToolTip tag: NSToolTipTag, point point: NSPoint, userData data: UnsafeMutableRawPointer?) -> String     func layer(_ layer: CALayer, shouldInheritContentsScale newScale: CGFloat, from window: NSWindow) -> Bool     func namesOfPromisedFilesDropped(atDestination dropDestination: URL) -> [String]?     func draggingSourceOperationMask(forLocal flag: Bool) -> NSDragOperation     func draggedImage(_ image: NSImage!, beganAt screenPoint: NSPoint)     func draggedImage(_ image: NSImage!, endedAt screenPoint: NSPoint, operation operation: NSDragOperation)     func draggedImage(_ image: NSImage!, movedTo screenPoint: NSPoint)     func ignoreModifierKeysWhileDragging() -> Bool     func draggedImage(_ image: NSImage!, endedAt screenPoint: NSPoint, deposited flag: Bool)     func accessibilitySetOverrideValue(_ value: Any?, forAttribute attribute: String) -> Bool     func accessibilityAttributeNames() -> [Any]     func accessibilityAttributeValue(_ attribute: String) -> Any?     func accessibilityIsAttributeSettable(_ attribute: String) -> Bool     func accessibilitySetValue(_ value: Any?, forAttribute attribute: String)     func accessibilityParameterizedAttributeNames() -> [Any]     func accessibilityAttributeValue(_ attribute: String, forParameter parameter: Any?) -> Any?     func accessibilityActionNames() -> [Any]     func accessibilityActionDescription(_ action: String) -> String?     func accessibilityPerformAction(_ action: String)     func accessibilityIsIgnored() -> Bool     func accessibilityHitTest(_ point: NSPoint) -> Any?     var accessibilityFocusedUIElement: Any? { get }     func accessibilityIndex(ofChild child: Any) -> Int     func accessibilityArrayAttributeCount(_ attribute: String) -> Int     func accessibilityArrayAttributeValues(_ attribute: String, index index: Int, maxCount maxCount: Int) -> [Any]     var accessibilityNotifiesWhenDestroyed: Bool { get }     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension EKRecurrenceEnd : CVarArg { } extension EKRecurrenceEnd : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [EKRecurrenceEnd.endDate](https://developer.apple.com/documentation/eventkit/ekrecurrenceend/1415648-enddate)

|  | Declaration |
| --- | --- |
| From | ``` var endDate: NSDate? { get } ``` |
| To | ``` var endDate: Date? { get } ``` |

Modified [EKRecurrenceEnd.init(end: Date)](https://developer.apple.com/documentation/eventkit/ekrecurrenceend/1415644-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(endDate endDate: NSDate) ``` |
| To | ``` convenience init(end endDate: Date) ``` |

Modified [EKRecurrenceFrequency [enum]](https://developer.apple.com/documentation/eventkit/ekrecurrencefrequency)

|  | Declaration |
| --- | --- |
| From | ``` enum EKRecurrenceFrequency : Int {     case Daily     case Weekly     case Monthly     case Yearly } ``` |
| To | ``` enum EKRecurrenceFrequency : Int {     case daily     case weekly     case monthly     case yearly } ``` |

Modified [EKRecurrenceFrequency.daily](https://developer.apple.com/documentation/eventkit/ekrecurrencefrequency/ekrecurrencefrequencydaily)

|  | Declaration |
| --- | --- |
| From | ``` case Daily ``` |
| To | ``` case daily ``` |

Modified [EKRecurrenceFrequency.monthly](https://developer.apple.com/documentation/eventkit/ekrecurrencefrequency/ekrecurrencefrequencymonthly)

|  | Declaration |
| --- | --- |
| From | ``` case Monthly ``` |
| To | ``` case monthly ``` |

Modified [EKRecurrenceFrequency.weekly](https://developer.apple.com/documentation/eventkit/ekrecurrencefrequency/ekrecurrencefrequencyweekly)

|  | Declaration |
| --- | --- |
| From | ``` case Weekly ``` |
| To | ``` case weekly ``` |

Modified [EKRecurrenceFrequency.yearly](https://developer.apple.com/documentation/eventkit/ekrecurrencefrequency/yearly)

|  | Declaration |
| --- | --- |
| From | ``` case Yearly ``` |
| To | ``` case yearly ``` |

Modified [EKRecurrenceRule](https://developer.apple.com/documentation/eventkit/ekrecurrencerule)

|  | Declaration |
| --- | --- |
| From | ``` class EKRecurrenceRule : EKObject, NSCopying {     init(recurrenceWithFrequency type: EKRecurrenceFrequency, interval interval: Int, end end: EKRecurrenceEnd?)     init(recurrenceWithFrequency type: EKRecurrenceFrequency, interval interval: Int, daysOfTheWeek days: [EKRecurrenceDayOfWeek]?, daysOfTheMonth monthDays: [NSNumber]?, monthsOfTheYear months: [NSNumber]?, weeksOfTheYear weeksOfTheYear: [NSNumber]?, daysOfTheYear daysOfTheYear: [NSNumber]?, setPositions setPositions: [NSNumber]?, end end: EKRecurrenceEnd?)     var calendarIdentifier: String { get }     @NSCopying var recurrenceEnd: EKRecurrenceEnd?     var frequency: EKRecurrenceFrequency { get }     var interval: Int { get }     var firstDayOfTheWeek: Int { get }     var daysOfTheWeek: [EKRecurrenceDayOfWeek]? { get }     var daysOfTheMonth: [NSNumber]? { get }     var daysOfTheYear: [NSNumber]? { get }     var weeksOfTheYear: [NSNumber]? { get }     var monthsOfTheYear: [NSNumber]? { get }     var setPositions: [NSNumber]? { get } } ``` |
| To | ``` class EKRecurrenceRule : EKObject, NSCopying {     init(recurrenceWith type: EKRecurrenceFrequency, interval interval: Int, end end: EKRecurrenceEnd?)     init(recurrenceWith type: EKRecurrenceFrequency, interval interval: Int, daysOfTheWeek days: [EKRecurrenceDayOfWeek]?, daysOfTheMonth monthDays: [NSNumber]?, monthsOfTheYear months: [NSNumber]?, weeksOfTheYear weeksOfTheYear: [NSNumber]?, daysOfTheYear daysOfTheYear: [NSNumber]?, setPositions setPositions: [NSNumber]?, end end: EKRecurrenceEnd?)     var calendarIdentifier: String { get }     @NSCopying var recurrenceEnd: EKRecurrenceEnd?     var frequency: EKRecurrenceFrequency { get }     var interval: Int { get }     var firstDayOfTheWeek: Int { get }     var daysOfTheWeek: [EKRecurrenceDayOfWeek]? { get }     var daysOfTheMonth: [NSNumber]? { get }     var daysOfTheYear: [NSNumber]? { get }     var weeksOfTheYear: [NSNumber]? { get }     var monthsOfTheYear: [NSNumber]? { get }     var setPositions: [NSNumber]? { get } } ``` |

Modified [EKRecurrenceRule.init(recurrenceWith: EKRecurrenceFrequency, interval: Int, daysOfTheWeek: [EKRecurrenceDayOfWeek]?, daysOfTheMonth: [NSNumber]?, monthsOfTheYear: [NSNumber]?, weeksOfTheYear: [NSNumber]?, daysOfTheYear: [NSNumber]?, setPositions: [NSNumber]?, end: EKRecurrenceEnd?)](https://developer.apple.com/documentation/eventkit/ekrecurrencerule/1507320-init)

|  | Declaration |
| --- | --- |
| From | ``` init(recurrenceWithFrequency type: EKRecurrenceFrequency, interval interval: Int, daysOfTheWeek days: [EKRecurrenceDayOfWeek]?, daysOfTheMonth monthDays: [NSNumber]?, monthsOfTheYear months: [NSNumber]?, weeksOfTheYear weeksOfTheYear: [NSNumber]?, daysOfTheYear daysOfTheYear: [NSNumber]?, setPositions setPositions: [NSNumber]?, end end: EKRecurrenceEnd?) ``` |
| To | ``` init(recurrenceWith type: EKRecurrenceFrequency, interval interval: Int, daysOfTheWeek days: [EKRecurrenceDayOfWeek]?, daysOfTheMonth monthDays: [NSNumber]?, monthsOfTheYear months: [NSNumber]?, weeksOfTheYear weeksOfTheYear: [NSNumber]?, daysOfTheYear daysOfTheYear: [NSNumber]?, setPositions setPositions: [NSNumber]?, end end: EKRecurrenceEnd?) ``` |

Modified [EKRecurrenceRule.init(recurrenceWith: EKRecurrenceFrequency, interval: Int, end: EKRecurrenceEnd?)](https://developer.apple.com/documentation/eventkit/ekrecurrencerule/1507273-init)

|  | Declaration |
| --- | --- |
| From | ``` init(recurrenceWithFrequency type: EKRecurrenceFrequency, interval interval: Int, end end: EKRecurrenceEnd?) ``` |
| To | ``` init(recurrenceWith type: EKRecurrenceFrequency, interval interval: Int, end end: EKRecurrenceEnd?) ``` |

Modified [EKReminder](https://developer.apple.com/documentation/eventkit/ekreminder)

|  | Declaration |
| --- | --- |
| From | ``` class EKReminder : EKCalendarItem {      init(eventStore eventStore: EKEventStore)     class func reminderWithEventStore(_ eventStore: EKEventStore) -> EKReminder     @NSCopying var startDateComponents: NSDateComponents?     @NSCopying var dueDateComponents: NSDateComponents?     var completed: Bool     @NSCopying var completionDate: NSDate?     var priority: Int } ``` |
| To | ``` class EKReminder : EKCalendarItem {      init(eventStore eventStore: EKEventStore)     class func withEventStore(_ eventStore: EKEventStore) -> EKReminder     var startDateComponents: DateComponents?     var dueDateComponents: DateComponents?     var isCompleted: Bool     var completionDate: Date?     var priority: Int } ``` |

Modified [EKReminder.completionDate](https://developer.apple.com/documentation/eventkit/ekreminder/1507286-completiondate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var completionDate: NSDate? ``` |
| To | ``` var completionDate: Date? ``` |

Modified [EKReminder.dueDateComponents](https://developer.apple.com/documentation/eventkit/ekreminder/1507383-duedatecomponents)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var dueDateComponents: NSDateComponents? ``` |
| To | ``` var dueDateComponents: DateComponents? ``` |

Modified [EKReminder.isCompleted](https://developer.apple.com/documentation/eventkit/ekreminder/1507502-iscompleted)

|  | Declaration |
| --- | --- |
| From | ``` var completed: Bool ``` |
| To | ``` var isCompleted: Bool ``` |

Modified [EKReminder.startDateComponents](https://developer.apple.com/documentation/eventkit/ekreminder/1507558-startdatecomponents)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var startDateComponents: NSDateComponents? ``` |
| To | ``` var startDateComponents: DateComponents? ``` |

Modified [EKReminderPriority [enum]](https://developer.apple.com/documentation/eventkit/ekreminderpriority)

|  | Declaration |
| --- | --- |
| From | ``` enum EKReminderPriority : UInt {     case None     case High     case Medium     case Low } ``` |
| To | ``` enum EKReminderPriority : UInt {     case none     case high     case medium     case low } ``` |

Modified [EKReminderPriority.high](https://developer.apple.com/documentation/eventkit/ekreminderpriority/ekreminderpriorityhigh)

|  | Declaration |
| --- | --- |
| From | ``` case High ``` |
| To | ``` case high ``` |

Modified [EKReminderPriority.low](https://developer.apple.com/documentation/eventkit/ekreminderpriority/ekreminderprioritylow)

|  | Declaration |
| --- | --- |
| From | ``` case Low ``` |
| To | ``` case low ``` |

Modified [EKReminderPriority.medium](https://developer.apple.com/documentation/eventkit/ekreminderpriority/ekreminderprioritymedium)

|  | Declaration |
| --- | --- |
| From | ``` case Medium ``` |
| To | ``` case medium ``` |

Modified [EKReminderPriority.none](https://developer.apple.com/documentation/eventkit/ekreminderpriority/ekreminderprioritynone)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [EKSource](https://developer.apple.com/documentation/eventkit/eksource)

|  | Declaration |
| --- | --- |
| From | ``` class EKSource : EKObject {     var sourceIdentifier: String { get }     var sourceType: EKSourceType { get }     var title: String { get }     var calendars: Set<EKCalendar> { get }     func calendarsForEntityType(_ entityType: EKEntityType) -> Set<EKCalendar> } ``` |
| To | ``` class EKSource : EKObject {     var sourceIdentifier: String { get }     var sourceType: EKSourceType { get }     var title: String { get }     var calendars: Set<EKCalendar> { get }     func calendars(for entityType: EKEntityType) -> Set<EKCalendar> } ``` |

Modified [EKSource.calendars(for: EKEntityType) -> Set<EKCalendar>](https://developer.apple.com/documentation/eventkit/eksource/1507387-calendarsforentitytype)

|  | Declaration |
| --- | --- |
| From | ``` func calendarsForEntityType(_ entityType: EKEntityType) -> Set<EKCalendar> ``` |
| To | ``` func calendars(for entityType: EKEntityType) -> Set<EKCalendar> ``` |

Modified [EKSourceType [enum]](https://developer.apple.com/documentation/eventkit/eksourcetype)

|  | Declaration |
| --- | --- |
| From | ``` enum EKSourceType : Int {     case Local     case Exchange     case CalDAV     case MobileMe     case Subscribed     case Birthdays } ``` |
| To | ``` enum EKSourceType : Int {     case local     case exchange     case calDAV     case mobileMe     case subscribed     case birthdays } ``` |

Modified [EKSourceType.birthdays](https://developer.apple.com/documentation/eventkit/eksourcetype/eksourcetypebirthdays)

|  | Declaration |
| --- | --- |
| From | ``` case Birthdays ``` |
| To | ``` case birthdays ``` |

Modified [EKSourceType.calDAV](https://developer.apple.com/documentation/eventkit/eksourcetype/eksourcetypecaldav)

|  | Declaration |
| --- | --- |
| From | ``` case CalDAV ``` |
| To | ``` case calDAV ``` |

Modified [EKSourceType.exchange](https://developer.apple.com/documentation/eventkit/eksourcetype/exchange)

|  | Declaration |
| --- | --- |
| From | ``` case Exchange ``` |
| To | ``` case exchange ``` |

Modified [EKSourceType.local](https://developer.apple.com/documentation/eventkit/eksourcetype/eksourcetypelocal)

|  | Declaration |
| --- | --- |
| From | ``` case Local ``` |
| To | ``` case local ``` |

Modified [EKSourceType.mobileMe](https://developer.apple.com/documentation/eventkit/eksourcetype/eksourcetypemobileme)

|  | Declaration |
| --- | --- |
| From | ``` case MobileMe ``` |
| To | ``` case mobileMe ``` |

Modified [EKSourceType.subscribed](https://developer.apple.com/documentation/eventkit/eksourcetype/eksourcetypesubscribed)

|  | Declaration |
| --- | --- |
| From | ``` case Subscribed ``` |
| To | ``` case subscribed ``` |

Modified [EKSpan [enum]](https://developer.apple.com/documentation/eventkit/ekspan)

|  | Declaration |
| --- | --- |
| From | ``` enum EKSpan : Int {     case ThisEvent     case FutureEvents } ``` |
| To | ``` enum EKSpan : Int {     case thisEvent     case futureEvents } ``` |

Modified [EKSpan.futureEvents](https://developer.apple.com/documentation/eventkit/ekspan/ekspanfutureevents)

|  | Declaration |
| --- | --- |
| From | ``` case FutureEvents ``` |
| To | ``` case futureEvents ``` |

Modified [EKSpan.thisEvent](https://developer.apple.com/documentation/eventkit/ekspan/thisevent)

|  | Declaration |
| --- | --- |
| From | ``` case ThisEvent ``` |
| To | ``` case thisEvent ``` |

Modified [EKStructuredLocation](https://developer.apple.com/documentation/eventkit/ekstructuredlocation)

|  | Declaration |
| --- | --- |
| From | ``` class EKStructuredLocation : EKObject, NSCopying {     convenience init(title title: String)     class func locationWithTitle(_ title: String) -> Self     convenience init(mapItem mapItem: MKMapItem)     class func locationWithMapItem(_ mapItem: MKMapItem) -> Self     var title: String     var geoLocation: CLLocation?     var radius: Double } ``` |
| To | ``` class EKStructuredLocation : EKObject, NSCopying {     convenience init(title title: String)     class func withTitle(_ title: String) -> Self     convenience init(mapItem mapItem: MKMapItem)     class func withMapItem(_ mapItem: MKMapItem) -> Self     var title: String     var geoLocation: CLLocation?     var radius: Double } ``` |

Modified [EKWeekday [enum]](https://developer.apple.com/documentation/eventkit/ekweekday)

|  | Declaration |
| --- | --- |
| From | ``` enum EKWeekday : Int {     case Sunday     case Monday     case Tuesday     case Wednesday     case Thursday     case Friday     case Saturday     static var EKSunday: EKWeekday { get }     static var EKMonday: EKWeekday { get }     static var EKTuesday: EKWeekday { get }     static var EKWednesday: EKWeekday { get }     static var EKThursday: EKWeekday { get }     static var EKFriday: EKWeekday { get }     static var EKSaturday: EKWeekday { get } } ``` |
| To | ``` enum EKWeekday : Int {     case sunday     case monday     case tuesday     case wednesday     case thursday     case friday     case saturday     static var EKSunday: EKWeekday { get }     static var EKMonday: EKWeekday { get }     static var EKTuesday: EKWeekday { get }     static var EKWednesday: EKWeekday { get }     static var EKThursday: EKWeekday { get }     static var EKFriday: EKWeekday { get }     static var EKSaturday: EKWeekday { get } } ``` |

Modified [EKWeekday.friday](https://developer.apple.com/documentation/eventkit/ekweekday/ekweekdayfriday)

|  | Declaration |
| --- | --- |
| From | ``` case Friday ``` |
| To | ``` case friday ``` |

Modified [EKWeekday.monday](https://developer.apple.com/documentation/eventkit/ekweekday/monday)

|  | Declaration |
| --- | --- |
| From | ``` case Monday ``` |
| To | ``` case monday ``` |

Modified [EKWeekday.saturday](https://developer.apple.com/documentation/eventkit/ekweekday/ekweekdaysaturday)

|  | Declaration |
| --- | --- |
| From | ``` case Saturday ``` |
| To | ``` case saturday ``` |

Modified [EKWeekday.sunday](https://developer.apple.com/documentation/eventkit/ekweekday/sunday)

|  | Declaration |
| --- | --- |
| From | ``` case Sunday ``` |
| To | ``` case sunday ``` |

Modified [EKWeekday.thursday](https://developer.apple.com/documentation/eventkit/ekweekday/ekweekdaythursday)

|  | Declaration |
| --- | --- |
| From | ``` case Thursday ``` |
| To | ``` case thursday ``` |

Modified [EKWeekday.tuesday](https://developer.apple.com/documentation/eventkit/ekweekday/ekweekdaytuesday)

|  | Declaration |
| --- | --- |
| From | ``` case Tuesday ``` |
| To | ``` case tuesday ``` |

Modified [EKWeekday.wednesday](https://developer.apple.com/documentation/eventkit/ekweekday/wednesday)

|  | Declaration |
| --- | --- |
| From | ``` case Wednesday ``` |
| To | ``` case wednesday ``` |

Modified [NSNotification.Name.EKEventStoreChanged](https://developer.apple.com/documentation/foundation/nsnotification/name/1507525-ekeventstorechanged)

|  | Name | Declaration |
| --- | --- | --- |
| From | EKEventStoreChangedNotification | ``` let EKEventStoreChangedNotification: String ``` |
| To | EKEventStoreChanged | ``` static let EKEventStoreChanged: NSNotification.Name ``` |

Modified [EKEventSearchCallback](https://developer.apple.com/documentation/eventkit/ekeventsearchcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias EKEventSearchCallback = (EKEvent, UnsafeMutablePointer<ObjCBool>) -> Void ``` |
| To | ``` typealias EKEventSearchCallback = (EKEvent, UnsafeMutablePointer<ObjCBool>) -> Swift.Void ``` |

Modified [EKEventStoreRequestAccessCompletionHandler](https://developer.apple.com/documentation/eventkit/ekeventstorerequestaccesscompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias EKEventStoreRequestAccessCompletionHandler = (Bool, NSError?) -> Void ``` |
| To | ``` typealias EKEventStoreRequestAccessCompletionHandler = (Bool, Error?) -> Swift.Void ``` |

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
