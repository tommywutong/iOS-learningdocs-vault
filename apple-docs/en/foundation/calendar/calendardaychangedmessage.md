---
title: Calendar.CalendarDayChangedMessage
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/calendar/calendardaychangedmessage
source_url: 'https://developer.apple.com/documentation/foundation/calendar/calendardaychangedmessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/calendardaychangedmessage.json'
content_hash: 'sha256:059e1dbc2a2bea3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# Calendar.CalendarDayChangedMessage

<sub>Structure</sub>

A message sent by a calendar when the system’s calendar day changes, as determined by the system calendar, locale, and time zone.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CalendarDayChangedMessage
```

## Overview

If the device is asleep when the day changes, the calendar sends this message when the device wakes up. If the device has been asleep for multiple days, the calendar sends only one message.

Observe this message with the identifier [calendarDayChanged](../notificationcenter/messageidentifier/calendardaychanged.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [Subject](../notificationcenter/asyncmessage/subject.md) of this message type is [Calendar](../calendar.md).

This message interoperates with the notification [NSCalendarDayChangedNotification](../nsnotification/name-swift.struct/nscalendardaychanged.md). The system notifies observers of the message when the [NotificationCenter](../notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Relationships

- **Conforms To**: [AsyncMessage](../notificationcenter/asyncmessage.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a message for a calendar day change

- [init()](<calendardaychangedmessage/init().md>) — Creates a message for a change in calendar day.
