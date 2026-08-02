---
title: Calendar and Reminders Programming Guide
apple_id: TP40009765
resource_type: Guide
platform: watchOS|iOS|macOS
topic: Data Management
technology: EventKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/EventKitProgGuide/ReadingAndWritingReminders/ReadingAndWritingReminders.html
archived_at: '2026-07-27T06:57:07.506686Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Calendar and Reminders Programming Guide](Introduction%20to%20Calendars%20and%20Reminders.md)


[Next](Configuring%20Alarms.md)[Previous](Reading%20and%20Writing%20Calendar%20Events.md)

# Reading and Writing Reminders

Reminders are tasks that may be tied to a specific time or location. They are similar to calendar events, but can be marked complete and may not necessarily span an exact period of time.

Because [EKReminder](https://developer.apple.com/documentation/eventkit/ekreminder) inherits from [EKCalendarItem](https://developer.apple.com/documentation/eventkit/ekcalendaritem), you can perform the same methods on a reminder as you would on an event, such as adding an alarm with [addAlarm:](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507397-addalarm) or setting a recurrence rule with [addRecurrenceRule:](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507256-addrecurrencerule).

__Important:__ If your iOS app links on or after iOS 10.0 and you need to access Reminders data, be sure to include the [NSRemindersUsageDescription](../../General/Information%20Property%20List%20Key%20Reference/Cocoa%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomjw) key in your `Info.plist` file.

## Retrieving Reminders

As with events, you must first establish a connection to the event store to access existing reminders. See [Connecting to the Event Store](Reading%20and%20Writing%20Calendar%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2donzvfvjvomy) if you have not already done so.

To initialize a connection with access to reminders, pass `EKEntityMaskReminder` instead of `EKEntityMaskEvent`.

```
EKEventStore *store = [[EKEventStore alloc] initWithAccessToEntityTypes:EKEntityMaskReminder];
```

Just like searching for events, there are two ways to retrieve reminders.

### Using Predicates

You can call [fetchRemindersMatchingPredicate:completion:](https://developer.apple.com/documentation/eventkit/ekeventstore/1507500-fetchremindersmatchingpredicate) to access multiple reminders that match a predicate. Pass a predicate returned by one of the following methods:

- [predicateForIncompleteRemindersWithDueDateStarting:ending:calendars:](https://developer.apple.com/documentation/eventkit/ekeventstore/1507143-predicateforincompletereminders) finds incomplete reminders within an optional time period
- [predicateForCompletedRemindersWithCompletionDateStarting:ending:calendars:](https://developer.apple.com/documentation/eventkit/ekeventstore/1507447-predicateforcompletedreminderswi) finds completed reminders within an optional time period
- [predicateForRemindersInCalendars:](https://developer.apple.com/documentation/eventkit/ekeventstore/1507086-predicateforremindersincalendars) finds all reminders

You can iterate across matched reminders by passing a block to the _completion_ argument, as shown in Listing 2-1.

__Listing 2-1__  Fetching reminders with a predicate

```
NSPredicate *predicate = [store predicateForRemindersInCalendars:nil];

[store fetchRemindersMatchingPredicate:predicate completion:^(NSArray *reminders) {
    for (EKReminder *reminder in reminders) {
        // do something for each reminder
    }
}];
```

__Note:__ Unlike fetching events via predicate (see [Using Predicates](Reading%20and%20Writing%20Calendar%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2donzvfvjvony)), you can fetch reminders via predicate asynchronously without dispatching to another thread.

If you’d like to abort your fetch request by predicate, call `cancelFetchRequest:` while passing the identifier as returned by [fetchRemindersMatchingPredicate:completion:](https://developer.apple.com/documentation/eventkit/ekeventstore/1507500-fetchremindersmatchingpredicate).

### Using Unique Identifiers

If you know a specific reminder’s unique identifier from previously fetching it with a predicate, you can call the [calendarItemWithIdentifier:](https://developer.apple.com/documentation/eventkit/ekeventstore/1507433-calendaritemwithidentifier) instance method. `calendarItemWithIdentifier:` can fetch any calendar item (reminders and events), whereas [eventWithIdentifier:](https://developer.apple.com/documentation/eventkit/ekeventstore/1507490-eventwithidentifier) fetches only events.

## Creating and Editing Reminders

You can create reminders using the [reminderWithEventStore:](https://developer.apple.com/documentation/eventkit/ekreminder/1507429-init) class method. The [title](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507305-title) and [calendar](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507169-calendar) properties are required. The calendar for a reminder is the list with which it is grouped.

Like events, reminders can trigger time-based or location-based alarms to alert the user of a certain task. Read [Configuring Alarms](Configuring%20Alarms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tonrvfvbuqnrnknltc) for more information on how to attach alarms to calendar items.

To associate a start date or due date with a reminder, use the [startDateComponents](https://developer.apple.com/documentation/eventkit/ekreminder/1507558-startdatecomponents) and [dueDateComponents](https://developer.apple.com/documentation/eventkit/ekreminder/1507383-duedatecomponents) properties. To complete a reminder, set the [completed](https://developer.apple.com/documentation/eventkit/ekreminder/1507383-duedatecomponents) property to `YES`, which automatically sets [completionDate](https://developer.apple.com/documentation/eventkit/ekreminder/1507383-duedatecomponents) to the current date.

## Saving and Removing Reminders

__Important:__ If your app modifies a user’s Calendar database, _it must get confirmation from the user before doing so_. An app should never modify the Calendar database without specific instruction from the user.

Reminders are saved in a similar fashion to events. To save a reminder to the Calendar database, call the [saveReminder:commit:error:](https://developer.apple.com/documentation/eventkit/ekeventstore/1507181-savereminder) method. To remove an event, call the [removeReminder:commit:error:](https://developer.apple.com/documentation/eventkit/ekeventstore/1507108-remove) method.

Remember, the [title](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507305-title) and [calendar](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507169-calendar) properties must explicitly be set before you save your reminder.

__Note:__ Just like when saving or removing events, make sure that if you pass `NO` to the _commit_ parameter, you later invoke the [commit:](https://developer.apple.com/documentation/eventkit/ekeventstore/1507424-commit) method to save your changes.

[Next](Configuring%20Alarms.md)[Previous](Reading%20and%20Writing%20Calendar%20Events.md)
