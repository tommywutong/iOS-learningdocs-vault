---
title: 'init(identifier:expiration:priority:isFinal:antecedent:metadata:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwconnectiongroup/message/init(identifier:expiration:priority:isfinal:antecedent:metadata:)'
source_url: 'https://developer.apple.com/documentation/network/nwconnectiongroup/message/init(identifier:expiration:priority:isfinal:antecedent:metadata:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnectiongroup/message/init%28identifier%3Aexpiration%3Apriority%3Aisfinal%3Aantecedent%3Ametadata%3A%29.json'
content_hash: 'sha256:80e6e3dab8396eeb'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWConnectionGroup](../../nwconnectiongroup.md) · [Message](../message.md)

# init(identifier:expiration:priority:isFinal:antecedent:metadata:)

<sub>Initializer</sub>

Initializes a custom message context you use to send data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
override init(identifier: String, expiration: UInt64 = super, priority: Double = super, isFinal: Bool = super, antecedent: NWConnection.ContentContext? = nil, metadata: [NWProtocolMetadata]? = super)
```

## See Also

### Sending Messages

- [default](default.md) — A static object you use to send a message with default properties.
