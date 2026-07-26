---
title: didBecomeInvalid
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/notificationcenter/messageidentifier/didbecomeinvalid
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/didbecomeinvalid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/messageidentifier/didbecomeinvalid.json'
content_hash: 'sha256:02c0afbbae6884be'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NotificationCenter](../../notificationcenter.md) · [MessageIdentifier](../messageidentifier.md)

# didBecomeInvalid

<sub>Type Property</sub>

An identifier for a message about a port becoming invalid.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var didBecomeInvalid: NotificationCenter.BaseMessageIdentifier<Port.DidBecomeInvalidMessage> { get }
```

## Discussion

Use this identifier with [NotificationCenter](../../notificationcenter.md)’s `addObserver(of:for:using:)` or `messages(of:for:bufferSize:)` methods to observe messages of type [DidBecomeInvalidMessage](../../port/didbecomeinvalidmessage.md).
