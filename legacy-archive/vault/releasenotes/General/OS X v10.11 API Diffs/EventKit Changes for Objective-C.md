---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/EventKit.html
archived_at: '2026-07-18T02:53:02.008288Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# EventKit Changes for Objective-C

### EventKit

#### EKAlarm.h

Modified [EKAlarm.absoluteDate](https://developer.apple.com/documentation/eventkit/ekalarm/1507486-absolutedate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSDate *absoluteDate ``` |
| To | ``` @property(nonatomic, copy, nullable) NSDate *absoluteDate ``` |

Modified [+[EKAlarm alarmWithAbsoluteDate:]](https://developer.apple.com/documentation/eventkit/ekalarm/1507130-init)

|  | Declaration |
| --- | --- |
| From | ``` + (EKAlarm *)alarmWithAbsoluteDate:(NSDate *)date ``` |
| To | ``` + (EKAlarm * _Nonnull)alarmWithAbsoluteDate:(NSDate * _Nonnull)date ``` |

Modified [+[EKAlarm alarmWithRelativeOffset:]](https://developer.apple.com/documentation/eventkit/ekalarm/1507338-alarmwithrelativeoffset)

|  | Declaration |
| --- | --- |
| From | ``` + (EKAlarm *)alarmWithRelativeOffset:(NSTimeInterval)offset ``` |
| To | ``` + (EKAlarm * _Nonnull)alarmWithRelativeOffset:(NSTimeInterval)offset ``` |

Modified [EKAlarm.emailAddress](https://developer.apple.com/documentation/eventkit/ekalarm/1507267-emailaddress)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *emailAddress ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *emailAddress ``` |

Modified [EKAlarm.soundName](https://developer.apple.com/documentation/eventkit/ekalarm/1507227-soundname)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *soundName ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *soundName ``` |

Modified [EKAlarm.structuredLocation](https://developer.apple.com/documentation/eventkit/ekalarm/1507331-structuredlocation)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) EKStructuredLocation *structuredLocation ``` |
| To | ``` @property(nonatomic, copy, nullable) EKStructuredLocation *structuredLocation ``` |

Modified [EKAlarm.url](https://developer.apple.com/documentation/eventkit/ekalarm/1589757-url)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSURL *url ``` |
| To | ``` @property(nonatomic, copy, nullable) NSURL *url ``` |

#### EKCalendar.h

Modified [+[EKCalendar calendarForEntityType:eventStore:]](https://developer.apple.com/documentation/eventkit/ekcalendar/1507516-init)

|  | Declaration |
| --- | --- |
| From | ``` + (EKCalendar *)calendarForEntityType:(EKEntityType)entityType eventStore:(EKEventStore *)eventStore ``` |
| To | ``` + (EKCalendar * _Nonnull)calendarForEntityType:(EKEntityType)entityType eventStore:(EKEventStore * _Nonnull)eventStore ``` |

Modified [EKCalendar.calendarIdentifier](https://developer.apple.com/documentation/eventkit/ekcalendar/1507380-calendaridentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *calendarIdentifier ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSString *calendarIdentifier ``` |

Modified [EKCalendar.color](https://developer.apple.com/documentation/eventkit/ekcalendar/1507513-color)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSColor *color ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSColor *color ``` |

Modified [EKCalendar.source](https://developer.apple.com/documentation/eventkit/ekcalendar/1507288-source)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, strong) EKSource *source ``` |
| To | ``` @property(nonatomic, strong, nonnull) EKSource *source ``` |

Modified [EKCalendar.title](https://developer.apple.com/documentation/eventkit/ekcalendar/1507487-title)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *title ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSString *title ``` |

#### EKCalendarItem.h

Modified [-[EKCalendarItem addAlarm:]](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507397-addalarm)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addAlarm:(EKAlarm *)alarm ``` |
| To | ``` - (void)addAlarm:(EKAlarm * _Nonnull)alarm ``` |

Modified [-[EKCalendarItem addRecurrenceRule:]](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507256-addrecurrencerule)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addRecurrenceRule:(EKRecurrenceRule *)rule ``` |
| To | ``` - (void)addRecurrenceRule:(EKRecurrenceRule * _Nonnull)rule ``` |

Modified [EKCalendarItem.alarms](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507211-alarms)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *alarms ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<EKAlarm *> *alarms ``` |

Modified [EKCalendarItem.attendees](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507140-attendees)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy, readonly) NSArray *attendees ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSArray<__kindof EKParticipant *> *attendees ``` |

Modified [EKCalendarItem.calendar](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507169-calendar)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, strong) EKCalendar *calendar ``` |
| To | ``` @property(nonatomic, strong, nonnull) EKCalendar *calendar ``` |

Modified [EKCalendarItem.calendarItemExternalIdentifier](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507283-calendaritemexternalidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *calendarItemExternalIdentifier ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSString *calendarItemExternalIdentifier ``` |

Modified [EKCalendarItem.calendarItemIdentifier](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507075-calendaritemidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *calendarItemIdentifier ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSString *calendarItemIdentifier ``` |

Modified [EKCalendarItem.creationDate](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507213-creationdate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSDate *creationDate ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSDate *creationDate ``` |

Modified [EKCalendarItem.lastModifiedDate](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507374-lastmodifieddate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSDate *lastModifiedDate ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSDate *lastModifiedDate ``` |

Modified [EKCalendarItem.location](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507269-location)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *location ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *location ``` |

Modified [EKCalendarItem.notes](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507507-notes)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *notes ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *notes ``` |

Modified [EKCalendarItem.recurrenceRules](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507135-recurrencerules)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *recurrenceRules ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<EKRecurrenceRule *> *recurrenceRules ``` |

Modified [-[EKCalendarItem removeAlarm:]](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507133-removealarm)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeAlarm:(EKAlarm *)alarm ``` |
| To | ``` - (void)removeAlarm:(EKAlarm * _Nonnull)alarm ``` |

Modified [-[EKCalendarItem removeRecurrenceRule:]](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507495-removerecurrencerule)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeRecurrenceRule:(EKRecurrenceRule *)rule ``` |
| To | ``` - (void)removeRecurrenceRule:(EKRecurrenceRule * _Nonnull)rule ``` |

Modified [EKCalendarItem.timeZone](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507104-timezone)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSTimeZone *timeZone ``` |
| To | ``` @property(nonatomic, copy, nullable) NSTimeZone *timeZone ``` |

Modified [EKCalendarItem.title](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507305-title)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *title ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSString *title ``` |

Modified [EKCalendarItem.URL](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507265-url)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSURL *URL ``` |
| To | ``` @property(nonatomic, copy, nullable) NSURL *URL ``` |

#### EKError.h

Added [EKErrorOSNotSupported](https://developer.apple.com/documentation/eventkit/ekerror/code/osnotsupported)

#### EKEvent.h

Added [EKEvent.birthdayContactIdentifier](https://developer.apple.com/documentation/eventkit/ekevent/1507349-birthdaycontactidentifier)Added [EKEvent.structuredLocation](https://developer.apple.com/documentation/eventkit/ekevent/1507185-structuredlocation)Modified [EKEvent.birthdayPersonUniqueID](https://developer.apple.com/documentation/eventkit/ekevent/1507361-birthdaypersonuniqueid)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *birthdayPersonUniqueID ``` | -- |
| To | ``` @property(nonatomic, readonly, nullable) NSString *birthdayPersonUniqueID ``` | OS X 10.11 |

Modified [-[EKEvent compareStartDateWithEvent:]](https://developer.apple.com/documentation/eventkit/ekevent/1507335-comparestartdate)

|  | Declaration |
| --- | --- |
| From | ``` - (NSComparisonResult)compareStartDateWithEvent:(EKEvent *)other ``` |
| To | ``` - (NSComparisonResult)compareStartDateWithEvent:(EKEvent * _Nonnull)other ``` |

Modified [EKEvent.endDate](https://developer.apple.com/documentation/eventkit/ekevent/1507121-enddate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSDate *endDate ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSDate *endDate ``` |

Modified [EKEvent.eventIdentifier](https://developer.apple.com/documentation/eventkit/ekevent/1507437-eventidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *eventIdentifier ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSString *eventIdentifier ``` |

Modified [+[EKEvent eventWithEventStore:]](https://developer.apple.com/documentation/eventkit/ekevent/1507483-init)

|  | Declaration |
| --- | --- |
| From | ``` + (EKEvent *)eventWithEventStore:(EKEventStore *)eventStore ``` |
| To | ``` + (EKEvent * _Nonnull)eventWithEventStore:(EKEventStore * _Nonnull)eventStore ``` |

Modified [EKEvent.occurrenceDate](https://developer.apple.com/documentation/eventkit/ekevent/1507244-occurrencedate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSDate *occurrenceDate ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSDate *occurrenceDate ``` |

Modified [EKEvent.organizer](https://developer.apple.com/documentation/eventkit/ekevent/1507357-organizer)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) EKParticipant *organizer ``` |
| To | ``` @property(nonatomic, readonly, nullable) EKParticipant *organizer ``` |

Modified [EKEvent.startDate](https://developer.apple.com/documentation/eventkit/ekevent/1507372-startdate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSDate *startDate ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSDate *startDate ``` |

#### EKEventStore.h

Added [EKEventStore.delegateSources](https://developer.apple.com/documentation/eventkit/ekeventstore/1507419-delegatesources)Added [-[EKEventStore initWithSources:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507179-initwithsources)Modified [-[EKEventStore calendarItemsWithExternalIdentifier:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507281-calendaritems)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)calendarItemsWithExternalIdentifier:(NSString *)externalIdentifier ``` |
| To | ``` - (NSArray<EKCalendarItem *> * _Nonnull)calendarItemsWithExternalIdentifier:(NSString * _Nonnull)externalIdentifier ``` |

Modified [-[EKEventStore calendarItemWithIdentifier:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507433-calendaritem)

|  | Declaration |
| --- | --- |
| From | ``` - (EKCalendarItem *)calendarItemWithIdentifier:(NSString *)identifier ``` |
| To | ``` - (EKCalendarItem * _Nonnull)calendarItemWithIdentifier:(NSString * _Nonnull)identifier ``` |

Modified [-[EKEventStore calendarsForEntityType:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507128-calendars)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)calendarsForEntityType:(EKEntityType)entityType ``` |
| To | ``` - (NSArray<EKCalendar *> * _Nonnull)calendarsForEntityType:(EKEntityType)entityType ``` |

Modified [-[EKEventStore calendarWithIdentifier:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507484-calendarwithidentifier)

|  | Declaration |
| --- | --- |
| From | ``` - (EKCalendar *)calendarWithIdentifier:(NSString *)identifier ``` |
| To | ``` - (EKCalendar * _Nullable)calendarWithIdentifier:(NSString * _Nonnull)identifier ``` |

Modified [-[EKEventStore cancelFetchRequest:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507342-cancelfetchrequest)

|  | Declaration |
| --- | --- |
| From | ``` - (void)cancelFetchRequest:(id)fetchIdentifier ``` |
| To | ``` - (void)cancelFetchRequest:(id _Nonnull)fetchIdentifier ``` |

Modified [-[EKEventStore commit:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507424-commit)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)commit:(NSError **)error ``` |
| To | ``` - (BOOL)commit:(NSError * _Nullable * _Nullable)error ``` |

Modified [EKEventStore.defaultCalendarForNewEvents](https://developer.apple.com/documentation/eventkit/ekeventstore/1507062-defaultcalendarfornewevents)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) EKCalendar *defaultCalendarForNewEvents ``` |
| To | ``` @property(nonatomic, readonly, nonnull) EKCalendar *defaultCalendarForNewEvents ``` |

Modified [-[EKEventStore defaultCalendarForNewReminders]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507543-defaultcalendarfornewreminders)

|  | Declaration |
| --- | --- |
| From | ``` - (EKCalendar *)defaultCalendarForNewReminders ``` |
| To | ``` - (EKCalendar * _Nonnull)defaultCalendarForNewReminders ``` |

Modified [-[EKEventStore enumerateEventsMatchingPredicate:usingBlock:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507518-enumerateeventsmatchingpredicate)

|  | Declaration |
| --- | --- |
| From | ``` - (void)enumerateEventsMatchingPredicate:(NSPredicate *)predicate usingBlock:(EKEventSearchCallback)block ``` |
| To | ``` - (void)enumerateEventsMatchingPredicate:(NSPredicate * _Nonnull)predicate usingBlock:(EKEventSearchCallback _Nonnull)block ``` |

Modified [-[EKEventStore eventsMatchingPredicate:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507183-events)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)eventsMatchingPredicate:(NSPredicate *)predicate ``` |
| To | ``` - (NSArray<EKEvent *> * _Nonnull)eventsMatchingPredicate:(NSPredicate * _Nonnull)predicate ``` |

Modified [EKEventStore.eventStoreIdentifier](https://developer.apple.com/documentation/eventkit/ekeventstore/1507442-eventstoreidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *eventStoreIdentifier ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSString *eventStoreIdentifier ``` |

Modified [-[EKEventStore eventWithIdentifier:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507490-eventwithidentifier)

|  | Declaration |
| --- | --- |
| From | ``` - (EKEvent *)eventWithIdentifier:(NSString *)identifier ``` |
| To | ``` - (EKEvent * _Nullable)eventWithIdentifier:(NSString * _Nonnull)identifier ``` |

Modified [-[EKEventStore fetchRemindersMatchingPredicate:completion:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507500-fetchremindersmatchingpredicate)

|  | Declaration |
| --- | --- |
| From | ``` - (id)fetchRemindersMatchingPredicate:(NSPredicate *)predicate completion:(void (^)(NSArray *reminders))completion ``` |
| To | ``` - (id _Nonnull)fetchRemindersMatchingPredicate:(NSPredicate * _Nonnull)predicate completion:(void (^ _Nonnull)(NSArray<EKReminder *> * _Nullable reminders))completion ``` |

Modified [-[EKEventStore init]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507252-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)init ``` |
| To | ``` - (id _Nonnull)init ``` |

Modified [-[EKEventStore initWithAccessToEntityTypes:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1536382-initwithaccesstoentitytypes)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithAccessToEntityTypes:(EKEntityMask)entityTypes ``` |
| To | ``` - (id _Nonnull)initWithAccessToEntityTypes:(EKEntityMask)entityTypes ``` |

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

Modified [-[EKEventStore removeCalendar:commit:error:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507523-removecalendar)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)removeCalendar:(EKCalendar *)calendar commit:(BOOL)commit error:(NSError **)error ``` |
| To | ``` - (BOOL)removeCalendar:(EKCalendar * _Nonnull)calendar commit:(BOOL)commit error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[EKEventStore removeEvent:span:commit:error:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507469-removeevent)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)removeEvent:(EKEvent *)event span:(EKSpan)span commit:(BOOL)commit error:(NSError **)error ``` |
| To | ``` - (BOOL)removeEvent:(EKEvent * _Nonnull)event span:(EKSpan)span commit:(BOOL)commit error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[EKEventStore removeReminder:commit:error:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507108-remove)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)removeReminder:(EKReminder *)reminder commit:(BOOL)commit error:(NSError **)error ``` |
| To | ``` - (BOOL)removeReminder:(EKReminder * _Nonnull)reminder commit:(BOOL)commit error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[EKEventStore requestAccessToEntityType:completion:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507547-requestaccess)

|  | Declaration |
| --- | --- |
| From | ``` - (void)requestAccessToEntityType:(EKEntityType)entityType completion:(EKEventStoreRequestAccessCompletionHandler)completion ``` |
| To | ``` - (void)requestAccessToEntityType:(EKEntityType)entityType completion:(EKEventStoreRequestAccessCompletionHandler _Nonnull)completion ``` |

Modified [-[EKEventStore saveCalendar:commit:error:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507080-savecalendar)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)saveCalendar:(EKCalendar *)calendar commit:(BOOL)commit error:(NSError **)error ``` |
| To | ``` - (BOOL)saveCalendar:(EKCalendar * _Nonnull)calendar commit:(BOOL)commit error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[EKEventStore saveEvent:span:commit:error:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507295-save)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)saveEvent:(EKEvent *)event span:(EKSpan)span commit:(BOOL)commit error:(NSError **)error ``` |
| To | ``` - (BOOL)saveEvent:(EKEvent * _Nonnull)event span:(EKSpan)span commit:(BOOL)commit error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[EKEventStore saveReminder:commit:error:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507181-savereminder)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)saveReminder:(EKReminder *)reminder commit:(BOOL)commit error:(NSError **)error ``` |
| To | ``` - (BOOL)saveReminder:(EKReminder * _Nonnull)reminder commit:(BOOL)commit error:(NSError * _Nullable * _Nullable)error ``` |

Modified [EKEventStore.sources](https://developer.apple.com/documentation/eventkit/ekeventstore/1507315-sources)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)sources ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<EKSource *> *sources ``` |

Modified [-[EKEventStore sourceWithIdentifier:]](https://developer.apple.com/documentation/eventkit/ekeventstore/1507521-source)

|  | Declaration |
| --- | --- |
| From | ``` - (EKSource *)sourceWithIdentifier:(NSString *)identifier ``` |
| To | ``` - (EKSource * _Nonnull)sourceWithIdentifier:(NSString * _Nonnull)identifier ``` |

Modified [EKAuthorizationStatus](https://developer.apple.com/documentation/eventkit/ekauthorizationstatus)

|  | Header |
| --- | --- |
| From | EventKit/EKEventStore.h |
| To | EventKit/EKTypes.h |

Modified [EKAuthorizationStatusAuthorized](https://developer.apple.com/documentation/eventkit/ekauthorizationstatus/ekauthorizationstatusauthorized)

|  | Header |
| --- | --- |
| From | EventKit/EKEventStore.h |
| To | EventKit/EKTypes.h |

Modified [EKAuthorizationStatusDenied](https://developer.apple.com/documentation/eventkit/ekauthorizationstatus/denied)

|  | Header |
| --- | --- |
| From | EventKit/EKEventStore.h |
| To | EventKit/EKTypes.h |

Modified [EKAuthorizationStatusNotDetermined](https://developer.apple.com/documentation/eventkit/ekauthorizationstatus/ekauthorizationstatusnotdetermined)

|  | Header |
| --- | --- |
| From | EventKit/EKEventStore.h |
| To | EventKit/EKTypes.h |

Modified [EKAuthorizationStatusRestricted](https://developer.apple.com/documentation/eventkit/ekauthorizationstatus/restricted)

|  | Header |
| --- | --- |
| From | EventKit/EKEventStore.h |
| To | EventKit/EKTypes.h |

#### EKObject.h

Removed [-[EKObject isNew]](https://developer.apple.com/documentation/eventkit/ekobject/1812546-isnew)Added [EKObject.new](https://developer.apple.com/documentation/eventkit/ekobject/1507402-isnew)Modified [EKObject.hasChanges](https://developer.apple.com/documentation/eventkit/ekobject/1507333-haschanges)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)hasChanges ``` |
| To | ``` @property(nonatomic, readonly) BOOL hasChanges ``` |

#### EKParticipant.h

Removed EKParticipant.isCurrentUserAdded [EKParticipant.contactPredicate](https://developer.apple.com/documentation/eventkit/ekparticipant/1507163-contactpredicate)Added [EKParticipant.currentUser](https://developer.apple.com/documentation/eventkit/ekparticipant/1507248-currentuser)Modified [-[EKParticipant ABPersonInAddressBook:]](https://developer.apple.com/documentation/eventkit/ekparticipant/1507504-abpersoninaddressbook)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` - (ABPerson *)ABPersonInAddressBook:(ABAddressBook *)addressBook ``` | -- |
| To | ``` - (ABPerson * _Nullable)ABPersonInAddressBook:(ABAddressBook * _Nonnull)addressBook ``` | OS X 10.11 |

Modified [EKParticipant.name](https://developer.apple.com/documentation/eventkit/ekparticipant/1507480-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *name ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSString *name ``` |

Modified [EKParticipant.URL](https://developer.apple.com/documentation/eventkit/ekparticipant/1507435-url)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSURL *URL ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSURL *URL ``` |

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

Modified [EKRecurrenceEnd.endDate](https://developer.apple.com/documentation/eventkit/ekrecurrenceend/1415648-enddate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSDate *endDate ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSDate *endDate ``` |

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

Modified [EKRecurrenceRule.calendarIdentifier](https://developer.apple.com/documentation/eventkit/ekrecurrencerule/1507340-calendaridentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *calendarIdentifier ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSString *calendarIdentifier ``` |

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

Modified [EKRecurrenceRule.recurrenceEnd](https://developer.apple.com/documentation/eventkit/ekrecurrencerule/1507254-recurrenceend)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) EKRecurrenceEnd *recurrenceEnd ``` |
| To | ``` @property(nonatomic, copy, nullable) EKRecurrenceEnd *recurrenceEnd ``` |

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

Modified [EKReminder.completionDate](https://developer.apple.com/documentation/eventkit/ekreminder/1507286-completiondate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSDate *completionDate ``` |
| To | ``` @property(nonatomic, copy, nullable) NSDate *completionDate ``` |

Modified [EKReminder.dueDateComponents](https://developer.apple.com/documentation/eventkit/ekreminder/1507383-duedatecomponents)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSDateComponents *dueDateComponents ``` |
| To | ``` @property(nonatomic, copy, nullable) NSDateComponents *dueDateComponents ``` |

Modified [+[EKReminder reminderWithEventStore:]](https://developer.apple.com/documentation/eventkit/ekreminder/1507429-init)

|  | Declaration |
| --- | --- |
| From | ``` + (EKReminder *)reminderWithEventStore:(EKEventStore *)eventStore ``` |
| To | ``` + (EKReminder * _Nonnull)reminderWithEventStore:(EKEventStore * _Nonnull)eventStore ``` |

Modified [EKReminder.startDateComponents](https://developer.apple.com/documentation/eventkit/ekreminder/1507558-startdatecomponents)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSDateComponents *startDateComponents ``` |
| To | ``` @property(nonatomic, copy, nullable) NSDateComponents *startDateComponents ``` |

#### EKSource.h

Modified [-[EKSource calendarsForEntityType:]](https://developer.apple.com/documentation/eventkit/eksource/1507387-calendarsforentitytype)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSet *)calendarsForEntityType:(EKEntityType)entityType ``` |
| To | ``` - (NSSet<EKCalendar *> * _Nonnull)calendarsForEntityType:(EKEntityType)entityType ``` |

Modified [EKSource.sourceIdentifier](https://developer.apple.com/documentation/eventkit/eksource/1507275-sourceidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *sourceIdentifier ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSString *sourceIdentifier ``` |

Modified [EKSource.title](https://developer.apple.com/documentation/eventkit/eksource/1507385-title)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *title ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSString *title ``` |

#### EKStructuredLocation.h

Added [+[EKStructuredLocation locationWithMapItem:]](https://developer.apple.com/documentation/eventkit/ekstructuredlocation/1507493-init)Modified [EKStructuredLocation.geoLocation](https://developer.apple.com/documentation/eventkit/ekstructuredlocation/1507110-geolocation)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, strong) CLLocation *geoLocation ``` |
| To | ``` @property(nonatomic, strong, nullable) CLLocation *geoLocation ``` |

Modified [+[EKStructuredLocation locationWithTitle:]](https://developer.apple.com/documentation/eventkit/ekstructuredlocation/1507366-init)

|  | Declaration |
| --- | --- |
| From | ``` + (EKStructuredLocation *)locationWithTitle:(NSString *)title ``` |
| To | ``` + (instancetype _Nonnull)locationWithTitle:(NSString * _Nonnull)title ``` |

Modified [EKStructuredLocation.title](https://developer.apple.com/documentation/eventkit/ekstructuredlocation/1507137-title)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, strong) NSString *title ``` |
| To | ``` @property(nonatomic, strong, nonnull) NSString *title ``` |

#### EKTypes.h

Added [EKParticipantScheduleStatus](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus)Added [EKParticipantScheduleStatusCannotDeliver](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/ekparticipantschedulestatuscannotdeliver)Added [EKParticipantScheduleStatusDelivered](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/ekparticipantschedulestatusdelivered)Added [EKParticipantScheduleStatusDeliveryFailed](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/ekparticipantschedulestatusdeliveryfailed)Added [EKParticipantScheduleStatusNone](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/none)Added [EKParticipantScheduleStatusNoPrivileges](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/ekparticipantschedulestatusnoprivileges)Added [EKParticipantScheduleStatusPending](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/ekparticipantschedulestatuspending)Added [EKParticipantScheduleStatusRecipientNotAllowed](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/recipientnotallowed)Added [EKParticipantScheduleStatusRecipientNotRecognized](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/ekparticipantschedulestatusrecipientnotrecognized)Added [EKParticipantScheduleStatusSent](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/sent)Added [EKWeekday](https://developer.apple.com/documentation/eventkit/ekweekday)Added [EKWeekdayFriday](https://developer.apple.com/documentation/eventkit/ekweekday/ekweekdayfriday)Added [EKWeekdayMonday](https://developer.apple.com/documentation/eventkit/ekweekday/ekweekdaymonday)Added [EKWeekdaySaturday](https://developer.apple.com/documentation/eventkit/ekweekday/saturday)Added [EKWeekdaySunday](https://developer.apple.com/documentation/eventkit/ekweekday/ekweekdaysunday)Added [EKWeekdayThursday](https://developer.apple.com/documentation/eventkit/ekweekday/thursday)Added [EKWeekdayTuesday](https://developer.apple.com/documentation/eventkit/ekweekday/ekweekdaytuesday)Added [EKWeekdayWednesday](https://developer.apple.com/documentation/eventkit/ekweekday/ekweekdaywednesday)Modified [EKAuthorizationStatus](https://developer.apple.com/documentation/eventkit/ekauthorizationstatus)

|  | Header |
| --- | --- |
| From | EventKit/EKEventStore.h |
| To | EventKit/EKTypes.h |

Modified [EKAuthorizationStatusAuthorized](https://developer.apple.com/documentation/eventkit/ekauthorizationstatus/ekauthorizationstatusauthorized)

|  | Header |
| --- | --- |
| From | EventKit/EKEventStore.h |
| To | EventKit/EKTypes.h |

Modified [EKAuthorizationStatusDenied](https://developer.apple.com/documentation/eventkit/ekauthorizationstatus/denied)

|  | Header |
| --- | --- |
| From | EventKit/EKEventStore.h |
| To | EventKit/EKTypes.h |

Modified [EKAuthorizationStatusNotDetermined](https://developer.apple.com/documentation/eventkit/ekauthorizationstatus/ekauthorizationstatusnotdetermined)

|  | Header |
| --- | --- |
| From | EventKit/EKEventStore.h |
| To | EventKit/EKTypes.h |

Modified [EKAuthorizationStatusRestricted](https://developer.apple.com/documentation/eventkit/ekauthorizationstatus/restricted)

|  | Header |
| --- | --- |
| From | EventKit/EKEventStore.h |
| To | EventKit/EKTypes.h |

Modified [EKFriday](https://developer.apple.com/documentation/eventkit/ekweekday/1451835-ekfriday)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [EKMonday](https://developer.apple.com/documentation/eventkit/ekweekday/ekmonday)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [EKSaturday](https://developer.apple.com/documentation/eventkit/ekweekday/eksaturday)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [EKSunday](https://developer.apple.com/documentation/eventkit/ekweekday/eksunday)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [EKThursday](https://developer.apple.com/documentation/eventkit/ekweekday/1451894-ekthursday)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [EKTuesday](https://developer.apple.com/documentation/eventkit/ekweekday/1451993-ektuesday)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [EKWednesday](https://developer.apple.com/documentation/eventkit/ekweekday/1451817-ekwednesday)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

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
