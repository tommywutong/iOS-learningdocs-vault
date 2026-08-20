---
title: SimpleCalendar
apple_id: DTS10003991
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: CalendarStore
published: '2006-07-27'
source_url: https://developer.apple.com/library/archive/samplecode/SimpleCalendar/Introduction/Intro.html
archived_at: '2026-07-18T03:23:54.705120Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# SimpleCalendar

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2006-07-27 Uses the Calendar Store framework to fetch iCal events and display them on a custom calendar. |
| __Build Requirements:__ | Leopard Preview |
| __Runtime Requirements:__ | Leopard Preview |

The SimpleCalendar application uses both read and write Calendar Store APIs. It initially fetches a range of event objects from Calendar Store, and uses Cocoa Bindings to display events on individual days of a monthly calendar. It observes iCal notifications and updates local records if they are changed externally. It also observes user changes to local records and saves them to Calendar Store.
This sample uses pre-release APIs. Please see the headers in CalendarStore.framework for a list of known issues.

[Next](ReadMe.txt.md)

