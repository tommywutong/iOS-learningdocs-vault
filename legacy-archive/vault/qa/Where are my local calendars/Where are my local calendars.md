---
title: Where are my local calendars?
apple_id: DTS40017391
resource_type: QA
platform: iOS
topic: General
technology: EventKit
published: '2016-07-05'
source_url: https://developer.apple.com/library/archive/qa/qa1926/_index.html
archived_at: '2026-07-18T02:37:04.143856Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1926

# Where are my local calendars?

## Q:  EKEventStore's calendarsForEntityType does not return my local calendars when iCloud calendars are enabled on my device. They also do not appear among the calendars in the Calendar application. Where are they?

A: That is the expected behavior when your local calendars do not have any events. When you enable calendars for a remote account such as iCloud or Exchange in the Settings application on your device as shown in Figure 1, we check whether any of your local calendars have events.

__Figure 1__  iCloud calendars enabled in the Settings app on your device.

!

__Figure 2__   In the Calendar app before enabling iCloud calendars: EmptyLocalCalendar is a calendar without events and LocalCalendarWithEvents is a calendar with events.

!!

__Listing 1__  Running EKEventStore's calendarsForEntityType show these calendars and their type is local.

```swift
extension EKCalendar
{
    /// - returns: The name matching a given calendar type.
    var nameMatchingCalendarType: String
    {
        switch self.type
        {
            case .Local: return "A local calendar."
            case .CalDAV: return "A CalDAV or iCloud calendar."
            case .Exchange: return "An Exchange calendar."
            case .Subscription: return "A locally subscribed calendar."
            case .Birthday: return "A birthday calendar."
        }
    }
}


// Fetch all event calendars
let calendars = self.eventStore.calendarsForEntityType(.Event)

// Display all returned calendars
for calendar in calendars
{
    print("Calendar: \(calendar.title) Type: \(calendar.nameMatchingCalendarType)")
}

// Calendar: US Holidays                 Type: A locally subscribed calendar.
// Calendar: EmptyLocalCalendar          Type: A local calendar.
// Calendar: LocalCalendarWithEvents     Type: A local calendar.
// Calendar: Birthdays                   Type: A birthday calendar.
```

We offer to remove or migrate your local calendars to the remote account if any of them has events as shown in Figure 3.

__Figure 3__  After enabling calendars for iCloud, LocalCalendarWithEvents and EmptyLocalCalendar appear among iCloud calendars in the Calendar app.

!!

__Listing 2__  After enabling calendars for iCloud, running EKEventStore's calendarsForEntityType show these calendars with a CalDAV or iCloud type.

```swift
extension EKCalendar
{
    /// - returns: The name matching a given calendar type.
    var nameMatchingCalendarType: String
    {
        switch self.type
        {
            case .Local: return "A local calendar."
            case .CalDAV: return "A CalDAV or iCloud calendar."
            case .Exchange: return "An Exchange calendar."
            case .Subscription: return "A locally subscribed calendar."
            case .Birthday: return "A birthday calendar."
        }
    }
}


// Fetch all event calendars
let calendars = self.eventStore.calendarsForEntityType(.Event)

// Display all returned calendars
for calendar in calendars
{
    print("Calendar: \(calendar.title) Type: \(calendar.nameMatchingCalendarType)")
}

// Calendar: US Holidays                Type: A locally subscribed calendar.
// Calendar: Trips                      Type: A CalDAV or iCloud calendar.
// Calendar: EmptyLocalCalendar         Type: A CalDAV or iCloud calendar.
// Calendar: LocalCalendarWithEvents    Type: A CalDAV or iCloud calendar.
// Calendar: Meetings                   Type: A CalDAV or iCloud calendar.
// Calendar: Birthdays                  Type: A birthday calendar.
```

We hide your local calendars if they are empty as shown in Figure 4 and Listing 3.

__Figure 4__  In the Calendar app before enabling iCloud: EmptyLocalCalendar is a calendar with no events. After enabling calendars for iCloud, EmptyLocalCalendar does not appear in the Calendar app.

!!

__Listing 3__  Running EKEventStore's calendarsForEntityType does not show EmptyLocalCalendar.

```swift
extension EKCalendar
{
    /// - returns: The name matching a given calendar type.
    var nameMatchingCalendarType: String
    {
        switch self.type
        {
            case .Local: return "A local calendar."
            case .CalDAV: return "A CalDAV or iCloud calendar."
            case .Exchange: return "An Exchange calendar."
            case .Subscription: return "A locally subscribed calendar."
            case .Birthday: return "A birthday calendar."
        }
    }
}


// Fetch all event calendars
let calendars = self.eventStore.calendarsForEntityType(.Event)

// Display all returned calendars
for calendar in calendars
{
    print("Calendar: \(calendar.title) Type: \(calendar.nameMatchingCalendarType)")
}

// Calendar: US Holidays   Type: A locally subscribed calendar.
// Calendar: Trips         Type: A CalDAV or iCloud calendar.
// Calendar: Meetings      Type: A CalDAV or iCloud calendar.
// Calendar: Birthdays     Type: A birthday calendar.
```

Disable calendars for your remote account in the Settings app on your device to view your local calendars.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-07-05 | New document that explains why local calendars are hidden when enabling calendars for remote source accounts on a device. |

