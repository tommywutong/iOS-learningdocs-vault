---
title: Calendar and Reminders Programming Guide
apple_id: TP40009765
resource_type: Guide
platform: watchOS|iOS|macOS
topic: Data Management
technology: EventKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/EventKitProgGuide/ReadingAndWritingEvents.html
archived_at: '2026-07-27T06:57:07.496811Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Calendar and Reminders Programming Guide](Introduction%20to%20Calendars%20and%20Reminders.md)


[Next](Reading%20and%20Writing%20Reminders.md)[Previous](Introduction%20to%20Calendars%20and%20Reminders.md)

# Reading and Writing Calendar Events

You can fetch, create, edit, and delete events from a user’s Calendar database using the [EKEventStore](https://developer.apple.com/documentation/eventkit/ekeventstore) class. You can fetch a custom set of events that match a predicate you provide, or you can fetch an individual event by its unique identifier. After you fetch an event, you can access its associated calendar information with the properties of the [EKEvent](https://developer.apple.com/documentation/eventkit/ekevent) class. Likewise, you can modify its calendar information by setting the properties of the `EKEvent` class.

__Important:__ If your iOS app links on or after iOS 10.0 and you need to access Calendar data, be sure to include the [NSCalendarsUsageDescription](../../General/Information%20Property%20List%20Key%20Reference/Cocoa%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomjv) key in your `Info.plist` file.

## Connecting to the Event Store

You initialize an [EKEventStore](https://developer.apple.com/documentation/eventkit/ekeventstore) object with the designated initializer:

```
EKEventStore *store = [[EKEventStore alloc] initWithAccessToEntityTypes:EKEntityMaskEvent];
```

An `EKEventStore` object requires a relatively large amount of time to initialize and release. Consequently, you should not initialize and release a separate event store for each event-related task. Instead, initialize a single event store when your app loads, and use it repeatedly to ensure that your connection is long-lived.

An event store instance must not be released before other EventKit objects; otherwise, undefined behavior may occur.

## Retrieving Events

There are two ways to retrieve events. Fetching via predicates, or search query, will return zero or more events that match a given query. Fetching via unique identifiers will return a single event that corresponds to the given identifier.

__Note:__ Retrieving events from the Calendar database does not necessarily return events in chronological order. To sort an array of `EKEvent` objects by date, call [sortedArrayUsingSelector:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/sortedArrayUsingSelector:) on the array, providing the selector for the [compareStartDateWithEvent:](https://developer.apple.com/documentation/eventkit/ekevent/1507335-comparestartdate) method.

### Using Predicates

It’s common to fetch events that fall within a date range. The `EKEventStore` method [eventsMatchingPredicate:](https://developer.apple.com/documentation/eventkit/ekeventstore/1507183-events) fetches all events that fall within the date range specified in the predicate you provide. Listing 1-1 demonstrates how to fetch all events that occur between one day before and one year after the current date.

__Note:__ Although the [eventsMatchingPredicate:](https://developer.apple.com/documentation/eventkit/ekeventstore/1507183-events) method accepts a parameter of type `NSPredicate`, you must supply a predicate created with the `EKEventStore` method [predicateForEventsWithStartDate:endDate:calendars:](https://developer.apple.com/documentation/eventkit/ekeventstore/1507479-predicateforevents).

__Listing 1-1__  Fetching events with a predicate

```
// Get the appropriate calendar
NSCalendar *calendar = [NSCalendar currentCalendar];

// Create the start date components
NSDateComponents *oneDayAgoComponents = [[NSDateComponents alloc] init];
oneDayAgoComponents.day = -1;
NSDate *oneDayAgo = [calendar dateByAddingComponents:oneDayAgoComponents
                                              toDate:[NSDate date]
                                             options:0];

// Create the end date components
NSDateComponents *oneYearFromNowComponents = [[NSDateComponents alloc] init];
oneYearFromNowComponents.year = 1;
NSDate *oneYearFromNow = [calendar dateByAddingComponents:oneYearFromNowComponents
                                                   toDate:[NSDate date]
                                                  options:0];

// Create the predicate from the event store's instance method
NSPredicate *predicate = [store predicateForEventsWithStartDate:oneDayAgo
                                                        endDate:oneYearFromNow
                                                      calendars:nil];

// Fetch all events that match the predicate
NSArray *events = [store eventsMatchingPredicate:predicate];
```

You can specify a subset of calendars to search by passing an array of [EKCalendar](https://developer.apple.com/documentation/eventkit/ekcalendar) objects as the _calendars_ parameter of the [predicateForEventsWithStartDate:endDate:calendars:](https://developer.apple.com/documentation/eventkit/ekeventstore/1507479-predicateforevents) method. You can get the user’s calendars from the event store’s [calendarsForEntityType:](https://developer.apple.com/documentation/eventkit/ekeventstore/1507128-calendars) method. Passing `nil` tells the method to fetch from all of the user’s calendars.

Because the [eventsMatchingPredicate:](https://developer.apple.com/documentation/eventkit/ekeventstore/1507183-events) method is synchronous, you may not want to run it on your app’s main thread. For asynchronous behavior, run the method on another thread with the `dispatch_async` function or with an [NSOperation](https://developer.apple.com/documentation/foundation/nsoperation) object.

### Using Unique Identifiers

If you know the event’s unique identifier because you fetched it previously with a predicate, you can use the `EKEventStore` method [eventWithIdentifier:](https://developer.apple.com/documentation/eventkit/ekeventstore/1507490-eventwithidentifier) to fetch the event. If it is a recurring event, this method will return the first occurrence of the event. You can get an event’s unique identifier with the [eventIdentifier](https://developer.apple.com/documentation/eventkit/ekevent/1507437-eventidentifier) property.

## Creating and Editing Events

__Note:__ If you’re developing on iOS, you have the option of letting users modify event data with the event view controllers provided in the EventKit UI framework. For information on how to use these event view controllers, see [Providing Interfaces for Events](Providing%20Interfaces%20for%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tonrvfvbuqmrnknlti).

Create a new event with the [eventWithEventStore:](https://developer.apple.com/documentation/eventkit/ekevent/1507483-init) method of the [EKEvent](https://developer.apple.com/documentation/eventkit/ekevent) class.

You can edit the details of a new event or an event you previously fetched from the Calendar database by setting the event’s corresponding properties. Some of the details you can edit include:

- The event’s title with the [title](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507305-title) property
- The event’s start and end dates with the [startDate](https://developer.apple.com/documentation/eventkit/ekevent/1507372-startdate) and [endDate](https://developer.apple.com/documentation/eventkit/ekevent/1507121-enddate) properties
- The calendar with which the event is associated with the [calendar](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507169-calendar) property
- The alarms associated with the event with the [alarms](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507211-alarms) property (see [Configuring Alarms](Configuring%20Alarms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tonrvfvbuqnrnknltc) for more details)
- The event’s recurrence rule, if it is a repeating event, with the [recurrenceRules](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507135-recurrencerules) property (see [Creating Recurring Events](Creating%20Recurring%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tonrvfvbuqmznknltc) for more details)

## Saving and Removing Events

__Important:__ If your app modifies a user’s Calendar database, _it must get confirmation from the user before doing so_. An app should never modify the Calendar database without specific instruction from the user.

Changes you make to an event are not permanent until you save them. Save your changes to the Calendar database with the `EKEventStore` method [saveEvent:span:commit:error:](https://developer.apple.com/documentation/eventkit/ekeventstore/1507295-saveevent). If you want to remove an event from the Calendar database, use the `EKEventStore` method [removeEvent:span:commit:error:](https://developer.apple.com/documentation/eventkit/ekeventstore/1507469-remove). Whether you are saving or removing an event, implementing the respective method automatically syncs your changes with the calendar the event belongs to (CalDAV, Exchange, and so on).

If you are saving a recurring event, your changes can apply to all future occurrences of the event by specifying [EKSpanFutureEvents](https://developer.apple.com/documentation/eventkit/ekspan/ekspanfutureevents) for the _span_ parameter of the `saveEvent:span:commit:error:` method. Likewise, you can remove all future occurrences of an event by specifying [EKSpanFutureEvents](https://developer.apple.com/documentation/eventkit/ekspan/ekspanfutureevents) for the _span_ parameter of the [removeEvent:span:commit:error:](https://developer.apple.com/documentation/eventkit/ekeventstore/1615882-removeevent) method.

__Note:__ If you pass `NO` to the _commit_ parameter, make sure that you later invoke the [commit:](https://developer.apple.com/documentation/eventkit/ekeventstore/1507424-commit) method to permanently save your changes.

## Performing Batch Operations on Events

You can perform an operation on all events that match a provided predicate with the `EKEventStore` method [enumerateEventsMatchingPredicate:usingBlock:](https://developer.apple.com/documentation/eventkit/ekeventstore/1507518-enumerateeventsmatchingpredicate). You must create the predicate for this method with the `EKEventStore` method [predicateForEventsWithStartDate:endDate:calendars:](https://developer.apple.com/documentation/eventkit/ekeventstore/1507479-predicateforevents). The operation you provide is a block of type `EKEventSearchCallback`.

```c
typedef void (^EKEventSearchCallback)(EKEvent *event, BOOL *stop);
```

The block is passed two parameters:

**_event_**
: The event that is currently being operated on.

**_stop_**
: A Boolean value determining whether [enumerateEventsMatchingPredicate:usingBlock:](https://developer.apple.com/documentation/eventkit/ekeventstore/1507518-enumerateeventsmatchingpredicate) should stop processing events when this block returns. If `YES`, any event that matches the predicate but has not yet been processed will remain unprocessed.

__Important:__ Keep in mind that using this method can result in significant changes to the user’s Calendar database. Make sure the user is fully informed of the actions you are about to perform when you request user confirmation.

Because the `enumerateEventsMatchingPredicate:usingBlock:` method is synchronous, you may not want to run it on your app’s main thread. For asynchronous behavior, run the method on another thread with the `dispatch_async` function or with an [NSOperation](https://developer.apple.com/documentation/foundation/nsoperation) object.

[Next](Reading%20and%20Writing%20Reminders.md)[Previous](Introduction%20to%20Calendars%20and%20Reminders.md)
