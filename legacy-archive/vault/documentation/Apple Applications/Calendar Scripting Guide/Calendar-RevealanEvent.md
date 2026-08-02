---
title: Calendar Scripting Guide
apple_id: TP40016646
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/CalendarScriptingGuide/Calendar-RevealanEvent.html
archived_at: '2026-07-15T05:17:12.867057Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Calendar Scripting Guide](index.md)



## Revealing an Event

Use the `show` command to bring Calendar to the front and show a specified event, as demonstrated in Listing 10-1 and Listing 10-2.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&name=Reveal%20an%20Event&script=tell%20application%20%22Calendar%22%0D%20%20%20%20tell%20calendar%20%22Project%20Calendar%22%0D%20%20%20%20%20%20%20%20show%20%28first%20event%20where%20its%20summary%20%3D%20%22Important%20Meeting!%22%29%0D%20%20%20%20end%20tell%0Dend%20tell)

__Listing 10-1__AppleScript: Revealing an event

1. `tell application "Calendar"`
2. `tell calendar "Project Calendar"`
3. `show (first event where its summary = "Important Meeting!")`
4. `end tell`
5. `end tell`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&name=Reveal%20an%20Event&script=var%20app%20%3D%20Application.currentApplication%28%29%0Dvar%20Calendar%20%3D%20Application%28%22Calendar%22%29%0D%0Dvar%20projectCalendars%20%3D%20Calendar.calendars.whose%28%7Bname%3A%20%22Project%20Calendar%22%7D%29%0Dvar%20projectCalendar%20%3D%20projectCalendars%5B0%5D%20%0Dvar%20events%20%3D%20projectCalendar.events.whose%28%7Bsummary%3A%20%22Important%20Meeting!%22%7D%29%0Dvar%20event%20%3D%20events%5B0%5D%0Devent.show%28%29)

__Listing 10-2__JavaScript: Revealing an event

1. `var app = Application.currentApplication()`
2. `var Calendar = Application("Calendar")`
4. `var projectCalendars = Calendar.calendars.whose({name: "Project Calendar"})`
5. `var projectCalendar = projectCalendars[0]`
6. `var events = projectCalendar.events.whose({summary: "Important Meeting!"})`
7. `var event = events[0]`
8. `event.show()`

[Locating an Event](Calendar-LocateanEvent.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbwfvbuqojvfvjvony)

[Adding an Alarm to an Event](Calendar-AddanAlarmtoanEvent.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbwfvbuqojxfvjvomy)
