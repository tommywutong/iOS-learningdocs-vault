---
title: Calendar Store Programming Guide
apple_id: TP40004334
resource_type: Guide
platform: macOS
topic: Data Management
technology: CalendarStore
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/CalendarStoreProgGuide/Articles/CreatingObjects.html
archived_at: '2026-07-15T05:17:17.383519Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Calendar Store Programming Guide](Introduction%20to%20Calendar%20Store%20Programming%20Guide.md)


[Next](Creating%20Recurring%20Events.md)[Previous](Fetching%20Objects.md)

# Creating Objects

Your application can also create Calendar Store objects—such as calendars, events, and tasks—that are visible in iCal. Each type of object has properties you set that are either optional or mandatory—for example, events and tasks have a title and calendar property. Some properties you do not set—they are read-only. This article describes how to create each type of object.

Note that none of the changes you make to Calendar Store objects, including creating new objects, persist unless you save the object using one of the `save...` methods in `CalCalendarStore`. For example, if you create a `CalEvent` object, then use the `saveEvent:span:error:` method of `CalCalendarStore` to save it. Read [Saving Changes](Saving%20Changes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tanjyfvjvomi) for more information on saving Calendar Store objects.

Event and task objects inherit common properties from the `CalCalendarItem` class. Note that you must set the `calendar` property of items before you attempt to save them. (Read [Fetching Calendars](Fetching%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2donzvfvjvony) for how to fetch calendar objects that you can use to set the `calendar` property.) All other properties defined in the `CalCalendarItem` class are either optional or read-only. The `dateStamp` and `uid` properties are read-only. All other calendar item properties—such as `notes`, `url`, `title`, and `alarms`—are optional.

You create a calendar object using the `calendar` class method of `CalCalendar`. Optionally, you can then set the `color`, `notes`, or `title` properties. Currently, you can create iCal calendars only. For example, the following code fragment creates a new calendar titled “Kids”:

```
// Create an iCal calendar
CalCalendar *kidsCalendar = [CalCalendar calendar];
kidsCalendar.title = @"Kids";
```


You create a `CalEvent` object using the `event` class method of `CalCalendar`, and, typically, set the `calendar`, `startDate`, `endDate`, and `title` properties. For example, the following code fragment creates a one hour appointment:

```
// Create a simple event.
CalEvent *event = [CalEvent event];
event.calendar = calendar;
event.title = @"Dentist";
event.startDate = [NSDate dateWithNaturalLanguageString:@"3pm January 9, 2007"];
event.endDate = [NSDate dateWithNaturalLanguageString:@"4pm January 9, 2007"];
event.location = @"1123 Fremont Avenue";
```

Read [Creating Recurring Events](Creating%20Recurring%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tanrtfvjvomi) for how to create events that repeat according to a specified daily, weekly, monthly, or yearly pattern.

You create a task object using the `task` `CalTask` class method, and typically, set the `calendar`, `title`, `dueDate`, and `priority` properties. For example, the following code fragment creates a task:

```
// Create a simple task.
CalTask *task = [CalTask task];
task.calendar = calendar;
task.title = @"File Tax Return";
task.dueDate = [NSDate dateWithNaturalLanguageString:@"12am April 15, 2007"];
task.priority = CalPriorityHigh;
```

Note that the `isCompleted` and `completedDate` properties are interdependent. If you set one of these properties, the value of the other property changes too. Read _CalTask Class Reference_ for more details.

You can add alarms to both event and task objects. You create an alarm object using the `alarm` `CalAlarm` class method and then set the `action` property.

If you set the `action` property to `CalAlarmActionEmail`, set the `emailAddress` property to the email address that is sent a notification when the alarm triggers. If you set the `action` property to `CalAlarmActionSound`, set the `sound` property to the sound that is played when the alarm triggers. If you set the `action` property to `CalAlarmActionProcedure`, set the `URL` property to the file that opens when the alarm triggers.

Optionally, you can specify a relative or an absolute trigger. Only one of these is active at a time. If you set the `relativeTrigger` property, then the `absoluteTrigger` property is set to `nil`, and vice versa. Use the `relativeTrigger` property if you want the alarm to trigger a specified interval before the task `dueDate` or event `startDate` properties. For example, you might want the alarm to trigger 15 minutes or 24 hours before a task is due. Use the `absoluteTrigger` property if you want the alarm to trigger at a precise time on a specified date.

For example, the following code fragment adds an alarm to a task that triggers 15 minutes before the due date:

```
// Add an alarm to a task.
CalAlarm *alarm = [CalAlarm alarm];
alarm.action = CalAlarmActionSound;
alarm.sound = @"Basso";
alarm.relativeTrigger = -15*60;
[task addAlarm:alarm];
```

The `addAlarm:` method is inherited from the `CalCalendarItem` class along with other methods for adding and removing alarms. Note that alarms you add to events and tasks are automatically saved when the events and tasks are saved.

[Next](Creating%20Recurring%20Events.md)[Previous](Fetching%20Objects.md)

