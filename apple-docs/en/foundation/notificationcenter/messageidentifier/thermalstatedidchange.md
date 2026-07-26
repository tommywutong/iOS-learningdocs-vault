---
title: thermalStateDidChange
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/notificationcenter/messageidentifier/thermalstatedidchange
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/thermalstatedidchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/messageidentifier/thermalstatedidchange.json'
content_hash: 'sha256:28ee4362a0f2be54'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NotificationCenter](../../notificationcenter.md) · [MessageIdentifier](../messageidentifier.md)

# thermalStateDidChange

<sub>Type Property</sub>

An identifier for a message about a thermal state change.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var thermalStateDidChange: NotificationCenter.BaseMessageIdentifier<ProcessInfo.ThermalStateDidChangeMessage> { get }
```

## Discussion

Use this identifier with [NotificationCenter](../../notificationcenter.md)’s `addObserver(of:for:using:)` or `messages(of:for:bufferSize:)` methods to observe messages of type [ThermalStateDidChangeMessage](../../processinfo/thermalstatedidchangemessage.md).

## See Also

### Identifying process info messages

- [powerStateDidChange](powerstatedidchange.md) — An identifier for a message about a power state change.
- [didTerminate](didterminate.md) — An identifier for a message about a stopped task.
