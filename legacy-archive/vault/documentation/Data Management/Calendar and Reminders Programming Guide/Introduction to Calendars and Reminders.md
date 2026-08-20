---
title: Calendar and Reminders Programming Guide
apple_id: TP40009765
resource_type: Guide
platform: watchOS|iOS|macOS
topic: Data Management
technology: EventKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/EventKitProgGuide/Introduction/Introduction.html
archived_at: '2026-07-27T06:57:07.482404Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Reading%20and%20Writing%20Calendar%20Events.md)

# Introduction to Calendars and Reminders

The EventKit framework helps you access users’ Calendar and Reminders information. Although two different apps display users’ calendar and reminder data, the same framework manipulates the data. Similarly, the database that stores this data, called the Calendar database, holds both calendar and reminder information.

__Figure I-1__  EventKit architecture

（原归档配图未能恢复：`EventKitProgGuide.png`）

__Important:__ An iOS app linked on or after iOS 10.0 must include in its `Info.plist` file the usage description keys for the types of data it needs to access or it will crash. To access Reminders and Calendar data specifically, it must include [NSRemindersUsageDescription](../../General/Information%20Property%20List%20Key%20Reference/Cocoa%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomjw) and [NSCalendarsUsageDescription](../../General/Information%20Property%20List%20Key%20Reference/Cocoa%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomjv), respectively.

To access the user’s Calendar data, all sandboxed OS X apps must include the `com.apple.security.personal-information.calendars` entitlement. To learn more about entitlements related to App Sandbox, see [Enabling App Sandbox](../../Miscellaneous/Entitlement%20Key%20Reference/Enabling%20App%20Sandbox.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknlti).

EventKit not only allows your app to retrieve users’ existing calendar and reminder data, but it also lets your app create new events and reminders for any of their calendars. In addition, EventKit lets users edit and delete their events and reminders (collectively known as “calendar items”). More advanced tasks, such as adding alarms or specifying recurring events, can be achieved with EventKit as well. If a change to the Calendar database occurs from outside of your app, EventKit is able to detect the change by notification so your app can act appropriately. Changes made to calendar items with EventKit are automatically synced to the associated calendar (CalDAV, Exchange, and so on).

This document describes EventKit concepts and common programming tasks. You should read this document if you want to display or edit calendar events and/or reminder data from within your app. EventKit provides limited access to a user’s Calendar database; it does not include everything that would be desired for implementing a full-featured calendar or reminder app, such as adding attendees or accounts.

## At a Glance

This document contains the following chapters, which describe how to integrate with users’ calendar and reminder data within your app:

- [Reading and Writing Calendar Events](Reading%20and%20Writing%20Calendar%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2donzvfvjvomi) explains how to retrieve, create, and modify calendar events.
- [Reading and Writing Reminders](Reading%20and%20Writing%20Reminders.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tonrvfvbuqnjnknltc) explains how to retrieve, create, and modify reminders.
- [Configuring Alarms](Configuring%20Alarms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tonrvfvbuqnrnknltc) explains how to attach alarms to a calendar item.
- [Creating Recurring Events](Creating%20Recurring%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tonrvfvbuqmznknltc) explains how to make an event a recurring event.
- [Observing External Changes to the Calendar Database](Observing%20External%20Changes%20to%20the%20Calendar%20Database.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tonrvfvbuqnbnknltc) explains how to register for notifications regarding external changes to the Calendar database.
- [Providing Interfaces for Events](Providing%20Interfaces%20for%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tonrvfvbuqmrnknlti) explains how to display event view controllers to allow your users to create and edit events.

## See Also

This document is a companion guide to the following references:

- _[Event Kit Framework Reference](https://developer.apple.com/documentation/eventkit)_ provides an in-depth description of the EventKit API, a framework that grants access to a user’s Calendar database.
- _[Event Kit UI Framework Reference](https://developer.apple.com/documentation/eventkitui)_ details the EventKit UI API, an iOS-specific framework that provides view controllers for displaying and editing calendar events.

[Next](Reading%20and%20Writing%20Calendar%20Events.md)
