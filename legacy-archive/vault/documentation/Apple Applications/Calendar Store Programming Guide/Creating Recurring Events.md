---
title: Calendar Store Programming Guide
apple_id: TP40004334
resource_type: Guide
platform: macOS
topic: Data Management
technology: CalendarStore
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/CalendarStoreProgGuide/Articles/CreatingRecurringEvents.html
archived_at: '2026-07-15T05:17:17.391256Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Calendar Store Programming Guide](Introduction%20to%20Calendar%20Store%20Programming%20Guide.md)


[Next](Saving%20Changes.md)[Previous](Creating%20Objects.md)

# Creating Recurring Events

Recurring events are events that repeat daily, weekly, monthly, or yearly. Actually, the pattern that repeats can be quite complex, such as every Tuesday and Thursday of the first and second week of every month of the year.

Typically, you create an event by sending `event` to the `CalEvent` class. Then you set the `startDate` and optionally the `endDate` properties of the new event object returned by this method. Read [Creating Events](Creating%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcnjyfvjvomq) for how to create a basic event object. If you are creating a recurring event, you also need to set the `recurrenceRule` property. The recurrence rule is the object that describes the recurring pattern.

This article describes how to create recurrence rules.

A recurrence rule defines a time/date pattern that repeats given some interval. A combination of classes are used to represent a recurrence rule including `CalRecurrenceRule`, `CalRecurrenceEnd`, and `CalNthWeekDay`. [Figure 2](Calendar%20Store%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2donzqfvjvomy) in [Calendar Store Overview](Calendar%20Store%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2donzqfvjvomi) depicts the relationship between these classes and an event.

The `CalRecurrenceRule` class is used to describe the recurrence rule—the pattern that repeats—for a recurring event. The patterns you can create are limited to the types of recurring events the user can create in iCal. `CalRecurrenceRule` provides convenience methods for creating different types of recurrence rules.

The convenience methods are initialization methods that you send to a newly created `CalRecurrenceRule` object. The initialization methods set all the properties of a `CalRecurrenceRule` object—you cannot set the properties directly since they are read-only.

Each initialization method creates a particular type of recurrence rule that uses a time unit of measurements between intervals. You can create daily, weekly, monthly, or yearly recurrence rules. If the initialization method begins with `initMonthly...`, then the object returned is a monthly recurrence rule that uses a single month as the unit of time between intervals. Similarly, use `initDaily...`, `initWeekly...`, and `initYearly...` methods to create daily, weekly, and yearly recurrence rules respectively. Use the `recurrenceType` property of a `CalRecurrenceRule` to determine the type.

Each of the initialization methods has an `...Interval` and an `end:` argument described in Table 1. The end rule is a `CalRecurrenceEnd` object that specifies how a recurring event ends. The other arguments that may appear in the different initialization methods are used to create more complex recurrence rules—for example, they specify the day of the week or week of the month in the pattern. Table 1 describes the values of these additional arguments.

The `CalNthWeekDay` class depicted in [Figure 2](Calendar%20Store%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2donzqfvjvomy) is used to get information about a recurring event, not create one. The `nthWeekDaysOfTheMonth` property of a `CalRecurrenceEnd` object is an array of `CalNthWeekDay` objects. See _CalNthWeekDay Class Reference_ for more information about this class.

__Table 1__  Initialization method arguments

| Argument | Value | Description |
| `...Interval` | An integer greater than `0`. | The number of time units between occurrences of an event where time units are a day, week, month, or year depending on the `init...` method used. |
| `forDayOfTheWeek:` | An integer ranging from `1` to `7` where Sunday is `1`. | The day of the week when an event occurs. |
| `forDaysOfTheWeek:` | An array of integers ranging from `1` to `7` where Sunday is `1`. | The days of the week when an event occurs. |
| `forWeekOfTheMonth` | An integer value of either `1`, `2`, `3`, `4`, or `-1` where `-1` is the last week of the month. | The week of the month when an event occurs. |
| `forDaysOfTheMonth` | An array of integers ranging from `1` to `31`. | The day of the month when an event occurs. |
| `forMonthsOfTheYear` | An array of integers ranging from `1` to `12`. | The day of the month when an event occurs. |
| `end:` | A `CalRecurrenceEnd` object. | Specifies how a recurring event ends. |

