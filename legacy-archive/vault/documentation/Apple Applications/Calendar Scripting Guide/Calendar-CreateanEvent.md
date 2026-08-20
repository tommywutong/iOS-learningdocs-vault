---
title: Calendar Scripting Guide
apple_id: TP40016646
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/CalendarScriptingGuide/Calendar-CreateanEvent.html
archived_at: '2026-07-15T05:17:10.854405Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Calendar Scripting Guide](index.md)



## Creating an Event

Use the `make` command to create events on a given calendar. Listing 8-1 and Listing 8-2 demonstrate how to do this by creating a 1-hour meeting event, tomorrow, on a project calendar. The result of each example is a reference to the newly created event.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&name=Create%20an%20Event&script=set%20theStartDate%20to%20%28current%20date%29%20%2B%20%281%20*%20days%29%0Dset%20hours%20of%20theStartDate%20to%2015%0Dset%20minutes%20of%20theStartDate%20to%200%0Dset%20seconds%20of%20theStartDate%20to%200%0Dset%20theEndDate%20to%20theStartDate%20%2B%20%281%20*%20hours%29%0D%0Dtell%20application%20%22Calendar%22%0D%20%20%20%20tell%20calendar%20%22Project%20Calendar%22%0D%20%20%20%20%20%20%20%20make%20new%20event%20with%20properties%20%7Bsummary%3A%22Important%20Meeting!%22%2C%20start%20date%3AtheStartDate%2C%20end%20date%3AtheEndDate%7D%0D%20%20%20%20end%20tell%0Dend%20tell)

__Listing 8-1__AppleScript: Creating a new event

1. `set theStartDate to (current date) + (1 * days)`
2. `set hours of theStartDate to 15`
3. `set minutes of theStartDate to 0`
4. `set seconds of theStartDate to 0`
5. `set theEndDate to theStartDate + (1 * hours)`
7. `tell application "Calendar"`
8. `tell calendar "Project Calendar"`
9. `make new event with properties {summary:"Important Meeting!", start date:theStartDate, end date:theEndDate}`
10. `end tell`
11. `end tell`
12. `--> Result: event id "10D0A87A-3B92-474B-8365-D5434280AA31" of calendar id "CDF2EA89-AE82-44C0-B1B6-449128A5E151" of application "Calendar"`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&name=Create%20an%20Event&script=var%20app%20%3D%20Application.currentApplication%28%29%0Dapp.includeStandardAdditions%20%3D%20true%0Dvar%20Calendar%20%3D%20Application%28%22Calendar%22%29%0D%0Dvar%20eventStart%20%3D%20app.currentDate%28%29%0DeventStart%20%3D%20eventStart%0DeventStart.setDate%28eventStart.getDate%28%29%20%2B%201%29%0DeventStart.setHours%2815%29%0DeventStart.setMinutes%280%29%0DeventStart.setSeconds%280%29%0Dvar%20eventEnd%20%3D%20new%20Date%28eventStart.getTime%28%29%29%0DeventEnd.setHours%2816%29%0D%0Dvar%20projectCalendars%20%3D%20Calendar.calendars.whose%28%7Bname%3A%20%22Project%20Calendar%22%7D%29%0Dvar%20projectCalendar%20%3D%20projectCalendars%5B0%5D%0Dvar%20event%20%3D%20Calendar.Event%28%7Bsummary%3A%20%22Important%20Meeting!%22%2C%20startDate%3A%20eventStart%2C%20endDate%3A%20eventEnd%7D%29%0DprojectCalendar.events.push%28event%29%0Devent)

__Listing 8-2__JavaScript: Creating a new event

1. `var app = Application.currentApplication()`
2. `app.includeStandardAdditions = true`
3. `var Calendar = Application("Calendar")`
5. `var eventStart = app.currentDate()`
6. `eventStart = eventStart`
7. `eventStart.setDate(eventStart.getDate() + 1)`
8. `eventStart.setHours(15)`
9. `eventStart.setMinutes(0)`
10. `eventStart.setSeconds(0)`
11. `var eventEnd = new Date(eventStart.getTime())`
12. `eventEnd.setHours(16)`
14. `var projectCalendars = Calendar.calendars.whose({name: "Project Calendar"})`
15. `var projectCalendar = projectCalendars[0]`
16. `var event = Calendar.Event({summary: "Important Meeting!", startDate: eventStart, endDate: eventEnd})`
17. `projectCalendar.events.push(event)`
18. `event`
19. `// Result: Application("Calendar").calendars.whose({_match: [ObjectSpecifier().name, "Project Calendar"]}).calendars.at(0).events.byId("D7D2AC03-C5DF-4415-B6E3-0243E0314808")`

[Showing a Specific Date](Calendar-GotoaSpecificDate.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbwfvbuqojtfvjvomy)

[Locating an Event](Calendar-LocateanEvent.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbwfvbuqojvfvjvony)
