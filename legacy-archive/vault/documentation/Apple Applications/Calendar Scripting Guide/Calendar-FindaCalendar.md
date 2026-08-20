---
title: Calendar Scripting Guide
apple_id: TP40016646
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/CalendarScriptingGuide/Calendar-FindaCalendar.html
archived_at: '2026-07-15T05:17:11.359366Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Calendar Scripting Guide](index.md)



## Finding a Calendar

You can locate a calendar by searching for its name, as demonstrated in Listing 4-1 and Listing 4-2. The result of each example is a reference to the found calendar, which has been assigned to a variable for potential use later in a script.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&name=Find%20a%20Calendar&script=tell%20application%20%22Calendar%22%0A%20%20%20%20set%20theCalendarName%20to%20%22Project%20Calendar%22%0A%20%20%20%20set%20theCalendar%20to%20first%20calendar%20where%20its%20name%20%3D%20theCalendarName%0Aend%20tell)

__Listing 4-1__AppleScript: Finding a calendar matching a specific name

1. `tell application "Calendar"`
2. `set theCalendarName to "Project Calendar"`
3. `set theCalendar to first calendar where its name = theCalendarName`
4. `end tell`
5. `--> Result: calendar id "80CCA5CA-808B-43B3-936D-4D9D7B33B516" of application "Calendar"`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&name=Find%20a%20Calendar&script=var%20Calendar%20%3D%20Application%28%22Calendar%22%29%0Dvar%20calendarName%20%3D%20%22Project%20Calendar%22%0DCalendar.calendars.whose%28%7Bname%3A%20%22Project%20Calendar%22%7D%29)

__Listing 4-2__JavaScript: Finding a calendar matching a specific name

1. `var Calendar = Application("Calendar")`
2. `var calendarName = "Project Calendar"`
3. `Calendar.calendars.whose({name: "Project Calendar"})`
4. `// Result: Application("Calendar").calendars.whose({_match: [ObjectSpecifier().name, "Project Calendar"]})`

[Creating a Calendar](Calendar-CreateaCalendar.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbwfvbuqobzfvjvomy)

[Subscribing to a Calendar](Calendar-SubscribetoaCalendar.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbwfvbuqojrfvjvona)
