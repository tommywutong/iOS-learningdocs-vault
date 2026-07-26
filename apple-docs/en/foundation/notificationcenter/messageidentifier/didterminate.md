---
title: didTerminate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/notificationcenter/messageidentifier/didterminate
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/didterminate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/messageidentifier/didterminate.json'
content_hash: 'sha256:6e43105546ad5312'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NotificationCenter](../../notificationcenter.md) · [MessageIdentifier](../messageidentifier.md)

# didTerminate

<sub>Type Property</sub>

An identifier for a message about a stopped task.

<sub>macOS</sub>

```swift
static var didTerminate: NotificationCenter.BaseMessageIdentifier<Process.DidTerminateMessage> { get }
```

## Discussion

Use this identifier with [NotificationCenter](../../notificationcenter.md)’s `addObserver(of:for:using:)` or `messages(of:for:bufferSize:)` methods to observe messages of type [DidTerminateMessage](../../process/didterminatemessage.md).

## See Also

### Identifying process info messages

- [powerStateDidChange](powerstatedidchange.md) — An identifier for a message about a power state change.
- [thermalStateDidChange](thermalstatedidchange.md) — An identifier for a message about a thermal state change.
