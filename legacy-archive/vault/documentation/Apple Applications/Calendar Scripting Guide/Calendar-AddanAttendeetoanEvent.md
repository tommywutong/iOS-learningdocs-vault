---
title: Calendar Scripting Guide
apple_id: TP40016646
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/CalendarScriptingGuide/Calendar-AddanAttendeetoanEvent.html
archived_at: '2026-07-15T05:17:09.864870Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Calendar Scripting Guide](index.md)



## Adding an Attendee to an Event

Calendar events can contain attendees. Listing 12-1 and Listing 12-2 demonstrate how to add an attendee to an event.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&name=Add%20Attendee%20to%20Event&script=tell%20application%20%22Calendar%22%0D%20%20%20%20tell%20calendar%20%22Project%20Calendar%22%0D%20%20%20%20%20%20%20%20set%20theEvent%20to%20%28first%20event%20where%20its%20summary%20%3D%20%22Important%20Meeting!%22%29%0D%20%20%20%20%20%20%20%20tell%20theEvent%0D%20%20%20%20%20%20%20%20%20%20%20%20make%20new%20attendee%20at%20end%20of%20attendees%20with%20properties%20%7Bemail%3A%22example%40apple.com%22%7D%0D%20%20%20%20%20%20%20%20end%20tell%0D%20%20%20%20end%20tell%0D%20%20%20%20reload%20calendars%0Dend%20tell)

__Listing 12-1__AppleScript: Adding an attendee to an event

1. `tell application "Calendar"`
2. `tell calendar "Project Calendar"`
3. `set theEvent to (first event where its summary = "Important Meeting!")`
4. `tell theEvent`
5. `make new attendee at end of attendees with properties {email:"example@apple.com"}`
6. `end tell`
7. `end tell`
8. `reload calendars`
9. `end tell`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&name=Add%20Attendee%20to%20Event&script=var%20app%20%3D%20Application.currentApplication%28%29%0Dvar%20Calendar%20%3D%20Application%28%22Calendar%22%29%0D%0Dvar%20projectCalendars%20%3D%20Calendar.calendars.whose%28%7Bname%3A%20%22Project%20Calendar%22%7D%29%0Dvar%20projectCalendar%20%3D%20projectCalendars%5B0%5D%20%0Dvar%20events%20%3D%20projectCalendar.events.whose%28%7Bsummary%3A%20%22Important%20Meeting!%22%7D%29%0Dvar%20event%20%3D%20events%5B0%5D%0D%0Dvar%20attendee%20%3D%20Calendar.Attendee%28%7Bemail%3A%20%22example%40apple.com%22%7D%29%0Devent.attendees.push%28attendee%29%0D%0DCalendar.reloadCalendars%28%29)

__Listing 12-2__JavaScript: Adding an attendee to an event

1. `var app = Application.currentApplication()`
2. `var Calendar = Application("Calendar")`
4. `var projectCalendars = Calendar.calendars.whose({name: "Project Calendar"})`
5. `var projectCalendar = projectCalendars[0]`
6. `var events = projectCalendar.events.whose({summary: "Important Meeting!"})`
7. `var event = events[0]`
9. `var attendee = Calendar.Attendee({email: "example@apple.com"})`
10. `event.attendees.push(attendee)`
12. `Calendar.reloadCalendars()`

[Adding an Alarm to an Event](Calendar-AddanAlarmtoanEvent.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbwfvbuqojxfvjvomy)
