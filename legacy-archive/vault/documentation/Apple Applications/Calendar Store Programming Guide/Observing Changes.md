---
title: Calendar Store Programming Guide
apple_id: TP40004334
resource_type: Guide
platform: macOS
topic: Data Management
technology: CalendarStore
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/CalendarStoreProgGuide/Articles/ObservingChanges.html
archived_at: '2026-07-15T05:17:17.408190Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Calendar Store Programming Guide](Introduction%20to%20Calendar%20Store%20Programming%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Saving%20Changes.md)

# Observing Changes

If you fetch Calendar Store objects, you typically want to observe changes to the objects so your application data is in sync with the Calendar Store database. You especially need to do this if you maintain strong references to the calendar objects or display information about the objects to the user. For example, if an event’s start date changes in iCal, you might want to update the view of that event in your application too. Similarly, if the user makes changes to an event in your application, you might want to make the change to the Calendar Store database so that iCal updates its display. To do this, you need to observe changes made externally and internally. How you observe end-user changes is application dependent. This article demonstrates how to do this using Cocoa bindings.

`CalCalendarStore` defines several notifications that are posted when another process changes fetched objects. A separate notification is posted for each type of object (calendars, events, and tasks) and contains information about changes to multiple objects—it does not post a notification for each individual change. Similar to Core Data change notifications, the notification user dictionary contains information about what objects were inserted, updated, or deleted. The handlers for these notifications should update the local object to reflect the changes.

If you are displaying information about calendars, then observe the `CalCalendarsChangedExternallyNotification` notification. If you are displaying information about events, then observe the `CalEventsChangedExternallyNotification` notification. If you are displaying information about tasks, then observe the `CalTasksChangedExternallyNotification` notification.

For example, the following code fragment registers for external event changes:

```
[[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(eventsChanged:)
     name:CalEventsChangedExternallyNotification object:[CalCalendarStore defaultCalendarStore]];
```


You can also observe changes made specifically by your application. For example, update the display when you change calendar objects internally. The internal notifications are `CalCalendarsChangedNotification`, `CalEventsChangedNotification`, and `CalTasksChangedNotification`.

For example, the following code fragment registers for internal event changes:

```
[[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(eventsChanged:)
    name:CalEventsChangedNotification object:[CalCalendarStore defaultCalendarStore]];
```


The notification handler method should check to see what objects need to be deleted, inserted, or updated as shown in Listing 1. Since how you apply changes to local objects is application dependent, those portions of this method implementation are omitted in the listing.

__Listing 1__  Applying changes

```objc
- (void)eventsChanged:(NSNotification *)notification
{
    // Apply delete changes
    NSArray *deletedRecords = [[notification userInfo] valueForKey:CalDeletedRecordsKey];
    if (deletedRecords != nil){
        // insert code that deletes local objects
    }

    // Apply insert changes
    NSArray *insertedRecords = [[notification userInfo] valueForKey:CalInsertedRecordsKey];
    if (insertedRecords != nil){
        // insert code that adds new local objects
    }

    // Apply update changes
    NSArray *updatedRecords = [[notification userInfo] valueForKey:CalUpdatedRecordsKey];
    if (updatedRecords != nil){
        // insert code that updates existing objects
    }

    return;
```

Note that the values for the keys contained in the user information dictionary—`CalInsertedRecordsKey`, `CalDeletedRecordsKey`, and `CalUpdatedRecordsKey`—are arrays of UIDs, not arrays of `CalCalendar`, `CalEvent`, or `CalTask` objects. Therefore, you need to maintain a strong reference to either the corresponding `CalCalendar`, `CalEvent`, or `CalTask` objects when you originally fetched them, or keep their UIDs so you can match the remote changes with the local representation of these objects.

When inserting or updating objects, use the corresponding `calendarWithUID:`, `eventWithUID:occurrence:`, or `taskWithUID:` method to fetch the inserted or updated objects from the Calendar Store database.

If you are updating an object, you can either compare property values between the new and old object, or replace the old object with the new object. Calendar Store does not automatically update existing calendar objects—for example, it does not update a previously fetched `CalEvent` object. If you maintain strong references to `CalEvent` objects—for example, add them to an array—then you typically replace the old `CalEvent` object with the new `CalEvent` object to apply an update.

For this reason, you should take precautions when using calendar objects with Cocoa bindings. For example, implement your own model object that uses the calendar object as an internal representation or discard references to calendar objects after making a strong reference to the UID and other property values.

If you have an end-user application that allows the user to edit calendar objects, then you also need to handle changes made by the user and propagate these changes back to the Calendar Store database. How you do this is largely application dependent unless you use Cocoa bindings.

If you use Cocoa bindings, then you should observe local changes to calendar object properties. If you have a strong reference to a `CalEvent` object and the user can directly edit the `CalEvent` object—for example, you use an `NSArrayController` object to display an array of `CalEvent` objects in an editable table view—, then you should observe changes to `CalEvent` properties. At least observe changes to all `CalEvent` properties that you use in your application.

The following code fragment observes local start and end date changes to a `CalEvent` object.

```
// Observe changes to the start and end dates
[event addObserver:self forKeyPath:@"startDate"
           options:(NSKeyValueObservingOptionNew | NSKeyValueObservingOptionOld)
           context:NULL];
[event addObserver:self forKeyPath:@"endDate"
           options:(NSKeyValueObservingOptionNew | NSKeyValueObservingOptionOld)
           context:NULL];
```

Your implementation of the [observeValueForKeyPath:ofObject:change:context:](https://developer.apple.com/documentation/objectivec/nsobject/1416553-observevalueforkeypath) method of `NSObject` should save the local changes to the Calendar Store database using either the `saveCalendar:error:`, `saveEvent:span:error:`, or `saveTask:error:` method depending on the type of object that changed. See [Saving Changes](Saving%20Changes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tanjyfvjvomi) for more information on saving changes to the Calendar Store database.

If the end-user can also add and delete calendar objects, then you also need to observe changes to your mutable array—the array that is providing the content to your `NSArrayController` object. See _[Cocoa Bindings Programming Topics](../../Cocoa/Cocoa%20Bindings%20Programming%20Topics/Introduction%20to%20Cocoa%20Bindings%20Programming%20Topics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3do2i)_ for a complete description of Cocoa bindings.

[Next](Document%20Revision%20History.md)[Previous](Saving%20Changes.md)

