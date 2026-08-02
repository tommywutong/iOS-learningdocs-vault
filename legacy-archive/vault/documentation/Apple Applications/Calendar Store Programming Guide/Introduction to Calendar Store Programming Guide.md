---
title: Calendar Store Programming Guide
apple_id: TP40004334
resource_type: Guide
platform: macOS
topic: Data Management
technology: CalendarStore
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/CalendarStoreProgGuide/Introduction/Introduction.html
archived_at: '2026-07-15T05:17:17.421699Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Calendar%20Store%20Overview.md)

# Introduction to Calendar Store Programming Guide

Calendar Store is a framework that allows Cocoa applications to access iCal data. You can fetch iCal records—such as calendars, events, and tasks—and receive notifications when these records change in iCal. You can also make some local changes to records and save them to the Calendar Store database. This document describes Calendar Store concepts and common programming tasks.

You should read this document if you want to display or edit iCal data in your application. Calendar Store is ideal for integrating subsets of iCal data into your application. Calendar Store simplifies fetching and saving changes to records since you don’t have to implement your own persistent storage or deal with the complexity of the Calendars schema. Calendar Store also notifies applications of changes made in iCal so your application data stays fresh. It is suitable for developing widgets, plug-ins, and augmenting other types of applications that use calendar data. It is not suitable for implementing full-featured calendar applications.

You should read these articles if you just want to fetch Calendar Store objects:

- [Calendar Store Overview](Calendar%20Store%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2donzqfvjvomi) describes the Calendar Store architecture and core classes.
- [Fetching Objects](Fetching%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2donzvfvjvomi) explains how to fetch calendar, event, and task objects.
- [Observing Changes](Observing%20Changes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tanrsfvjvomi) explains how to observe changes made to these objects by other processes.

You should also read these articles if you want to create or modify Calendar Store objects:

- [Creating Objects](Creating%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcnjyfvjvomi) explains how to create commonly used objects: calendars, events, tasks, and alarms.
- [Creating Recurring Events](Creating%20Recurring%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tanrtfvjvomi) explains how to create recurring events—events that repeat according to a custom pattern.
- [Saving Changes](Saving%20Changes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tanjyfvjvomi) explains how to save changes you make locally to Calendar Store objects.

For an in-depth description of the Calendar Store API, read:

- _Calendar Store Framework Reference_

The following project contain more sample code:

- _[SimpleCalendar](../../../samplecode/SimpleCalendar/SimpleCalendar.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgojzge)_
[Next](Calendar%20Store%20Overview.md)

