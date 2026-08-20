---
title: Calendar Scripting Guide
apple_id: TP40016646
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/CalendarScriptingGuide/Calendar-CreateaCalendar.html
archived_at: '2026-07-15T05:17:10.373928Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Calendar Scripting Guide](index.md)



## Creating a Calendar

Use the `make` command to create a new calendar on your Mac, as demonstrated in Listing 3-1 and Listing 3-2. The result of the `make` command is a reference to the newly created calendar, which can be assigned to a variable for later use in a script. For example, after you create a calendar, a script could add events to it.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&name=Create%20New%20Calendar&script=tell%20application%20%22Calendar%22%0D%09set%20theCalendarName%20to%20%22Project%20Calendar%22%0D%09set%20theCalendarDescription%20to%20%22Calendar%20for%20top%20secret%20Apple%20project.%22%0D%09set%20theNewCalendar%20to%20make%20new%20calendar%20with%20properties%20%7Bname%3AtheCalendarName%2C%20description%3AtheCalendarDescription%7D%0Dend%20tell)

__Listing 3-1__AppleScript: Creating a new calendar

1. `tell application "Calendar"`
2. `set theCalendarName to "Project Calendar"`
3. `set theCalendarDescription to "Calendar for top secret Apple project."`
4. `set theNewCalendar to make new calendar with properties {name:theCalendarName, description:theCalendarDescription}`
5. `end tell`
6. `--> Result: calendar 3 of application "Calendar"`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&name=Create%20New%20Calendar&script=var%20Calendar%20%3D%20Application%28%22Calendar%22%29%0Dvar%20calendarName%20%3D%20%22Project%20Calendar%22%0Dvar%20calendarDescription%20%3D%20%22Calendar%20for%20top%20secret%20Apple%20project.%22%0Dvar%20newCalendar%20%3D%20Calendar.Calendar%28%7Bname%3A%20calendarName%2C%20description%3A%20calendarDescription%7D%29.make%28%29)

__Listing 3-2__JavaScript: Creating a new calendar

1. `var Calendar = Application("Calendar")`
2. `var calendarName = "Project Calendar"`
3. `var calendarDescription = "Calendar for top secret Apple project."`
4. `var newCalendar = Calendar.Calendar({name: calendarName, description: calendarDescription}).make()`
5. `// Result: Application("Calendar").calendars.at(3)`

[About this Guide](AboutthisGuide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbwfvbuqmjqgywvgvzr)

[Finding a Calendar](Calendar-FindaCalendar.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbwfvbuqojqfvjvomy)
