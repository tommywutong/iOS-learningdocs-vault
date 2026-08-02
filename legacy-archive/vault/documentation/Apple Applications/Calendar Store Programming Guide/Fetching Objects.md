---
title: Calendar Store Programming Guide
apple_id: TP40004334
resource_type: Guide
platform: macOS
topic: Data Management
technology: CalendarStore
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/CalendarStoreProgGuide/Articles/FetchingRecords.html
archived_at: '2026-07-15T05:17:17.401573Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Calendar Store Programming Guide](Introduction%20to%20Calendar%20Store%20Programming%20Guide.md)


[Next](Creating%20Objects.md)[Previous](Calendar%20Store%20Overview.md)

# Fetching Objects

Calendar Store provides several methods for fetching objects—such as calendars, events, and tasks—from the Calendar Store database. You can fetch all calendars or specific ones using a unique identifier. You can fetch events and tasks specifying a date range or use a predicate to fetch a custom set of objects. However, you cannot fetch all events because recurring events may result in an infinite number of event objects—there are multiple event objects for a recurring “master” event. Typically, you fetch objects in batches as your application uses them—for example, fetch the next month or year of events when the user clicks the Next button. This article describes the methods you use to fetch these Calendar Store objects.

You can fetch all calendars in the Calendar Store database or specific calendars using a unique identifier called a UID.

Use the `calendars` method if you want to fetch all calendars. Note that there is a to-one relationship from an event or task to a calendar object. However, there is not an inverse to-many relationship from a calendar to its events and tasks. Therefore, when you fetch calendars, you are just creating instances of the `CalCalendar` class. Read [Fetching Events](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2donzvfvjvomq)and [Fetching Tasks](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2donzvfvjvomy) for how to fetch other types of objects.

A calendar object’s UID is guaranteed to be unique for the lifetime of the calendar object. So you may retain the UID and use it to fetch individual calendar objects on an as needed basis. Use the `calendarWithUID:` method to fetch a calendar object using a UID.

You can fetch individual events specifying a UID—for example, if you retain an event UID from a previous fetch. However, you typically fetch events using a predicate, which provides the maximum flexibility. You essentially create a database query specifying the property values or range of property values you want the results to match. For your convenience, Calendar Store provides methods for common types of fetches. The following sections progress from the most simple to the most complex fetches.

To fetch an individual event, use the `eventWithUID:occurrence:` method, specifying a UID. If the event is recurring, specify an occurrence date of the individual event you want—recurring events have the same UID. If you don’t know the UID for an event, read [Using Predicates to Fetch Events](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2donzvfvjvoni) for how to fetch events using a predicate.

It’s very common to fetch events in a date range. For example, fetch all events that occur in the current month and then fetch all events that occur in the previous and next months. The `CalCalendarStore` class provides convenience methods for creating these types of predicates that can be passed to the `eventsWithPredicate:` method to perform the actual fetch.

For example, the following code fragment in Listing 1 uses the `eventPredicateWithStartDate:endDate:calendars:` class method to create an event predicate for the current year, and the `eventsWithPredicate:` method for fetching the events.

__Listing 1__  Fetching Current Year Events

```
// Create a predicate to fetch all events for this year
NSInteger year = [[NSCalendarDate date] yearOfCommonEra];
NSDate *startDate = [[NSCalendarDate dateWithYear:year month:1 day:1 hour:0 minute:0 second:0 timeZone:nil] retain];
NSDate *endDate = [[NSCalendarDate dateWithYear:year month:12 day:31 hour:23 minute:59 second:59 timeZone:nil] retain];
NSPredicate *eventsForThisYear = [CalCalendarStore eventPredicateWithStartDate:startDate endDate:endDate
   calendars:[[CalCalendarStore defaultCalendarStore] calendars]];

// Fetch all events for this year
NSArray *events = [[CalCalendarStore defaultCalendarStore] eventsWithPredicate:eventsForThisYear];
```


The Calendar Store framework doesn’t allow you to fetch all events because recurring events may result in an infinite number of event objects.

You can use an event predicate to fetch all events belonging to the same recurrence within a date range. Recurring events have the same UID, so use the `eventPredicateWithStartDate:endDate:UID:calendars:` method similar to the `eventPredicateWithStartDate:endDate:calendars:` method of Listing 1, except specify the common UID. The events returned include all events within the date range belonging to the same recurrence, or a single event if it’s not a recurring event.

As explained in [Fetching in Batches](Calendar%20Store%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2donzqfvjvoni), the events returned by the `eventsWithPredicate:` method contain only recurring events for the first four years of a date range. For this reason, you typically fetch events in batches—no greater than a four year span—as you need them in your application.

Similar to events, you can fetch individual tasks by specifying a UID or multiple tasks by using a predicate. Again, fetching tasks using a predicate provides the maximum flexibility. You essentially create a database query specifying the property values or range of property values you want the results to match. Similar to creating event predicates, Calendar Store provides convenience methods for creating common task predicates.

To fetch an individual task, use the `taskWithUID:` method, specifying a UID. If you don’t know the UID for a task, read Using Predicates to Fetch Tasks for how to fetch tasks with specific criteria.

You can create a predicate to fetch all tasks, fetch all incomplete tasks, fetch all incomplete tasks due before a specific date, or fetch all completed tasks since a specified date. In all cases, you can specify what calendars the tasks must belong to.

For example, this code fragment creates a predicate using the `taskPredicateWithCalendars:` method to fetch all tasks in all calendars:

```
NSPredicate *predicate = [CalCalendarStore taskPredicateWithCalendars:[[CalCalendarStore defaultCalendarStore] calendars]];
NSArray *tasks = [[CalCalendarStore defaultCalendarStore] tasksWithPredicate:predicate];
```

Similarly, use the `taskPredicateWithTasksCompletedSince:calendars:`, `taskPredicateWithUncompletedTasks:`, and `taskPredicateWithUncompletedTasksDueBefore:calendars:` methods to create predicates to perform other types of fetches.

[Next](Creating%20Objects.md)[Previous](Calendar%20Store%20Overview.md)

