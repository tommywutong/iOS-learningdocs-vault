---
title: Calendar and Reminders Programming Guide
apple_id: TP40009765
resource_type: Guide
platform: watchOS|iOS|macOS
topic: Data Management
technology: EventKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/EventKitProgGuide/CreatingRecurringEvents/CreatingRecurringEvents.html
archived_at: '2026-07-27T06:57:07.521315Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Calendar and Reminders Programming Guide](Introduction%20to%20Calendars%20and%20Reminders.md)


[Next](Observing%20External%20Changes%20to%20the%20Calendar%20Database.md)[Previous](Configuring%20Alarms.md)

# Creating Recurring Events

Recurring events repeat over a specified interval of time. To make an event a recurring event, assign it a recurrence rule, which describes when the event occurs. Recurrence rules are represented by instances of the [EKRecurrenceRule](https://developer.apple.com/documentation/eventkit/ekrecurrencerule) class.

Recurrence is applicable to both calendar events and reminders. Unlike with recurring events, only the first incomplete reminder of a recurring set is obtainable. This is true with EventKit as well as the Reminders app. When the reminder is completed, the next reminder in the recurrence set becomes available.

## Using Basic Rules

You can create a recurrence rule with a simple daily, weekly, monthly, or yearly pattern using the [initRecurrenceWithFrequency:interval:end:](https://developer.apple.com/documentation/eventkit/ekrecurrencerule/1507273-initrecurrencewithfrequency) method. You provide three values to this method:

- __The recurrence frequency__. This is a value of type [EKRecurrenceFrequency](https://developer.apple.com/documentation/eventkit/ekrecurrencefrequency) that indicates whether the recurrence rule is daily, weekly, monthly, or yearly.
- __The recurrence interval__. This is an integer greater than 0 that specifies how often a pattern repeats. For example, if the recurrence rule is a weekly recurrence rule and its interval is `1`, then the pattern repeats every week. If the recurrence rule is a monthly recurrence rule and its interval is `3`, then the pattern repeats every three months.
- __The recurrence end__. This optional parameter is an instance of the [EKRecurrenceEnd](https://developer.apple.com/documentation/eventkit/ekrecurrenceend) class, which indicates when the recurrence rule ends. The recurrence end can be based on a specific end date or on an amount of occurrences.

  If you don’t want to specify an end for the recurrence rule, pass `nil`.

## Using Complex Rules

You can create a recurrence rule with a complex pattern using the [initRecurrenceWithFrequency:interval:daysOfTheWeek:daysOfTheMonth:monthsOfTheYear:weeksOfTheYear:daysOfTheYear:setPositions:end:](https://developer.apple.com/documentation/eventkit/ekrecurrencerule/1507320-init) method. As you do for a basic recurrence rule, you provide a frequency, an interval, and an optional end for the recurring event. In addition, you can provide a combination of optional values describing a custom rule, as listed in [Table 4-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tonrvfvbuqmznknlti).

__Table 4-1__  Complex recurrence rule breakdown

| Parameter name | Accepted values | Can be combined with | Example |
| _days_  The days of the week on which the event occurs. | An array of [EKRecurrenceDayOfWeek](https://developer.apple.com/documentation/eventkit/ekrecurrencedayofweek) objects. | All recurrence rules except for daily recurrence rules. | An array containing `EKTuesday` and `EKFriday` objects will create a recurrence that occurs every Tuesday and Friday. |
| _monthDays_  The days of the month on which the event occurs. | An array of nonzero `NSNumber` objects ranging from –31 to 31. Negative values indicate counting backward from the end of the month. | Monthly recurrence rules only. | An array containing the values `1` and `–1` will create a recurrence that occurs on the first and last day of every month. |
| _months_  The months of the year in which the event occurs. | An array of `NSNumber` objects with values ranging from 1 to 12, corresponding to Gregorian calendar months. | Yearly recurrence rules only. | If your originating event occurs on January 10, you can provide an array containing the values `1` and `2` to create a recurrence that occurs every January 10 and February 10. |
| _weeksOfTheYear_  The weeks of the year in which the event occurs. | An array of nonzero `NSNumber` objects ranging from –53 to 53. Negative values indicate counting backward from the end of the year. | Yearly recurrence rules only. | If your originating event occurs on a Wednesday, you can provide an array containing the values `1` and `–1` to create a recurrence that occurs on the Wednesday of the first and last weeks of every year. If a specified week does not contain a Wednesday in the current year, as can be the case for the first or last week of a year, the event does not occur. |
| _daysOfTheYear_  The days of the year on which the event occurs. | An array of nonzero `NSNumber` objects ranging from –366 to 366. Negative values indicate counting backward from the end of the year. | Yearly recurrence rules only. | You can provide an array containing the values `1` and `–1` to create a recurrence that occurs on the first and last day of every year. |
| _setPositions_  The occurrences to include in the recurrence rule. This filter is applied to the set of occurrences determined from the other parameters you provide. | An array of nonzero `NSNumber` objects ranging from –366 to 366. Negative values indicate counting backward from the end of the list of occurrences. | All recurrence rules except for daily recurrence rules. | If you provide an array containing the values `1` and `–1` to a yearly recurrence rule that has specified Monday through Friday as its value for days of the week, the recurrence occurs only on the first and last weekday of every year. |

You can provide values for any number of the parameters in [Table 4-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tonrvfvbuqmznknlti). Parameters that don’t apply to a particular recurrence rule are ignored. If you provide a value for more than one of the above parameters, the recurrence occurs only on days that apply to all provided values.

Once you have created a recurrence rule, you can apply it to a calendar event or reminder with the [addRecurrenceRule:](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507256-addrecurrencerule) instance method of [EKCalendarItem](https://developer.apple.com/documentation/eventkit/ekcalendaritem).

[Next](Observing%20External%20Changes%20to%20the%20Calendar%20Database.md)[Previous](Configuring%20Alarms.md)
