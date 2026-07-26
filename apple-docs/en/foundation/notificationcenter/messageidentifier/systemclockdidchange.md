---
title: systemClockDidChange
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/notificationcenter/messageidentifier/systemclockdidchange
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/systemclockdidchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/messageidentifier/systemclockdidchange.json'
content_hash: 'sha256:9bc7e272371a85be'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NotificationCenter](../../notificationcenter.md) · [MessageIdentifier](../messageidentifier.md)

# systemClockDidChange

<sub>Type Property</sub>

An identifier for a message about a change in the system clock.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var systemClockDidChange: NotificationCenter.BaseMessageIdentifier<Date.SystemClockDidChangeMessage> { get }
```

## Discussion

Use this identifier with [NotificationCenter](../../notificationcenter.md)’s `addObserver(of:for:using:)` or `messages(of:for:bufferSize:)` methods to observe messages of type [SystemClockDidChangeMessage](../../date/systemclockdidchangemessage.md).

## See Also

### Identifying calendar, date, and time zone messages

- [calendarDayChanged](calendardaychanged.md) — An identifier for a message about a change in calendar day.
- [systemTimeZoneDidChange](systemtimezonedidchange.md) — An identifier for a message about a change in the system time zone.
