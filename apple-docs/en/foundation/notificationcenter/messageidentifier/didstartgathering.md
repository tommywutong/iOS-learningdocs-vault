---
title: didStartGathering
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/notificationcenter/messageidentifier/didstartgathering
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/didstartgathering'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/messageidentifier/didstartgathering.json'
content_hash: 'sha256:ea77835b8f21cb71'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NotificationCenter](../../notificationcenter.md) · [MessageIdentifier](../messageidentifier.md)

# didStartGathering

<sub>Type Property</sub>

An identifier for a message about a metadata query that is starting its initial result gathering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var didStartGathering: NotificationCenter.BaseMessageIdentifier<NSMetadataQuery.DidStartGatheringMessage> { get }
```

## Discussion

Use this identifier with [NotificationCenter](../../notificationcenter.md)’s `addObserver(of:for:using:)` or `messages(of:for:bufferSize:)` methods to observe messages of type [DidStartGatheringMessage](../../nsmetadataquery/didstartgatheringmessage.md).

## See Also

### Identifying metadata query messages

- [didFinishGathering](didfinishgathering.md) — An identifier for a message about a metadata query that finished its initial result gathering.