The interval argument is an integer greater than `0` that specifies how often a pattern repeats given the recurrence end’s unit of time. For example, if the time unit is a week and the interval is `1`, then the pattern repeats every week. If the time unit is a month and the interval is `2`, then the pattern repeats bimonthly. If the time unit is a year and the interval is `3`, then the pattern repeats every three years. The convenience method you use to create the recurrence rule determines the time unit.

The recurrence end argument is optional and specifies how the recurring event ends. The recurrence end argument is a `CalRecurrenceEnd` object that specifies either a counter or an ending date. If the recurrence end object uses a counter, the event ends after the counter decrements to `0`. Otherwise, it ends on the specified date.

Use the `recurrenceEndWithOccurrenceCount:` `CalRecurrenceEnd` method to create a recurrence end that uses a counter, or the `recurrenceEndWithEndDate:` `CalRecurrenceEnd` method to create a recurrence end that uses an end date.

The simplest and most common recurring event is one that occurs in daily intervals—for example, an event that occurs every day or an event that occurs every two days.

Use the `initDailyRecurrenceWithInterval:end:` method to create an event that occurs once a day and repeats in daily intervals. Use the `...Interval:` argument to specify the number of days between occurrences (see Specifying an Interval) and optionally, use the `end:` argument to specify when the event ends (see Creating a Recurrence End).

For example, the following code fragment creates a never-ending event that occurs every other day starting today:

```
// Create a daily event that occurs every other day.
CalEvent *event = [CalEvent event];
event.calendar = calendar;
event.title = @"Bath Nite";
event.startDate = [NSDate date];
event.endDate = [NSDate distantFuture];
event.recurrenceRule = [[CalRecurrenceRule alloc] initDailyRecurrenceWithInterval:2 end:nil];
```


Weekly recurrence rules are useful for events that occur on the same days of the week—for example, a class that meets at the same time on Mondays, Wednesdays, and Fridays of every week.

Similar to creating a daily recurrence rule, use the `initWeeklyRecurrenceWithInterval:end:` method to create an event that occurs once a week and repeats in weekly intervals. The day of the week defaults to the day of the week of the start date. If the start date is a Tuesday, the weekly event repeats on Tuesdays at the specified interval. For example, use this method to create an event that occurs every-other week starting today as in the following code fragment:

```
// Create a weekly event that occurs every other week from the start date.
CalEvent *event = [CalEvent event];
event.calendar = calendar;
event.title = @"Pay Day";
event.startDate = [NSDate date];
event.endDate = [NSDate distantFuture];
event.recurrenceRule = [[CalRecurrenceRule alloc] initWeeklyRecurrenceWithInterval:2 end:nil];
```

Use the `initWeeklyRecurrenceWithInterval:forDaysOfTheWeek:end:` method to create an event that occurs multiple times per week and repeats in weekly intervals. Use the `forDaysOfTheWeek:` argument to specify which days of the week the event occurs. This argument is an array of integers ranging from `1` to `7` where Sunday is equal to `1`. For example, the following code fragment creates an event that occurs every 3rd week on Mondays and Wednesdays starting today:

```
CalEvent *event = [CalEvent event];
event.calendar = calendar;
event.title = @"3rd Week MW";
event.startDate = [NSDate date];
event.endDate = [NSDate distantFuture];
NSArray *days = [NSArray arrayWithObjects:[NSNumber numberWithInt:2], [NSNumber numberWithInt:4], nil];
event.recurrenceRule = [[CalRecurrenceRule alloc] initWeeklyRecurrenceWithInterval:3 forDaysOfTheWeek:days end:nil];
```

