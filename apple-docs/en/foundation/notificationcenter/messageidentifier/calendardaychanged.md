---
title: calendarDayChanged
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/notificationcenter/messageidentifier/calendardaychanged
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/calendardaychanged'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/messageidentifier/calendardaychanged.json'
content_hash: 'sha256:f314c70e499354eb'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NotificationCenter](../../notificationcenter.md) · [MessageIdentifier](../messageidentifier.md)

# calendarDayChanged

<sub>Type Property</sub>

An identifier for a message about a change in calendar day.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var calendarDayChanged: NotificationCenter.BaseMessageIdentifier<Calendar.CalendarDayChangedMessage> { get }
```

## Discussion

Use this identifier with [NotificationCenter](../../notificationcenter.md)’s `addObserver(of:for:using:)` or `messages(of:for:bufferSize:)` methods to observe messages of type [CalendarDayChangedMessage](../../calendar/calendardaychangedmessage.md).

## See Also

### Identifying calendar, date, and time zone messages

- [systemClockDidChange](systemclockdidchange.md) — An identifier for a message about a change in the system clock.
- [systemTimeZoneDidChange](systemtimezonedidchange.md) — An identifier for a message about a change in the system time zone.
