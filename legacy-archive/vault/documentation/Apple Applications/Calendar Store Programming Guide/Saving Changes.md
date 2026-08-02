---
title: Calendar Store Programming Guide
apple_id: TP40004334
resource_type: Guide
platform: macOS
topic: Data Management
technology: CalendarStore
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/CalendarStoreProgGuide/Articles/SavingChanges.html
archived_at: '2026-07-15T05:17:17.415552Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Calendar Store Programming Guide](Introduction%20to%20Calendar%20Store%20Programming%20Guide.md)


[Next](Observing%20Changes.md)[Previous](Creating%20Recurring%20Events.md)

# Saving Changes

Changes you make locally to calendar objects are not persistent until you save them to the Calendar Store database. This includes calendar, event, and task objects that you create locally. For example, instantiating a `CalEvent` object doesn’t automatically add it and save it to the database. This article describes the `CalCalendarStore` methods you use to save each type of object.

Although errors are rare, you should always check the return value of the `save...` `CalCalendarStore` methods and if an error occurs, take the appropriate action. For example, the sample code in this article displays an alert panel when an error occurs.

Use the `saveCalendar:error:` `CalCalendarStore` method to save a new `CalCalendar` object or to save changes to an existing `CalCalendar` object. Note that changes to events or tasks belonging to a calendar are not automatically saved when you save the calendar. Read [Saving Changes to Events](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tanjyfvjvomy)and [Saving Changes to Tasks](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tanjyfvjvona) for how to save events and tasks.

Use the `saveEvent:span:error:` `CalCalendarStore` method to save a new `CalEvent` object or to save changes to an existing `CalEvent` object. If you are adding a new object, the `calendar` property of the `CalEvent` object needs to be set before you invoke this method.

The code fragment in Listing 1 shows how to save changes to an event object.

__Listing 1__  Saving events

```
// Save changes to an event
NSError *calError;
if ([[CalCalendarStore defaultCalendarStore] saveEvent:event span:CalSpanThisEvent error:&calError] == NO){
    NSAlert *alertPanel = [NSAlert alertWithError:calError];
    (void) [alertPanel runModal];
    // terminate the application?
}
```

Similarly, use the `removeEvent:span:error:` `CalCalendarStore` method to delete an event from the Calendar Store database. This method returns `YES` if successful, and `NO` if an error occurred.

You use the `span:` argument for each of these methods to specify which events of a recurring event to apply the changes to. Pass the `CalSpanThisEvent` constant for a nonrecurring event. Otherwise, use the `CalSpanFutureEvents` constant to apply the changes to all future events or the `CalSpanAllEvents` constant to apply the changes to all events in the recurrence.

Use the `saveTask:error:``CalCalendarStore` method to save a new `CalTask` object or to save changes to an existing `CalTask` object. If you are adding a new object, the `calendar` property of the `CalTask` object needs to be set before you invoke this method.

Use the `removeTask:error:` `CalCalendarStore` method to remove a task from the Calendar Store database. Again, check the return value of this method in case an error occurs.

[Next](Observing%20Changes.md)[Previous](Creating%20Recurring%20Events.md)