Note that the event occurs on the given start date regardless of whether it matches the weekly pattern. For example, if the start date is a Tuesday and the days of the weekly pattern are Mondays and Wednesdays, then the event occurs on the Tuesday start date and thereafter, Mondays and Wednesdays at the specified interval.

Similar to weekly recurrence rules, monthly recurrence rules are useful for creating patterns that repeat in monthly intervals.

Use the `initMonthlyRecurrenceWithInterval:end:` method to create an event that occurs once a month and repeats in monthly intervals. For example, use this method to create an event that occurs on the 15th of every month for the next 6 months.

```
// Create a monthly event that occurs on the 15th of every month for 6 months.
CalEvent *event = [CalEvent event];
event.calendar = calendar;
event.title = @"Loan Payment";
event.startDate = [NSDate dateWithNaturalLanguageString:@"01/15/07"];
event.endDate = [NSDate dateWithNaturalLanguageString:@"06/15/07"];
CalRecurrenceEnd *end = [CalRecurrenceEnd recurrenceEndWithOccurrenceCount:6];
event.recurrenceRule = [[CalRecurrenceRule alloc] initMonthlyRecurrenceWithInterval:1 end:end];
```

Use the `initMonthlyRecurrenceWithInterval:forDaysOfTheMonth:end:` method to create an event that occurs multiple times a month and repeats in monthly intervals. Use the `forDaysOfTheMonth:` argument to specify the days of the month that the event occurs. This argument is an array of integers ranging from `1` to `31` representing the days of the month. For example, use this method to create an event that occurs on the 1st and 15th of every month.

Use the `initMonthlyRecurrenceWithInterval:forDayOfTheWeek:forWeekOfTheMonth:end:` method to create an event that has both a weekly and monthly pattern that repeats in monthly intervals. Use the `forDayOfTheWeek:` argument to specify the day of the week that the pattern occurs. Use the `forWeekOfTheMonth:` argument to specify the weeks within a month that the pattern occurs. See [Table 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tanrtfvjvona) for details on these arguments.

Yearly recurrence rules are needed to create more complex recurring events. For example, events that occur quarterly or twice a year on the same month and day of the year. Even some complex monthly patterns can be easier to represent using a yearly recurrence rule.

Use the `initYearlyRecurrenceWithInterval:end:` method to create an event that occurs once a year and repeats in a yearly interval. For example, if the start date is July 4th, 2006 and the interval is `1`, then the event would occur every 4th of July after the start date.

Use the `initYearlyRecurrenceWithInterval:forMonthsOfTheYear:end:` method to create an event that occurs multiple times a year and repeats in yearly intervals. For example, if the start date is April 10, 2007, the interval is `1`, the `forMonthsOfTheYear:` argument is an array containing the integers `4` and `12`, then this event occurs on April 10th and December 10th of every year after 2005 as shown in this code fragment:

```
// Create a yearly event that occurs on the 10th of April and December of every year.
CalEvent *event = [CalEvent event];
event.calendar = calendar;
event.title = @"Property Taxes";
event.startDate = [NSDate dateWithNaturalLanguageString:@"April 10, 2007"];
event.endDate = event.endDate = [NSDate distantFuture];
NSArray *months = [NSArray arrayWithObjects:[NSNumber numberWithInt:4], [NSNumber numberWithInt:12], nil];
event.recurrenceRule = [[CalRecurrenceRule alloc] initYearlyRecurrenceWithInterval:1 forMonthsOfTheYear:months end:nil];
```

Use the `initYearlyRecurrenceWithInterval:forDayOfTheWeek:forWeekOfTheMonth:forMonthsOfTheYear:end:` method to create an event that has a predictable weekly, monthly, and yearly pattern.

[Next](Saving%20Changes.md)[Previous](Creating%20Objects.md)

