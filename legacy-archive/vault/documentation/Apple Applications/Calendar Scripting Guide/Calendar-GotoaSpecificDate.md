---
title: Calendar Scripting Guide
apple_id: TP40016646
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/CalendarScriptingGuide/Calendar-GotoaSpecificDate.html
archived_at: '2026-07-15T05:17:11.863030Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Calendar Scripting Guide](index.md)



## Showing a Specific Date

Use the `view calendar` command to show a specific date in the calendar window. Listing 7-1 and Listing 7-2 show the current date.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&name=Show%20the%20Current%20Date&script=tell%20application%20%22Calendar%22%0D%20%20%20%20view%20calendar%20at%20current%20date%0Dend%20tell)

__Listing 7-1__AppleScript: Showing a specific date

1. `tell application "Calendar"`
2. `view calendar at current date`
3. `end tell`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&name=Show%20the%20Current%20Date&script=var%20app%20%3D%20Application.currentApplication%28%29%0Dapp.includeStandardAdditions%20%3D%20true%0Dvar%20Calendar%20%3D%20Application%28%22Calendar%22%29%0Dvar%20date%20%3D%20app.currentDate%28%29%0DCalendar.viewCalendar%28%7Bat%3A%20date%7D%29)

__Listing 7-2__JavaScript: Showing a specific date

1. `var app = Application.currentApplication()`
2. `app.includeStandardAdditions = true`
3. `var Calendar = Application("Calendar")`
4. `var date = app.currentDate()`
5. `Calendar.viewCalendar({at: date})`

[Switching Calendar Views](Calendar-SwitchCalendarViews.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbwfvbuqojsfvjvomy)

[Creating an Event](Calendar-CreateanEvent.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbwfvbuqojufvjvomy)
