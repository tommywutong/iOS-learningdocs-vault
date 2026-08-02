---
title: Calendar Scripting Guide
apple_id: TP40016646
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/CalendarScriptingGuide/Calendar-AddanAlarmtoanEvent.html
archived_at: '2026-07-15T05:17:09.350676Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Calendar Scripting Guide](index.md)



## Adding an Alarm to an Event

Calendar events can contain alarms that display messages, send emails, and play sounds. Listing 11-1 and Listing 11-2 show how to add alarms to an event. Each example adds two alarms—a message alarm and a message-with-sound alarm.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&name=Add%20Alarms%20to%20Event&script=tell%20application%20%22Calendar%22%0D%20%20%20%20tell%20calendar%20%22Project%20Calendar%22%0D%20%20%20%20%20%20%20%20set%20theEvent%20to%20%28first%20event%20where%20its%20summary%20%3D%20%22Important%20Meeting!%22%29%0D%20%20%20%20%20%20%20%20tell%20theEvent%0D%20%20%20%20%20%20%20%20%20%20%20%20--%20Add%20a%20message%20alarm%0D%20%20%20%20%20%20%20%20%20%20%20%20make%20new%20display%20alarm%20at%20end%20of%20display%20alarms%20with%20properties%20%7Btrigger%20interval%3A-5%7D%0D%0D%20%20%20%20%20%20%20%20%20%20%20%20--%20Add%20a%20message%20with%20sound%20alarm%0D%20%20%20%20%20%20%20%20%20%20%20%20make%20new%20sound%20alarm%20at%20end%20of%20sound%20alarms%20with%20properties%20%7Btrigger%20interval%3A-5%2C%20sound%20name%3A%22Sosumi%22%7D%0D%20%20%20%20%20%20%20%20end%20tell%0D%20%20%20%20end%20tell%0D%20%20%20%20reload%20calendars%0Dend%20tell)

__Listing 11-1__AppleScript: Adding alarms to an event

1. `tell application "Calendar"`
2. `tell calendar "Project Calendar"`
3. `set theEvent to (first event where its summary = "Important Meeting!")`
4. `tell theEvent`
5. `-- Add a message alarm`
6. `make new display alarm at end of display alarms with properties {trigger interval:-5}`
8. `-- Add a message with sound alarm`
9. `make new sound alarm at end of sound alarms with properties {trigger interval:-5, sound name:"Sosumi"}`
10. `end tell`
11. `end tell`
12. `reload calendars`
13. `end tell`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&name=Add%20Alarms%20to%20Event&script=var%20app%20%3D%20Application.currentApplication%28%29%0Dvar%20Calendar%20%3D%20Application%28%22Calendar%22%29%0D%0Dvar%20projectCalendars%20%3D%20Calendar.calendars.whose%28%7Bname%3A%20%22Project%20Calendar%22%7D%29%0Dvar%20projectCalendar%20%3D%20projectCalendars%5B0%5D%20%0Dvar%20events%20%3D%20projectCalendar.events.whose%28%7Bsummary%3A%20%22Important%20Meeting!%22%7D%29%0Dvar%20event%20%3D%20events%5B0%5D%0D%0D%2F%2F%20Add%20a%20message%20alarm%0Dvar%20displayAlarm%20%3D%20Calendar.DisplayAlarm%28%7BtriggerInterval%3A%20-5%7D%29%0Devent.displayAlarms.push%28displayAlarm%29%0D%0D%2F%2F%20Add%20a%20message%20with%20sound%20alarm%0Dvar%20soundAlarm%20%3D%20Calendar.SoundAlarm%28%7BtriggerInterval%3A%20-5%2C%20soundName%3A%20%22Sosumi%22%7D%29%0Devent.soundAlarms.push%28soundAlarm%29%0D%0DCalendar.reloadCalendars%28%29)

__Listing 11-2__JavaScript: Adding alarms to an event

1. `var app = Application.currentApplication()`
2. `var Calendar = Application("Calendar")`
4. `var projectCalendars = Calendar.calendars.whose({name: "Project Calendar"})`
5. `var projectCalendar = projectCalendars[0]`
6. `var events = projectCalendar.events.whose({summary: "Important Meeting!"})`
7. `var event = events[0]`
9. `// Add a message alarm`
10. `var displayAlarm = Calendar.DisplayAlarm({triggerInterval: -5})`
11. `event.displayAlarms.push(displayAlarm)`
13. `// Add a message with sound alarm`
14. `var soundAlarm = Calendar.SoundAlarm({triggerInterval: -5, soundName: "Sosumi"})`
15. `event.soundAlarms.push(soundAlarm)`
17. `Calendar.reloadCalendars()`

[Revealing an Event](Calendar-RevealanEvent.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbwfvbuqojwfvjvomy)

[Adding an Attendee to an Event](Calendar-AddanAttendeetoanEvent.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbwfvbuqojyfvjvomy)
