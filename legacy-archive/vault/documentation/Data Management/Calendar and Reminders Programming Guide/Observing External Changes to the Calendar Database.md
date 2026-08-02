---
title: Calendar and Reminders Programming Guide
apple_id: TP40009765
resource_type: Guide
platform: watchOS|iOS|macOS
topic: Data Management
technology: EventKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/EventKitProgGuide/ObservingChanges/ObservingChanges.html
archived_at: '2026-07-27T06:57:07.527080Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Calendar and Reminders Programming Guide](Introduction%20to%20Calendars%20and%20Reminders.md)


[Next](Providing%20Interfaces%20for%20Events.md)[Previous](Creating%20Recurring%20Events.md)

# Observing External Changes to the Calendar Database

It’s possible for another process or app to modify the Calendar database while your app is running. If your app fetches calendar events or reminders, you should register to be notified about changes to the Calendar database. By doing so, you ensure that the calendar and reminder information you display to the user is current.

## Registering for Notifications

An [EKEventStore](https://developer.apple.com/documentation/eventkit/ekeventstore) object posts an [EKEventStoreChangedNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1507525-ekeventstorechanged) notification whenever it detects changes to the Calendar database. Register for this notification if your app handles event or reminder data.

The following code registers for the [EKEventStoreChangedNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1507525-ekeventstorechanged) notification, as shown in [Listing 5-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tonrvfvbuqnbnknltk).

__Listing 5-1__  The `EKEventStoreChangedNotification` notification

```
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(storeChanged:)
                                             name:EKEventStoreChangedNotification
                                           object:eventStore];
```

## Responding to Notifications

When you receive an [EKEventStoreChangedNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1507525-ekeventstorechanged) notification, it’s possible that objects you’ve fetched—such as an `EKEvent`, `EKReminder`, or `EKCalendar`, among others—have changed. The effect of these changes depends on whether an event was added, modified, or deleted.

- If an event was added, it does not affect any of your previously fetched events or reminders, but the added event may fall within the date range of events you are displaying to the user.
- If an event was modified or deleted, properties of `EKEvent` and `EKReminder` objects representing that event may become out of date.

Because your local data is often invalidated or incomplete when a change occurs in the Calendar database, you should refetch your current date range of events whenever you receive an [EKEventStoreChangedNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1507525-ekeventstorechanged) notification. If you are currently modifying an event and you do not want to refetch it unless it is absolutely necessary to do so, you can call the `refresh` method on the event. If the method returns `YES`, you can continue to use the event; otherwise, you need to refetch it.

__Note:__ Events being modified in an event view controller with EventKit UI for iOS are updated automatically when a change occurs in the Calendar database. For a more in-depth look at EventKit UI, read the next chapter, [Providing Interfaces for Events](Providing%20Interfaces%20for%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tonrvfvbuqmrnknlti).

[Next](Providing%20Interfaces%20for%20Events.md)[Previous](Creating%20Recurring%20Events.md)
