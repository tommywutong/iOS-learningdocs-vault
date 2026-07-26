---
title: systemTimeZoneDidChange
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/notificationcenter/messageidentifier/systemtimezonedidchange
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/systemtimezonedidchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/messageidentifier/systemtimezonedidchange.json'
content_hash: 'sha256:b3fdfb75d96b8e4c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NotificationCenter](../../notificationcenter.md) · [MessageIdentifier](../messageidentifier.md)

# systemTimeZoneDidChange

<sub>Type Property</sub>

An identifier for a message about a change in the system time zone.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var systemTimeZoneDidChange: NotificationCenter.BaseMessageIdentifier<TimeZone.SystemTimeZoneDidChangeMessage> { get }
```

## Discussion

Use this identifier with [NotificationCenter](../../notificationcenter.md)’s `addObserver(of:for:using:)` or `messages(of:for:bufferSize:)` methods to observe messages of type [SystemTimeZoneDidChangeMessage](../../timezone/systemtimezonedidchangemessage.md).

## See Also

### Identifying calendar, date, and time zone messages

- [calendarDayChanged](calendardaychanged.md) — An identifier for a message about a change in calendar day.
- [systemClockDidChange](systemclockdidchange.md) — An identifier for a message about a change in the system clock.
