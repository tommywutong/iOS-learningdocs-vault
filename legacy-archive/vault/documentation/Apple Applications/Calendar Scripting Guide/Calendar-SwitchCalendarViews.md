---
title: Calendar Scripting Guide
apple_id: TP40016646
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/CalendarScriptingGuide/Calendar-SwitchCalendarViews.html
archived_at: '2026-07-15T05:17:14.387596Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Calendar Scripting Guide](index.md)



## Switching Calendar Views

Use the `switch view` command to change the display of the calendar window to day, week, or month view, as demonstrated in Listing 6-1 and Listing 6-2.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&name=Switch%20to%20Day%20View&script=tell%20application%20%22Calendar%22%0D%20%20%20%20switch%20view%20to%20day%20view%0Dend%20tell)

__Listing 6-1__AppleScript: Switching the calendar to day view

1. `tell application "Calendar"`
2. `switch view to day view`
3. `end tell`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&name=Switch%20to%20Week%20View&script=var%20Calendar%20%3D%20Application%28%22Calendar%22%29%0DCalendar.switchView%28%7Bto%3A%20%22week%20view%22%7D%29)

__Listing 6-2__JavaScript: Switching the calendar to week view

1. `var Calendar = Application("Calendar")`
2. `Calendar.switchView({to: "week view"})`

[Subscribing to a Calendar](Calendar-SubscribetoaCalendar.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbwfvbuqojrfvjvona)

[Showing a Specific Date](Calendar-GotoaSpecificDate.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbwfvbuqojtfvjvomy)
