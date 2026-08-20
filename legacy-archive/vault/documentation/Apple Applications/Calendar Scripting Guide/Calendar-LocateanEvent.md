---
title: Calendar Scripting Guide
apple_id: TP40016646
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/CalendarScriptingGuide/Calendar-LocateanEvent.html
archived_at: '2026-07-15T05:17:12.378671Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Calendar Scripting Guide](index.md)



## Locating an Event

There are many ways to locate an event through scripting. The most accurate way is to match an event to a unique identifier. Listing 9-1 and Listing 9-2 look for an event with a specific `uid` property value. This method assumes you know the `uid` for the event.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&name=Locate%20an%20Event%20by%20ID&script=tell%20application%20%22Calendar%22%0D%20%20%20%20tell%20calendar%20%22Project%20Calendar%22%0D%20%20%20%20%20%20%20%20first%20event%20where%20its%20uid%20%3D%20%22538E181E-7043-45A5-8F61-4711724F1A1B%22%0D%20%20%20%20end%20tell%0Dend%20tell)

__Listing 9-1__AppleScript: Locating an event by its ID

1. `tell application "Calendar"`
2. `tell calendar "Project Calendar"`
3. `first event where its uid = "538E181E-7043-45A5-8F61-4711724F1A1B"`
4. `end tell`
5. `end tell`
6. `--> Result: event id "538E181E-7043-45A5-8F61-4711724F1A1B" of calendar id "CDF2EA89-AE82-44C0-B1B6-449128A5E151" of application "Calendar"`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&name=Locate%20an%20Event%20by%20ID&script=var%20app%20%3D%20Application.currentApplication%28%29%0Dvar%20Calendar%20%3D%20Application%28%22Calendar%22%29%0D%0Dvar%20projectCalendars%20%3D%20Calendar.calendars.whose%28%7Bname%3A%20%22Project%20Calendar%22%7D%29%0Dvar%20projectCalendar%20%3D%20projectCalendars%5B0%5D%20%0D%0Dvar%20event%20%3D%20projectCalendar.events.byId%28%22DD524F6C-A48B-4841-B086-A8891ED84C8D%22%29%0Devent)

__Listing 9-2__JavaScript: Locating an event by its ID

1. `var app = Application.currentApplication()`
2. `var Calendar = Application("Calendar")`
4. `var projectCalendars = Calendar.calendars.whose({name: "Project Calendar"})`
5. `var projectCalendar = projectCalendars[0]`
7. `var event = projectCalendar.events.byId("DD524F6C-A48B-4841-B086-A8891ED84C8D")`
8. `event`
9. `// Result: Application("Calendar").calendars.whose({_match: [ObjectSpecifier().name, "Project Calendar"]}).calendars.at(0).events.byId("DD524F6C-A48B-4841-B086-A8891ED84C8D")`

### Locating an Event by Name

Another way to locate an event is by name. The `summary` property value contains the name of the event as it appears on the calendar. Listing 9-3 and Listing 9-4 look for an event with a `summary` property value of `"Important Meeting!"`. A disadvantage of this method is that event summaries aren’t unique. Therefore, multiple events may exist with the same summary, making it difficult to identify a specific one.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&name=Locate%20an%20Event%20by%20Summary&script=tell%20application%20%22Calendar%22%0D%20%20%20%20tell%20calendar%20%22Project%20Calendar%22%0D%20%20%20%20%20%20%20%20first%20event%20where%20its%20summary%20%3D%20%22Important%20Meeting!%22%0D%20%20%20%20end%20tell%0Dend%20tell)

__Listing 9-3__AppleScript: Locating an event by its summary

1. `tell application "Calendar"`
2. `tell calendar "Project Calendar"`
3. `first event where its summary = "Important Meeting!"`
4. `end tell`
5. `end tell`
6. `--> Result: event id "538E181E-7043-45A5-8F61-4711724F1A1B" of calendar id "CDF2EA89-AE82-44C0-B1B6-449128A5E151" of application "Calendar"`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&name=Locate%20an%20Event%20by%20Summary&script=var%20app%20%3D%20Application.currentApplication%28%29%0Dvar%20Calendar%20%3D%20Application%28%22Calendar%22%29%0D%0Dvar%20projectCalendars%20%3D%20Calendar.calendars.whose%28%7Bname%3A%20%22Project%20Calendar%22%7D%29%0Dvar%20projectCalendar%20%3D%20projectCalendars%5B0%5D%20%0D%0Dvar%20events%20%3D%20projectCalendar.events.whose%28%7Bsummary%3A%20%22Important%20Meeting!%22%7D%29%0Dvar%20event%20%3D%20events%5B0%5D%0Devent)

__Listing 9-4__JavaScript: Locating an event by its summary

1. `var app = Application.currentApplication()`
2. `var Calendar = Application("Calendar")`
4. `var projectCalendars = Calendar.calendars.whose({name: "Project Calendar"})`
5. `var projectCalendar = projectCalendars[0]`
7. `var events = projectCalendar.events.whose({summary: "Important Meeting!"})`
8. `var event = events[0]`
9. `event`
10. `// Result: Application("Calendar").calendars.whose({_match: [ObjectSpecifier().name, "Project Calendar"]}).calendars.at(0).events.whose({_match: [ObjectSpecifier().summary, "Important Meeting!"]}).events.at(0)`

### Locating an Event by Date

You can also locate events by date. Start dates and end dates also include times, so if you’re looking for an event that falls on a specific date, make sure you search for events within a specific timeframe. Listing 9-5 and Listing 9-6 demonstrate this technique by looking for any events with a start date and an end date between 12 a.m. today and 12 a.m. tomorrow.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&name=Locate%20an%20Event%20by%20Date&script=set%20theStartDate%20to%20current%20date%0Dset%20hours%20of%20theStartDate%20to%200%0Dset%20minutes%20of%20theStartDate%20to%200%0Dset%20seconds%20of%20theStartDate%20to%200%0Dset%20theEndDate%20to%20theStartDate%20%2B%20%281%20*%20days%29%20-%201%0D%0Dtell%20application%20%22Calendar%22%0D%20%20%20%20tell%20calendar%20%22Project%20Calendar%22%0D%20%20%20%20%20%20%20%20every%20event%20where%20its%20start%20date%20is%20greater%20than%20or%20equal%20to%20theStartDate%20and%20end%20date%20is%20less%20than%20or%20equal%20to%20theEndDate%0D%20%20%20%20end%20tell%0Dend%20tell)

__Listing 9-5__AppleScript: Locating events by its date

1. `set theStartDate to current date`
2. `set hours of theStartDate to 0`
3. `set minutes of theStartDate to 0`
4. `set seconds of theStartDate to 0`
5. `set theEndDate to theStartDate + (1 * days) - 1`
7. `tell application "Calendar"`
8. `tell calendar "Project Calendar"`
9. `every event where its start date is greater than or equal to theStartDate and end date is less than or equal to theEndDate`
10. `end tell`
11. `end tell`
12. `--> Result: {event id "538E181E-7043-45A5-8F61-4711724F1A1B" of calendar id "CDF2EA89-AE82-44C0-B1B6-449128A5E151" of application "Calendar"}`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&name=Locate%20an%20Event%20by%20Date&script=var%20app%20%3D%20Application.currentApplication%28%29%0Dapp.includeStandardAdditions%20%3D%20true%0Dvar%20Calendar%20%3D%20Application%28%22Calendar%22%29%0D%0Dvar%20startDate%20%3D%20app.currentDate%28%29%0DstartDate%20%3D%20startDate%0DstartDate.setHours%280%29%0DstartDate.setMinutes%280%29%0DstartDate.setSeconds%280%29%0Dvar%20endDate%20%3D%20app.currentDate%28%29%0DendDate.setHours%2823%29%0DendDate.setMinutes%2859%29%0DendDate.setSeconds%2859%29%0D%0Dvar%20projectCalendars%20%3D%20Calendar.calendars.whose%28%7Bname%3A%20%22Project%20Calendar%22%7D%29%0Dvar%20projectCalendar%20%3D%20projectCalendars%5B0%5D%20%0Dvar%20events%20%3D%20projectCalendar.events.whose%28%7BstartDate%3A%20%7B_greaterThan%3A%20startDate%7D%2C%20endDate%3A%20%7B_lessThanEquals%3A%20endDate%7D%7D%29%0Dvar%20event%20%3D%20events%5B0%5D%0Devent)

__Listing 9-6__JavaScript: Locating events by date

1. `var app = Application.currentApplication()`
2. `app.includeStandardAdditions = true`
3. `var Calendar = Application("Calendar")`
5. `var startDate = app.currentDate()`
6. `startDate = startDate`
7. `startDate.setHours(0)`
8. `startDate.setMinutes(0)`
9. `startDate.setSeconds(0)`
10. `var endDate = app.currentDate()`
11. `endDate.setHours(23)`
12. `endDate.setMinutes(59)`
13. `endDate.setSeconds(59)`
15. `var projectCalendars = Calendar.calendars.whose({name: "Project Calendar"})`
16. `var projectCalendar = projectCalendars[0]`
17. `var events = projectCalendar.events.whose({startDate: {_greaterThan: startDate}, endDate: {_lessThanEquals: endDate}})`
18. `var event = events[0]`
19. `event`
20. `// Result: Application("Calendar").calendars.whose({_match: [ObjectSpecifier().name, "Project Calendar"]}).calendars.at(0).events.whose({_and: [{_match: [ObjectSpecifier().startDate, {">": Wed Nov 18 2015 00:00:00 GMT-0800 (PST)}]}, {_match: [ObjectSpecifier().endDate, {"<": Wed Nov 18 2015 23:59:59 GMT-0800 (PST)}]}]}).events.at(0)`

[Creating an Event](Calendar-CreateanEvent.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbwfvbuqojufvjvomy)

[Revealing an Event](Calendar-RevealanEvent.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbwfvbuqojwfvjvomy)
