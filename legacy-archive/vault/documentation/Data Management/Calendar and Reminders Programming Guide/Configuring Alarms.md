---
title: Calendar and Reminders Programming Guide
apple_id: TP40009765
resource_type: Guide
platform: watchOS|iOS|macOS
topic: Data Management
technology: EventKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/EventKitProgGuide/ConfiguringAlarms/ConfiguringAlarms.html
archived_at: '2026-07-27T06:57:07.512358Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Calendar and Reminders Programming Guide](Introduction%20to%20Calendars%20and%20Reminders.md)


[Next](Creating%20Recurring%20Events.md)[Previous](Reading%20and%20Writing%20Reminders.md)

# Configuring Alarms

An easy way to alert users of their upcoming events is to give them the option of setting alarms for their calendar items. Regardless of the app that’s currently running, alarms come to the foreground as a notification and remind users of the scheduled event. If an alarm is set to a calendar event, the notification comes from the Calendar app; if an alarm is set to a reminder, the notification comes from the Reminders app. Alarms can be time-based, firing at a specified time, or location-based, firing when crossing a geofence (for more information about geofences, see [Setting Geofences](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tonrvfvbuqnrnknlti)).

Alarms can be applied to both calendar events and reminders.

__Note:__ An alarm is not intended to serve as a `UILocalNotification`. An alarm requires you to create an event or reminder that is visible in the user’s Calendar or Reminders app. A `UILocalNotification` is better suited for general purposes that don’t involve the Calendar database.

## Attaching and Removing Alarms

You can add an alarm to an event with the [addAlarm:](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507397-addalarm) method. Alarms can be created with an absolute date or with an offset relative to the start date of the event. Alarms created with a relative offset must occur before or at the start date of the event.

In OS X, you can trigger an action alongside the alarm; for example, set:

- The [emailAddress](https://developer.apple.com/documentation/eventkit/ekalarm/1507267-emailaddress) property to send an email
- The [soundName](https://developer.apple.com/documentation/eventkit/ekalarm/1507227-soundname) property to play a sound
- The [url](https://developer.apple.com/documentation/eventkit/ekalarm/1589757-url) property to open a URL

You can remove an alarm from an event with the [removeAlarm:](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507133-removealarm) method.

## Setting Geofences

__Note:__ Geofences are supported on both OS X and iOS, but they are more effective on mobile devices.

A geofence is a virtual border surrounding a geographic location that, when crossed, can trigger an alarm for an event. Geofences are a useful way to remind users of tasks they need to do when entering or exiting a certain region. For example, when a user leaves their workplace, an alarm can fire that reminds them to stop by the grocery store. As a developer, you have control over specifying the latitude and longitude of the center, as well as the radius of the geofence.

Configure a geofence for an event by creating an alarm and setting its structured location and proximity. Call the [locationWithTitle:](https://developer.apple.com/documentation/eventkit/ekstructuredlocation/1507366-locationwithtitle) method to create a structured location. To set longitude and latitude coordinates, pass a [CLLocation](https://developer.apple.com/documentation/corelocation/cllocation) to the [geoLocation](https://developer.apple.com/documentation/eventkit/ekstructuredlocation/1507110-geolocation) property of the structured location returned. A value of `0` for the [radius](https://developer.apple.com/documentation/eventkit/ekstructuredlocation/1507489-radius) property will use the system’s default radius; to choose a radius of your own, specify a value in meters.

While geofence-enabled alarms can be applied to events, they are more practical for reminders.

[Next](Creating%20Recurring%20Events.md)[Previous](Reading%20and%20Writing%20Reminders.md)
